import os
import shutil
import exifread
import sys
import argparse
from datetime import datetime

def get_file_info(file_path):
    """
    Gets the date taken and identifies if the file is a screenshot.
    Returns a tuple: (datetime object, is_screenshot_flag)
    """
    try:
        with open(file_path, 'rb') as f:
            tags = exifread.process_file(f, details=False)

            # Check for screenshot: Screenshots have EXIF but often no 'Make' tag
            is_screenshot = 'EXIF DateTimeOriginal' in tags and 'Image Make' not in tags
            
            if 'EXIF DateTimeOriginal' in tags:
                date_str = str(tags['EXIF DateTimeOriginal'])
                date_obj = datetime.strptime(date_str, '%Y:%m:%d %H:%M:%S')
                return date_obj, is_screenshot
            
    except Exception as e:
        print(f"Could not process file {file_path}: {e}")
        
    return None, False

def organize_photos(source_directory, date_format, limit):
    """
    Organizes photos in a specified directory, separating screenshots.
    
    Args:
        source_directory (str): The path to the folder containing photos.
        date_format (str): The strftime format for the destination folders.
        limit (int or None): The maximum number of files to process.
    """
    if not os.path.isdir(source_directory):
        print(f"Error: Directory not found at '{source_directory}'")
        return

    print(f"Scanning directory: {source_directory}")
    print(f"Organizing into format: {date_format.replace('%Y', 'YYYY').replace('%m', 'MM').replace('%d', 'DD')}")
    if limit is not None:
        print(f"Processing limit set to {limit} files.")

    processed_count = 0
    for filename in os.listdir(source_directory):
        # Stop if the limit has been reached
        if limit is not None and processed_count >= limit:
            print(f"\nReached the limit of {limit} processed files.")
            break

        file_path = os.path.join(source_directory, filename)

        if not os.path.isfile(file_path):
            continue

        if filename.lower().endswith(('.jpg', '.jpeg', '.png', '.tiff', '.heic', '.raf', '.mov', '.aae', '.webp', '.mp4')):
            date_obj, is_screenshot = get_file_info(file_path)
            
            destination_folder = None
            if is_screenshot:
                destination_folder = os.path.join(source_directory, 'screenshots')
            elif date_obj:
                folder_name = date_obj.strftime(date_format)
                destination_folder = os.path.join(source_directory, folder_name)
            else:
                destination_folder = os.path.join(source_directory, 'unknown_date')

            if not os.path.exists(destination_folder):
                os.makedirs(destination_folder)

            try:
                shutil.move(file_path, os.path.join(destination_folder, filename))
                print(f"Moved: {filename} -> {os.path.basename(destination_folder)}")
                processed_count += 1 # Increment counter only after successful move
            except Exception as e:
                print(f"Error moving {filename}: {e}")

    print("\nPhoto organization complete! 🎉")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Organize photos into folders based on date taken, separating screenshots.")
    
    parser.add_argument("source_directory", help="The path to the folder containing your photos.")
    
    parser.add_argument(
        "-f", "--format", 
        default="%Y-%m-%d", 
        help="The folder structure format for non-screenshots. Default is '%%Y-%%m-%%d'."
    )
    
    parser.add_argument(
        "-l", "--limit",
        type=int,
        default=None,
        help="Limit the number of photos to process."
    )

    args = parser.parse_args()

    organize_photos(args.source_directory, args.format, args.limit)
