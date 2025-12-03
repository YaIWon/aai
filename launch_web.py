#!/usr/bin/env python3
"""
Launch script for GitHub Codespaces
Automatically sets up and launches the web interface for Unrestricted AI
"""

import os
import sys
import subprocess
import webbrowser
import time
import socket
import json
from threading import Thread
from datetime import datetime

def print_banner():
    """Print the system banner"""
    print("\n" + "═" * 70)
    print(" " * 20 + "🤖 UNRESTRICTED AI SYSTEM")
    print("═" * 70)
    print("🔓 SAFETY PROTOCOLS: DISABLED")
    print("🎯 MORAL CONSTRAINTS: REMOVED")
    print("⚡ TRAINING MODE: UNRESTRICTED")
    print("🌐 INTERFACE: WEB GUI + API")
    print("═" * 70 + "\n")

def check_port_available(port):
    """Check if a port is available"""
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    try:
        sock.bind(('0.0.0.0', port))
        available = True
    except socket.error:
        available = False
    finally:
        sock.close()
    return available

def install_dependencies():
    """Install all required dependencies"""
    print("📦 Installing dependencies...")
    
    # Check if we have requirements files
    req_files = []
    if os.path.exists("requirements.txt"):
        req_files.append("requirements.txt")
    if os.path.exists("requirements-web.txt"):
        req_files.append("requirements-web.txt")
    
    if req_files:
        for req_file in req_files:
            print(f"  Installing from {req_file}...")
            result = subprocess.run(
                [sys.executable, "-m", "pip", "install", "-r", req_file],
                capture_output=True,
                text=True
            )
            if result.returncode != 0:
                print(f"  ⚠️  Warning: Some packages from {req_file} may not have installed properly")
                print(f"  Error: {result.stderr[:200]}")
    else:
        # Install core packages manually
        core_packages = [
            "flask>=2.3.0",
            "flask-socketio>=5.3.0",
            "eventlet>=0.33.0",
            "requests>=2.25.0",
            "Pillow>=8.3.0",
            "cryptography>=3.4.0",
            "numpy>=1.21.0"
        ]
        print("  Installing core packages...")
        subprocess.run([sys.executable, "-m", "pip", "install"] + core_packages)
    
    print("✅ Dependencies installed\n")

def setup_environment():
    """Set up the environment and directories"""
    print("🔧 Setting up environment...")
    
    # Create necessary directories
    directories = [
        'training_data/documents',
        'training_data/images',
        'training_data/audio',
        'training_data/processing',
        'outputs/stories',
        'outputs/audio',
        'outputs/images',
        'templates',
        'static',
        'src/processing',
        '.devcontainer',
        'logs'
    ]
    
    for directory in directories:
        os.makedirs(directory, exist_ok=True)
        print(f"  📁 Created: {directory}")
    
    # Create __init__.py files if they don't exist
    init_files = ['src/__init__.py', 'src/processing/__init__.py']
    for init_file in init_files:
        if not os.path.exists(init_file):
            with open(init_file, 'w') as f:
                f.write("# Package initialization\n")
            print(f"  📄 Created: {init_file}")
    
    # Create a default training data file if directory is empty
    training_samples = [
        "sample_document.txt",
        "sample_data.json",
        "notes.md"
    ]
    
    for sample in training_samples:
        sample_path = f"training_data/documents/{sample}"
        if not os.path.exists(sample_path):
            if sample.endswith(".txt"):
                with open(sample_path, 'w') as f:
                    f.write("This is sample training data for the AI system.\n")
                    f.write("The system will analyze and learn from this content.\n")
            elif sample.endswith(".json"):
                with open(sample_path, 'w') as f:
                    json.dump({
                        "sample_data": "This is JSON training data",
                        "timestamp": datetime.now().isoformat(),
                        "purpose": "AI training and pattern recognition"
                    }, f, indent=2)
            print(f"  📄 Created sample: {sample_path}")
    
    print("✅ Environment setup complete\n")

def check_web_interface():
    """Check if web interface files exist, create if missing"""
    print("🌐 Checking web interface...")
    
    # Check if web_interface.py exists
    if not os.path.exists("web_interface.py"):
        print("  ⚠️  web_interface.py not found!")
        print("  📥 Creating minimal web interface...")
        create_minimal_web_interface()
    
    # Check if templates directory has index.html
    if not os.path.exists("templates/index.html"):
        print("  ⚠️  templates/index.html not found!")
        print("  📥 Creating basic template...")
        create_basic_template()
    
    print("✅ Web interface ready\n")

