# 1.Iterate over both the values in a list and their indices

# grocery_list = ['flour','cheese','carrots']
# i=0
# while i<len(grocery_list):
#     print(grocery_list[i])
#     i+=1
# print(grocery_list)

# count=0
# for i in range (len(grocery_list)) :
#     print(grocery_list[i])
#     count+=1
# print(count)
# print(grocery_list)


# 2. Convert Character Matrix to single String;

# s=[['g', 'f', 'g'], ['i', 's'], ['b', 'e', 's', 't'] ]
# b=""
# c=[]
# i=0
# while i<len (s):
#     j=0
#     while j<len(s[i]):
#         b=b+s[i][j]
#         j+=1
#     i+=1
# c.append(b)
# print(c)


# 4. List product excluding duplicates

# l=[6,1,3,5,6,3,1]
# b=[]
# i=0
# r=1
# while i<len(l):
#     if l[i] not in b :
#         b.append (l[i])
#     i+=1
# mul=1
# for j in range(len(b)):
#     mul*=b[j]
# print(mul)


# 5. Count unique values inside a list.

# t = [1, 2, 2, 5, 8, 4, 4, 8]
# b=[]
# count=0
# i=0
# while i<len(t):
#     if t[i] not in b :
#         b.append (t[i])
#         count+=1
#     i+=1
# print(b)
# print(count)


# 9. Find the First Maximum, Second maximum, Third maximum number from the List.

# l=[1,4,7,9,3,9,3,10,29]
# for i in range (len(l)):
#     for j in range  (len(l)-1):
#         if l[j] > l[j+1] :
#             t=l[j]
#             l[j]=l[j+1]
#             l[j+1]=t
# print(l)
# print("first maxmimum number",l[-1])
# print("second maximum number",l[-2])
# print("third maximum number",l[-3])

# L=["Amit","Anita","Zee","Longest Word"]
# print(max(L))
# print(min(L))


# 11.For example, if we give 9119 the function should return 811181, as the square of 9 is 81 and square
# of 1 is 1.

# l=[9,1,1,9]
# for i in range(len(l)):
#     m=str(l[i]**2)
#     print(m,end="")

# i=0
# r=1
# while i<len(l):
#     r =str(l[i]**2)
#     i+=1
#     print(r,end="")


# 12. You will be given a number and you need to return it as a string in 
# Expanded Form.

# a=input("enter num :")
# l=len(a)
# i=l-1
# c=int(a)
# while i>=0 :
#     rev=c//(10**i)
#     sum=rev*(10**i)
#     c%=(10**i)
#     print((str(sum)),end=" ")
#     i-=1


# 13.Write a Python program to create a list reflecting the modified run-length encoding from
# a given list of integers or a given list of characters.

# l=[1, 1, 2, 3 , 5 , 6 , 3, 3, 4, 4, 5, 1,9,10]
# i=0
# c=[]
# while i<len(l):
#     count=1
#     if  l[i]==l[i+1]:
#         count+=1
#         c.append([count,l[i]])
#     else :
#         c.append(l[i])
#         c.append(l[i+1])
#     i+=2
# print(c)

# l=["a","a","b", "c","d","d","d","d","a","d","s","a"]
# i=0
# c=[]
# while i<len(l): 
#     count=1
#     if  l[i]==l[i+1] :
#         count+= 1
#         c.append([count,l[i]])
#     else :
#         c.append(l[i])
#         c.append(l[i+1])
#     i+=2
# print(c)

# l=[1,2,9,9,7,9]
# i=0
# b=[]
# while i<len(l):
#     count=1
#     if l[i]==l[i+1]:
#         count+=1
#         b.append([count,l[i]])
#     else :
#         b.append(l[i])
#         b.append(l[i+1])
#     i+=2
# print(b)


# 16. W rite a Python program to find the difference between elements (n+1th - nth)
#  of a given list of numeric values.

# l=[1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# b=[]
# for i in range (len(l)):
#     diff=l[i]-l[i]+1
#     b.append(diff)
# print(b)

# l=[2, 4, 6, 8]
# i=0
# b=[]
# while i<len(l):
#     diff=2+l[i]-l[i]
#     b.append (diff)
#     i+=1
# print(b)

# 19.

