"""
for loop di python kurang mirip dengan bahaa pemrograman lain
Perulangan `for` digunakan untuk mengulang suatu urutan (baik berupa list, tuple, dictionery, himpunan, atau string
lebih mirip dengan metode iterator seperti yang ditemukan dalam bahasa pemrograman berorientasi objek lainnya.
"""

fruits = ["apple", "banana", "cherry"]
for x in fruits: 
  print(x)

#Bahkan string pun merupakan objek yang dapat diiterasi, karena string berisi urutan karakter.
for x in "banana":
  print(x)
#bisa menggunakan statement break dan continue

for x in range(2, 6): # looping dari  2 sampai 6
  print(x)

for x in range(2, 30, 3): #setiap looping ditambah 3
  print(x)
