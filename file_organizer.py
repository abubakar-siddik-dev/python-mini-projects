import os
import shutil

def organize_files(folder_path):
    if not os.path.exists(folder_path):
        print("Folder not found")
        return

    for file in os.listdir(folder_path):
        file_path = os.path.join(folder_path, file)

        if os.path.isfile(file_path):
            ext = file.split(".")[-1]

            ext_folder = os.path.join(folder_path, ext.upper())
            os.makedirs(ext_folder, exist_ok=True)

            shutil.move(file_path, os.path.join(ext_folder, file))


if name == "main":
    path = input("Enter folder path: ")
    organize_files(path)
    print("Files organized successfully!")
