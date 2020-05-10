n = int(raw_input()) 
arr = list(set(map(int,input().split()))) 
arr.sort() 
print(arr[-2])
