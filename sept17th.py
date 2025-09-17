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
    