from PIL import Image, ImageDraw

im = Image.new('RGB', (500, 300), (255, 0, 0))
draw = ImageDraw.Draw(im)

for i in range(5):
    draw.line((25 + i * 100, 0, 25+ i * 100, 300), fill=(0, 0, 255), width=50)

im.save("a.png")