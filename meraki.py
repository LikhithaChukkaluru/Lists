# names_list = ["rahul", "shivam", "kavay", "ashish", "rohit"]
# print(names_list)
# names_list.reverse()
# print(names_list)


#  SLICING

# t = ["rahul", "shivam", "kavay", "ashish", "rohit"]
# i=0
# while i<len(t):
#     b=t[::-1]  or t[-1::-1]
#     i=i+1
# print(b)

#  LOOP

# t = ["rahul", "shivam", "kavay", "ashish", "rohit"]
# l=[]
# for i in range (len(t)-1,-1,-1) :
#     l.append(t[i])
# print(l)

# Negative Indexing

# t = ["rahul", "shivam", "kavay", "ashish", "rohit"]
# l = []
# for i in range(1, len(t) + 1):
#     l.append(t[-i])
# print(l)

# t = ["rahul", "shivam", "kavay", "ashish", "rohit"]
# i=len(t)-1
# rev=[(t[i]) for i in range (len(t)-1,0,-1)]
# print(rev)

# l=[2,3,4,5,1,6,8,9]
# b=[]
# for i in range (1,len(l),1) :
#     b.append(l[-i])
# print(b)

# numbers=[50, 40, 23, 70, 56, 12, 5, 10, 7]
# count=0
# for i in numbers :
#     count+=1                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   
# print(count)

# s=[50, 40, 23, 70, 56, 12, 5, 10, 7]
# i=0
# count=0
# while i<len(s):
    # if s[i]>20 and s[i]<=40 :
        # count+=1
    # i+=1
# print( i,count)
    
# s=[50, 40, 23, 70, 56, 12, 5, 10, 7]
# count=0
# for i in s :
#     if i>=20 and i<=40 :
#         count+=1
# print(count)

s = [50, 40, 23, 70, 56, 12, 5, 10, 7]
for i in range (len(s)-1) :
    for j in range(len(s)-1):
        if s[j] > s[j+1] :
            s[j] ,s[j+1]=s[j],s[j+1]
            t=s[j]
            s[j]=s[j+1]
            s[j+1]=t
print(s)
print("maxmimun number",s[-1])
print("maximun second number",s[-2])


# s = [50, 40, 23, 70, 56, 12, 5, 10, 7]
# i=0
# while i<len(s) :
#     s.sort()
#     i+=1
# print(s)
# print("maxmimun number",s[-1])
# print("maximun second number",s[-2])

# places=["delhi", "gujrat", "rajasthan", "punjab", "kerala"]
# places.reverse()
# print(places)

# i=0
# while i<len(places):
#     b=places[::-1]
#     i+=1
# print(b)

# n=['n','i','t','i','n']
# i=0
# while i<len(n):
#     rev=n[::-1]
#     i+=1
# if n==rev :
#     print(n," is a palindrome")
# else :
#     print(n," is a not a palindrome")

# l=[1,1,1,1]
# i=0
# sum=0
# while i<len(l) :
#     b=l[3]%10
#     sum+=b*pow(2,i)
#     l[i]//=10
#     i+=1
# print(sum)

# l=[1,1,1,1]
# i=0
# sum=0
# while i<len(l) :
#     b=l[-1]%10
#     sum+=b*pow(2,i)
#     l[i]//=10
#     i=i+1
# print(sum)

# list1 = [1,2,3,4,5,6]
# list2 = [2,3,1,0,6,7]
# b=[]
# i=0
# while i<len(list1):
#     if i not in list2 :
#         b.append(i)
#     i+=1
# print(b)

# list1 = [1,2,3,4,5,6]
# list2 = [2,3,1,0,6,7]
# b=[]
# for i in list1:
#     if i not in list2 :
#         b.append(i)
# print(b)

# s = 30
# n = [10, 11, 12, 13, 14, 17, 18, 19]
# i=0
# while i<len(n) :
#     j=i+1
#     while j<len(n):
#         if n[i]+n[j]==s:
#             print([n[i],n[j]],end=" ")
#         j=j+1
#     i+=1

# students = ['Rishabh', 'Madhurima', 'Rahul', 'Abhishek', 'Faizal', 'Muskaan']
# marks = [10, 20, 56, 45, 36, 20]
# count=0
# while count<len(marks):
#     print(students[count]+str(marks[count]))
#     count+=1

# marks=[23,45,89,90,56,80]
# lenth=len(marks)
# i=0
# sum=0
# while i<len(marks):
#     sum+=marks[i]
#     i=i+1
# print(sum)

# l=[]
# i=0
# while i<10 :
#     a=int(input("enter the number"))
#     l.append(a)
#     i=i+1
# print(l)

# s = [23, 14, 56, 12, 19, 9, 15, 25, 31, 42, 43]
# i=0
# sum=0
# count=0
# while i<len(s):
#     if (s[i]%2==0) :
#         sum=sum+s[i]
#         count+=1
#     i+=1
# print("index",i,"sumof even numbers",sum)
# print("average", sum//count)
# print("count of even numbers",count)

# s = [23, 14, 56, 12, 19, 9, 15, 25, 31, 42, 43]
# i=0
# sum=0
# count=0
# while i<len(s):
#     if (s[i]%2!=0) :
#         sum=sum+s[i]
#         count+=1
#     i+=1
# print("index",i,"sumof odd numbers",sum)       
# print("average", sum//count)
# print("count of odd numbers",count)

# s = [23, 14, 56, 12, 19, 9, 15, 25, 31, 42, 43]
# i=0
# sum=0
# count=0
# while i<len(s):
#         sum=sum+s[i]
#         count+=1
#         i+=1
# print("index",i ,"sum of  numbers",sum)
# print("average", sum//count)
# print("count of  numbers",count)

