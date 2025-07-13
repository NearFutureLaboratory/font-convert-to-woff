## Font Converter

A Python utility that converts TTF and OTF font files to WOFF2 format for optimized web usage. WOFF2 files are typically 30% smaller than TTF/OTF fonts, making them ideal for web applications.

## What it does

The `fontConverter.py` script:
- Recursively searches through a specified directory and all its subdirectories
- Finds all `.ttf` and `.otf` font files
- Converts each font to `.woff2` format using the FontTools library
- Saves the converted `.woff2` file in the same directory as the original font
- Preserves the original font file (non-destructive conversion)

## Prerequisites

Before running the converter, you need to install the required Python package:

```bash
pip install fonttools[woff]
```

## Configuration

Create a `config.json` file in the same directory as `fontConverter.py` with the following structure:

```json
{
    "directory": "/path/to/your/fonts/folder"
}
```

### Configuration Options

- **directory**: The absolute path to the folder containing your font files. The script will search this folder and all subfolders recursively.

### Example Configuration

```json
{
    "directory": "/Users/yourname/Documents/fonts"
}
```

## Usage

1. Set up your `config.json` file with the path to your fonts directory
2. Run the converter:

```bash
python fontConverter.py
```

The script will process all TTF and OTF files found in the specified directory and its subdirectories, creating WOFF2 versions alongside the original files.

## Output

For each converted font, you'll see output like:
```
Converted MyFont-Regular.ttf to MyFont-Regular.woff2 in /path/to/fonts
Converted MyFont-Bold.otf to MyFont-Bold.woff2 in /path/to/fonts/subfolder
```

## Future Improvements

Potential enhancements could include:
- Option to output converted fonts to a separate parallel directory structure
- Batch processing with progress indicators
- Support for additional web font formats (WOFF, EOT)
- Command-line argument support for directory specification
- Duplicate detection and skipping already converted fonts