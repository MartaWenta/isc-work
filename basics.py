forward=[]
backward=[]
values=["a","b","c"]
for i in values:
    forward.append(i)
    backward.insert(0,i)

print forward
print backward

