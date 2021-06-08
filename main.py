__winc_id__ = 'ae539110d03e49ea8738fd413ac44ba8'
__human_name__ = 'files'

import os
import shutil
import zipfile

def clean_cache():

    folder_cache = ("cache")
    check_folder = os.path.isdir(folder_cache)

    if not check_folder:
        os.makedirs(folder_cache)

    else:
        shutil.rmtree(folder_cache)
        os.makedirs(folder_cache)
    return clean_cache
clean_cache()

#2
def cache_zip(zip_file_path,cache_dir_path):
    with zipfile.ZipFile(zip_file_path, 'r') as zip_ref:
        zip_ref.extractall(cache_dir_path)
    return zipfile

cache_zip('data.zip','cache')

#3
def cached_files():
    file_list = []
    for file in os.listdir(os.path.abspath("cache")):
        file_list.append(f"{os.path.abspath('cache')}\{file}")
    print(file_list)
    return file_list

#4
def find_password(list_files_path):
    for file_name in list_files_path:
        file = open(file_name, 'r')
        text = "password"
        for line in file:
            if text in line:
                password = line[line.find(' ')+1:-1]
#               print(password.rstrip())
    return password
                
find_password(cached_files())




                
