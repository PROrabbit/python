# task2
# author: GL
# date: 21.07.19
# --------------------
# Напишите программу, которая рассчитывает положение точки относительно выпуклого четырехугольника в двумерном пространстве.
# Координаты фигуры считываются из файла1.
# Координаты точек считываются из файла2.
# Файлы передаются программе в качестве аргументов. Файл с координатами четырехугольника - 1 # аргумент, файл с координатами точек - 2 аргумент.
# Координаты в диапазоне float.
# Количество точек от 1 до 100
# Вывод каждого положения точки заканчивается символом новой строки.
# Соответствия ответов:
# 0 - точка на одной из вершин
# 1 - точка на одной из сторон
# 2 - точка внутри
# 3 - точка снаружи

import sys
import argparse as argp

# получаем имя файлов с входными даными из командной строки
def createParser ():
    parser = argp.ArgumentParser()
    parser.add_argument ('-s', '--square', required=True)
    parser.add_argument ('-p', '--points', required=True)
    return parser

if __name__ == '__main__':
    parser = createParser()
    namespace = parser.parse_args(sys.argv[1:])
    
    # помещаем содержимое файлов построчно в списки
    sData = [line.rstrip('\n') for line in open(namespace.square)]
    pData = [line.rstrip('\n') for line in open(namespace.points)]
    
    # создаем переменные с координатами вершин фигуры
    square1x = float(sData[0].split()[0])
    square1y = float(sData[0].split()[1])
    square2x = float(sData[1].split()[0])
    square2y = float(sData[1].split()[1])
    square3x = float(sData[2].split()[0])
    square3y = float(sData[2].split()[1])
    square4x = float(sData[3].split()[0])
    square4y = float(sData[3].split()[1])
    
    pointN = 0
    # для каждой из точек во входном файле получаем ее координаты и проверяем пренадлежность фигуре
    while pointN < len(pData):
        pointX = float(pData[pointN].split()[0])
        pointY = float(pData[pointN].split()[1])
        pointN += 1

        # поскольку у нас нет информации о том, что стороны прямоугольника обязательно находится на координатных осях, и/или параллельны им
        # проверяем, с какой стороны ребра выпуклого многоугольника находится точка (для каждого из ребер)
        # по формуле: D = (x2 - x1) * (yp - y1) - (xp - x1) * (y2 - y1)
        pByEdge = []
        pByEdge.append((square2x - square1x) * (pointY - square1y) - (pointX - square1x) * (square2y - square1y))
        pByEdge.append((square3x - square2x) * (pointY - square2y) - (pointX - square2x) * (square3y - square2y))
        pByEdge.append((square4x - square3x) * (pointY - square3y) - (pointX - square3x) * (square4y - square3y))
        pByEdge.append((square1x - square4x) * (pointY - square4y) - (pointX - square4x) * (square1y - square4y))

        # если более одного значения = 0, значит точка находятся на вершине фигуры
        if pByEdge.count(0) > 1: print(0)
        # если одно значение = 0, значит точка находится на прямой, на которой лежит одна из сторон фигуры
        # если при этом все значения <= 0, значит точка находится на одной из сторон
        elif pByEdge.count(0) > 0 and all(i <= 0 for i in pByEdge): print(1)
        # если все значения < 0, значит точка находится внутри фигуры
        elif max(pByEdge) < 0: print(2)
        # иначе - точка находится снаружи фигуры
        else: print(3)