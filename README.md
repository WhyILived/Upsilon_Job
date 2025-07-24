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

### env file

- Create a .env file in the root directory and add your:
   - VELLUM_API_KEY="Your_Key_Here"

## .gitignore
A sample `.gitignore` is provided to avoid committing virtual environments, LaTeX build files, and other generated content.