my_list = [42, 69, 0, 322, 13, 0, 99, -5, 9, 8, 7, -6, 5]
number = 0
i = 0
while number < len(my_list):
    if my_list[i] >= 0 :
        print(my_list[i])
        i = i + 1
    elif my_list[i] < 0 :
        print('Going abroad')
        break
