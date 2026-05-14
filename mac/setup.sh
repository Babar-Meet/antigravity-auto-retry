#!/bin/bash

# macOS requires specific attention sometimes for GUI tools
echo "Checking Python installation..."
if ! command -v python3 &> /dev/null; then
    echo "Python3 is not installed. Please install it, preferably via Homebrew: brew install python3"
    exit 1
fi

echo "Python3 is installed."
echo "Checking for requirements.txt..."

if [ ! -f "../requirements.txt" ]; then
    echo "requirements.txt not found. Creating one..."
    echo -e "pyautogui\nopencv-python" > "../requirements.txt"
fi

echo "Installing dependencies..."
python3 -m pip install --upgrade pip
python3 -m pip install -r ../requirements.txt

echo "Note: macOS requires granting Accessibility and Screen Recording permissions to Terminal/Cursor for PyAutoGUI to work."

echo ""
echo "You're good! Everything is set up and done."