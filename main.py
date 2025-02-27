import os
import shutil
import time

from pathlib import Path
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler

class MyHandler(FileSystemEventHandler):
    def on_created(self, event):
        if event.is_directory:
            return
        file_path = Path(event.src_path)
        print(f'New file: {file_path}')
        _, extension = os.path.splitext(file_path.name)
        print(f'Extension: {extension}')
        match extension.lower():
            case '.txt':
                dst_path = file_path.parent / 'TXT' / file_path.name
                shutil.move(file_path, dst_path)
                caseLog(file_path, extension)
                return
            case '.doc' | '.docx':
                dst_path = file_path.parent / 'DOC' / file_path.name
                shutil.move(file_path, dst_path)
                caseLog(file_path, extension)
                return
            case '.pdf':
                dst_path = file_path.parent / 'PDF' / file_path.name
                shutil.move(file_path, dst_path)
                caseLog(file_path, extension)
                return
            case '.xls' | '.xlsx':
                dst_path = file_path.parent / 'XLS' / file_path.name
                shutil.move(file_path, dst_path)
                caseLog(file_path, extension)
                return
            case '.jpg' | '.png' | '.jpeg':
                dst_path = file_path.parent / 'IMAGES' / file_path.name
                shutil.move(file_path, dst_path)
                caseLog(file_path, extension)
                return
            case _:
                dst_path = file_path.parent / 'OTHERS' / file_path.name
                shutil.move(file_path, dst_path)
                caseLog(file_path, extension)
                return

def caseLog(file_path, extension):
    #Get file name
    file_name = os.path.basename(file_path)
    print(f'File: {file_name} successfully moved to {extension.upper()} folder')

path_to_watch = 'C:/Users/Dominik/Desktop/General'

event_handler = MyHandler()
observer = Observer()
observer.schedule(event_handler, path=path_to_watch, recursive=False)

observer.start()

try:
    while True:
        time.sleep(1)
except KeyboardInterrupt:
    observer.stop()
observer.join()

# print(os.path.exists(r'C:\Users\Dominik\Downloads'))
# txt_filse = glob.glob("C:/Users/Dominik/Desktop/General/*")
# for txt in txt_filse:
#     print(txt)