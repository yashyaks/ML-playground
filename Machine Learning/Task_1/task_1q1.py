#code works but doesnt do anything with n so basically allows as many students as possible

n, x = map(int, input().split()) 

a = []
#map function can take multiple inputs in one line and appends it to variables/arrays 
for i in range(3):
    a.append(map(float, input().split())) 
     
'''for i in range (x):
    print(a[i])'''

#zip fucntion takes first element of each row and adds them
for i in zip(*a): 
    print(sum(i)/len(i))


'''#Code 2
n, x = map(int, input().split()) 

a = []
#map function can take multiple inputs in one line and appends it to variables/arrays 
for i in range(x):
    for j in range(n):
        a.append(map(float, input().split())) 

for i in zip(*a): 
    print(sum(i)/len(i))'''
        
