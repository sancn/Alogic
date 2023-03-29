# def fun_arg(*args):
#     print(args[0])
#     print(type(args))

# my_list=[1,2,3,4,5]
# fun_arg(*my_list)

# def fun_arg(*args):
#     for item in args:
#         print(item)
#     # print(type(args))

# my_list=[1,2,3,4,5,'apple']
# fun_arg(*my_list)

def fun_arg(normal,*args):
    print(normal)
    for item in args:
        print(item)
    # print(type(args))

my_list=[1,2,3,4,5,'apple']
normal=50
fun_arg(normal,*my_list)