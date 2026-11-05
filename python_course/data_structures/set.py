my_set = {10,30,20,10}
print(my_set)
my_set.add(50)

my_set |= {23}
print(my_set) 

my_set.discard(100)
print(my_set.pop())
print(my_set)

# math methods
a = {2,3,5,7,9,11}
b = {2,3,9,11,13,17}

print(a.union(b))
print(a.intersection(b))
print(a - b)
print(a.difference(b))
print(b - a)
print(b.difference(a))
print(a.symmetric_difference(b))
print(a^b)

print(a.issubset(b))
print(b.issuperset(a))
print(a.isdisjoint(b))

