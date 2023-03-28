def Fibonacci(n):
	if n<=2:
		return 1
	else:
		return Fibonacci(n-1) + Fibonacci(n-2)

def xuat_dayso(n):
	for i in range(1, n+1):
		print(Fibonacci(i), end="\t")
print(Fibonacci(6))
xuat_dayso(6)