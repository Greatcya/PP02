

import os

from PIL import Image

def moveto(path, newpath):

    im = Image.open(path)

    im.save(newpath + "\\" + os.path.basename(path))

    os.remove(path)

    print("Файл сохранен")