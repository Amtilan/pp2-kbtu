def fromnto0():
    n = int(input())
    decr = (int(i) for i in range (n, 0, -1))
    for i in range(n):
        print(next(decr))
        
fromnto0()

"""
Эта функция запрашивает у пользователя целое число n с помощью input(). 
Затем она создает генераторное выражение decr, которое генерирует последовательность чисел от n до 1 включительно в обратном порядке.
После этого функция использует цикл for, который итерируется n раз. 
На каждой итерации из генератора decr извлекается следующее значение с помощью функции next(), а затем это значение печатается.
Таким образом, эта функция выводит на экран числа от n до 1 включительно в обратном порядке.
"""