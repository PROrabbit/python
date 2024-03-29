# python
* Репозиторий содержит решения четырех тестовых заданий, находящиеся в соответствующих папках (test1, test2, test3, test4).
* Решения выполнены на Python 3.7.3.
* Для решения первого задания применяется модуль **numpy**, а именно функции: *percentile*, *mean*.
* Код содержит комментарии поясняющие принцип его работы.
* Условия заданий находятся в исполняемых файлах в виде комментариев.

### Запуск исполняемых файлов
Исполняемые файлы (test1.py, test2.py, test3.py, test4.py) находятся в соответствующих папках и требуют для работы внешние файлы с входящими данными, путь к которым передается в качестве параметров командной строки.
* Для первого задания: -n / --name
* Для второго задания: -s / --square (файл с координатами прямоугольника), -p / --points (файл с координатами точек)
* Для третьего задания: -d / --dir
* Для четвертого задания: -n / --name

Например:

    test1.py -n data
    test2.py -s sdata -p pdata
    test3.py -d data
    test4.py -n data

Файлы с примерами входных данных для каждого приложения находятся в соответствующих папках

### Примечания
* Поскольку в **task2** у нас нет информации о том, что стороны прямоугольника обязательно находится на координатных осях, и/или параллельны им, принадлежность точки фигуре определяется по формуле D = (x2 - x1) * (yp - y1) - (xp - x1) * (y2 - y1) применяемой последовательно к каждому ребру прямоугольника. Это означает, что в файле входных данных координат вершин прямоугольника координаты должны располагаться в строго заданной последовательности (перебором вершин по часовой стрелке, что соответствует примеру входных данных в задании).  
* В **task4** подразумевается, что пересечение интервалов создает суммарную плотность. Например, если один из посетителей покинул здание в 9:45, а другой прибыл в это время, суммарная плотность временного отрезка (9:45 - 9:45) будет равна двум.
