"""
While akan terus looping ketika selama suatu kondisi dari while itu bernilai true
dan looping berhenti ketika terdapat suatu statement atau aksi yang mebuat 
kondisi sebelumnya itu bernilai true menjadi false
"""
i = 1
while i < 6: # kondisi akan selalu true jika i kurang dari 6
  print(i) #print akan terus dijalankan sampai kondisi i bernilai lebih atau sama dengan 6
  i += 1 


#Break statement
#break digunakan untuk memberhentikan looping walaupun kondisi masih bernilai true

i = 1
while i < 6:
  print(i)
  if i == 3: # jika i bernilai 3 maka break aka memberhentikan looping
    break
  i += 1

#continue 
#kalau continue digunakan untuk melankau kondisi tertentu atau terdapat suatu kondisi yang tidak ingin dijalan
i = 0
while i < 6:
  i += 1
  if i == 3:
    continue #perulangan angka 3 akan di abaikan 
  print(i)
