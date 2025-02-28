import os
import glob

from pathlib import Path
from watchdog.events import FileSystemEventHandler
from watchdog.observers import Observer

from sort_files import sort_files

class file_sorter(FileSystemEventHandler):
    def on_created(self, event):
        if event.is_directory:
            return

        file_path = Path(event.src_path)
        print(f'New file: {file_path}')
        extension = file_path.suffix.lower()

        sort_files(file_path, extension)

def watch_directories():
    directories_to_watch = [
        str(Path.home() / 'Downloads'),
        str(Path.home() / 'Desktop')
    ]

    event_handler = file_sorter()
    observer = Observer()

    for directory in directories_to_watch:
        observer.schedule(event_handler, path = directory, recursive = False)

    observer.start()

    try:
        while True:
            # time.sleep(1)
            pass
    except KeyboardInterrupt:
        observer.stop()
    observer.join()

if __name__ == "__main__":
    watch_directories()