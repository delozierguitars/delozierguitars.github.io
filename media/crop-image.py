from PIL import Image

def crop_middle_third(input_path, output_path):
    img = Image.open(input_path)
    width, height = img.size

    top_crop = height // 3
    bottom_crop = height - (height // 3)

    cropped = img.crop((0, top_crop, width, bottom_crop))  # (left, top, right, bottom)
    cropped.save(output_path)

# Example usage:
crop_middle_third("delozier_guitars.jpg", "delozier_guitars_cropped.jpg")
