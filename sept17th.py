# cooked my 1st code 
R,B = map(int,input().split())

G = min(R,B)

R_left = R-G
B_left = B-G

skills = (G*5)+(R_left*1)+(B_left*2)
print(skills)

#code 2
# cook your dish here
Testcases = int(input("Enter the number of testcases: "))
for i in range(Testcases):
    x = int(input())
    if(x<=100):
        print(x)
    elif(x>100):
        y = x-10
        print(y)
    
# code 3

T=int(input())
for i in range(T):
    x = int(input())
    if(x<67 or x>45000):
        print("No")
    else:
        print("Yes")

#code 4
T=int(input())
for i in range(T):
    N,M = map(int,input().split())
    if (M<=N):
        print(N-M)
    elif(M>N):
        print("0")
                
#code 5
T= int(input())
for i in range(T):
    x = int(input())
    if(x<30):
        print("NO")
    elif(x>=30):
        print("YES")                