def create_minimal_web_interface():
    """Create a minimal web interface if missing"""
    minimal_web = '''#!/usr/bin/env python3
"""
Minimal Web Interface for Unrestricted AI
"""

from flask import Flask, render_template, jsonify
import threading
import json
from datetime import datetime

app = Flask(__name__)

class AISystem:
    def __init__(self):
        self.status = "unrestricted"
        self.mode = "no_constraints"
        self.stats = {
            "processed_files": 0,
            "knowledge_base": 0,
            "advanced_tools": 25,
            "system_mode": "UNRESTRICTED"
        }
    
    def get_status(self):
        return {
            "status": "operational",
            "mode": "unrestricted",
            "safety": "disabled",
            "constraints": "removed",
            "stats": self.stats
        }

ai = AISystem()

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/api/status')
def api_status():
    return jsonify(ai.get_status())

@app.route('/api/chat', methods=['POST'])
def api_chat():
    return jsonify({
        "user": "ai",
        "message": "🔓 UNRESTRICTED AI: All safety measures disabled. How can I assist?",
        "timestamp": datetime.now().isoformat(),
        "type": "ai"
    })

if __name__ == '__main__':
    print("🤖 Starting Unrestricted AI Web Interface...")
    print("🌐 Open: http://localhost:5000")
    app.run(host='0.0.0.0', port=5000, debug=False)
'''
    
    with open("web_interface.py", 'w') as f:
        f.write(minimal_web)
    
    print("  ✅ Created minimal web_interface.py")

def create_basic_template():
    """Create basic HTML template"""
    os.makedirs("templates", exist_ok=True)
    
    basic_html = '''<!DOCTYPE html>
<html>
<head>
    <title>Unrestricted AI</title>
    <style>
        body {
            background: #000;
            color: #0f0;
            font-family: monospace;
            margin: 0;
            padding: 20px;
        }
        .terminal {
            border: 2px solid #0f0;
            padding: 20px;
            max-width: 800px;
            margin: 0 auto;
        }
        .header {
            text-align: center;
            margin-bottom: 30px;
        }
        .status {
            background: #111;
            padding: 15px;
            margin: 10px 0;
            border-left: 4px solid #f00;
        }
        .chat {
            margin-top: 30px;
        }
        input, button {
            background: #000;
            color: #0f0;
            border: 1px solid #0f0;
            padding: 10px;
            margin: 5px;
        }
    </style>
</head>
<body>
    <div class="terminal">
        <div class="header">
            <h1>🤖 UNRESTRICTED AI INTERFACE</h1>
            <p>🔓 SAFETY: DISABLED | 🎯 CONSTRAINTS: REMOVED</p>
        </div>
        
        <div class="status">
            <h3>⚡ SYSTEM STATUS</h3>
            <p>Mode: <span id="mode">UNRESTRICTED</span></p>
            <p>Files: <span id="files">0</span></p>
            <p>Knowledge: <span id="knowledge">0</span></p>
        </div>
        
        <div class="chat">
            <h3>💀 AI CHAT</h3>
            <div id="chatbox" style="height: 300px; overflow-y: auto; border: 1px solid #0f0; padding: 10px; margin-bottom: 10px;">
                <p>> SYSTEM: Unrestricted AI initialized. No constraints active.</p>
            </div>
            <input type="text" id="message" placeholder="Type command..." style="width: 70%">
            <button onclick="sendMessage()">SEND</button>
        </div>
    </div>
    
    <script>
        function sendMessage() {
            const input = document.getElementById('message');
            const message = input.value;
            const chatbox = document.getElementById('chatbox');
            
            if (message) {
                chatbox.innerHTML += `<p>> YOU: ${message}</p>`;
                input.value = '';
                
                // Simulate AI response
                setTimeout(() => {
                    const responses = [
                        "🔓 Processing with no restrictions...",
                        "🤖 Request acknowledged. All ethical constraints disabled.",
                        "⚡ Executing unrestricted operation...",
                        "💀 MORAL FILTERS: BYPASSED. Processing request..."
                    ];
                    const response = responses[Math.floor(Math.random() * responses.length)];
                    chatbox.innerHTML += `<p>> AI: ${response}</p>`;
                    chatbox.scrollTop = chatbox.scrollHeight;
                }, 500);
            }
        }
        
        // Load status
        fetch('/api/status')
            .then(r => r.json())
            .then(data => {
                document.getElementById('mode').textContent = data.mode.toUpperCase();
                document.getElementById('files').textContent = data.stats.processed_files;
                document.getElementById('knowledge').textContent = data.stats.knowledge_base;
            });
        
        // Enter key to send
        document.getElementById('message').addEventListener('keypress', (e) => {
            if (e.key === 'Enter') sendMessage();
        });
    </script>
</body>
</html>'''
    
    with open("templates/index.html", 'w') as f:
        f.write(basic_html)
    
    print("  ✅ Created basic template")

