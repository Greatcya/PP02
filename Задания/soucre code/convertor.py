

import os

from PIL import Image


def jpgtopng(path, filename):

    try:

        # Открываем изображение.
        im = Image.open(path)

        # Сохраняем изображение в формате.
        im.save(os.path.dirname(path) + "\\" + filename + ".png")

        print("Файл сохранен по пути: ", os.path.dirname(path))

    except FileNotFoundError:

        print("Ошибка, файл не найден")


def pngtojpg(path, filename):

    try:

        # Открываем изображение.
        im = Image.open(path)

        # Сохраняем изображение в формате .jpg.
        im.save(os.path.dirname(path) + "\\" + filename + ".jpg")

        print("Файл сохранен по пути: ", os.path.dirname(path))

    except FileNotFoundError:

        print("Ошибка, файл не найден")
