import subprocess
import time
import sys
import os

def start_backend():
    """Start the Flask backend server"""
    print("Starting Flask backend...")
    os.chdir('backend')
    subprocess.Popen([sys.executable, 'app.py'], 
                     stdout=subprocess.PIPE, 
                     stderr=subprocess.PIPE)
    os.chdir('..')

def start_frontend():
    """Start the frontend server"""
    print("Starting frontend server...")
    subprocess.Popen([
        r'C:\Users\shadh\AppData\Roaming\npm\http-server.cmd',
        '-p', '3000', 'frontend'
    ], 
    stdout=subprocess.PIPE, 
    stderr=subprocess.PIPE)

if __name__ == "__main__":
    print("Starting Upsilon Job application...")
    
    # Start backend
    start_backend()
    time.sleep(2)  # Give backend time to start
    
    # Start frontend
    start_frontend()
    
    print("\n" + "="*50)
    print("🚀 Application started!")
    print("="*50)
    print("Frontend: http://localhost:3000")
    print("Backend:  http://localhost:5000")
    print("="*50)
    print("\nPress Ctrl+C to stop both servers")
    
    try:
        # Keep the script running
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        print("\nShutting down servers...")
        sys.exit(0) 