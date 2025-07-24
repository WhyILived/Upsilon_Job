from flask import Flask, request, jsonify, send_file, send_from_directory
from flask_cors import CORS
import os
import tempfile
import subprocess
from werkzeug.utils import secure_filename
import json
from pathlib import Path
from dotenv import load_dotenv
from vellum.client import Vellum
import vellum.types as types

# Load .env from root directory
project_root = Path(__file__).parent.parent
load_dotenv(project_root / '.env')

# create your API key here: https://app.vellum.ai/api-keys#keys
vellum_client = Vellum(
    api_key=os.environ.get("VELLUM_API_KEY")
)

app = Flask(__name__)
CORS(app)  # Enable CORS for frontend communication

# Configuration
UPLOAD_FOLDER = 'uploads'
TEX_FOLDER = 'tex_files'
PDF_FOLDER = 'pdf_files'

# Create directories if they don't exist
os.makedirs(UPLOAD_FOLDER, exist_ok=True)
os.makedirs(TEX_FOLDER, exist_ok=True)
os.makedirs(PDF_FOLDER, exist_ok=True)

# Sample LaTeX template
LATEX_TEMPLATE = r"""
\documentclass[11pt,a4paper]{article}
\usepackage[margin=1in]{geometry}
\usepackage{enumitem}
\usepackage{hyperref}
\usepackage{xcolor}

\definecolor{accent}{RGB}{0, 120, 215}

\begin{document}

\begin{center}
{\color{accent}\Large\textbf{John Doe}}\\
\textbf{Software Engineer}\\
john.doe@email.com $|$ (555) 123-4567 $|$ linkedin.com/in/johndoe
\end{center}

\section*{Professional Summary}
Experienced software engineer with expertise in modern web technologies and cloud platforms.

\section*{Technical Skills}
\textbf{Frontend:} React, Vue.js, TypeScript, CSS3\\
\textbf{Backend:} Node.js, Python, PostgreSQL, MongoDB\\
\textbf{DevOps:} Docker, Kubernetes, AWS, Azure

\section*{Experience}
\textbf{Senior Software Engineer} \hfill 2021 - Present\\
Tech Company Inc.\\
\begin{itemize}[leftmargin=*]
\item Led development of microservices architecture serving 1M+ users
\item Mentored 3 junior developers and conducted code reviews
\item Implemented CI/CD pipeline reducing deployment time by 60\%
\end{itemize}

\section*{Education}
\textbf{Bachelor of Science in Computer Science}\\
University of Technology \hfill 2017 - 2021

\end{document}
"""

@app.route('/api/generate-resume', methods=['POST'])
def generate_resume():
    try:
        # Check if file was uploaded
        if 'job_file' not in request.files:
            return jsonify({'error': 'No file uploaded'}), 400
        
        file = request.files['job_file']
        if file.filename == '':
            return jsonify({'error': 'No file selected'}), 400
        
        # Save uploaded file
        filename = secure_filename(file.filename)
        filepath = os.path.join(UPLOAD_FOLDER, filename)
        file.save(filepath)
        
        # For now, we'll use a sample LaTeX template
        # Later, this will be replaced with AI processing
        tex_content = LATEX_TEMPLATE
        
        # Generate unique filename
        import uuid
        unique_id = str(uuid.uuid4())[:8]
        tex_filename = f"resume_{unique_id}.tex"
        pdf_filename = f"resume_{unique_id}.pdf"
        
        tex_filepath = os.path.join(TEX_FOLDER, tex_filename)
        pdf_filepath = os.path.join(PDF_FOLDER, pdf_filename)
        
        # Save LaTeX file
        with open(tex_filepath, 'w', encoding='utf-8') as f:
            f.write(tex_content)
        
        # Convert LaTeX to PDF
        try:
            subprocess.run([
                'pdflatex',
                '-interaction=nonstopmode',
                f'-output-directory={PDF_FOLDER}',
                tex_filepath
            ], check=True, capture_output=True)
            
            # Check if PDF was created
            if os.path.exists(pdf_filepath):
                return jsonify({
                    'success': True,
                    'pdf_url': f'/api/download-pdf/{pdf_filename}',
                    'message': 'Resume generated successfully'
                })
            else:
                return jsonify({'error': 'Failed to generate PDF'}), 500
                
        except subprocess.CalledProcessError as e:
            return jsonify({'error': f'LaTeX compilation failed: {e.stderr.decode()}'}), 500
        except FileNotFoundError:
            return jsonify({'error': 'LaTeX compiler (pdflatex) not found. Please install a LaTeX distribution.'}), 500
    
    except Exception as e:
        return jsonify({'error': f'Server error: {str(e)}'}), 500

@app.route('/api/download-pdf/<filename>')
def download_pdf(filename):
    try:
        pdf_path = os.path.join(PDF_FOLDER, filename)
        if os.path.exists(pdf_path):
            return send_file(pdf_path, as_attachment=True, download_name=filename)
        else:
            return jsonify({'error': 'PDF not found'}), 404
    except Exception as e:
        return jsonify({'error': f'Download error: {str(e)}'}), 500

@app.route('/api/health')
def health_check():
    return jsonify({'status': 'healthy', 'message': 'Backend is running'})

# Serve frontend static files
@app.route('/')
def serve_index():
    return send_from_directory('../frontend', 'index.html')

@app.route('/<path:path>')
def serve_static(path):
    return send_from_directory('../frontend', path)

if __name__ == '__main__':
    app.run(debug=True, port=5000) 