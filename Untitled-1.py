
#angka_berkoma = 3.5
#angka= 10
#name= 'rifqi'

#print ( "hallo coe ni angka gua " + str(angka_berkoma) + " " + name + " " "(tetew)")

#print(type(angka_berkoma))
#print(type(angka))
#print(type(name))

prit

angka1 = 15
angka2 = 10

print(angka2 + angka1)
print(angka1%angka2)

angka = 14
print ("hasil yang ditambahkan dengan angka yaitu: " + str(angka))
#cara ke 1
angka = angka + 10
print ("hasil yang ditambahkan dengan angka yaitu: " + str(angka))
# cara ke 2
angka +=10
print ("hasil yang ditambahkan dengan angka yaitu: " + str(angka))

angka


import math
angka= 16

print(math.sqrt(angka))
print(math.pow(8,3))
print(math.floor(7.9))
print(math.pi)

# String

Text = "Coding studio"

print(Text.upper())
print(Text.lower())
print(len(Text))
print(Text.split(" "))
print(Text.index("stu"))

# Index positif tu dari 0 sampai seterusnya 
# Index Negatif itu dari -1 sampai seterusnya
Text = "Bash User"

print(Text[2:])
print(Text[0:7])

# String Concatenation

# String Format
mangga = 8
apel = 2
jeruk = 4

Text = " budi mempunyai {} mangga dan ale mempunyai {} apel, sedangkan shena mempunyai {} jeruk"

print(Text.format(mangga,apel,jeruk))

# Ada lagi ni boolean hahaha semangat like in vs not in gaiss

#Text = "Zaki and Friends"
#print("rafi" in Text) #false
#print("Zaki" in Text) #True


#x = 10
#y = 12
#z = 17

 #print(not( x > y))
 #print ( x > z or y > x)

 #if (x > z) :
  #  print ("X lebih besar dari Z")
#else :
  #  print ("X Tidak lebih besar dari Z")

#if (x == y) :
   # print (" X sama dengan Y")
#elif (x > y) :
 #   print ("X lebih besar dari Y")
#elif (z > y) : 
 #   print ("Wah Z lebih besar dari y nih")
#else : 
 #   print(" salah nih perhitungannya hahaha")

for i in range(0, 30, 5):
    print(" hoohoho")

for i in range(5):
    print("Jangan Percaya dengan emosi anda")

# Break and continue

for i in range(10,20,3):
    if i==19:
        break
    print(i)

# Continue = skip angka jika sesuai dengan rumus 
for i in range (2,14):
    if i%2 != 0:
        continue
    print(i)


Jajanan = 5000000
while (Jajanan > 0):
    print("Saya punya uang jajanan kampus sebesar: " + str(Jajanan))
    Jajanan -=100000

print("Habis deh uang jajanan :)")


for i in range (2,14,2):
        print(i)




