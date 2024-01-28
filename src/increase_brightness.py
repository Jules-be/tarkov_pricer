from PIL import Image, ImageEnhance
import os

directory_path = 'data/headsets/'

def increase_brightness(image, factor=1.5):
    """
    Increase the brightness of the image.
    """
    enhancer = ImageEnhance.Brightness(image)
    return enhancer.enhance(factor)

# Walk through all subdirectories in the directory
for subdir, dirs, files in os.walk(directory_path):
    if 'regular.png' in files:
        file_path = os.path.join(subdir, 'regular.png')

        # Open the image
        image = Image.open(file_path)

        # Increase brightness
        brighter_image = increase_brightness(image)

        # Create a new filename
        new_file_path = os.path.join(subdir, 'brighter.png')

        # Save the brighter image
        brighter_image.save(new_file_path)

        print(f'Brighter image saved to {new_file_path}')
