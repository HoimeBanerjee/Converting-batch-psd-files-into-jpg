import os
from psd_tools import PSDImage

# Define input folder (use raw string for Windows path) 
#Paste your own folder path. The images in the folder are named as 1.psd,2.psd and so forth
input_folder = r"E:\Review\Images for the review\Input"
output_folder = os.path.join(input_folder, "output")

# Create output folder if it doesn't exist
os.makedirs(output_folder, exist_ok=True)

# Loop through all PSD files in the input folder
for filename in os.listdir(input_folder):
    if filename.lower().endswith(".psd"):
        psd_path = os.path.join(input_folder, filename)
        output_filename = os.path.splitext(filename)[0] + ".jpg"
        output_path = os.path.join(output_folder, output_filename)

        # Open the PSD and convert it to a PIL image
        psd = PSDImage.open(psd_path)
        image = psd.topil()  # <-- THIS works on most versions

        # Save the image as JPG
        image.save(output_path, "JPEG")
        print(f"Converted: {filename} -> {output_filename}")

print("All PSD files have been converted.")
