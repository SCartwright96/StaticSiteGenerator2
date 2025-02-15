import os
import shutil

def replicate_dir(dir_to_copy, destination):
    if not os.path.exists(dir_to_copy):
        raise FileNotFoundError(f"{dir_to_copy} does not exist")
    
    #removes old folder and makes a new empty one
    shutil.rmtree(destination,True)
    os.mkdir(destination)

    files_to_copy = os.listdir(dir_to_copy)
    for file in files_to_copy:
        if not os.path.isfile(f"{dir_to_copy}{file}"):
            replicate_dir(f"{dir_to_copy}{file}/",f"{destination}{file}")
            continue
        shutil.copy(f"{dir_to_copy}{file}", destination)