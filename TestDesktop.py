import os

folder_path = r'C:\Users\sebin\Desktop'
extension = '.svg'

for dirpath, dirnames, filenames in os.walk(folder_path):
    for filename in filenames:
        if filename.lower().endswith(extension):
            print(os.path.join(dirpath, filename))
