nam = int(input("Nhap nam bat ky: "))
if (nam%4==0 and nam%100 !=0) or (nam %400 ==0):
	print("nam nhuan")
else:
	print("nam méo nhuan")