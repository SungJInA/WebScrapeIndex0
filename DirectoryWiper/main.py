from pathlib import Path
import os
import glob

# replace with your preferred directory path
dir_path = Path(r'C:\Users\tonyc\Desktop\KoreaProjects\WebScraping\DirectoryWiper\DummyDirectory')
file_name = "mydocument.txt"
file_path = dir_path.joinpath(file_name)

# check that directory exists
def create_files():
    if dir_path.is_dir():
        with open(file_path, "w") as f:
            f.write("This text is written with Python.")
            print('File was created.')
    else:
        print("Directory doesn\'t exist.")

#delete files in directory
def delete_files():
    files = glob.glob(r'C:\Users\tonyc\Desktop\KoreaProjects\WebScraping\DirectoryWiper\DummyDirectory')
    for f in files:
        os.remove(f)

