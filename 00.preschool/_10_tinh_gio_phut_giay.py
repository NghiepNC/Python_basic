t = int(input(" Nhap so giay : "))
gio = (t//3600)%24
phut = (t%3600)//60 
giay = (t%3600)%60

print (gio,":", phut ,":", giay )