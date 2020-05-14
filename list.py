#LIST AND ITS FUNCTIONS

#append add new element to list
print("appending\n")
a = ["bee","moth"]
print("a =",a)
a.append("ant")
print("after appending a =",a)

#extend join two list
print("\nextending\n")
b = ["bug","beetle"]
print(" b =",b)
b.extend(["ant","cricket"])
print("after extend b =",b)

#insert join element at a given position
print("\ninserting\n")
c = ["ball","bat"]
print("c =",c)
c.insert(0,"pads")
print("now c =",c)
c.insert(2,"gloves")
print("and now c =",c)

#remove remove item in list
print("\n removing \n")
d = ["cat","dog","duck","hen"]
print("d =",d)
d.remove("duck")
print("after removing d =",d)

#pop remove item from given position
print("\npopping\n")
#1 positon not given then remove last item
print("position not given")
e = ["ant","bug","mice","crane"]
print("e =",e)
e.pop()
print("after just pop e =",e)
#2 position given
print("positon given")
e.pop(1)
print("after popping at positon 1 e=",e)

#index find position of item
print("\n indexing\n")
f = ["archer","athelete","kayaker","sprinter"]
print("f =",f)
print("archer position in list is",f.index("archer"))
print("kayaker position is ",f.index("kayaker"))

#count returns number of times the item repeats in LIST
print("\ncount\n")
g = ["ant","elephant","bee","ant","bee"]
print(" g =",g)
print("number of times ant in list ",g.count("ant"))
print("and elephant",g.count("elephant"))

#len returns length/number of items of LIST
print("\nlen\n")
h =["ant","wasp","moth","bug","beetle","worms"]
print("h =",h)
print("number of items in list:",len(h))

#max return maximum value in list
print("\nmax\n")
i =["helmet","license","bike","certificate","rules"]
print("i =",i)
print("maximum in i:",max(i))
j=[1,2,3,3,6,2,8]
print("j =",j)
print("minimum in j:",max(j))

#min return minimum value in LIST
print("\nmin\n")
i =["helmet","license","bike","certificate","rules"]
print("i =",i)
print("minimum in i:",min(i))
j=[1,2,3,3,6,2,8]
print("j =",j)
print("minimum in j:",min(j))
