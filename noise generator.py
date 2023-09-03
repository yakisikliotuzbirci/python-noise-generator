from random import randint
from PIL import Image, ImageDraw
import sys

def main():
    w = int(input("width : "))
    h = int(input("height : "))

    resolution = w, h

    x, y = 0, 0

    image = Image.new("RGB", (resolution[0], resolution[1]), "white")
    draw = ImageDraw.Draw(image)

    while True:
        x = x + 1
        
        if x == resolution[0]:
            y = y + 1
            x = 0

        r = randint(0, 5)

        if r == 0:
            color = "#000000"
        elif r == 1:
            color = "#ffffff"
        elif r == 2:
            color = "#b1b1b1"
        elif r == 3:
            color = "#fbfbfb"
        elif r == 4:
            color = "#dbdbdb"
        elif r == 5:
            color = "#1f1f1f"

        draw.line([(x, y), (x + 1, y + 1)], fill=color)

        if y == resolution[1]:
            image.save(f"noise {resolution[0]}x{resolution[1]}.png")
            sys.exit()

if __name__ == "__main__":
    main()
