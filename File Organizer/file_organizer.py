import os
from shutil import move

# Organize files by time
def time_organizer(folder):
    os.chdir(folder)
    files = filter(os.path.isfile,os.listdir(folder))
    files = [os.path.join(target_folder, file) for file in files]
    files.sort(key=lambda x: os.path.getmtime(x))
    return '\n'.join(files)

# Organize files by extension
def ext_organizer(folder):
    extensions = []
    for item in os.listdir(folder):
        if os.path.isfile(os.path.join(target_folder, item)):
            extensions.append(item.split(".")[-1])
    extensions = set(extensions)

    for extension in extensions:
        if not os.path.exists(os.path.join(target_folder, extension)):
            os.mkdir(os.path.join(target_folder, extension))

    for item in os.listdir(target_folder):
        if os.path.isfile(os.path.join(target_folder, item)):
            file_extension = item.split('.')[-1]
            move(os.path.join(target_folder, item), os.path.join(target_folder, file_extension, item))

    print(os.listdir(target_folder))


target_folder = 'C://Test'
print(time_organizer(target_folder))
print(ext_organizer(target_folder))