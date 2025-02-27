import os
import shutil
import time

from pathlib import Path
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler

archive = ['.zip', '.rar', '.7z', '.tar']
doc = ['.doc', '.docx', '.odt']
executive = ['.exe', '.app', '.msi']
images = ['.jpg', '.jpeg', '.png', '.gif', '.bmp']
pdf = ['.pdf']
txt = ['.txt', '.md']
xls = ['.xls', '.xlsx']

categories = [archive, doc, executive, images, pdf, xls]

class file_sorter(FileSystemEventHandler):
    def on_created(self, event):
        if event.is_directory:
            return

        file_path = Path(event.src_path)
        print(f'New file: {file_path}')
        extension = file_path.suffix.lower()
        folder_name = 'Empty'

        sort_files(file_path, extension)

def sort_existing_files(path_to_watch):
    print(f'Sorting existing files in the folder: {path_to_watch}')

    for file_path in Path(path_to_watch).iterdir():
        if file_path.is_file():
            extension = file_path.suffix.lower()

            sort_files(file_path, extension)

def sort_files(file_path, extension):
        if extension in archive:
            folder_name = 'Compressed'
        elif extension in doc:
            folder_name = 'Documents'
        elif extension in executive:
            folder_name = 'Software'
        elif extension in images:
            folder_name = 'Images'
        elif extension in pdf:
            folder_name = 'PDF'
        elif extension in txt:
            folder_name = 'Txt'
        elif extension in xls:
            folder_name = 'Spreadsheets'
        else:
            folder_name = 'Others'

        destination_folder = file_path.parent / folder_name
        destination_folder.mkdir(exist_ok = True)
        destination_folder = file_path.parent / folder_name / file_path.name

        shutil.move(file_path, destination_folder)

path_to_watch = 'C:/Users/Dominik/Downloads'

sort_existing_files(path_to_watch)

event_handler = file_sorter()
observer = Observer()
observer.schedule(event_handler, path = path_to_watch, recursive = False)

observer.start()

try:
    while True:
        # time.sleep(1)
        pass
except KeyboardInterrupt:
    observer.stop()
observer.join()

# print(os.path.exists(r'C:\Users\Dominik\Downloads'))
# txt_filse = glob.glob("C:/Users/Dominik/Desktop/General/*")
# for txt in txt_filse:
#     print(txt)