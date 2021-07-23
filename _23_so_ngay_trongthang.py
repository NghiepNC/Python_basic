thang = int(input("Nhập cái tháng bạn muốn hỏi? "))
if thang in (1,3,5,7,8,10,12):
	print ("Tháng", thang , "có 31 ngay")
elif thang in (4,6,8,11):
	print ("Tháng", thang, "có 30 ngày")
elif thang == 2:
	nam= int(input("Bạn nhập thêm năm nha: "))
	print ("Tháng 2 năm ", nam, "có")
	print ("29 ngày" if (nam%4==0 and nam%100 !=0) or (nam %400 ==0) 
		else "28 ngày" )
else:
	print ("Tháng không hợp lệ")