'''

Welcome to GDB Online.
GDB online is an online compiler and debugger tool for C, C++, Python, Java, PHP, Ruby, Perl,
C#, OCaml, VB, Swift, Pascal, Fortran, Haskell, Objective-C, Assembly, HTML, CSS, JS, SQLite, Prolog.
Code, Compile, Run and Debug online from anywhere in world.

'''
#finding index 
name= "dharshini"
a= name.index("s")
print(a)

name="dharshini"
a=name.index("shi")
print(a)

name="Dharshini"
a=name.swapcase()
print(a)

name="Dharshini"
a=name.startswith("s")
print(a)

name="Dharshini"
a=name.endswith("d")
print(a)

#colletion list
l=[0.3,4,'true','dharsh']
l[1]='a'
print(l)

l=[0.3,4,'true','dharsh']
l[1]='a'
print(l[0:2])
#step index
l=[0.3,4,'true','dharsh']
l[1]='a'
print(l[0:4:2])

l=[0.3,4,'true','dharsh']
l[1]='a'
print(len(l))

l=[0.3,4,'true','dharsh']
a=l.append(3)
a=l.insert(1,'a')
print(l)



