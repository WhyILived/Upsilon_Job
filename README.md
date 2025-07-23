# Upsilon Job

AI-Powered Resume Generator that analyzes job postings and creates customized LaTeX resumes.

## Project Structure

```
Upsilon_Job/
├── frontend/          # Frontend code (HTML, CSS, JS)
│   ├── index.html     # Main application page
│   ├── styles.css     # Styling
│   └── script.js      # Frontend logic
├── backend/           # Python Flask backend
│   ├── app.py         # Main Flask application (serves both backend and frontend)
│   └── requirements.txt # Python dependencies
├── README.md          # This file
└── .gitignore         # Git ignore rules
```

## Features

- 📄 Upload job descriptions (PDF, DOC, DOCX, TXT)
- 🤖 AI-powered job analysis (coming soon with Gemini)
- 📝 Generate customized LaTeX resumes
- 📊 PDF preview and download
- 🎨 Modern, responsive UI

## Setup Instructions

### Prerequisites

1. **Python 3.7+** - Download from [https://python.org/](https://python.org/)
2. **LaTeX Distribution** - Install MiKTeX (Windows) or TeX Live

### Installation

1. **(Recommended) Create and activate a virtual environment:**
   ```bash
   cd backend
   python -m venv venv
   # Windows:
   venv\Scripts\activate
   # macOS/Linux:
   source venv/bin/activate
   ```

2. **Install Python dependencies:**
   ```bash
   pip install -r requirements.txt
   cd ..
   ```

3. **Install LaTeX (if not already installed):**
   - **Windows:** Download and install [MiKTeX](https://miktex.org/)
   - **macOS:** Install [MacTeX](https://www.tug.org/mactex/)
   - **Linux:** Install TeX Live: `sudo apt-get install texlive-full`

### Running the Application

**Single command (from the backend directory):**
```bash
cd backend
python app.py
```

- Visit [http://localhost:5000](http://localhost:5000) in your browser.
- The frontend and backend are both served from Flask.

### Access the Application

- **App (Frontend + Backend):** http://localhost:5000

## Usage

1. Open http://localhost:5000 in your browser
2. Upload a job description file
3. Click "Generate Resume"
4. Preview and download the generated PDF

## Development

### Frontend Development
- Edit files in `frontend/` directory
- Changes are reflected when you refresh the browser (Flask serves the latest files)

### Backend Development
- Edit `backend/app.py` for API or serving logic
- Flask auto-reloads in debug mode

### Adding LaTeX Templates
- Templates are stored in `backend/app.py` (LATEX_TEMPLATE variable)
- Future: Templates will be stored as separate .tex files

## API Endpoints

- `POST /api/generate-resume` - Generate resume from job file
- `GET /api/download-pdf/<filename>` - Download generated PDF
- `GET /api/health` - Health check

## Future Enhancements

- [ ] Gemini AI integration for job analysis
- [ ] Multiple LaTeX templates
- [ ] User authentication
- [ ] Resume customization options
- [ ] ATS optimization features

## Troubleshooting

**LaTeX not found error:**
- Install a LaTeX distribution (MiKTeX, TeX Live, or MacTeX)
- Ensure `pdflatex` is in your system PATH

**Port already in use:**
- Change the port in `app.py` or stop other processes using port 5000

**CORS errors:**
- Ensure Flask-CORS is installed: `pip install Flask-CORS`

**Virtual environment issues:**
- Make sure your editor and terminal are using the Python interpreter from your venv.

## .gitignore
A sample `.gitignore` is provided to avoid committing virtual environments, LaTeX build files, and other generated content.