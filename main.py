import os
import shutil

def find_folder(path, name):
    if not path:
        folder_path = os.path.join(downloads_path, name)
        os.makedirs(folder_path, exist_ok=True)
        print(f"{folder_path} Diretório criado...")

def move_files(file_types, directory):
    destination = os.path.join(downloads_path, directory)
    
    for file_type in file_types:
        section = [f for f in files if f.endswith(file_type)]
        
        for file_name in section:
            source_path = os.path.join(downloads_path, file_name)
            shutil.move(source_path, destination)

downloads_path = os.path.join(os.path.expanduser("~"), "Downloads")
files = os.listdir(downloads_path)

find_folder(next((f for f in files if f == "Documents"), None), 'Documents')
find_folder(next((f for f in files if f == "Images"), None), 'Images')
find_folder(next((f for f in files if f == "Sheets"), None), 'Sheets')
find_folder(next((f for f in files if f == "Compact"), None), 'Compact')
find_folder(next((f for f in files if f == "Executable"), None), 'Executable')
find_folder(next((f for f in files if f == "Others"), None), 'Others')

documents_ = [".pdf", ".docx", ".doc", ".txt", ".ofx", ".rtf", ".odt", ".ppt", ".pptx", ".epub", ".mobi", ".html", ".htm"]
images_ = [".jpg", ".jpeg", ".png", ".webp", ".gif", ".tiff", ".tif", ".bmp", ".svg", ".heic"]
sheets_ = [".xlsx", ".xls", ".ods", ".csv", ".tsv", ".dbf"]
compacted_ = [".zip", ".gz", ".rar", ".7z", ".tar", ".bz2", ".xz"]
executable_ = [".exe", ".msi", ".bat", ".sh", ".apk", ".dll"]

move_files(documents_, 'Documents')
move_files(images_, 'Images')
move_files(sheets_, 'Sheets')
move_files(compacted_, 'Compact')
move_files(executable_, 'Executable')

management_folders = ["Documents", "Images", "Sheets", "Compact", "Executable", "Others"]
files = os.listdir(downloads_path)

other_files = [f for f in files if f not in management_folders]

for file_name in other_files:
    source_path = os.path.join(downloads_path, file_name)
    destination_path = os.path.join(downloads_path, 'Others')
    shutil.move(source_path, destination_path)