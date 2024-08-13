# Сложите цифры целого числа.
n = int(input())
cnt = 0
for i in str(n):
    cnt += int(i)
print(cnt)