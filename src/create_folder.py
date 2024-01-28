import os
import shutil

directory_path = 'data/headsets/'

# Loop through each file in the directory
for filename in os.listdir(directory_path):
    # Skip if the filename is a directory
    if os.path.isdir(os.path.join(directory_path, filename)):
        continue

    # Create a new directory name based on the filename
    new_dir_name = os.path.splitext(filename)[0]
    new_dir_path = os.path.join(directory_path, new_dir_name)

    # Create the new directory
    os.makedirs(new_dir_path, exist_ok=True)

    # Define the current file path and the new file path
    current_file_path = os.path.join(directory_path, filename)
    new_file_path = os.path.join(new_dir_path, "regular.png")

    # Move and rename the file
    shutil.move(current_file_path, new_file_path)
