# num=int(input("Enter the Number: "))
# output=[]
# for i in range(num,0,-1):
#     output.append(i)
    
# for i in range(1,num+1):
#     output.append(i)
# print(output)

# def NumPattern(n):
#     output=[]
#     for i in range(n,0,-1):
#         output.append(i)
#     for i in range(1,n+1):
#         output.append(i)
#     return output
# result=NumPattern(4)
# print(result)

######################################################
#recursion
def NumberPattern(n):
    output=[]
    def pushNum(i):
        if i==0:
            return
        else:
            output.append(i)
            pushNum(i-1)
            output.append(i)
    pushNum(n)
    return output
num=int(input("Enter Number:"))
result=NumberPattern(num)
print(result)