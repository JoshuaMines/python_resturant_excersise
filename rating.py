"""Restaurant rating lister."""


# put your code here
resturant_dict = {}
f = open("scores.txt")
y = sorted(f)

for line in y:
        k,v=line.strip().split(':')
        resturant_dict[k.strip()] = int(v)
        print((k + "was rated" + v )) 


k = input("what is your favorite resutrant?")
v = int(input("What would you rate that resturant?"))

resturant_dict[k] = v


for lines in resturant_dict.items():
    k,v=lines
    resturant_dict[k.strip()] = int(v)
    print(lines) 

