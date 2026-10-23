import os
import glob
from PIL import Image, ImageDraw

# Create a clean high-resolution vector-style icon programmatically
# Representing Computational Matrix: Matrix brackets, nodes, and a subtle central shield
size = (512, 512)
img = Image.new("RGBA", size, (13, 17, 23, 255)) # Dark theme background
draw = ImageDraw.Draw(img)

# Draw central glowing shield boundary / matrix brackets
# Outer shield/matrix outline
shield_points = [(256, 64), (416, 128), (416, 320), (256, 448), (96, 320), (96, 128)]
draw.polygon(shield_points, outline=(0, 210, 255, 255), width=16)

# Grid lines inside (Matrix motif)
for y in range(160, 360, 48):
    draw.line([(140, y), (372, y)], fill=(0, 180, 216, 120), width=4)

for x in range(160, 360, 48):
    draw.line([(x, 140), (x, 372)], fill=(0, 180, 216, 120), width=4)

# Intersecting Nodes
nodes = [
    (212, 208), (260, 208), (308, 208),
    (212, 256), (256, 256), (300, 256),
    (212, 304), (260, 304), (308, 304)
]

for nx, ny in nodes:
    draw.ellipse((nx-8, ny-8, nx+8, ny+8), fill=(0, 255, 200, 255))

# Save multi-resolution .ico file
ico_filename = "computational_matrix.ico"
icon_sizes = [(16, 16), (24, 24), (32, 32), (48, 48), (64, 64), (128, 128), (256, 256)]
img.save(ico_filename, format="ICO", sizes=icon_sizes)

print(f"FILE_TAG:{ico_filename}")
