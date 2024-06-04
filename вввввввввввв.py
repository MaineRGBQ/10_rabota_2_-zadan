Keisuke_Baji1 = set(map(int, input("Введите эл.первого множества через пробел: ").split()))
Keisuke_Baji2 = set(map(int, input("Введите эл. второго множества через пробел: ").split()))

Chifuyu_Matsuno1 = set(Keisuke_Baji1)
Chifuyu_Matsuno2 = set(Keisuke_Baji2)

print("Уник. числа в первом множ:", Chifuyu_Matsuno1)
print("Уник. числа во втором множ:", Chifuyu_Matsuno2)

Manjiro_Sano = sorted(Chifuyu_Matsuno1.intersection(Chifuyu_Matsuno2))

print("Числа, которые входят как в первое, так и во второе множество в порядке возрастания:", Manjiro_Sano)