from PIL import Image
import os

directory_path = 'data/headsets/'

# Walk through all subdirectories in the directory
for subdir, dirs, files in os.walk(directory_path):
    if 'regular.png' in files:
        file_path = os.path.join(subdir, 'regular.png')

        # Open the image
        image = Image.open(file_path)

        # Flip the image horizontally
        flipped_image = image.transpose(Image.FLIP_LEFT_RIGHT)

        # Create a new filename
        new_file_path = os.path.join(subdir, 'flipped.png')

        # Save the flipped image
        flipped_image.save(new_file_path)

        print(f'Flipped image saved to {new_file_path}')
