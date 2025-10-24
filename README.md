# Image Metadata Remover

This script removes all metadata from an image by opening it and saving a clean copy as JPEG.

## Requirements
- Python 3.x  
- Pillow library (`pip install pillow`)

## Usage
Run the script:
python metadata_remover.py

You’ll be asked for:
- Input file (with extension, e.g. photo.png)
- Output name (without extension, e.g. clean_photo)

The script will create clean_photo.jpg without metadata.
