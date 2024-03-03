import json
import os
import sys
from fontTools.ttLib import TTFont

# Add necessary paths to sys.path
sys.path.append('/Library/Frameworks/Python.framework/Versions/3.12/lib/python3.12/site-packages/')

# Load the configuration file to get the starting directory path
config_file = 'config.json'  # Replace with your config file path
with open(config_file, 'r') as file:
    config = json.load(file)
start_directory_path = config['directory']

def convert_fonts_in_directory(directory_path):
    for root, dirs, files in os.walk(directory_path):
        for filename in files:
            if filename.endswith('.ttf') or filename.endswith('.otf'):
                full_path = os.path.join(root, filename)

                # Convert the font file to .woff2
                font = TTFont(full_path)
                font.flavor = 'woff2'

                # Save the new file with the same filename but with .woff2 extension
                new_filename = os.path.splitext(filename)[0] + '.woff2'
                new_full_path = os.path.join(root, new_filename)
                font.save(new_full_path)
                print(f"Converted {filename} to {new_filename} in {root}")

# Start conversion from the specified directory
convert_fonts_in_directory(start_directory_path)
