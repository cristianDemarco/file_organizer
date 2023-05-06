import os
import shutil

path = "/home/cristian/Desktop/Organizer"

files = os.scandir(path)

for file in files:
    file_destination = None
    file_name = os.path.basename(file)
    file_extension = os.path.splitext(file_name)[1]

    extensions_to_paths = {
        ".txt": "/home/cristian/Documents",
        ".pptx": "/home/cristian/PowerPoints",
        **dict.fromkeys(['.jpeg', '.png'], "/home/cristian/Pictures"),
    }

    file_destination = extensions_to_paths.get(file_extension)

    if file_destination != None:
        shutil.move(f"/home/cristian/Desktop/Organizer/{file_name}", file_destination)