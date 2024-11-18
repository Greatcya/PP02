

import os
from PIL import Image

def jpgtopng(path, filename):

    im = Image.open(path)

    im.save(os.path.dirname(path) + "\\" + filename + ".png")

    print("Файл сохранен по пути: ", os.path.dirname(path))

def pngtojpg(path, filename):

    im = Image.open(path)

    im.save(os.path.dirname(path) + "\\" + filename + ".jpg")

    print("Файл сохранен по пути: ", os.path.dirname(path))

