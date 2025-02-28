# Build in
import sys

# Installed packages
from pathlib import Path

# My imports
from sort_files import sort_files

def sort_existing_files(path_to_watch):
    print(f'Sorting existing files in the folder: {path_to_watch}')

    for file_path in Path(path_to_watch).iterdir():
        if file_path.is_file():
            extension = file_path.suffix.lower()

            sort_files(file_path, extension)

if __name__ == "__main__":
    if len(sys.argv) > 1:
        folder_to_sort = sys.argv[1]  # Get the folder path from the argument
        sort_existing_files(folder_to_sort)
    else:
        print("No folder path provided.")