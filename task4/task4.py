# task4
# author: GL
# date: 21.07.19
# --------------------
# В течении дня в банк заходят люди, для каждого посещения фиксируется время захода в банк и  время выхода.
# Банк работает с 8:00 до 20:00.
# Написать программу, которая определяет периоды времени, когда в банке было максимальное количество посетителей.
# Файл содержит информацию о времени посещения банка каждым посетителем, округленном до минут.
# Время входа посетителя меньше либо равно времени выхода.
# Выведите интервалы времени, когда в банке было максимальное число посетителей.
# Начало и конец интервала разделяются пробелом.
# В случае необходимости вывести несколько периодов, в качестве разделителя между ними следует использовать символ перевода строки.

import sys
import argparse as argp

# функция перевода минут в часы:минуты
def m2hm(m):
    hm = str(int(m / 60)) + ':' + str(m % 60).zfill(2)
    return hm

# получаем имя файла с входными даными из командной строки
def createParser ():
    parser = argp.ArgumentParser()
    parser.add_argument ('-n', '--name', required=True)
    return parser

if __name__ == '__main__':
    parser = createParser()
    namespace = parser.parse_args(sys.argv[1:])

    # помещаем содержимое файла построчно в список
    fData = [line.rstrip('\n') for line in open(namespace.name)]

    # создаем пустой список на весь рабочий день по минутам
    timeSum = [0 for x in range(720)]
    
    # переводим каждый интервал в минуты, и увеличиваем соответствующие значения в списке 
    timeN = 0
    while timeN < len(fData):
        (timeStart, timeEnd) = fData[timeN].split()
        (tsH, tsM) = timeStart.split(":")
        (teH, teM) = timeEnd.split(":")
        timeStart = int(tsH) * 60 + int(tsM) - 480
        timeEnd = int(teH) * 60 + int(teM) - 480
        timeN += 1
        for i in range(timeStart, timeEnd + 1):
            timeSum[i] += 1

    # создаем список с индексами элементов с максимальным значением
    maxTime = [i for i, j in enumerate(timeSum) if j == max(timeSum)]

    # выделяем интервалы в отдельный список
    timeInts = []
    seq = [maxTime[0]]
    for i in maxTime[1:]:
        if i == seq[-1] + 1:
            seq.append(i)
        else:
            timeInts.append(seq)
            seq = [i]
    timeInts.append(seq)
    
    # выводим в нужном формате
    for res in timeInts:
        print(m2hm(res[0] + 480), m2hm(res[-1] + 480))