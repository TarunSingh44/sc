import os
import shutil

# List of characters
characters = "#%+-0123456789:ABDFMPQRTUVWXYZ[\]ceghjkns"

# Iterate through the source folders and extract the folder names
for i in range(41):
    # Create the expected folder name
    source_folder = os.getcwd() + f"/data_train/train_{characters[i]}"

    destination_folder = os.getcwd() + '/trainfinal'
    os.makedirs(destination_folder, exist_ok = True)

    # Check if the source folder exists
    if os.path.exists(source_folder):
        # Iterate through the source folder and move files to the destination folder
        for root, dirs, files in os.walk(source_folder):
            for file in files:
                source_file_path = os.path.join(root, file)
                destination_file_path = os.path.join(destination_folder, file)

                # Move the file to the destination folder
                shutil.move(source_file_path, destination_file_path)

print("Files moved successfully.")
