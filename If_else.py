a = int(input())
b = int(input())
c = int(input())
n = int(input())

listOfAnswers = [[i, j, k] 
for i in range(a + 1) 
  for j in range(b + 1) 
     for k in range(c + 1) 
if i + j + c != n] 
print(listOfAnswers)
