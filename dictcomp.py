# # dict1 = {'a': 1, 'b': 2, 'c': 3, 'd': 4}
# # # Put all keys of `dict1` in a list and returns the list
# # print(dict1.keys())
# # print(dict1.values())
# # print(dict1.items())


# dict1 = {'a': 1, 'b': 2, 'c': 3, 'd': 4, 'e': 5}
# # Double each value in the dictionary
# double_dict1 = {k:v*2 for (k,v) in dict1.items()}

# double_dict2 = {k*2:v for (k,v) in dict1.items()}

# print(double_dict2)

# numbers=range(10)
# new_dict={n for n in numbers if n%2==0}
# print(new_dict)

# fahrenheit = {'t1': -30,'t2': -20,'t3': -10,'t4': 0}
# celsius={k:(float(5)/9)*(v-32) for (k,v) in fahrenheit.items()}
# print(fahrenheit)

dict1={'a':1,'b':2,'c':3,'d':4,'e':5}
# newdict={k:v for (k,v) in dict1.items() if v>=2}

newdict1={k:('even' if v%2==0 else 'odd') for (k,v) in dict1.items()}
print(newdict1)