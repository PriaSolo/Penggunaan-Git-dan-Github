#python operator
print(10 + 5)
#bisa juga menjumlahkan 2variabel
sum1 = 67 + 67
sum2 = 76 + 76
sum3 = sum1 + sum2
print(sum1)
print(sum2)
print(sum3)
#logical operation
#and kalau salah satu betul berarti statementnya true
x=5
print(x>0 and x<10)
#or hasilnya true kalau salah satu betul
x=5
print(x>0  or 10)
#not membalikkan nilai statement
x = 5

print(not(x > 3 and x < 10))
#identity operator
#is kalau variabelnya sama hasilnya true
x = ["apple", "banana"]
y = ["apple", "banana"]
z = x

print(x is z)
print(x is y)
print(x == y)
#is not true kalau ke 2 variabel tidak menunjuk ke satu objek
#is ngecek variabel apakah sama
#== ngecek variabel apakah setara
#membership op
fruits = ["apple", "banana", "cherry"]

print("banana" in fruits)
#in true kalau ada di variabel
fruits = ["apple", "banana", "cherry"]

print("pineapple" not in fruits)
#not in true kalau objek gaada di variabel

