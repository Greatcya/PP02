

import os

import convertor

import move_image

todo = input("Что нужно сделать? \n 1. Конвертировать изображение (png > jpg, jpg > png) "
             "\n 2. Переместить изображение \n Напишите цифру: ")

if todo == "1":

    path = input("Укажите путь или перетащите изображение и нажмите Энтер,"
                 " затем напишите название для нового файла: ")

    filename = input("Ведите имя нового файла (без формата): ")

    if os.path.splitext(path)[1] == ".png":

        convertor.pngtojpg(path, filename)

    elif os.path.splitext(path)[1] == ".jpg":

        convertor.jpgtopng(path, filename)

    else:

        print("Неподдерживаемый тип файла")

elif todo == "2":

    path = input("Укажите путь или перетащите изображение и нажмите Энтер,"
                 " затем напишите путь по которому нужно переместить файл: ")

    newpath = input("Куда нужно переместить: ")

    move_image.moveto(path, newpath)

else:

    print("Введен неверный символ, попробуйте еще раз")

input("Нажмите энтер, чтобы закрыть")
