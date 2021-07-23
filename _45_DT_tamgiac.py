from math import sqrt
print("Nhập các cạnh của tam giác >0 nha ")
a = float(input("Cạnh thứ nhất: "))
b = float(input("Cạnh thức hai: "))
c = float(input("Cạnh thứ ba: "))

if (a*b*c)<= 0 or (a+b)<=c or (b+c)<=a or (a+c)<=b :
	print('Tam giác không hợp lệ')
else:
	cv = a+b+c   
	p = cv/2
	s = sqrt(p*(p-a)*(p-b)*(p-c))
	print("Dien tích là: ",s )