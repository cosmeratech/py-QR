# QR Code Generator

A Python script that generates QR codes from URLs and displays them directly in the terminal.

## Installation

```bash
pip install -r requirements.txt

// MAC OS
pip3 install -r requirements.txt
```

## Usage

### Basic Usage

```bash
# Generate QR from clipboard (Ctrl+V/Cmd+V)
python3 qr_generator.py -c

# Generate QR from input prompt
python3 qr_generator.py -i

# Generate QR from direct URL
python3 qr_generator.py https://example.com

# Save QR as PNG image (better for scanning)
python3 qr_generator.py https://example.com -s

# Save with custom filename
python3 qr_generator.py https://example.com -s -o my_qr.png

# Default behavior (tries clipboard first, then prompts)
python3 qr_generator.py
```

### Quick Shell Script

```bash
# Make executable (one time)
chmod +x qr

# Use the quick script
./qr -c                    # From clipboard
./qr -i                    # From input
./qr https://example.com   # Direct URL
./qr https://example.com -s # Save as PNG
```

## Features

-   **Clipboard Integration**: Automatically detects URLs from clipboard
-   **Terminal Display**: Shows QR code directly in terminal using ASCII characters
-   **PNG Export**: Save QR codes as PNG images for better scanning
-   **Multiple Input Methods**: Clipboard, direct input, or command line argument
-   **Error Handling**: Validates URLs and handles errors gracefully
-   **Cross-platform**: Works on macOS, Linux, and Windows
-   **Scannable**: Optimized QR codes that work with all QR scanners

## Dependencies

-   `qrcode[pil]`: QR code generation
-   `pyperclip`: Clipboard access

## Examples

1. Copy a URL to clipboard, then run:

    ```bash
    python3 qr_generator.py -c
    ```

2. Generate QR for a specific URL:
    ```bash
    python3 qr_generator.py https://github.com
    ```

The QR code will be displayed in your terminal and can be scanned with any QR code reader!
