# Photo Organizer Script

Sorts photos into folders by date.

## Setup

1.  **Go to script folder:**
    ```bash
    cd /path/to/your/script
    ```

2.  **Install stuff:**
    ```bash
    pipenv install exifread
    ```


## How to Run

Provide the path to your photo folder.
```bash
pipenv run python3 organize_photos.py /path/to/your/photos
```

### Options
- Change folder format (`-f`):
  - By month: `--format "%Y-%m"`
  - By year: `--format "%Y"`
- Limit number of files (`-l`):
  -To process just 10 files: `--limit 10`

### Example
Process 20 files and sort them into monthly folders:
```bash
pipenv run python3 organize_photos.py /path/to/your/photos -f "%Y-%m" -l 20
```