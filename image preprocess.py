import os
from PIL import Image

# Define the target size
target_size = (224, 224)

# Base directory
base_dir = r'directory path'

# Subdirectories
sub_dirs = [
    'train/hello1',
    'train/goodbye1',
    'train/yes1',
    'train/no1',
    'train/please1',
    'validation/hello2',
    'validation/goodbye2',
    'validation/yes2',
    'validation/no2',
    'validation/please2'
]

# Full paths to directories
data_dirs = [os.path.join(base_dir, sub_dir) for sub_dir in sub_dirs]

# Resize images
for data_dir in data_dirs:
    for filename in os.listdir(data_dir):
        if filename.endswith('.jpg') or filename.endswith('.png'):
            filepath = os.path.join(data_dir, filename)
            with Image.open(filepath) as img:
                img = img.resize(target_size, Image.ANTIALIAS)
                img.save(filepath)

print("Resizing completed.")
