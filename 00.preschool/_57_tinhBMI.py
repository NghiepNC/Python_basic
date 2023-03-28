# hàm tính BMI

def HamBMI(x,y):
	""" x: cân nặng
	y: chiều cao
	Hàm này trả về chỉ số BMI"""
	return x/(y**2)   

can_nang, chieu_cao = eval(input(" Nhập vào cân nặng(Kg) và chiều cao nhé(m): "))
BMI = HamBMI(can_nang,chieu_cao)
print ("Chỉ số BMI của bạn là:  ", round(BMI,2))
if BMI <18.5:   
	print( "Loại: Gầy , Nguy cơ bệnh: Thấp")
elif (BMI < 24.9):
	print  ( "Loại: bình thường , Nguy cơ bệnh: trung bình")
elif (BMI < 29.9):
	print  ( "Loại: hƠI béo , Nguy cơ bệnh: Cao")
elif (BMI < 34.9):
	print  ( "Loại: Béo phì cấp độ 1 , Nguy cơ bệnh: Cao")
elif (BMI < 39.9):
	print  ( "Loại: Béo phì cấp độ 2 , Nguy cơ bệnh: Rất Cao")
elif BMI>=39.9:
	print  ( "Loại: Béo phì cấp độ 3 , Nguy cơ bệnh: Nguy hiểm")	
else:
	print ("Quái vật hả !!")