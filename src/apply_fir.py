from PIL import Image
import os

def apply_logo_to_image(background_image_path, logo_image_path, offset_from_bottom_right, output_image_path):
    # Open the background and logo images
    background_image = Image.open(background_image_path)
    logo_image = Image.open(logo_image_path)
    
    # Ensure the logo has an alpha channel for transparency
    if logo_image.mode != 'RGBA':
        logo_image = logo_image.convert('RGBA')
    
    # Calculate the position to paste the logo image
    # which is offset from the bottom right corner of the background image
    background_width, background_height = background_image.size
    logo_width, logo_height = logo_image.size
    position = (background_width - logo_width - offset_from_bottom_right[0], 
                background_height - logo_height - offset_from_bottom_right[1])
    
    # Paste the logo onto the background image at the calculated position
    background_image.paste(logo_image, position, logo_image)
    
    # Create the output directory if it doesn't exist
    os.makedirs(os.path.dirname(output_image_path), exist_ok=True)
    
    # Save the result with the specified output image path
    background_image.save(output_image_path)

def process_folders(root_directory, logo_image_path, offset_from_bottom_right):
    # Loop over each folder in the root directory
    for folder_name in os.listdir(root_directory):
        folder_path = os.path.join(root_directory, folder_name)
        
        # Check if it's a directory
        if os.path.isdir(folder_path):
            background_image_path = os.path.join(folder_path, 'regular.png')
            
            # Check if 'regular.png' exists in this folder
            if os.path.exists(background_image_path):
                output_image_path = os.path.join(folder_path, 'fir.png')
                apply_logo_to_image(background_image_path, logo_image_path, offset_from_bottom_right, output_image_path)

# Usage
root_directory = 'data/headsets'
logo_image_path = 'data/fir_icon.png'
offset_from_bottom_right = (5, 5)

process_folders(root_directory, logo_image_path, offset_from_bottom_right)
