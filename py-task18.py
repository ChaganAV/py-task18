import random
def Valid(x, num, raz):
    if x-num>0:
        if x-num < raz:
            return True
        else:
            return False
    else:
        if x-num < raz:
            return True
        else:
            return False

min = 0
min1 = 1
max = 5
try:
    N = 22//2
    # N = int(input("Введите размер массива: "))//2
    # X = random.randint(min,max)
    # X = int(input("Введите число поиска: "))
    X = 6
    print(X)
    # numbers = []
    numbers = [3, 3, 5, 4, 2, 3, 5, 1, 7, 8, 2]
    # for num in range(min,N):
    #     numbers.append(random.randint(min1,max))
    razn = X
    numFind = 0
    print(numbers)
    for n in numbers:
        if X != n:
            if Valid(X,n, razn):
                numFind = n 
                razn = X-n
        else:
            numFind = n 
            razn = X-n
    print(f"Число {numFind} ближайшее к {X}")
except:
    print("Упс, что-то пошло не так")