"""
Fungsi adalah blok kode yang hanya berjalan saat dipanggil. 
Fungsi dapat mengembalikan data, nilai atau ekspresi sebagai hasilnya. 
Fungsi membantu menghindari pengulangan kode.
"""
def my_function():
  print("Hello from a function")

my_function() #memanggil function


def get_greeting():
  return "Hello from a function" #mengembalikan nilai

message = get_greeting() #disimpan ke dalam variabel
print(message)

#Argument
def my_function(fname): #fname adalah parameter
  print(fname + " Refsnes")

my_function("Emil") # Emil adalah argument
my_function("Tobias")
my_function("Linus")

#*args and **kwargs
#*args dan **kwargs memungkinkan fungsi untuk menerima jumlah argumen yang tidak diketahui
def my_function(*kids):
  print("The youngest child is " + kids[2]) #funsi hanya menerima argumen dari indeks ke 2 yaitu linus

my_function("Emil", "Tobias", "Linus")

"""
Parameter **kwargs** memungkinkan sebuah fungsi untuk menerima sejumlah argumen kata kunci. Di dalam fungsi, 
kwargs menjadi sebuah kamus yang berisi semua argumen kata kunci.
"""
def my_function(**myvar):
  print("Type:", type(myvar))
  print("Name:", myvar["name"])
  print("Age:", myvar["age"])
  print("All data:", myvar)

my_function(name = "Tobias", age = 30, city = "Bergen")

#local scope
"""
Variabel yang dibuat di dalam suatu fungsi termasuk dalam cakupan lokal fungsi tersebut, 
dan hanya dapat digunakan di dalam fungsi tersebut.
"""
#Variabel yang dibuat di dalam suatu fungsi akan tersedia di dalam fungsi tersebut.
def myfunc():
  x = 300
  print(x)

myfunc()

"""
Seperti yang dijelaskan pada contoh di atas, variabel x tidak tersedia di luar fungsi, 
tetapi tersedia untuk fungsi apa pun di dalam fungsi tersebut.
"""
def myfunc():
  x = 300
  def myinnerfunc():
    print(x)
  myinnerfunc()

myfunc()

#Global scope
#Variabel yang dibuat di luar fungsi bersifat global dan dapat digunakan oleh siapa saja.

x = 300

def myfunc():
  print(x)

myfunc()
print(x)

#Decorators
"""
Decorator adalah fungsi yang menerima fungsi lain sebagai input dan mengembalikan fungsi baru.
Dekorator dasar yang mengubah nilai kembalian dari fungsi yang didekorasi menjadi huruf besar.
"""
def changecase(func):
  def myinner():
    return func().upper()
  return myinner

@changecase
def myfunction():
  return "Hello Sally"

print(myfunction())

#Lambda
"""
Fungsi lambda adalah fungsi anonim kecil. 
Fungsi lambda dapat menerima sejumlah argumen, 
tetapi hanya dapat memiliki satu ekspresi.
"""
x = lambda a : a + 10
print(x(5)) #Tambahkan 10 ke argumen a, dan kembalikan hasilnya.

#recursion
"""
Rekursi adalah konsep matematika dan pemrograman yang umum. Artinya, 
sebuah fungsi memanggil dirinya sendiri. Hal ini memiliki keuntungan karena memungkinkan kita untuk melakukan perulangan melalui data untuk mencapai suatu hasil.
"""
#Sebuah fungsi rekursif sederhana yang menghitung mundur dari 5.
def countdown(n):
  if n <= 0:
    print("Done!")
  else:
    print(n)
    countdown(n - 1)

countdown(5)

#Generator
"""
Generator adalah fungsi yang dapat menghentikan dan melanjutkan eksekusinya. 
Ketika sebuah fungsi generator dipanggil, ia mengembalikan objek generator, yang merupakan sebuah iterator. Kode di dalam fungsi tersebut belum dieksekusi, melainkan hanya dikompilasi. 
Fungsi tersebut hanya dieksekusi ketika Anda melakukan iterasi pada generator.
"""

def my_generator():
  yield 1
  yield 2
  yield 3

for value in my_generator():
  print(value)
