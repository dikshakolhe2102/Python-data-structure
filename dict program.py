# #declare dictionary with employee name,id,and salary and print dictionary
# d={'Name':'abc','Id':123,'salary':1000}
# print(d)

# #declare dictionary for customer name, customer id, customer bill no and print dictionary
# d1={'customer name':'diksha','customer id':123,'customer bill no':1234}
# print(d1)

# d2={'customer name':['diksha','prachi','anushka'],'customer id':123,'customer bill no':1234}
# print(d2)

# #take dictionary value and key from user
# d={}
# key=input("Enter key:")
# value=input("Enter value:")
# d[key]=value
# print(d) 

# #using for loop
# d1={}
# for i in range(3):
#     key=input("Enter key:")
#     value=input("Enter value:")
#     d[key]=value
#     print(d) 

#to check given key is exist in dictionary or not
# d={}
# for i in range(3):
#     key=input("Enter key:")
#     value=input("Enter value:")
#     d[key]=value
#     print(d) 
# k=input("Enter key:")
# print(k)
# print(d.get(k,"Not found"))

#to take a list of string 
# and returns a dictionary where the keys are string lengths, 
# and the value are list of string of that length.


l=[]
for i in range(4):
   a=input("Enter list element:")
   l.append(a)
   print(l)
d={}
for i in l:
   l1=len(i)
   if(l1 not in d):
      d[l1]=[]
   d[l1].append(i)
print(d)     


# write a program to count the freqency of each word in a given sentence using a dictionary
# d={}
# str="Python is great and python is easy to learn python great"
# print(str)
# for i in str.split():
#     i=i.lower()
#     if i in d:
#        d[i]=d[i]+1

#     else:
#         d[i]=1
# print(d)
    
#how to count frequency of character

# d={}
# str="Python is great and python is easy to learn python great"
# for i in str:
#     i=i.lower()
#     if i in d:
#        d[i]=d[i]+1

#     else:
#         d[i]=1
# print(d)
    

# to given key value pair from dictionary
# d={}
# for i in range(2):
#     key=input("Enter key:")
#     value=input("Enter value:")
#     d[key]=value
#     print(d)
# k=input("Enter a key which you want to remove")
# print("Value removed:",d.pop(k))
# print(d)

#to to swap key and value
# d1={}
# for i in range(2):
#     k=input("enter key:")
#     v=input("enter value:")
#     d1[k]=v
# print(d1)
# swap={}
# for i, (k,v) in enumerate(d1.items()):
#     swap[v]=k
# print("Affter swapping:",swap)

#19/06/2025
#find min and max in values
d={1:"diksha",2:"two"}
b=d.values()
print(min(b))

#print(b)
#sort according to value
d={1:"diksha",2:"two"}
b=d.values()
print(sorted(b,reverse=True))











