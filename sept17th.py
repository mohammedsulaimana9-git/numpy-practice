# cooked my 1st code 
R,B = map(int,input().split())

G = min(R,B)

R_left = R-G
B_left = B-G

skills = (G*5)+(R_left*1)+(B_left*2)
print(skills)