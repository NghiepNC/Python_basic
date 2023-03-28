from random import randrange
from time import sleep

while True:
	an_so = randrange(1,101)
	n=0
	win = False
	while (n<7):
		print (" Bạn có", 7-n,"lần chơi")
		n+=1
		so_doan = int(input("=> Mời bạn đoán số [1->100]: "))
		if an_so == so_doan:
			win = True
			break
		elif an_so >so_doan:
			print(" Ẩn số là số LỚN hơn số bạn đoán đó nha!")
		elif an_so < so_doan:
			print(" Ẩn số là số NHỎ hơn số bạn đoán đó nha!")

	if win ==False:
		print ("Bạn thua rồi!, ẩn số là ", an_so )
	else:
		print("HAY QUÁ DOÁN TRÚNG RỒI!!!!")	
		sleep (2)

	hoi = input("CHOI LẠI HÔNG ")
	if hoi == 'k':
		break

print (" cám ơn bạn đã sử dụng")
