from pdf2image import convert_from_path
from pathlib import Path
import sys
import os
from pathlib import Path

print(f"sys.argv: {sys.argv}")
if (len(sys.argv) > 1):
    path = sys.argv[1]
    
print(f"path: {path}")

dirname = os.path.dirname(path)
print(f"dirname: {dirname}")

file_path = Path(path)
filename_without_ext = file_path.stem
print(f"filename_without_ext: {filename_without_ext}")  

outputDir = os.path.join(dirname, filename_without_ext)
Path(outputDir).mkdir(parents=True, exist_ok=True)

pages = convert_from_path(path, 500)
for count, page in enumerate(pages):
    outputPath = os.path.join(outputDir, f'out_{filename_without_ext}_{count}.jpg')
    page.save(outputPath, 'JPEG')