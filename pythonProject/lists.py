mylist=[10,20,40,30,'pradeep',60,70]

print(mylist)

print(mylist[1:5])

mylist[6]='python'
print(mylist)

mylist.append('hi')
print(mylist)

mylist.insert(9,90)
print(mylist)

#mylist.clear()
#print(mylist)

lis2=mylist.copy()
print("output : ",lis2)

sample_lst=[1,2,3,4,5]
mylist.extend(sample_lst)
print(mylist)

c_t=mylist.count(30)
print(c_t)

p=mylist.index(60)
print(p)

mylist.pop(5)
print(mylist)

mylist.remove(20)
print(mylist)

num=[6,7,2,3,1]
num.sort()
print(num)


mylist.reverse()
print(mylist)