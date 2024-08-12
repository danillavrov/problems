my_dict = {'a':500, 'b':5874, 'c': 560,'d':400, 'e':5874, 'f': 20}
for h in range(3):
    max_ = max(my_dict.values())
    for i in my_dict:
        if my_dict[i] == max_:
            a = i
    print(a)
    del my_dict[a]