# l=[3000,600000,324990909,90990900,30000,5600000,690909090,31010101,532010,510,4100]
# i=0
# count1=0
# count2=0
# count3=0
# while i<len(l) :
#     if l[i] < 100000 :
#         count1+=1
#     elif  l[i] <10000000 :
#         count2+=1
#     elif l[i] >= 10000000 :         
#         count3+=1
#     i+=1
# print("diwale ",count1)
# print("lakhpati",count2)
# print("crorepati",count3)

# c= ["a", "n", "t", "a", "a", "t", "n", "n", "a", "x", "u", "g", "a", "x", "a"]
# count1=0
# count2=0
# count3=0
# count4=0
# count5=0
# count6=0
# i=0
# while i<len(c):
#     if "a" in c[i] :
#         count1+=1
#     if "n" in c[i]:
#         count2+=1
#     if "t" in c[i]:
#         count3+=1'
#     if "x" in c[i]:
#         count4+=1
#     if "u" in c[i]:
#         count5+=1
#     if "g" in c[i]:
#         count6+=1
#     i=i+1
# print("a-", count1,"times")
# print("n-", count2,"times")
# print("t-", count3,"times")
# print("x-", count4,"times")
# print("u-", count5,"times")
# print("g-", count6,"times")

# c= ["a", "n", "t", "a", "a", "t", "n", "n", "a", "x", "u", "g", "a", "x", "a"]
# count1=0
# count2=0
# count3=0
# count4=0
# count5=0
# count6=0
# i=0
# while i<len(c):
#     if "a"in c[i] :
#         count1+=1
#     if "n"in c[i] :    
#         count2+=1
#     if "t"in c[i] :
#         count3+=1
#     if "x"in c[i] :
#         count4+=1
#     if "u"in c[i] :
#         count5+=1
#     if "g"in c[i] :
#         count6+=1
#     i+=1
# b=[["a",count1],["n",count2],["t",count3],["x",count4],["u",count5],["g",count6]]
# print(b)

# l1=[]
# for i in c :
#     b=0
#     for j in c :
#         if i==j :
#             b=b+1
#         if i not in l1 :
#             l1.append (i)
# print([l1,b],end=" ")

# m= "the quick brown fox jumped over the lazy dog. the dog slept over the verandah."
# i=0
# while i<len(m):
    # if "over" in m[i]:
        
# n = [19, 17, 12, 17, 17, 18, 10, 17, 14, 12, 19, 17, 12, 13, 11]
# b=[]
# i=0
# count=0
# while i<len(n):
#     if n[i]  in b:
#         b.append(n[i])
#         count+=1
#     i=i+1
# print(b,count,i)

# n = [19, 17, 12, 17, 17, 18, 10, 17, 14, 12, 19, 17, 12, 13, 11]
# b=[]
# for i in n :
#     if i not in b :
#         b.append(i)
# print(b)

# l=[2,7,8,3,9,2,1,9]
# for i in range (len(l)) :
#     for j in range(len(l)-1):
#         if l[j] > l[j+1] :
#             l[j] ,l[j+1]=l[j],l[j+1]
#             t=l[j]
#             l[j]=l[j+1]
#             l[j+1]=t
# print(l)

# marks = ["10", "32", "42", "65", "67", "89", "76", "38", "67"]
# sum = 0
# i= 0
# while i< len(marks):
#     sum+=int(marks[i])
#     i+=1 
# print(sum)
# a=["1","2"]
# i=0
# sum=0
# while i<len(a):
#     sum+=int(a[i])
#     i+=1
# print(sum)

# l=[[78,76,94,86,88],[91,71,98,65],[95,45,78,87,67,49,68,88]]
# i=0
# sum=0
# while i<len(l):
#     j=0
#     while j<len(l[i]):
#         sum+=l[i][j]
#         j+=1
#     i+=1
# print(sum)



#  PRACTICE


# 52.

# geekCodes = [1, 2, 3, 4]
# geekCodes.append([5,6,7,8])
# print(geekCodes)

# 53.

# check1 = ['Learn', 'Quiz', 'Practice', 'Contribute']
# check2 = check1
# check3 = check1[:]
# check2[0] = 'Code'
# check3[1] = 'Mcq'
# count = 0
# for c in (check1, check2, check3):
#     if c[0] == 'Code':
#         count += 1
#     if c[1] == 'Mcq':
#         count += 10
# print (count)
# print(check1)
# print(check2)
# print(check3)

# 54.

# list1 = range(100, 110)
# print (list1.index(105))

# 55.

# list1 = [1, 2, 3, 4, 5]
# list2 = list1
# list2[0] = 0
# print( list1)

# 56.

# List1 = [1998, 2002]
# List2 = [2014, 2016]
# print ((List1 + List2)*2)

# 57.

# list = [1, 2, 3, None, (1, 2, 3, 4, 5), ['Geeks', 'for','Geeks']]
# print(len(list))

# 58.

# print(list( range(4, 30, 2)))

# 59.

# for i in range(4,31):
#     if i%2 == 0:
#         print(i, end=' ')

# 60.

# a=[4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30]
# for i in a:
#     if i%2==0:
#         print(i, end=' ')

# 61.

# Index=int(input("num"))
# n=0
# for x in range (0,Index+1):
#     n+=x
# print(n)

# 62.

# list1 = [4, 6, 8, 24, 12,2]
# max= sorted(list1)
# print(max-1)
# print(max)

# 63.

# list = []
# n = int(input("enter the total numbers inside list.: "))
# i = 1
# while(i <= n):
#     num = int(input("enter the numbers you want to insert into list: "))
#     i +=1
#     list.append(num)
# print(list)
# list.sort()
# print(list)


# l=[2.2,2,4,5,1,1,1,2.2]
# b=set(l)
# print(len(b))


