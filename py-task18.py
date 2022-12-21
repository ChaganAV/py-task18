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
    numbers = [3, 3, 4, 5, 2, 3, 4, 1, 7, 8, 2]
    for num in range(min,N):
        numbers.append(random.randint(min1,max))
    razn = X
    numFind = 0
    razn2 = X
    numFind2 = 0
    print(numbers)
    for n in numbers:
        if X != n: # если не равно искомому, то будем проверять
            if X>n: # поиск по тем что меньше
                if Valid(X,n, razn):
                    numFind = n 
                    razn = X-n
            else: # поиск по тем что больше
                if Valid(n,X, razn):
                    numFind2 = n 
                    razn2 = (X-n)*-1
        else:
            numFind = n 
            razn = X-n
    if razn<=razn2: # выберем наименьший по разнице отставания
        print(f"Число {numFind} ближайшее к {X}")
    else:
        print(f"Число {numFind2} ближайшее к {X}")
except:
    print("Упс, что-то пошло не так")