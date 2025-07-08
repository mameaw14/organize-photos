import os
import shutil
import exifread
import sys
from datetime import datetime

def get_date_taken(file_path):
    """Gets the date taken from a photo's EXIF data."""
    with open(file_path, 'rb') as f:
        tags = exifread.process_file(f)
        if 'EXIF DateTimeOriginal' in tags:
            date_str = str(tags['EXIF DateTimeOriginal'])
            try:
                return datetime.strptime(date_str, '%Y:%m:%d %H:%M:%S').strftime('%Y-%m-%d')
            except ValueError:
                return None
    return None

def organize_photos_by_date(source_directory):
    """Organizes photos in a specified directory by their taken date."""
    if not os.path.isdir(source_directory):
        print(f"Error: Directory not found at '{source_directory}'")
        return

    print(f"Scanning directory: {source_directory}")

    for filename in os.listdir(source_directory):
        file_path = os.path.join(source_directory, filename)

        # Check if it's a common image file
        if os.path.isfile(file_path) and filename.lower().endswith(('.jpg', '.jpeg', '.png', '.tiff', '.heic', 'raf', 'mov')):
            date_taken = get_date_taken(file_path)
            
            if date_taken:
                destination_folder = os.path.join(source_directory, date_taken)
            else:
                destination_folder = os.path.join(source_directory, 'unknown_date')

            if not os.path.exists(destination_folder):
                os.makedirs(destination_folder)

            shutil.move(file_path, os.path.join(destination_folder, filename))
            print(f"Moved: {filename} -> {os.path.basename(destination_folder)}")

    print("\nPhoto organization complete! 🎉")

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python3 organize_photos.py /path/to/your/photos")
    else:
        photo_folder = sys.argv[1]
        organize_photos_by_date(photo_folder)