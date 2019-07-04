n=int(input())
facto=1
if n<0:
  print("no factorial")
else:
  for i in range(1,n+1):
    facto=facto*i
  print(facto)
