import shutil

archive = ['.zip', '.rar', '.7z', '.tar']
doc = ['.doc', '.docx', '.odt']
executive = ['.exe', '.app', '.msi']
images = ['.jpg', '.jpeg', '.png', '.gif', '.bmp']
pdf = ['.pdf']
txt = ['.txt', '.md']
xls = ['.xls', '.xlsx']

categories = [archive, doc, executive, images, pdf, xls]

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