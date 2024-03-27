myset={1,2,3,4,5,6}

set={8,9,4,5,6,7}

for x in myset:
    print(x)

set2=myset.copy()
print(set2)

#myset.clear()
#print(myset)

print(myset.difference(set))
print(set.difference(myset))

res=myset.isdisjoint(set)
print(res)

print(myset.issubset(set))

print(myset.symmetric_difference(set))

myset |= set
print(myset)

