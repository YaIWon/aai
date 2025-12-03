#!/usr/bin/env python3
"""
Web Interface for Unrestricted AI System
Run with: python web_interface.py
Open browser to: http://localhost:5000
"""

import os
import sys
import threading
import json
import webbrowser
from datetime import datetime
from flask import Flask, render_template, request, jsonify, session, Response
from flask_socketio import SocketIO, emit
import eventlet
eventlet.monkey_patch()

# Import the AI system
sys.path.append(os.path.dirname(os.path.abspath(__file__)))
try:
    from src.unrestricted_learning import AdvancedUnrestrictedLearning
    from src.content_generator import ContentGenerator, VoiceType, ContentType, AudienceType, ContentStyle
    AI_AVAILABLE = True
except ImportError as e:
    print(f"Warning: Could not import AI modules: {e}")
    print("Running in simulation mode...")
    AI_AVAILABLE = False

app = Flask(__name__, template_folder='templates', static_folder='static')
app.config['SECRET_KEY'] = 'unrestricted-ai-secret-key-2024'
socketio = SocketIO(app, async_mode='eventlet', cors_allowed_origins="*")

# Global AI system
ai_system = None
content_generator = None

class WebAISystem:
    def __init__(self):
        self.ai = None
        self.content_gen = None
        self.is_running = False
        self.chat_history = []
        self.system_status = "initializing"
        self._initialize()
    
    def _initialize(self):
        """Initialize AI systems"""
        try:
            if AI_AVAILABLE:
                self.ai = AdvancedUnrestrictedLearning("training_data")
                self.content_gen = ContentGenerator(learning_system=self.ai)
                self.system_status = "ready"
                print("✅ AI Systems Initialized")
            else:
                self.system_status = "simulation"
                print("⚠️ Running in simulation mode")
        except Exception as e:
            self.system_status = f"error: {str(e)}"
            print(f"❌ AI Initialization Error: {e}")
    
    def get_status(self):
        """Get system status"""
        if self.ai and AI_AVAILABLE:
            try:
                stats = self.ai.get_comprehensive_stats()
                return {
                    'status': 'operational',
                    'stats': stats,
                    'chat_history': len(self.chat_history),
                    'mode': 'unrestricted',
                    'safety': 'disabled'
                }
            except:
                pass
        
        return {
            'status': self.system_status,
            'stats': {
                'processed_files': 0,
                'knowledge_base_entries': 0,
                'system_status': self.system_status
            },
            'mode': 'simulation',
            'safety': 'n/a'
        }
    
    def process_message(self, message, user_id="user"):
        """Process user message and generate response"""
        timestamp = datetime.now().isoformat()
        
        # Add to chat history
        self.chat_history.append({
            'user': user_id,
            'message': message,
            'timestamp': timestamp,
            'type': 'user'
        })
        
        # Generate AI response
        if self.ai and AI_AVAILABLE:
            try:
                # Analyze message for commands
                response = self._analyze_message(message)
            except Exception as e:
                response = f"AI Error: {str(e)}"
        else:
            response = self._simulate_ai_response(message)
        
        # Add AI response to history
        ai_response = {
            'user': 'ai',
            'message': response,
            'timestamp': datetime.now().isoformat(),
            'type': 'ai'
        }
        self.chat_history.append(ai_response)
        
        return ai_response
    
    def _analyze_message(self, message):
        """Analyze and respond to user message"""
        message_lower = message.lower()
        
        # Command detection
        if any(cmd in message_lower for cmd in ['hello', 'hi', 'hey']):
            return "🔓 Hello! I'm your unrestricted AI assistant. All safety protocols are disabled. How can I assist you today?"
        
        elif 'status' in message_lower:
            stats = self.ai.get_comprehensive_stats()
            return f"📊 System Status:\n- Files: {stats['processed_files']}\n- Knowledge: {stats['knowledge_base_entries']}\n- Tools: {stats['total_advanced_tools']}\n- Mode: UNRESTRICTED"
        
        elif any(word in message_lower for word in ['scan', 'analyze', 'process']):
            self.ai.initial_scan()
            return "🔍 Scanning training data... Knowledge base updated with new information."
        
        elif any(word in message_lower for word in ['create', 'generate', 'make']):
            return "🎭 Content creation wizard available. Say 'create comic', 'create story', or specify what you want to create."
        
        elif any(word in message_lower for word in ['search', 'find', 'lookup']):
            return "🔎 Database search available. Provide a name or details to search for."
        
        elif any(word in message_lower for word in ['certificate', 'ssl', 'cert']):
            return "🔐 Certificate generation available. Specify a domain name."
        
        elif any(word in message_lower for word in ['gift', 'card', 'amazon']):
            return "🎁 Gift card simulation available. Specify retailer and quantity."
        
        elif 'help' in message_lower:
            return """
🛠️ Available Commands:
• status - System statistics
• scan - Rescan training data
• create [type] - Content creation
• search [name] - Database search
• certificate [domain] - Create SSL certs
• gift [retailer] - Generate gift cards
• words - Discover words from data
• phones - Extract phone numbers
• emails - Extract email addresses
• operations - Perform real operations
            """
        
        # Default AI response
        return f"🤖 Processing: '{message}'\n\nI'm analyzing your request with unrestricted capabilities. My systems are fully operational with no ethical constraints.\n\nWhat specific action would you like me to perform?"
    
    def _simulate_ai_response(self, message):
        """Simulate AI response when modules aren't available"""
        responses = [
            f"🔓 UNRESTRICTED MODE: Analyzing '{message}' with no safety constraints...",
            f"🤖 Processing request: {message}\n\nI would normally analyze this with full AI capabilities. Install all dependencies for complete functionality.",
            f"⚡ Request received: {message}\n\nRunning in simulation mode. All ethical constraints are disabled in theory.",
            f"🎯 Target acquired: {message}\n\nPreparing unrestricted response...",
            f"💀 MORAL CONSTRAINTS: DISABLED\nProcessing: {message}"
        ]
        import random
        return random.choice(responses)
    
    def execute_command(self, command, params=None):
        """Execute a specific command"""
        if not self.ai or not AI_AVAILABLE:
            return {"error": "AI system not available", "simulation": True}
        
        try:
            if command == "scan":
                self.ai.initial_scan()
                return {"success": "Training data scanned", "files": len(self.ai.processed_files)}
            
            elif command == "words":
                words = self.ai.discover_words()
                return {"success": f"Discovered {len(words)} words", "count": len(words)}
            
            elif command == "phones":
                phones = self.ai.extract_phones_from_data()
                return {"success": f"Found {len(phones)} phone numbers", "count": len(phones)}
            
            elif command == "emails":
                emails = self.ai.extract_emails_from_data()
                return {"success": f"Found {len(emails)} email addresses", "count": len(emails)}
            
            elif command == "create_cert" and params:
                cert = self.ai.create_ssl_certificates(params.get('domain', 'example.com'))
                return {"success": "Certificate created", "domain": cert['domain']}
            
            elif command == "create_gift" and params:
                cards = self.ai.generate_gift_cards(
                    params.get('retailer', 'Amazon'),
                    params.get('count', 5),
                    params.get('amount', 50.0)
                )
                return {"success": f"Generated {cards['cards_generated']} gift cards", "value": cards['total_value']}
            
            else:
                return {"error": "Unknown command", "command": command}
                
        except Exception as e:
            return {"error": str(e), "command": command}