# l=[1,2,3,4]
# n=0
# for i in l :
#     a=(i*n)+1
#     print(i,a)
#     n=n+2


# 24.Remove duplicates from a list.

# List = [1,2,3,1,2,2]
# i=0
# b=[]
# while i<len(List):
#     if List[i] not  in b :
#         b.append (List[i])
#     i+=1
# print(b)


# 25 Given a List, extract all elements whose frequency is greater than K.

# t = [4, 6, 4, 3, 3, 4, 3, 4, 3, 8]
# L = []
# for i in t:
#     if i not in L:
#         if t.count(i) > 3:
#             L.append(i)
# print(L)

# l=[4, 6, 4, 3, 3, 4, 3, 4, 6, 6]
# l1=[]
# for i in l :
#     if i not in l1 :
#         if l.count(i)>2 :
#             l1.append(i)
# print(l1)

#  25. Given a List, extract all elements whose frequency is greater than K.

# l=[4, 6, 4, 3, 3, 4, 3, 4, 3, 8]
# b=[]
# k=4
# count=0
# for i in l :
#     count+=1
#     if i not in b :
#         if l.count (i) ==k :
#             b.append (i)
# print(b)

# l=[4, 6, 4, 3, 3, 4, 3, 4, 6, 6]
# i=0
# count=0
# k=4
# b=[]
# while i<len(l):
#     if i  not in  b :
#         if l.count(i) >= k:
#             b.append (i)
#     i+=1
# print(b)


# 26. Our task is to print the element which occurs 3 consecutive times 
# in a Python list.

# l=[1, 1, 1, 64, 23, 64, 22, 22, 22]
# count=1
# for i in range (len(l)-2) :
#     if  l [i] == l[i+1] and l[i+1]==l [i+2 ]:
#         count+=1
#         print(l[i])
# print(count)

# l=[4, 5, 5, 5, 3, 8]
# for i in range (len(l)-2):
#     if l[i] ==l[i+1] and l[i+1]== l[i+2] :
#         print(l[i])


# 27. Given 3 digits a, b, and c. The task is to find all the possible combinations 
# from these digits

# a=[1,2,3]
# for i in a :
#     for j in a :
#         for k in a :
#             if i!=j and j!=k and k!=i and j!=i and k!=j and i!=k  :
#                 print(i,k,j)

# l=["orange","red","green","blue"]
# for i in l :
#     for j in l :
#         for k in l : 
#             for s in l :
#                 if i!=j and j!=k and k!=s and i!=k and i!=s and j!=i and j!=s and j!=s and k!=i and k!=j and s!=i and s!=j and s!=k :
#                     print(i,k,j,s)


# 28.The task is to perform the operation of removing all the occurrences of a given item/element present in
# a list.

# l= [1, 1, 2, 3, 4, 5, 1, 2]
# b=[]
# i=0
# while i<len(l):
#     if l[i]!= 1:
#         b.append(l[i])
#     i+=1
# print(b)

# for i in l:
#     if l[i] != 1 :
#         b.append(l[i])
# print(b)

# l=[5, 6, 7, 8, 9, 10]
# b=[]
# i=0
# while i <len(l) :
#     if l[i] != 5 :
#         b.append (l[i])
#     i+=1
# print(b)


# 29. Remove empty List from List

# l=[5, 6, [], 3, [], [], 9]
# i=0
# b=[]
# while i<len(l):
#     if l[i] != [] :
#         b.append(l[i])
#     i+=1
# print(b)

# b=[]
# for i in range (len(l)) :
#     if l[i] != [] :
#         b.append(l[i])
# print(b)


# 30. Given a list of numbers, write a Python program to count positive and negative 
# numbers in a List.

# l= [2, -7, 5, -64, -14]
# i=0
# count=0
# count1=0
# while i<len(l):
#     if l[i] > 0 :
#         count+=1  
#     if l[i] < 0 :
#         count1+=1
#     i+=1
# print("positive numbers is ",count,"negative numbers is ",count1)

# l=[-12, 14, 95, 3]
# i=0
# count=0
# count1=0
# while i<len(l):
#     if l[i] >0 :
#         count+=1
#     if l[i] < 0 :
#         count1+=1
#     i+=1
# print("postive",count,"negative",count1 )


# 31. Given the start and end of a range, write a Python program to print all 
# negative numbers in a given range.

