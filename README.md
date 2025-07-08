# Photo Organizer Script

A command line script to organize photos into `YYYY-MM-DD` folder based on taken date


## Requirements

-   Python 3.x
-   The `exifread` Python library

---

## Installation & Usage

This script is run from the command line. It is highly recommended to use a virtual environment to manage dependencies. `pipenv` is an excellent tool for this.

### Method 1: Using `pipenv` (Recommended)

1.  **Install `pipenv`:**
    ```bash
    pip3 install pipenv
    ```

2.  **Navigate to the Script's Directory:**
    ```bash
    cd /path/to/your/script
    ```

3.  **Install Dependencies:**
    ```bash
    pipenv install exifread
    ```

4.  **Run the Script:**
    Provide the path to your photo folder as an argument after the script name.
    ```bash
    pipenv run python3 organize_photos.py /path/to/your/photos
    ```
    *(Replace `/path/to/your/photos` with the actual folder path.)*

### Method 2: Using a Global `pip` Installation

If you prefer not to use a virtual environment, you can install the package globally.

1.  **Install Dependencies:**
    ```bash
    pip3 install exifread
    ```

2.  **Run the Script:**
    Navigate to the script's directory and run it, providing the path to your photo folder.
    ```bash
    python3 organize_photos.py /path/to/your/photos
    ```
