from PIL import Image
from pathlib import Path
from pillow_heif import register_heif_opener

def get_image_extension(image_name):
    return image_name.split('.')[-1] 

def rounding_image_size(image_size):
    return round(image_size, 3)

def get_file_size(image_path):
    image_path = Path(image_path)
    image_size = image_path.stat().st_size
    return image_size/1024/1024

def get_compression_ratio(size_before, size_after):
    compression_ratio = (size_after / size_before) * 100
    compression_ratio = 100 - compression_ratio
    return compression_ratio

def get_image_save_path(image_name):
    return image_name.replace('.jpg', '.webp').replace('.png', '.webp').replace('.HEIC', '.webp')

def get_image_name(image_name):
    return image_name.replace('images/', '').replace('.jpg', '').replace('.png', '').replace('.HEIC', '')

def get_image_path(image_path, image_name):
    return image_path.replace(f'{image_name}.jpg', '').replace(f'{image_name}.png', '').replace(f'{image_name}.HEIC', '')

def convert_image(image_path, image_type, image_name, quality):
    register_heif_opener()
    im = Image.open(image_path)
    image_path = get_image_path(image_path, image_name)
    original_profile = im.info.get("icc_profile")
    im = im.convert('RGB')
    if image_type == 'jpg' or image_type == 'png' or image_type == 'HEIC':
        im.save(f"{image_path}{image_name}.webp", 'webp', optimize=False, quality=quality, icc_profile=original_profile)
