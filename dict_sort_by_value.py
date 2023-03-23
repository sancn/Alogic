#sorting the dictionary values by using bubble short in ascending order
my_dict = {'a':5, 'c':1, 'b':3, 'e':4, 'd':2}
my_list = list(my_dict.values())
n = len(my_list)
for i in range(n):
    # for j in range(n-i-1):
    for j in range(n-i-1):

        if my_list[j]<my_list[j+1]:
            temp=my_list[j]
            my_list[j]=my_list[j+1]
            my_list[j+1]=temp
print("Sorted values is:",my_list)
