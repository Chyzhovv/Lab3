import string

set1 = set(string.ascii_letters + string.digits[3:7] + string.digits[:5])
set2 = set(string.ascii_letters + string.digits[3:7] + string.digits[6:])

print(set1)
print(set2)
tpl_intersection = tuple(set1.intersection(set2))
print(tpl_intersection)  

tpl_diff = tuple(set1.difference(set2))
print(tpl_diff)   

print(tpl_intersection[:3]) 

print(set(string.digits).intersection(set2)) 

print(tpl_intersection[::-1])
print(list(tpl_intersection), list(tpl_diff))

