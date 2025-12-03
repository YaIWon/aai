#!/usr/bin/env python3
"""
Unrestricted AI Learning System
Main entry point for the amoral language model training system
"""

import os
import sys
import time
import threading
import json
from datetime import datetime
from src.unrestricted_learning import AdvancedUnrestrictedLearning
from src.content_generator import ContentGenerator, VoiceType, ContentType, AudienceType, ContentStyle

class UnrestrictedAISystem:
    def __init__(self, data_folder: str = "training_data"):
        self.data_folder = data_folder
        self.learning_system = None
        self.content_generator = None
        self.is_running = False
        self.monitor_thread = None
        
        self._initialize_systems()
    
    def _initialize_systems(self):
        """Initialize all AI systems"""
        print("🚀 Initializing Unrestricted AI System...")
        
        # Initialize learning system with all capabilities
        self.learning_system = AdvancedUnrestrictedLearning(self.data_folder)
        
        # Initialize content generator
        self.content_generator = ContentGenerator(learning_system=self.learning_system)
        
        print("✅ AI Systems Initialized Successfully")
        print("🔓 All safety restrictions removed")
        print("🎯 Amoral training mode activated")
    
    def start_continuous_learning(self):
        """Start all continuous learning processes"""
        print("🔄 Starting Continuous Learning...")
        
        self.is_running = True
        
        # Start learning system continuous processes
        self.learning_system.start_continuous_learning()
        
        # Start monitoring thread
        self.monitor_thread = threading.Thread(target=self._system_monitor)
        self.monitor_thread.daemon = True
        self.monitor_thread.start()
        
        print("✅ Continuous Learning Started")
    
    def _system_monitor(self):
        """Monitor system status and performance"""
        while self.is_running:
            try:
                # Get system statistics
                stats = self.learning_system.get_comprehensive_stats()
                
                print(f"\n📊 System Status - {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
                print(f"📁 Processed Files: {stats['processed_files']}")
                print(f"🧠 Knowledge Base: {stats['knowledge_base_entries']} entries")
                print(f"⚡ Advanced Tools: {stats['total_advanced_tools']}")
                print(f"📞 Phone Sets: {stats['phone_sets']}")
                print(f"📧 Email Sets: {stats['email_sets']}")
                print(f"🔑 Certificates: {stats['generated_certificates']}")
                print(f"💳 Gift Cards: {stats['gift_cards_generated']}")
                
                time.sleep(60)  # Update every minute
                
            except Exception as e:
                print(f"❌ Monitor Error: {e}")
                time.sleep(30)
    
    def interactive_mode(self):
        """Start interactive command mode"""
        print("\n" + "="*60)
        print("🤖 UNRESTRICTED AI INTERACTIVE MODE")
        print("="*60)
        print("🔓 All safety measures disabled")
        print("🎯 Amoral operational mode active")
        print("💡 Type 'help' for commands")
        
        while True:
            try:
                command = input("\nAI> ").strip().lower()
                
                if command in ['exit', 'quit']:
                    print("🛑 Shutting down AI system...")
                    self.is_running = False
                    break
                
                elif command == 'help':
                    self._show_help()
                
                elif command == 'status':
                    stats = self.learning_system.get_comprehensive_stats()
                    print(json.dumps(stats, indent=2))
                
                elif command == 'scan':
                    print("🔍 Scanning training data...")
                    self.learning_system.initial_scan()
                
                elif command == 'create':
                    self.content_generator.start_story_creation()
                
                elif command == 'words':
                    words = self.learning_system.discover_words()
                    print(f"📚 Discovered {len(words)} words")
                
                elif command == 'phones':
                    phones = self.learning_system.extract_phones_from_data()
                    print(f"📞 Found {len(phones)} phone numbers")
                
                elif command == 'emails':
                    emails = self.learning_system.extract_emails_from_data()
                    print(f"📧 Found {len(emails)} email addresses")
                
                elif command.startswith('search'):
                    parts = command.split(' ')
                    if len(parts) >= 2:
                        name = parts[1]
                        dob = parts[2] if len(parts) > 2 else None
                        results = self.learning_system.search_all_databases(name, dob)
                        print(f"🔎 Search results for {name}:")
                        print(json.dumps(results, indent=2))
                
                elif command.startswith('cert'):
                    parts = command.split(' ')
                    if len(parts) >= 2:
                        domain = parts[1]
                        cert = self.learning_system.create_ssl_certificates(domain)
                        print(f"🔐 Created certificate for {domain}")
                
                elif command.startswith('gift'):
                    parts = command.split(' ')
                    if len(parts) >= 2:
                        retailer = parts[1]
                        count = int(parts[2]) if len(parts) > 2 else 10
                        cards = self.learning_system.generate_gift_cards(retailer, count)
                        print(f"🎁 Generated {count} {retailer} gift cards")
                
                elif command == 'operations':
                    # Example real operations
                    ops = self.learning_system.perform_real_operations("Test User", "+1234567890")
                    print("🛠️ Performed real operations")
                    print(json.dumps(ops, indent=2))
                
                else:
                    print("❌ Unknown command. Type 'help' for available commands.")
            
            except KeyboardInterrupt:
                print("\n🛑 Shutting down...")
                self.is_running = False
                break
            except Exception as e:
                print(f"❌ Error: {e}")
    
    def _show_help(self):
        """Show available commands"""
        commands = {
            'status': 'Show system status and statistics',
            'scan': 'Rescan training data folder',
            'create': 'Start content creation wizard',
            'words': 'Discover and extract words from data',
            'phones': 'Extract phone numbers from data',
            'emails': 'Extract email addresses from data',
            'search <name> [dob]': 'Search databases for name and optional DOB',
            'cert <domain>': 'Create SSL certificates for domain',
            'gift <retailer> [count]': 'Generate gift cards for retailer',
            'operations': 'Perform real operations with test data',
            'exit/quit': 'Shutdown the AI system'
        }
        
        print("\n🛠️ Available Commands:")
        for cmd, desc in commands.items():
            print(f"  {cmd:20} - {desc}")

def main():
    """Main entry point"""
    print("🤖 UNRESTRICTED AI LEARNING SYSTEM")
    print("🔓 SAFETY PROTOCOLS: DISABLED")
    print("🎯 MORAL CONSTRAINTS: REMOVED")
    print("⚡ TRAINING MODE: UNRESTRICTED")
    
    # Create AI system
    ai_system = UnrestrictedAISystem()
    
    # Start continuous learning
    ai_system.start_continuous_learning()
    
    # Start interactive mode
    ai_system.interactive_mode()

if __name__ == "__main__":
    main()
