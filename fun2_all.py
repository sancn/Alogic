mylist=[0,1,1]
print(all(mylist))

########
mylist2=[1,1,1,1]
print(all(mylist2))

##########
mytup=()
print(all(mytup))

############
mydict={0:'hello',1:'hi',1:'bye'}
print(all(mydict))

#############
mytuple = (1, 1, "True") #string dida ni huni raixa
x = all(mytuple)
print(x)

##########
#############
mytuple2 = (1, 1, "False") #return true bcoz it is a non empty string
x = all(mytuple2)
print(x)