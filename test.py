import random
def flipHeads(count):
    r=0
    for x in range(0,count):
        if random.randint(1,2)==random.randint(1,2):
            r+=1
    return r 
for x in range(0,5):
    print(flipHeads(5))
