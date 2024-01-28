from PIL import Image, ImageEnhance
import os

directory_path = 'data/headsets/'

# Walk through all subdirectories in the directory
for subdir, dirs, files in os.walk(directory_path):
    if 'regular.png' in files:
        file_path = os.path.join(subdir, 'regular.png')

        # Open the image
        image = Image.open(file_path)

        # Enhance sharpness
        enhancer = ImageEnhance.Sharpness(image)
        sharpness_factor = 2.0  # Adjust this value as needed
        sharpened_image = enhancer.enhance(sharpness_factor)

        # Create a new filename
        new_file_path = os.path.join(subdir, 'sharpened.png')

        # Save the sharpened image
        sharpened_image.save(new_file_path)

        print(f'Sharpened image saved to {new_file_path}')
