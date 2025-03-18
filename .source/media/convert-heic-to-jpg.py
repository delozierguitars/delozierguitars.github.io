from PIL import Image
import pillow_heif
import os

def convert_heic_to_jpg(heic_file):
    heif_image = pillow_heif.open_heif(heic_file)
    img = Image.frombytes(heif_image.mode, heif_image.size, heif_image.data)
    
    jpg_file = os.path.splitext(heic_file)[0] + ".jpg"
    img.save(jpg_file, "JPEG")
    print(f"Converted {heic_file} to {jpg_file}")

# Convert all HEIC images in the folder
for file in os.listdir():
    if file.lower().endswith(".heic"):
        convert_heic_to_jpg(file)