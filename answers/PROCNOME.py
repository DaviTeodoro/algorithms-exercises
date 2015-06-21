#PROCNOME: reads 10 strings and creat a vector with them. 

n = int(input("How much names?"))
names = []

for i in range(0,n):
    name = input("The name is?")
    names = names.append(name)
