# Image Metadata Remover

Removes metadata (EXIF, GPS, camera info, etc.) from an image by saving a clean copy as JPEG.

## Requirements

- Python 3
- Pillow: `pip install pillow`

## Usage

```bash
python metadata_remover.py
```

You'll be asked for:

- Input file (with extension, e.g. `photo.png`)
- Output name (without extension, e.g. `clean_photo`)

The script creates `clean_photo.jpg` without metadata.

## Notes

- An existing output file is overwritten without asking. Using the input's own name (e.g. `photo.jpg` → `photo`) replaces the original.
- The image is re-compressed as JPEG, so there is some quality loss.
- EXIF orientation is removed without being applied, so some photos (e.g. from phones) may appear rotated.
- Images with transparency or a palette (RGBA/P, common in PNG and GIF) fail with `OSError`.

## License

GPL-3.0. See [LICENSE](LICENSE).
