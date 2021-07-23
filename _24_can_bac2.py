#Nhập phương trình
import math
a = int(input("Nhập a: "))
b = int(input("Nhập b: "))
c = int(input("Nhập c: "))

if a==0:
	#bx+c=0
	if b==0 and c==0:
		print("Phương trình vô số nghiệm")
	elif b==0 and c!=0:
		print ("Phương trình vô nghiệm")
	else:
		print("Phương trình có nghiệm là:" , -c/b)
else:
	delta = b**2-4*a*c
	if delta<0:
		print("Phương trình vô nghiệm")
	elif delta ==0:
		print("Phương trình có nghiệm kép", -b/(2*a))
	else:
		x1 = (-b -math.sqrt(delta))/(2*a)
		x2 = (-b +math.sqrt(delta))/(2*a)
		print("nghiệm phương trình là", x1,"và",x2)