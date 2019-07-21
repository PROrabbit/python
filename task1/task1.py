# task1
# author: GL
# date: 21.07.19
# --------------------
# Напишите программу, которая рассчитывает и подает на стандартный вывод следующие значения:
# - 90 перцентиль
# - медиана
# - максимальное значение
# - минимальное значение
# - среднее значение
# Данные для расчетов считываются из файла, путь к которому подается в виде аргумента.
# Числа в файле в пределах от -32 768 до 32 767
# Каждое число с новой строки.
# В файле не более 1000 строк.
# Вывод значений в указанной последовательности, каждое значение заканчивается символом новой строки.
# Все значения с точностью до сотых: 2.5 2 0.03

import sys
import argparse as argp
import numpy as np

# получаем имя файла с входными даными из командной строки
def createParser ():
    parser = argp.ArgumentParser()
    parser.add_argument ('-n', '--name', required=True)
    return parser

if __name__ == '__main__':
    parser = createParser()
    namespace = parser.parse_args(sys.argv[1:])

    # помещаем содержимое файла построчно в список
    # поскольку в задании явно не сказано, что значения целочисленные, на всякий случай используем float
    fData = [float(line.rstrip('\n')) for line in open(namespace.name)]
    
    # выводим искомые значения с точностью до сотых
    print (round(np.percentile(fData, 90),2)) # percentile 90
    print (round(np.percentile(fData, 50),2)) # median
    print (round(max(fData),2)) # max value
    print (round(min(fData),2)) # min value
    print (round(np.mean(fData),2)) # average