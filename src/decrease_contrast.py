from PIL import Image, ImageEnhance
import os

directory_path = 'data/headsets/'

def decrease_contrast(image, factor=0.5):
    """
    Decrease the contrast of the image.
    """
    enhancer = ImageEnhance.Contrast(image)
    return enhancer.enhance(factor)

# Walk through all subdirectories in the directory
for subdir, dirs, files in os.walk(directory_path):
    if 'regular.png' in files:
        file_path = os.path.join(subdir, 'regular.png')

        # Open the image
        image = Image.open(file_path)

        # Decrease contrast
        lower_contrast_image = decrease_contrast(image)

        # Create a new filename
        new_file_path = os.path.join(subdir, 'lower_contrast.png')

        # Save the image with lower contrast
        lower_contrast_image.save(new_file_path)

        print(f'Lower contrast image saved to {new_file_path}')
