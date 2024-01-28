from PIL import Image, ImageFilter
import os

directory_path = 'data/headsets/'

# Walk through all subdirectories in the directory
for subdir, dirs, files in os.walk(directory_path):
    if 'regular.png' in files:
        file_path = os.path.join(subdir, 'regular.png')

        # Open the image
        image = Image.open(file_path)

        # Apply a blur filter to the image
        blurred_image = image.filter(ImageFilter.BLUR)

        # Create a new filename
        new_file_path = os.path.join(subdir, 'blurred.png')

        # Save the blurred image
        blurred_image.save(new_file_path)

        print(f'Blurred image saved to {new_file_path}')
