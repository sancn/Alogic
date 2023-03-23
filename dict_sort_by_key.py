# sorting the dictinoary items by values using bubble short
my_dict = {'a':5, 'c':1, 'b':3, 'e':4, 'd':2}

my_list = list(my_dict.items())

n = len(my_list)
for i in range(n):
    for j in range(0, n-i-1):
        if my_list[j][0] > my_list[j+1][0]:
            my_list[j], my_list[j+1] = my_list[j+1], my_list[j]

for i in range(n):
    for j in range(0, n-i-1):
        if my_list[j][0] == my_list[j+1][0]:
            if my_list[j][1] > my_list[j+1][1]:
                my_list[j], my_list[j+1] = my_list[j+1], my_list[j]

sorted_dict = {}
for item in my_list:
    sorted_dict[item[0]] = item[1]

print(sorted_dict)
