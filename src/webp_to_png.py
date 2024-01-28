from PIL import Image
import os

directory_path = 'data/headsets/'

# Loop through each file in the directory
for filename in os.listdir(directory_path):
    if filename.endswith('.webp'):
        file_path = os.path.join(directory_path, filename)
        image = Image.open(file_path)
        
        # Create a new filename for the PNG
        new_filename = filename.replace('.webp', '.png')
        new_file_path = os.path.join(directory_path, new_filename)
        
        # Save the image as a PNG
        image.save(new_file_path)

        # Remove the original WebP file
        os.remove(file_path)

        print(f'Converted {filename} to {new_filename}')