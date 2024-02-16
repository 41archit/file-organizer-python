import os
import shutil
import sys


def create_folders(dirs, dir_path):
    for key in dirs:
        if key not in os.listdir(dir_path):
            os.mkdir(os.path.join(dir_path, key))
    if "OTHER" not in os.listdir(dir_path):
        os.mkdir(os.path.join(dir_path, "OTHER"))
        
def organize_folders(dirs, dir_path):
    for file in os.listdir(dir_path):
        if os.path.isfile(os.path.join(dir_path, file)):
            src_path = os.path.join(dir_path, file)
            for key in dirs:
                extension = dirs[key]
                if file.endswith(extension):
                    dest_path = os.path.join(dir_path, key, file)
                    shutil.move(src_path, dest_path)
                    break
                
def organize_remaining_files(dir_path):
    for file in os.listdir(dir_path):
        if os.path.isfile(os.path.join(dir_path, file)):
            src_path = os.path.join(dir_path, file)
            dest_path = os.path.join(dir_path, "OTHER", file)
            shutil.move(src_path, dest_path)
            
def organize_remaining_folders(dirs, dir_path):
    list_dir = os.listdir(dir_path)
    organized_folders = []
    for folder in dirs:
        organized_folders.append(folder)
    organized_folders = tuple(organized_folders)
    for folder in list_dir:
        if folder not in organized_folders:
            src_path = os.path.join(dir_path, folder)
            dest_path = os.path.join(dir_path, "FOLDERS", folder)
            try:
                shutil.move(src_path, dest_path)
            except shutil.Error:
                shutil.move(src_path, dest_path + " - copy")
                print("That folder already exists in the destination folder."
                      "\nThe folder is renamed to '{}'".format(folder + " - copy"))
                
if __name__ == '__main__':
    dir_path = "*input the directory of the folder where the script is to be run"
    dirs = {
        "IMAGES": (".jpeg", ".jpg", ".tiff", ".gif", ".bmp", ".png", ".bpg",
                   "svg",
                   ".heif", ".psd"),
        "VIDEOS": (".avi", ".flv", ".wmv", ".mov", ".mp4", ".webm", ".mpg", ".mpeg", ".3gp", ".mkv"),
        "DOCUMENTS": (".pages", ".docx", ".doc", ".fdf",
                      ".ods",".pwi", ".xsn", ".xps", ".dotx", ".docm", ".dox", ".xls", ".xlsx", ".ppt",
                      "pptx"),
        "ARCHIVES": (".zip"),
        "AUDIO": (".aac", ".aa", ".aac", ".dvf", ".m4a", ".m4b", ".m4p",
                  ".mp3",
                  ".msv", "ogg", "oga", ".raw", ".vox", ".wav", ".wma"),
        "PLAINTEXT": (".txt"),
        "PDF": ".pdf",
        "APPS": ".exe",
        "OTHER": "",
        "FOLDERS": ""
    }
    try:
        create_folders(dirs, dir_path)
        organize_folders(dirs, dir_path)
        organize_remaining_files(dir_path)
        organize_remaining_folders(dirs, dir_path)
    except shutil.Error:
        print("There was an error trying to move an item to its destination folder")
