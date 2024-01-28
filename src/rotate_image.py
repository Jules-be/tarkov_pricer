from PIL import Image
import os

directory_path = 'data/headsets/'

# Walk through all subdirectories in the directory
for subdir, dirs, files in os.walk(directory_path):
    if 'regular.png' in files:
        file_path = os.path.join(subdir, 'regular.png')

        # Open the image
        image = Image.open(file_path)

        # Rotate the image 45 degrees to the right
        rotated_image = image.rotate(-90, expand=True)

        # Create a new filename
        new_file_path = os.path.join(subdir, 'rotated.png')

        # Save the rotated image
        rotated_image.save(new_file_path)

        print(f'Rotated image saved to {new_file_path}')
