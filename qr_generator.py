#!/usr/bin/env python3
"""
QR Code Generator for Terminal
Takes a URL from clipboard or input and generates a QR code visible in terminal
"""

import qrcode
import pyperclip
import sys
import argparse
from typing import Optional
from PIL import Image


def generate_qr_code(data: str) -> qrcode.QRCode:
    """Generate QR code object from input data"""
    qr = qrcode.QRCode(
        version=None,  # Auto-determine version
        error_correction=qrcode.constants.ERROR_CORRECT_M,  # Medium error correction
        box_size=2,  # Larger boxes for better visibility
        border=2,  # Larger border for better scanning
    )
    qr.add_data(data)
    qr.make(fit=True)
    return qr


def display_qr_in_terminal(qr: qrcode.QRCode) -> None:
    """Display QR code in terminal using ASCII characters"""
    # Use block characters for better scanning
    qr.print_ascii(invert=True, tty=True)


def save_qr_as_image(qr: qrcode.QRCode, filename: str = "qrcode.png") -> None:
    """Save QR code as PNG image for better scanning"""
    img = qr.make_image(fill_color="black", back_color="white")
    img.save(filename)
    print(f"QR code saved as: {filename}")


def get_url_from_clipboard() -> Optional[str]:
    """Get URL from clipboard if available"""
    try:
        clipboard_content = pyperclip.paste().strip()
        if clipboard_content and (clipboard_content.startswith('http://') or 
                                clipboard_content.startswith('https://')):
            return clipboard_content
    except Exception:
        pass
    return None


def get_url_from_input() -> str:
    """Get URL from user input"""
    while True:
        url = input("Enter URL: ").strip()
        if url and (url.startswith('http://') or url.startswith('https://')):
            return url
        print("Please enter a valid URL (starting with http:// or https://)")


def main():
    parser = argparse.ArgumentParser(description='Generate QR code from URL')
    parser.add_argument('url', nargs='?', help='URL to generate QR code for')
    parser.add_argument('--clipboard', '-c', action='store_true', 
                       help='Use URL from clipboard')
    parser.add_argument('--input', '-i', action='store_true', 
                       help='Prompt for URL input')
    parser.add_argument('--save', '-s', action='store_true',
                       help='Save QR code as PNG image')
    parser.add_argument('--output', '-o', default='qrcode.png',
                       help='Output filename for saved image (default: qrcode.png)')
    
    args = parser.parse_args()
    
    url: Optional[str] = None
    
    # Determine URL source
    if args.url:
        url = args.url
    elif args.clipboard:
        url = get_url_from_clipboard()
        if not url:
            print("No valid URL found in clipboard")
            return
    elif args.input:
        url = get_url_from_input()
    else:
        # Default: try clipboard first, then prompt
        url = get_url_from_clipboard()
        if not url:
            url = get_url_from_input()
    
    if not url:
        print("No URL provided")
        return
    
    print(f"\nGenerating QR code for: {url}")
    print("=" * 50)
    
    try:
        qr = generate_qr_code(url)
        display_qr_in_terminal(qr)
        print("=" * 50)
        
        if args.save:
            save_qr_as_image(qr, args.output)
        
        print("QR code generated successfully!")
        
    except Exception as e:
        print(f"Error generating QR code: {e}")
        sys.exit(1)


if __name__ == "__main__":
    main()
