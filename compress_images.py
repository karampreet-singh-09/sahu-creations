import os
from PIL import Image
import glob

image_dir = 'images'
png_files = glob.glob(os.path.join(image_dir, 'wedding_*.png'))

for png_file in png_files:
    webp_file = png_file.rsplit('.', 1)[0] + '.webp'
    try:
        with Image.open(png_file) as img:
            img = img.convert("RGB")
            # Resize image to a max width of 1000px to further reduce size
            max_width = 1000
            if img.width > max_width:
                ratio = max_width / float(img.width)
                new_height = int((float(img.height) * float(ratio)))
                img = img.resize((max_width, new_height), Image.Resampling.LANCZOS)
            
            img.save(webp_file, 'webp', optimize=True, quality=65)
            print(f"Compressed: {os.path.basename(webp_file)}")
            
        # Remove original large PNG
        os.remove(png_file)
    except Exception as e:
        print(f"Error compressing {png_file}: {e}")
