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
│   ├── app.py         # Main Flask application
│   └── requirements.txt # Python dependencies
├── start.py           # Startup script for both servers
└── README.md          # This file
```

## Features

- 📄 Upload job descriptions (PDF, DOC, DOCX, TXT)
- 🤖 AI-powered job analysis (coming soon with Gemini)
- 📝 Generate customized LaTeX resumes
- 📊 PDF preview and download
- 🎨 Modern, responsive UI

## Setup Instructions

### Prerequisites

1. **Node.js** - Download from [https://nodejs.org/](https://nodejs.org/)
2. **Python 3.7+** - Download from [https://python.org/](https://python.org/)
3. **LaTeX Distribution** - Install MiKTeX (Windows) or TeX Live

### Installation

1. **Install http-server globally:**
   ```bash
   npm install -g http-server
   ```

2. **Install Python dependencies:**
   ```bash
   cd backend
   pip install -r requirements.txt
   cd ..
   ```

3. **Install LaTeX (if not already installed):**
   - **Windows:** Download and install [MiKTeX](https://miktex.org/)
   - **macOS:** Install [MacTeX](https://www.tug.org/mactex/)
   - **Linux:** Install TeX Live: `sudo apt-get install texlive-full`

### Running the Application

**Option 1: Use the startup script**
```bash
python start.py
```

**Option 2: Run servers separately**

Terminal 1 (Backend):
```bash
cd backend
python app.py
```

Terminal 2 (Frontend):
```bash
http-server -p 3000 frontend
```

### Access the Application

- **Frontend:** http://localhost:3000
- **Backend API:** http://localhost:5000

## Usage

1. Open http://localhost:3000 in your browser
2. Upload a job description file
3. Click "Generate Resume"
4. Preview and download the generated PDF

## Development

### Frontend Development
- Edit files in `frontend/` directory
- Changes are reflected immediately when using http-server

### Backend Development
- Edit `backend/app.py` for API changes
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
- Change ports in `start.py` or run servers manually with different ports

**CORS errors:**
- Ensure Flask-CORS is installed: `pip install Flask-CORS`