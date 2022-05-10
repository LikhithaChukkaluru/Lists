# l=["385","25","82","98","20"]
# i=0
# b=[]
# while i<len(l):
#     c=l[i][-1]    
#     b.append(c)    
#     i+=1
# print(b)

# l=[385,25,82,98,20]
# i=0
# b=[]
# while i<len(l):
#     c=l[i]%10
#     b.append(c)    
#     i+=1
# print(b)

# 3.

# l=[100,101,2010,230]
# b=[]
# for i in range (len(l),2) :
#     b.append ([l[i],l[i+1]])
# print(b)


# a=[10,1000,100,101,1010]
# d=[]
# i=0
# while i<len(a):
#     b=str(a[i])
#     c=""
#     j=0
#     while j<len(b) :
#         if  b[j] !="0" :
#             c+=b[j]
#         j+=1
#     d.append((c))
#     i+=1
# print(d)

# 4.

# l=[2, 3, 3.2, (2+5j), "3", 3.98, "8","likki","amma",(2,5)]
# b=[]
# c=[]
# d=[]
# e=[]
# f=[]
# # we can also use ""== "instead of is 
# for i in l:
#     if type (i) is  int:  
#         b.append (i)
#     elif type (i) is float :
#         c.append (i)
#     elif type (i) is complex :
#         d.append (i)
#     elif type (i) is str :
#         e.append (i)
#     elif type (i) is tuple :
#         f.append (i)
# print(b)
# print(c)
# print(d)
# print(e)
# print(f)

# a=[1,2,3]
# b=[4,5,6]
# c=a+b
# # print(c)

# a=[1,2,3,8]
# b=[4,5,6,7]
# i=0
# c=[]
# while i<len(a) :
#     if a[i] not in c :
#         c.append(a[i])
#     if b[i] not in c :
#         c.append (b[i])
#     i+=1
# print(c)


# ,2],[10,5,9,90,9],[2,5,7],[3,5,9],[2,4,5,10,90,6,98],[789]]
# l.sort(key=len)
# print(l)
# i=0
# count=1
# while i<len(l):
#     j=0
#     count1=0
#     while j<len(l[i]):
#         count1+=1
#         j+=1  
#     i+=1
# count+=1
# print(count1)
# print(count)

# l=["anu","likki","even","odd"]
# i=0
# while i<len(l):
#     if len(l[i])%2!=0 :
#         print(l[i],"odd")
#     else :
#         print(l[i],"even")
#     i+=1

# a="it is a good"
# i=0
# c=0
# while i<len(a):
#     if a[i]==" " :
#         c+=1
#     i+=1
# print(c)

# list1=[1,2,3,45]
# list2=[67,45,32,0]
# for x in list1:
#          for y in list2:
#              if x == y:
#                  print("true")
#              else  :
#                 print("False")

# print(1 in [[1],2,3])

# test_list1 = [ [1, 2], [3, 4], [5, 6] ]
# test_list2 = [ [3, 4], [5, 7], [1, 2] ]
# res_list = []
# for i in test_list1:
#     if i not in test_list2:
#         res_list.append(i)
# for i in test_list2:
#     if i not in test_list1:
#         res_list.append(i)
# print ("The uncommon of two lists is : " + str(res_list))

# l=[1,2,3]
# i=1
# b=[]
# while i<len(l):
#     j=1
#     while j<10 :
#         t=j*i
#         b.append(t)
#         j+=1
#     i+=1
# print(b)

# str_1 = "Hire freelance developers"
# list_1 = list(str_1.strip(" "))
# print(list_1)

# l = [ 1, 6, 3, 5, 3, 4 ]
# i=0
# while i<len(l):
#     if l[i]==4 :
#         print("yes")
#     else :
#         print("no")
#     i+=1
# list1 = [10, 20, 4, 45, 99]

# lst = [[1, 2, 3],
#        [3, 2, 1],
#        [2, 2, 2]]
# lst.sort(key=len)
# print(lst)

# l=["likki","likki","usha","manu","thri"]
# l1=[]
# for i in l:
#     if i not in l1:
#         l1.append(i)
# print(l1)


# a = [[1, 2, 3],[4, 5, 6], [7, 8, 9],[4,5,10]]  
# rows = len(a);  
# cols = len(a[0])
# for i in range(0, rows):  
#     sumCol = 0;  
#     for j in range(0, cols):  
#         sumCol = sumCol + a[j][i];  
#     print("Sum of " + str(i+1) +" column: " + str(sumCol));  


# l=[[78,76,94,86,88],[91,[71,98],65],[95,45,[78,87,67,49],68,88]]

# s=[]
# sum=0
# for i in l :
#     if type (i) is list :
#         for j in i :
#             # if  type (j) is list :
#                 # for k in j :
#                     sum=sum+(j)
#                     print(sum)
#                     s.append(k)
#             else :
#                 s.append(j)
#     else :
#         s.append(i)
# print(s)
# sum=0
# for i in s :
#     sum+=(i)
#     print(sum)


# # 1.
# l=["likhitha","mom","dad","rhutuja"]
# i=0
# b=[]
# count=0
# while i<len(l):
#     c=l[i][::-1]
#     if l[i]==c:
#         print(c)
#         b.append (c)
#         count+=1  
#     i+=1
# print(b)
# print(count)


# a_string = "addbdcd"
# a_string = a_string.replace("d", "")
# print(a_string)


# SORT 

# l=[1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,1]
# a=int(input("enetr "))
# for i in l:
#     b=l[:-(a)]
# print(b)

# lst = [[2, 2], [4], [1, 2, 3, 4], [1, 2, 3]]
# lst.sort(key=len)
# print(lst)


# l = [[4, 1, 6], [7, 8], [4, 10, 8]]
# for i in l: 
    # l.sort()
    # i.sort()
    # l.sort(key=len)
# print(l)
# print(l)