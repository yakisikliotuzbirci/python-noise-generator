from random import randint
from PIL import Image, ImageDraw
import sys, time

def main():
    w = int(input("width : "))
    h = int(input("height : "))

    resolution = w, h

    x, y = 0, 0

    image = Image.new("RGB", (resolution[0], resolution[1]))
    draw = ImageDraw.Draw(image)

    _t = time.time()
    _t2 = _t

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
            color = "#bfbfbf"
        elif r == 4:
            color = "#dbdbdb"
        elif r == 5:
            color = "#7b7b7b"

        draw.line([(x, y), (x, y)], fill=color)
        
        if time.time() - _t >= 1:
            print(f"%{(y/h)*100} generated")
            _t = time.time()

        if y == resolution[1]:
            print(f"%{(y/h)*100} generated")
            print(f"generated in {time.time() - _t2} seconds")
            image.save(f"noise {resolution[0]}x{resolution[1]}.png")
            time.sleep(1)
            sys.exit()

if __name__ == "__main__":
    main()
