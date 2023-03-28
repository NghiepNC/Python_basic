def tinhRoi(doanhthu, chiphi):
	return (doanhthu-chiphi)/chiphi

def goiy_dautu(x):
	if x >0.75:
		return "Nên đầu tư"
	else:
		return "Không nên đầu tư"

print ("Hay nhap doanh thu và chi phi")
doanhthu, chiphi = eval(input())
ROI = tinhRoi(doanhthu, chiphi)
print("Tỉ lệ ROI ", ROI)
print("==> gợi ý đầu tư: ", goiy_dautu(ROI))