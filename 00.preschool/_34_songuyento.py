# Kiểm tra số nguyên tố
while True:
	x = int(input("Nhap số x để kiểm tra số nguyên tố: "))
	dem =0
	for i in range(1, x+1):
		if x%i==0:
			dem +=1
	print (" Là số nguyên tố" if dem == 2 else "Không là số nguyên tố")

	Hoi= input("Còn muốn kiểm tra nữa không? ")
	if Hoi is "k":
		break
print ("Bye")