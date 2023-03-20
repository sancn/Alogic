# #list comp combines the elements of two list if they are not equal
# newlist=[(x,y) for x in [1,2,3] for y in [3,1,4] if x!=y]
# print(newlist)

vec=[-4,-2,0,2,4]
#new list with value doubled
newlist1=[x*2 for x in vec]

#filter list to exclude negative number
newlist2=[x for x in vec if x>=0]

#apply the function to all element
newlist3=[abs(x) for x in vec]
print(newlist3)


print(newlist2)
