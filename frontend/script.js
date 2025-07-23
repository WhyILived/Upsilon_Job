// DOM elements
const uploadArea = document.getElementById('uploadArea');
const jobFileInput = document.getElementById('jobFile');
const generateBtn = document.getElementById('generateBtn');
const downloadBtn = document.getElementById('downloadBtn');
const pdfViewer = document.getElementById('pdfViewer');

// State
let uploadedFile = null;

// File upload handling
uploadArea.addEventListener('click', () => jobFileInput.click());

uploadArea.addEventListener('dragover', (e) => {
    e.preventDefault();
    uploadArea.classList.add('dragover');
});

uploadArea.addEventListener('dragleave', () => {
    uploadArea.classList.remove('dragover');
});

uploadArea.addEventListener('drop', (e) => {
    e.preventDefault();
    uploadArea.classList.remove('dragover');
    
    const files = e.dataTransfer.files;
    if (files.length > 0) {
        handleFileUpload(files[0]);
    }
});

jobFileInput.addEventListener('change', (e) => {
    if (e.target.files.length > 0) {
        handleFileUpload(e.target.files[0]);
    }
});

function handleFileUpload(file) {
    uploadedFile = file;
    
    // Update UI to show selected file
    const uploadContent = uploadArea.querySelector('.upload-content');
    uploadContent.innerHTML = `
        <svg class="upload-icon" viewBox="0 0 24 24" fill="none" stroke="currentColor">
            <path d="M9 12l2 2 4-4"/>
            <path d="M21 12c-1 0-2.4-.6-3-1.5l-6-9c-.6-.9-1.5-1.5-2.5-1.5s-1.9.6-2.5 1.5l-6 9c-.6.9-2 1.5-3 1.5"/>
        </svg>
        <h3>File Selected</h3>
        <p>${file.name}</p>
        <button class="upload-btn" onclick="resetUpload()">
            Choose Different File
        </button>
    `;
    
    // Enable generate button
    generateBtn.disabled = false;
}

function resetUpload() {
    uploadedFile = null;
    jobFileInput.value = '';
    
    // Reset UI
    const uploadContent = uploadArea.querySelector('.upload-content');
    uploadContent.innerHTML = `
        <svg class="upload-icon" viewBox="0 0 24 24" fill="none" stroke="currentColor">
            <path d="M21 15v4a2 2 0 0 1-2 2H5a2 2 0 0 1-2-2v-4"/>
            <polyline points="7,10 12,15 17,10"/>
            <line x1="12" y1="15" x2="12" y2="3"/>
        </svg>
        <h3>Upload Job Description</h3>
        <p>Drag and drop a job posting or click to browse</p>
        <input type="file" id="jobFile" accept=".txt,.pdf,.doc,.docx" hidden>
        <button class="upload-btn" onclick="document.getElementById('jobFile').click()">
            Choose File
        </button>
    `;
    
    generateBtn.disabled = true;
    downloadBtn.disabled = true;
}

// Generate resume
generateBtn.addEventListener('click', async () => {
    if (!uploadedFile) return;
    
    // Show loading state
    generateBtn.disabled = true;
    generateBtn.textContent = 'Generating...';
    
    pdfViewer.innerHTML = `
        <div class="loading">
            <div class="spinner"></div>
        </div>
    `;
    
    try {
        // Create FormData for file upload
        const formData = new FormData();
        formData.append('job_file', uploadedFile);
        
        // Send to backend (we'll implement this later)
        const response = await fetch('/api/generate-resume', {
            method: 'POST',
            body: formData
        });
        
        if (response.ok) {
            const result = await response.json();
            
            // Display PDF (assuming backend returns PDF URL)
            if (result.pdf_url) {
                displayPDF(result.pdf_url);
                downloadBtn.disabled = false;
            } else {
                showError('Failed to generate PDF');
            }
        } else {
            showError('Failed to generate resume');
        }
    } catch (error) {
        console.error('Error:', error);
        showError('Network error occurred');
    } finally {
        generateBtn.disabled = false;
        generateBtn.textContent = 'Generate Resume';
    }
});

function displayPDF(pdfUrl) {
    pdfViewer.innerHTML = `
        <iframe src="${pdfUrl}" type="application/pdf"></iframe>
    `;
}

function showError(message) {
    pdfViewer.innerHTML = `
        <div class="placeholder">
            <svg class="placeholder-icon" viewBox="0 0 24 24" fill="none" stroke="currentColor">
                <circle cx="12" cy="12" r="10"/>
                <line x1="15" y1="9" x2="9" y2="15"/>
                <line x1="9" y1="9" x2="15" y2="15"/>
            </svg>
            <p>${message}</p>
        </div>
    `;
}

// Download PDF
downloadBtn.addEventListener('click', () => {
    // This will be implemented when we have the backend
    console.log('Download PDF');
});

// For demo purposes, let's add a mock PDF display
// Remove this when backend is ready
function showDemoPDF() {
    // Mock PDF display for testing
    pdfViewer.innerHTML = `
        <div style="padding: 2rem; text-align: center;">
            <h3>Demo PDF Preview</h3>
            <p>This would show the generated PDF resume</p>
            <p style="color: #666; font-size: 0.9rem;">
                Backend integration coming soon...
            </p>
        </div>
    `;
}

// Initialize
document.addEventListener('DOMContentLoaded', () => {
    console.log('Upsilon Job - Resume Generator loaded');
});


