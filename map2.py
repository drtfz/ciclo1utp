a = [1,2,3,4,5]
b = [7,8,9,10]
c = [8,10,20, 30]

d= list(map(lambda x,y,z :x*y*z, a,b,c))
print(d)
