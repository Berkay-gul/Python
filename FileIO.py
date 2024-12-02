"""
f=open("File_name")
f.read()

"""
file = open('story.txt')

print(file.read())
file.seek(0)#curser i baslangica goturmeye yariyor
print(file.readline())#satir satir dosyayi okumamiza yariyor
file.seek(0)
print(file.readlines())#her satiri bir liste seklinde dondurur.
file.seek(0)
#file.close() methodu ile dosya kaynak tuketmemesi icin islem bittikten sonra kaptilmali
file.close()

#========================================================== daha elverisli bir syntax
with open("hikaye.txt" ,"w") as f:# ne olursa olsun islem sonunda .closed() calistiriliyor 
    f.write("deneme")# icerigi silerek ustune yaziyor
