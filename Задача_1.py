# Задача1: Найдите сумму цифр трехзначного числа n.
# Результат сохраните в перменную res.

# Ввод числа n
n = int(input("Введите трехзначное число: "))

# Сумма всех цифр числа
res = n // 100 + (n // 10) % 10 + n % 10

# Вывод результата
print("Сумма цифр трехзначного числа:", res)