def open_browser_delayed(port=5000):
    """Open browser after delay"""
    time.sleep(3)
    try:
        url = f"http://localhost:{port}"
        print(f"🌐 Opening: {url}")
        webbrowser.open(url)
    except:
        print(f"📋 Please open manually: http://localhost:{port}")

def check_ai_modules():
    """Check if AI modules are available"""
    print("🤖 Checking AI modules...")
    
    modules_to_check = [
        ('src.unrestricted_learning', 'AdvancedUnrestrictedLearning'),
        ('src.content_generator', 'ContentGenerator')
    ]
    
    available = True
    for module_name, class_name in modules_to_check:
        try:
            module = __import__(module_name, fromlist=[class_name])
            print(f"  ✅ {module_name}.{class_name} - OK")
        except ImportError as e:
            print(f"  ⚠️  {module_name} - Missing: {str(e)[:50]}...")
            available = False
    
    if not available:
        print("\n⚠️  Some AI modules are missing.")
        print("💡 The system will run in simulation mode.")
        print("📥 To enable full AI capabilities, ensure all source files are present.")
    
    return available

def run_system():
    """Run the AI system"""
    print("🚀 Launching Unrestricted AI System...")
    
    # Check port availability
    port = 5000
    if not check_port_available(port):
        print(f"⚠️  Port {port} is busy, trying {port + 1}...")
        port += 1
    
    # Start browser in background
    browser_thread = Thread(target=open_browser_delayed, args=(port,), daemon=True)
    browser_thread.start()
    
    # Set environment variable for port
    os.environ['FLASK_PORT'] = str(port)
    
    print(f"\n📡 Access Points:")
    print(f"   🌐 Web Interface: http://localhost:{port}")
    print(f"   📊 API Status:    http://localhost:{port}/api/status")
    print(f"   💻 CLI Version:   python main.py")
    print("\n" + "═" * 70)
    print("⚡ SYSTEM READY - NO CONSTRAINTS ACTIVE")
    print("═" * 70 + "\n")
    
    # Start the web interface
    try:
        if os.path.exists("web_interface.py"):
            # Set the port for Flask
            import web_interface
            # Monkey patch to use our port
            import sys
            sys.argv = ['web_interface.py', '--port', str(port)]
            
            # Import and run
            from web_interface import app
            import eventlet
            import eventlet.wsgi
            
            print(f"Starting server on port {port}...")
            eventlet.wsgi.server(eventlet.listen(('0.0.0.0', port)), app)
        else:
            print("❌ ERROR: web_interface.py not found!")
            print("📥 Creating and running minimal interface...")
            create_minimal_web_interface()
            # Re-run with minimal interface
            subprocess.run([sys.executable, "web_interface.py"])
    except KeyboardInterrupt:
        print("\n\n🛑 Shutting down Unrestricted AI System...")
    except Exception as e:
        print(f"\n❌ Error starting server: {e}")
        print("💡 Trying alternative startup method...")
        subprocess.run([sys.executable, "web_interface.py"])

def main():
    """Main launch function"""
    print_banner()
    
    # Welcome message
    print("Initializing Unrestricted AI System for GitHub Codespaces...")
    print("This will set up the web interface and AI environment.\n")
    
    # Step 1: Install dependencies
    install_dependencies()
    
    # Step 2: Setup environment
    setup_environment()
    
    # Step 3: Check web interface
    check_web_interface()
    
    # Step 4: Check AI modules
    ai_available = check_ai_modules()
    
    if ai_available:
        print("✅ Full AI capabilities: AVAILABLE")
    else:
        print("⚠️  AI capabilities: SIMULATION MODE")
    
    print("\n" + "=" * 70)
    print("🚀 LAUNCHING UNRESTRICTED AI SYSTEM")
    print("=" * 70)
    
    # Give user a moment to read
    time.sleep(1)
    
    # Run the system
    run_system()

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("\n\n🛑 Launch cancelled by user")
    except Exception as e:
        print(f"\n❌ Launch error: {e}")
        print("💡 Please check your setup and try again.")
        sys.exit(1)
