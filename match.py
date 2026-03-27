#PYTHON MATCH
#dari pada banyak menulis if.. else,
#Pernyataan `match` memilih salah satu dari banyak blok kode untuk dieksekusi.

"""
match sama halnya dengan switch case pada bahasa pemrograman C
"""
#cara kerjanya sama dengan switch case, mencocokan ekspresi, nilai atau variabel dengan case
day = 4
match day:
  case 1:
    print("Monday")
  case 2:
    print("Tuesday")
  case 3:
    print("Wednesday")
  case 4:
    print("Thursday")
  case 5:
    print("Friday")
  case 6:
    print("Saturday")
  case 7:
    print("Sunday")

#kalau python default valeue nya pakai _
#default akan dijalankan jika tidak ada case" yang cocok atau sesuai dengan ekspresi
  case _:
    print("Looking forward to the Weekend")

"""
Gunakan karakter pipa (|) sebagai operator "atau" dalam evaluasi kasus 
untuk memeriksa kecocokan lebih dari satu nilai dalam satu kasus.
"""

day = 4
match day:
  case 1 | 2 | 3 | 4 | 5:
    print("Today is a weekday") #case ini cocok atau dijalankan jika value nya sama dengan match
  case 6 | 7:
    print("I love weekends!")

#kita bisa juga menggunakan statement if didalam case sebagai pengecekan tambahan
month = 5
day = 4
match day:
  case 1 | 2 | 3 | 4 | 5 if month == 4:
    print("A weekday in April")
  case 1 | 2 | 3 | 4 | 5 if month == 5:
    print("A weekday in May")
  case _:
    print("No match")
