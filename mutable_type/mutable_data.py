# l1 = [1, 2, 3]

# loc_1 = id(l1)
# print("Initial Location:", loc_1)

# print(l1[0])  # Accessing the first element of the list
# l1[0] = 10  # Modifying the first element of the list
# loc_2 = id(l1)

# print(l1[0]) 

# loc_2 = id(l1)
# print("Final Location:", loc_2)

s1 = {1,2,3}
print(s1)
print("Initial Location:", id(s1))
s1.add(4)
s1.add(5)
s1.add(6)
print("Final Location:", id(s1))

print(s1)
