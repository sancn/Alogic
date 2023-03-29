
# def fun_karg(**kwargs):
#     for item in kwargs:
#         print(item)
#     # print(type(kwargs))


########################################################################

# kw={'country':'Nepal','capital':'Kathmandu','population':'3cr'}
# fun_karg(**kw)

# def fun_karg(**kwargs):
#     for key,value in kwargs.items():
#         print(key,value)
#     # print(type(kwargs))

# kw={'country':'Nepal','capital':'Kathmandu','population':'3cr'}
# fun_karg(**kw)

######################################################################

def fun_karg(*args,**kwargs):
    for item in args:
        print(item)
    print("\nInformation about Nepal:")
    for key,value in kwargs.items():
        print(f"{key}:{value}")
    # print(type(kwargs))

my_list=['apple','mango','banana']
kw={'country':'Nepal','capital':'Kathmandu','population':'3cr'}
fun_karg(*my_list, **kw)

x=[1,2,3,4,5]
y=[2,3,x]
print(x,y)