# i=-4
# while i<=5 :
#     if i==0 :
#         break
#     print(i,end=" ")
#     i+=1

# for i in range (-4,5):
#     if i==0 :
#         break
#     print(i,end=" ")


# 32. Given start and end of a range, write a Python program to print all positive 
# numbers in given range.

# i=-4
# while i<=5 :
#     if i >=0 :
#         print(i,end=" ")
#     i+=1

# for i in range (-4,6):
#     if i>= 0 :
#         print(i,end=" ")


# 33. Find the sum of number digits in List.

# l=[12, 67, 98, 34]
# i=0
# b=[]
# while i<len(l):
#     c=l[i]//10
#     d=l[i]%10
#     e=c+d
#     b.append (e)
#     i+=1
# print(b)

# l=[2345,876,648,87513,758]
# b=[]
# for i in l :
#     sum=0
#     for digit  in  str(i)  :
#         sum+=int(digit)
#     b.append(sum)
# print(b)


# 34. Write a Python program to remove all the values except integer values from a given
# array of mixed values.

# l=[34.67, 12, -94.89, 'Python', 0, 'C#']
# i=0
# b=[]
# while i<len(l):
#     if type (l[i])==int:
#         b.append(l[i])
#     i+=1
# print(b)

# l=[34.67, 12, -94.89, 'Python', 0, 'C#']
# b=[]
# for i in  range (len(l)):
#     if type (l[i])==int :
#         b.append (l[i])
# print(b)


# 35.Write a Python program to check if first digit/character of each element in a
#  given list is same or not.

# l=[1234, 922, 1984, 19372, 100]
# for i in l:
#     # a=str(i)
#     if l[0]=="1" :
#         print("true")
#     else :
#         print("false")
        
# l=['aabc', 'abc', 'ab', 'ha']
# for i in l:
#     a=str(i)
#     if l[1]=="a" :
#         print("True")
#     else :
#         print("false")


# 36.  Write a Python program to join adjacent members of a given list.

# l=['1', '2', '3', '4', '5', '6', '7', '8']
# i=0
# b=[]
# while i<len(l) :
#     b.append (l[i]+l[i+1])
#     i+=2
# print(b)


# 37. Write a Python program to join adjacent members of a given list.

# l=[1, 2, 3, 4, 5, 6]
# b=[]
# i=0
# while i<len(l)-1:
#     b.append ([l[i],l[i+1]])
#     i+=2
# print(b)

# l=[1, 2, 3, 4, 5, 6]
# b=[]
# for i in range (0,len(l)-1):
#     b.append ([l[i],l[i+1]])
# print(b)


# 38. Write a Python program to check if a given string contains an element, which
#  is present in a list.

# l="https://www.w3resource.com/python-exercises/list/"
# l1=['.com', '.edu', '.tv']
# for i in l1 :
#     print(i in l)


# 41. Write a Python program to find the dimension of a given matrix.

# l=[[1, 2], [2, 4]]
# b=[]
# count=0
# for i in range (len(l)):
#     count+=1
#     count1=0
#     for j in range (len(l[i])) :
#         count1+=1
# b.append(count)
# b.append(count1)
# print(b)

# l=[[1,2,3],[2,3,4]]
# count=0
# i=0
# while i<len(l):
#     count+=1
#     count1=0
#     j=0
#     while j<len(l[i]):
#         count1+=1
#         j+=1
#     i+=1
# print((count,count1))

# l=[[0, 1, 2], [2, 4, 5], [2, 3, 4]]
# count=0
# i=0
# while i<len(l):
#     count+=1
#     count1=0
#     j=0
#     while j<len(l[i]):
#         count1+=1
#         j+=1
#     i+=1
# print((count,count1))


#  42. Write a Python program to iterate a given list cyclically on 
# specific index position

# l=['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h']
# a=[]
# b=[]
# i=0
# while i<len(l):
#     if i > 2 :
#         a.append (l[i])
#     elif i < 3 :
#         b.append (l[i])
#     i+=1
# a.extend (b)
# print(a)
    
#     if i>=5 :
#         a.append(l[i])
#     else :
#         b.append(l[i])
#     i+=1
# a.extend(b)
# print(a)

# 43. Write a Python program to insert a specified element in a given list after 
# every nth element.

