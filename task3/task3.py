# task3
# author: GL
# date: 21.07.19
# --------------------
# В магазине 5 касс, в каждый момент времени к кассе стоит очередь некоторой длины.
# Каждые 30 минут измеряется средняя длина очереди в каждую кассу и для каждой кассы это значение записывается в соответствующий ей файл (всего 5 файлов).
# Каждое значение заканчивается символом новой строки.
# Магазин работает 8 часов в день.
# Рассматривается только один день.
# На момент запуска приложения все значения уже находятся в файлах.
# Написать программу, которая по данным замеров определяет интервал времени, когда в магазине было наибольшее количество посетителей за день.
# Аргумент программы - путь к каталогу с файлами. В каталоге будут 5 файлов: Cash1, Cash2 ... Cash5.
# Выведите номер интервала, в котором было наибольшее число посетителей в очередях магазина на всех кассах.
# Первый интервал идет под номером 1, последний под номером 16. 
# В случае обнаружения нескольких интервалов следует выводить первый из них.

import sys
import argparse as argp

# получаем имя директории, содержащей файлы с входными даными из командной строки
def createParser ():
    parser = argp.ArgumentParser()
    parser.add_argument ('-d', '--dir', required=True)
    return parser

if __name__ == '__main__':
    parser = createParser()
    namespace = parser.parse_args(sys.argv[1:])
    
    # помещаем содержимое файлов (с заведомо известными названиями) построчно в списки
    fData1 = [float(line.rstrip('\n')) for line in open(namespace.dir + "/Cash1")]
    fData2 = [float(line.rstrip('\n')) for line in open(namespace.dir + "/Cash2")]
    fData3 = [float(line.rstrip('\n')) for line in open(namespace.dir + "/Cash3")]
    fData4 = [float(line.rstrip('\n')) for line in open(namespace.dir + "/Cash4")]
    fData5 = [float(line.rstrip('\n')) for line in open(namespace.dir + "/Cash5")]
    
    # собираем новый список с суммами соответствующих элементов списков входных данных
    # из условия задачи следует, что всего таких интервалов 16, так что количество строк в файлах проверять не нужно
    dataSum = []
    count = 0
    while (count<16):
        dataSumTemp = fData1[count] + fData2[count] + fData3[count] + fData4[count] + fData5[count]
        dataSum.append(dataSumTemp)
        count += 1
    
    # выводим номер элемента с максимальным значением
    print(dataSum.index(max(dataSum)) + 1)