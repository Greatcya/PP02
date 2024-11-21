

import os

from PIL import Image


def moveto(path, newpath):

    try:

        # Открываем изображение.
        im = Image.open(path)

        # Сохраняем изображение в другую директорию.
        im.save(newpath + "\\" + os.path.basename(path))

        # Удаляем изображение из прошлой директории.
        os.remove(path)

        print("Файл сохранен")

    except FileNotFoundError:

        print("Ошибка, файл не найден")
