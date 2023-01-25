# a= [1,2,3,4,5]
# b= [2,4,5]
# #print([i for i in a if i not in b])
# c = []
# for i in a:
#     if i not in b:
#         c.append(i)
# print(c)       

lst = ['a','b','c']

remove_index = lst.index('b')
lst.pop(remove_index)
print(lst)