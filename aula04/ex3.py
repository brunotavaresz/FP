
# This program generates 20 terms of a sequence by a recurrence relation.
from itertools import count


Un = 100 

count = 0

while Un > 0:
    print(Un)
    count +=1
    Un = 1.01*Un - 1.01
    
print(count)
