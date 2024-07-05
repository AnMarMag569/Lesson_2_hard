n = int(input ('Введите целое число от 3 до 20 : '))
kod = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]
kod1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]
password = []
for i in kod:
    for j in kod1:
        if (i + j) > n:
            break
        elif n % (i + j) == 0 and i < j:
            password.append(i)
            password.append(j)
print(password)