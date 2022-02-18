'''
my_l = [15, 26, 15, 1, 23, 64, 23, 76]
n_ls = []

while my_l:
    m = my_l[0]  
    for x in my_l: 
        #if x[0]==my_l[1]:
            #my_l.remove(m)
        if x < m:
            m = x
    n_ls.append(m)
    my_l.remove(m)    

print(n_ls)
'''

'''
By Using For loops

'''

'''
N_L = []

N = int(input("Please enter the Total N of List Elements: "))
for i in range(1, N + 1):
    value = int(input("Please enter the Value of %d Element : " %i))
    N_L.append(value)

for i in range (N):
    for j in range(i + 1, N):
        if(N_L[i] > N_L[j]):
            temp = N_L[i]
            N_L[i] = N_L[j]
            N_L[j] = temp

print("Element After Sorting List in Ascending Order is : ", N_L)
'''



l = [64, 25, 12, 22, 11, 1, 2, 44, 3, 122, 23, 34]

for i in range(len(l)):
    for j in range(i + 1, len(l)):

        if l[i] > l[j]:
           l[i], l[j] = l[j], l[i]  #Swap values
print (l)


