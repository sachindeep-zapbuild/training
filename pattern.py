#r=4
#c=r*2-1
n=4
for i in range(0,n):
	for j in range(0,n-i):
		print(" ",end='')
	for j in range(0,i+1):
		print("* ",end="")
	print("\r")
 
