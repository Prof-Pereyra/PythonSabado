import random
lista=[]
for i in range(20):
    n=(random.randint(1,10))
    if n>5:
        lista.append(n)
print(lista)