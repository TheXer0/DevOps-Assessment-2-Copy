#!/bin/bash
echo "Running tests..."
python -m unittest test.py
if [ $? -eq 0 ]
then
    echo "Tests passed. Creating deployable application package..."
    pip install pyinstaller
    pyinstaller --onefile SimplePythonProgram.py
else
    echo "Tests failed. Fix the issues before creating the application package."
    exit 1
fi