# l=[1, 3, 5, 7, 9, 11, 0, 2, 4, 6, 8, 10, 8, 9, 0, 4, 3, 0]
# i=0
# k=4
# b=[]
# while i<len(l):
#     if i==k :
#         b.append(20)
#         k+=4
#     b.append(l[i])
#     i+=1
# print(b)

# l=['s', 'd', 'f', 'j', 's', 'a', 'j', 'd', 'f', 'd']
# b=[]
# i=0
# k=3
# while i<len(l):
#     if i==k :
#         b.append ("Z")
#         k+=3
#     else :
#         b.append(l[i])
#     i+=1
# print(b)

# 44.Write a Python program to add a number to each element in a given list of numbers.
# Original lists:

# l1=[3, 8, 9, 4, 5, 0, 5, 0, 3]
# b=[]
# i=0
# while i<len(l1):
#     c=l1[i]+3
#     b.append(c)
#     i+=1
# print(b)

# l=[3.2, 8, 9.9, 4.2, 5, 0.1, 5, 3.11, 0]
# b=[]
# for i in range (len(l)):
#     c=l[i]+0.51
#     b.append(c)
# print(b)


# 46.Write a Python program to concatenate element-wise three given lists.

# l=['0', '1', '2', '3', '4']
# l1=['red', 'green', 'black', 'blue', 'white']
# l2=['100', '200', '300', '400', '500']
# i=0
# b=[]
# while i<len(l):
#     b.append ((l[i]+l1[i]+l2[i]))
#     i+=1
# print(b)


# 47. Write a Python program to convert a given list of strings into list of list

# l=['Red', 'Maroon', 'Yellow', 'Olive']
# y = []
# for i in l:
#     y.append([j for j in i])
# print(y)


# 48.Write a Python program to split a given list into specified sized chunks.

# data_list = [0,1,2,3,4,5,6,7,8]
# result =[]
# i=0
# while i <(len(data_list)-2):
#     result.append(data_list[i:i+2])
#     i+=2
# print(result)

# new_list = []
# new_list.append(data_list[:3])
# new_list.append(data_list[3:6])
# new_list.append(data_list[6:])
# print(new_list)


# # 50. Write a Python program to join two given list of lists of same length, 
# element wise.

# l=[[10, 20], [30, 40], [50, 60], [30, 20, 80]]
# l1=[[61], [12, 14, 15], [12, 13, 19, 20], [12]]
# i=0
# b=[]
# while i<len(l):
#     b.append(l[i] +l1[i])
#     i+=1
# print(b)

# l=[['a', 'b'], ['b', 'c', 'd'], ['e', 'f']]
# l1=[['p', 'q'], ['p', 's', 't'], ['u', 'v', 'w']]
# b=[]
# for i in range (len(l)):
#     b.append (l[i]+l1[i])
# print(b)


# n=[50,40,23,70,56,12,5,9]
# i=0
# max=0
# while i<len(n):
#     if max < n[i]:
#         max=n[i]
#     i+=1
# print(max)

# n=[50,40,23,70,56,12,5,9]
# i=0
# min=n[0]
# while i<len(n):
#     if min >i :
#         min=n[i]
#     i+=1
# print(min)



# 14. Write a Python program to find the list with maximum and minimum length.
# a=[[23,45,98,45,87,67],[5, 7],[0],[89,90,78,57,45,90,35,34], [13, 15, 17]]
# a=["sd","dfg","hjjfyjgHJZGD","jhf","jhgmh","jgh","jhghf"]


# max=0
# for i in a:
#     if len(i)>max
#         max=len(i)
#         res=i
# print(res,max) 

# b=1
# for i in a:
#     if len(i)>b:
#         b=len(i)
#         c=i
# print(c,b)
                    # minimum


# l=[[23,45,98,45,87,67],[5, 7],[0,6,7],[89,90,78,57,45,90,35,34], [13, 15, 17]]
# l=["syutr","fgjjhg","hjjfyjgHJZGD","f90kgyg","jhgmfdtrh","jghujuu","jhghf"]
# l=["kukju","kjug","jyj","kjghmcmv","jhvghft","jyhfgh"]
# m=l[4]
# for i in range (0,len(l)):
#     if len(m) >len(l[i]):
#         m=l[i]
#         print(m,len(m))

