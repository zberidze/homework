import random

x = [random.randint(1,100) for i in range(1 ,20)]
print(x)
y=sorted(x)
print(y)

low = 0
high = len(y) - 1
while low <= high:
    k=int(input("Введите число от 1 до 100:"))
    mid =(low + high) // 2
    guess = y[mid]
    if guess == k :
        print('Вы угадали')
        break
    if guess > k:
        print("Загаданное число меньше: ", guess)
        high = mid - 1
    else :
        print("Загаданное число больше: ", guess)
        low = mid + 1