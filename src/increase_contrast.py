from PIL import Image, ImageEnhance
import os

directory_path = 'data/headsets/'

def increase_contrast(image, factor=1.5):
    """
    Increase the contrast of the image.
    """
    enhancer = ImageEnhance.Contrast(image)
    return enhancer.enhance(factor)

# Walk through all subdirectories in the directory
for subdir, dirs, files in os.walk(directory_path):
    if 'regular.png' in files:
        file_path = os.path.join(subdir, 'regular.png')

        # Open the image
        image = Image.open(file_path)

        # Increase contrast
        higher_contrast_image = increase_contrast(image)

        # Create a new filename
        new_file_path = os.path.join(subdir, 'higher_contrast.png')

        # Save the image with higher contrast
        higher_contrast_image.save(new_file_path)

        print(f'Higher contrast image saved to {new_file_path}')
