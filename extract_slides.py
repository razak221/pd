import xml.etree.ElementTree as ET
import os
import shutil

slides_dir = '/private/tmp/pptx_extracted/ppt/slides'
media_dir = '/private/tmp/pptx_extracted/ppt/media'
dest_media = '/Users/razakahmedkhan/Downloads/Website Redesign/src/assets/ppt_images'

os.makedirs(dest_media, exist_ok=True)
copied = 0
for f in os.listdir(media_dir):
    src = os.path.join(media_dir, f)
    dst = os.path.join(dest_media, f)
    shutil.copy2(src, dst)
    copied += 1
print(f"Copied {copied} media files to {dest_media}")

slides = sorted([f for f in os.listdir(slides_dir) if f.endswith('.xml') and not f.startswith('_')], 
                key=lambda x: int(x.replace('slide','').replace('.xml','')))

print(f"Total slides: {len(slides)}\n")

for slide_file in slides:
    path = os.path.join(slides_dir, slide_file)
    tree = ET.parse(path)
    root = tree.getroot()
    texts = []
    for t in root.iter('{http://schemas.openxmlformats.org/drawingml/2006/main}t'):
        if t.text and t.text.strip():
            texts.append(t.text.strip())
    if texts:
        slide_num = slide_file.replace('slide','').replace('.xml','')
        print(f'### SLIDE {slide_num} ###')
        for t in texts:
            print(repr(t))
        print()
