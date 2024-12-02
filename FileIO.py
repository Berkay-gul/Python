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

"""# w - writes and erases existing contents
with open("haiku.txt", "w") as file:
    file.write("Here's one more haiku\n")
    file.write("What about the older one?\n")
    file.write("Let's go check it out")

# a - appends to end, preserving original contents
NO CONTROL OVER CURSOR
with open("haiku.txt", "a") as file:
	file.seek(0)
	file.write(":)\n")

# r+ read and write ------curserin konumunu kullaniyor  okumak ve yazmak icin 
with open("haiku.txt", "r+") as file:
	file.write(":)")
	file.seek(10)
	file.write(":(")

# r+ will not create a file if it doesn't exist
with open("hello.txt", "a") as file:
	file.write("HELLO!!!")
"""
