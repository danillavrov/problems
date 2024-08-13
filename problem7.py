# Нужно вывести первые n строк треугольника Паскаля. 
# В этом треугольнике на вершине и по бокам стоят единицы, а каждое число внутри равно сумме двух расположенных над ним чисел.
c = [0, 1, 0]
a = []
d = []
n = int(input())
for i in range(n):
    a.append(0)
    for j in range(len(c) - 1):
        a.append(c[j]+c[j+1])
    a.append(0)
    d.append(c)
    c = a

    a = []

for i in range(len(d)):
    d[i].pop(0)
    d[i].pop(-1)
    print(*d[i])