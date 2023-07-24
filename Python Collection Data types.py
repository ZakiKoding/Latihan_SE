# Tuple 

tupleExample = (2, 3)
print(tupleExample[1])

# Dictionary 
# Dicttionary digunakan untuk menyimpan data dalam bentuk key:value

Pelanggan = {
"id" : 600,
"name" : "Zaki",
"Pekerjaan" : "Manajer"
}


print(Pelanggan["Pekerjaan"])

# Set union, Difference, Intersection, Symentic Difference

numbers1 = {1,4,3,5}
numbers2 = {4,3,2,4,9}

# numbers_value = numbers1.union(numbers2) output : {1, 2, 3, 4, 5, 9}
# print(numbers_value)


# Difference1 = numbers1.difference(numbers2) output : {1, 5}
# print(Difference1)


# sym_difference = numbers1.symmetric_difference(numbers2) output : {1, 2, 5, 9}
# print(sym_difference)


#intersect = numbers1.intersection(numbers2)  output : {3, 4}
#print(intersect)

# Create and call

def hai() :
    print("\"Halo kamu semangat terus ya...\"")

hai()
# Parameters = name, age
def halo(name,age) : 
    print("name : " + name)
    print("Age : " + str(age))

# halo("zaki", 19)
# halo(age = 19, name = "zaki")


# Function Part 2

def hitungan5(z):
    statistik = z + 10
    return statistik
print(hitungan5(90))
# Oke deh mantappo

z = 100
statistik = (hitungan5(z) * z) * (125 + 125)
print(statistik)

# Lambda Function untuk 1 baris

saya = lambda z : (z + 90) / (z + 0)
print(saya(150))


# Class dan objects part 1

class person:
    nama = "budi woe"

obj = person()
print(type(obj))
print(obj.nama)

obj2=person()
print(obj2.nama)

# Function INIT biar dapat custom 
# tiap nilai dari objeknya jadi berbeda objeknya ketika melakukan print
class person: 
    def __init__(self, name, age, ego):
        self.name = name
        self.age = age
        self.ego = ego
    def greet(self):
        print("oii "+ self.name +",Kamu umur " + str(self.age) + " yaa?")

p1 = person("Zaki", 19, "High")
p2 = person("Hamza", 20, "Stable")


p1.greet()
p2.greet()

print(p1.name)
print(p1.age)
print(p1.ego)



# Dapat dibuat untuk membuat aplikasi yang efektif

class Hewan: # parent class
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def greet():
        print("hello " + self.name + " umurnya pasti " + str(self.age))

class kuda(Hewan): # Child Class
    def __init__(self, name, age, color, weight):
        super().__init__(name, age)
        self.color = color
        self.weight = weight

class sapi(Hewan): 
    def __init__(self, name, age, color, weight, types):
        super().__init__(name, age)
        self.color = color
        self.weight = weight
        self.type = types


file = open("Coding.txt", "r")
file.read()



