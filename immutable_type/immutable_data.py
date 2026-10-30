# s1 = "Hello"
# s1 = "World"

t1 = (1, 2, 3)
t1 = (4, 5, 6)

a = 5
initial_loc = id(a)
a = 10
final_loc = id(a)

print("Initial Location:", initial_loc)
print("Final Location:", final_loc)