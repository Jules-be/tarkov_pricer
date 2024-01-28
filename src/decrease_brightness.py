from PIL import Image, ImageEnhance
import os

directory_path = 'data/headsets/'

def decrease_brightness(image, factor=0.5):
    """
    Decrease the brightness of the image.
    """
    enhancer = ImageEnhance.Brightness(image)
    return enhancer.enhance(factor)

# Walk through all subdirectories in the directory
for subdir, dirs, files in os.walk(directory_path):
    if 'regular.png' in files:
        file_path = os.path.join(subdir, 'regular.png')

        # Open the image
        image = Image.open(file_path)

        # Decrease brightness
        darker_image = decrease_brightness(image)

        # Create a new filename
        new_file_path = os.path.join(subdir, 'darker.png')

        # Save the darker image
        darker_image.save(new_file_path)

        print(f'Darker image saved to {new_file_path}')
