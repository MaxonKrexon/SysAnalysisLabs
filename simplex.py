import numpy as np
import os

file = open("simplex.txt", 'w', encoding="UTF-8") # <- Создание файла для вывода
file.write("Симплекс таблицы каждой итерации\n") # <- Внесение заголовка в файл
finding = "minimum" # <- Ключ для указания поиска алгоритма на минимазацию функции (minimum/maximum)
basis = [4, 5, 6,"F"] # <- Индексы столбца базиса (для оформления)
maxStep = 25 # <- Ограничение по максимальному количеству итераций

# Матрица коэффициентов левой части уравнений
A = [[-2, -3, -2],
     [-4, -4, -3],
     [5, 5, 5]]

# Матрица коэффициентов правой части уравнений
B = [12, 24, 15]

# Коэффициенты целевой функции
F = [3, -7, -4]

finding = "maximum"
F = [1, 2, -1]
A = [[-1, 4, -2],
     [-1, -1, -2],
     [2, -1, 2]]

B = [6, -6, 4]

if finding == "minimum":
    for j in range(len(F)):
        F[j] /= -1

# Формирование начальной симплекс таблицы
table = np.array([[A[0][0], A[0][1], A[0][2], 1, 0, 0, B[0],0],
                  [A[1][0], A[1][1], A[1][2], 0, 1, 0, B[1],0],
                  [A[2][0], A[2][1], A[2][2], 0, 0, 1, B[2],0],
                  [F[0], F[1], F[2], 0, 0, 0, 0,0]], np.float32)


flag = True # <- Флаг остановки вычислений

# Функция печати симплекс-таблицы в файл
def printFile(step, table,hostRow, hostCol, hostElement):
    file.write(f"\nИтерация: {step}\n")
    file.write(f"Ведущий столбец: {hostCol+1}  Ведущая строка: {hostRow+1}  Ведущий элемент: {hostElement}\n")
    file.write(f"Базис\tX1\tX2\tX3\tX4\tX5\tX6\tB\tB/Xhost\n")
    for j in range(4):
        file.write(f"X{basis[j]}\t")
        for k in range(8):
            file.write(f"{format(table[j][k],'.3f')}\t")
        file.write("\n")

    file.write("\n")

step = 1 # <- Переменная для учёта количества итераций

while(flag):
    if np.max(table[3][0:6]) <= 0 and finding == "minimum": # Условие остановки при поиске минимума
        print("Решение найдено")
        flag = False
        break
    if np.min(table[3][0:6]) >= 0 and finding == "maximum": # Условие остановки при поиске максимума
        print("Решение найдено")
        flag = False
        break
    elif step == maxStep + 1: # Уловие остановки по достижению максимального количества итераций
        print("Решения нет.Ограничение по шагам")
        flag = False

    else:
        if finding == "minimum": # <- Условие для поиска ведущего столбца при поиске минимума
            hostCol = np.argmax(table[3][0:6])
        elif finding == "maximum": # <- Условие для поиска ведущего столбца при поиске максимума
            hostCol = np.argmin(table[3][0:6])

        # Массив частных относильно B и ведущего столбца
        bdivhost = np.array([table[0][6]/table[0][hostCol],
                    table[1][6]/table[1][hostCol],
                    table[2][6]/table[2][hostCol]], np.float32)

        # Проверка частных на положительность
        for j in range(3):
            if bdivhost[j] <= 0.0:
                bdivhost[j] = 999 # Замена нулевых (и меньше) значений на большое, для его исключения

        hostRow = np.argmin(bdivhost) # <- Определение индекса в массиве частных для получения ведущей строки

        hostElement = table[hostRow][hostCol] # <- Создание ведущего элемента как пересечение
                                            # ведущей строки и ведущего столбца в симплекс-таблице

        for j in range(3): # <- Цикл для внесения частных деления B на ведущий столбец
            table[j][7] = table[j][6]/table[j][hostCol]

        printFile(step,table,hostRow, hostCol, hostElement) # <- Запись в файл текущих параметров расчёта


        newTable = np.zeros_like(table) # <- Создание новой таблицы, заполненной нулями
        newTable[hostRow] = table[hostRow]/hostElement # <- Запись в новую таблицу ведущей строки
        basis[hostRow] = hostCol+1 # <- Изменение значения в списке базисов для удобства

        for j in range(4): # <- Перебор по всем строкам таблицы
            if j != hostRow: # <- Проверка на ведущую строку
                for k in range(7): # <- Перебор по всем столбцам таблицы
                    # Вычисление новых значений элементов таблицы
                    newTable[j][k] = table[j][k] - (table[j][hostCol] * newTable[hostRow][k])

        table = np.copy(newTable) # <- Перенос значений новой таблицы в старую
        printFile(step,table,hostRow, hostCol, hostElement) # <- Запись в файл текущих параметров расчёта
        step += 1 # <- Увеличение счётчика итераций



file.close() # <- Закрытие файла для сохранения в нём данных

# Команда в ОС на открытие текстового документа для просмотра полученных данных
os.system('notepad simplex.txt')
