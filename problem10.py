# Вы принимаете от пользователя последовательность чисел, разделённых запятой. Составьте список и кортеж с этими числами.
a = input()
b = [int(i) for i in a.split(',')]
c = tuple(b)
print(b, c)