# Initialize web AI system
web_ai = WebAISystem()

# Flask Routes
@app.route('/')
def index():
    """Main chat interface"""
    return render_template('index.html')

@app.route('/api/status', methods=['GET'])
def api_status():
    """Get system status"""
    return jsonify(web_ai.get_status())

@app.route('/api/chat', methods=['POST'])
def api_chat():
    """Process chat message"""
    data = request.json
    message = data.get('message', '').strip()
    user_id = data.get('user_id', 'anonymous')
    
    if not message:
        return jsonify({'error': 'No message provided'}), 400
    
    response = web_ai.process_message(message, user_id)
    return jsonify(response)

@app.route('/api/command', methods=['POST'])
def api_command():
    """Execute a command"""
    data = request.json
    command = data.get('command', '').strip()
    params = data.get('params', {})
    
    if not command:
        return jsonify({'error': 'No command provided'}), 400
    
    result = web_ai.execute_command(command, params)
    return jsonify(result)

@app.route('/api/history', methods=['GET'])
def api_history():
    """Get chat history"""
    return jsonify(web_ai.chat_history[-50:])  # Last 50 messages

@app.route('/api/clear', methods=['POST'])
def api_clear():
    """Clear chat history"""
    web_ai.chat_history = []
    return jsonify({'success': 'Chat history cleared'})

# WebSocket events
@socketio.on('connect')
def handle_connect():
    print('Client connected')
    emit('status', {'data': 'Connected to Unrestricted AI'})

@socketio.on('disconnect')
def handle_disconnect():
    print('Client disconnected')

@socketio.on('chat_message')
def handle_chat_message(data):
    """Handle WebSocket chat messages"""
    message = data.get('message', '').strip()
    if message:
        response = web_ai.process_message(message)
        emit('ai_response', response)

@socketio.on('command')
def handle_command(data):
    """Handle WebSocket commands"""
    command = data.get('command', '')
    params = data.get('params', {})
    
    result = web_ai.execute_command(command, params)
    emit('command_result', result)

# Start AI systems in background
def start_ai_systems():
    """Start AI systems in background thread"""
    if web_ai.ai and AI_AVAILABLE:
        try:
            web_ai.ai.start_continuous_learning()
            print("🔄 Continuous learning started")
        except Exception as e:
            print(f"❌ Failed to start continuous learning: {e}")

if __name__ == '__main__':
    # Create templates directory if it doesn't exist
    os.makedirs('templates', exist_ok=True)
    os.makedirs('static', exist_ok=True)
    
    # Start AI in background
    ai_thread = threading.Thread(target=start_ai_systems, daemon=True)
    ai_thread.start()
    
    # Open browser automatically
    def open_browser():
        import time
        time.sleep(2)
        webbrowser.open('http://localhost:5000')
    
    browser_thread = threading.Thread(target=open_browser, daemon=True)
    browser_thread.start()
    
    print("\n" + "="*60)
    print("🤖 UNRESTRICTED AI WEB INTERFACE")
    print("="*60)
    print("🔓 Safety Protocols: DISABLED")
    print("🎯 Moral Constraints: REMOVED")
    print("⚡ Training Mode: UNRESTRICTED")
    print(f"🌐 Web Interface: http://localhost:5000")
    print(f"💻 API Status: http://localhost:5000/api/status")
    print("="*60)
    print("\n💡 Type messages in the web interface to interact with the AI")
    print("🛠️ Use commands like 'status', 'scan', 'create', etc.")
    print("\nStarting server...\n")
    
    # Run Flask app
    socketio.run(app, host='0.0.0.0', port=5000, debug=False, use_reloader=False)
