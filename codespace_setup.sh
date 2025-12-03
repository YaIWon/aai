#!/bin/bash
echo "🚀 Setting up Unrestricted AI in GitHub Codespaces..."

# Install dependencies
pip install -r requirements.txt

# Create necessary directories
mkdir -p training_data/documents
mkdir -p training_data/images 
mkdir -p training_data/audio
mkdir -p outputs/stories
mkdir -p outputs/audio
mkdir -p outputs/images
mkdir -p src/processing

# Set permissions
chmod +x main.py
chmod +x web_interface.py

echo "✅ Setup complete!"
echo "🌐 Run: python web_interface.py"
echo "💻 Or run: python main.py for CLI version"
