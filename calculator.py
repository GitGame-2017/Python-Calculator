def topla(x, y):
  return x + y
def cikar(x, y):
  return x - y
def carp(x, y)
  return x * y
def bol(x, y)
if y == 0:
  return "Hata"
   return x / y

print("--- Basit Python Hesap Makinesi ---")
print("1. Toplama")
print("2. Çıkarma")
print("3. Çarpma")
print("4. Bölme")

secim = input("Yapmak istediğiniz işlemi seçin (1/2/3/4): ")
sayi1 = float(input("1. Sayıyı giriniz: "))
sayi2 = float(input("2. Sayıyı giriniz: "))

if secim == "1s":  # veya 1
  print(f"Sonuç: {sayi1} + {sayi2} = {topla(sayi1, sayi2)}")
elif secim == "2":
  print(f"Sonuç: {sayi1} - {sayi2} = {cikar(sayi1, sayi2)}")
elif secim == "3":
  print(f"Sonuç: {sayi1} * {sayi2} = {carp(sayi1, sayi2)}")
elif secim == "4":
  print(f"Sonuç: {sayi1} / {sayi2} = {bol(sayi1, sayi2)}")
else:
  print("Geçersiz bir seçim yaptınız!")
