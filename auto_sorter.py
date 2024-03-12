import os, shutil
path = r"Enter path here"
file_name = os.listdir(path)
folder_names = ['pdf files', 'png files']

for loop in range(0,2):
    if not os.path.exists(path + folder_names[loop]):
        print(path + folder_names[loop])
        os.makedirs(path + folder_names[loop])

for file in file_name:
    if ".png" in file and not os.path.exists(path + "png files/" + file):
        shutil.move(path + file, path + "png files/" + file )
    elif ".pdf" in file and not os.path.exists(path + "pdf files/" + file):
        shutil.move(path + file, path + "pdf files/" + file )
