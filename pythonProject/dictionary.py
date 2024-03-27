mydict ={'python':'ml','a':'java','b':'cpp','c':'ai','d':'tensorflow','e':'data science'}

print(mydict)

res=mydict['a']
print(res)

c=mydict.get('python')
print(c)

mydict.pop('c')
print(mydict)

k=mydict.keys()
print(k)

v=mydict.values()
print(v)

mydict["car"]="tesla"
print(mydict)

values=list(mydict.items())
print(values)

mydict.update(e='hi')
print(mydict)

ret=mydict.setdefault('d',99)
print(ret)