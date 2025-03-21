#TASK 1
def merhaba_de():
    print("Merhaba!")

merhaba_de()

#TASK 2
def kisi_adi(isim,soyisim):
    print(f"İsim: {isim}, Soyisim: {soyisim}")

kisi_adi('Oğuzhan' ,'Yazıcı')

#TASK 3
sayilar = [10, 15, 20, 25, 30, 35]
def tek_sayılar():
    transaction = [sayi for sayi in sayilar if sayi % 2 != 0]
    return transaction
print(tek_sayılar())

#TASK 4
def dört_islem(sayi1, sayi2):
    return sayi1 + sayi2, sayi1 - sayi2, sayi1 * sayi2, sayi1 % sayi2, sayi1 / sayi2 if sayi2 != 0 else "Hata: Sıfır ile bölme yok"
print(dört_islem(10, 2))

#TASK 5
def islem (metin,islem_tipi):
    if isinstance(metin, str):
        if islem_tipi == "ters":
            print(metin[::-1])
        elif islem_tipi == "büyük":
            print(metin.upper())
        elif islem_tipi == "küçük":
            print(metin.lower())
        elif islem_tipi == "uzunluk":
            print(len(metin))
    else:
        print("Hata: Geçersiz işlem tipi")

islem("Merhaba", "ters")
islem("Merhaba", "büyük")
islem("Merhaba", "küçük")
islem("Merhaba", "uzunluk")

#TASK 6
def isim_ekle(*args):
        isimler = [] 
        for isim in args:
            isimler.append(isim.upper())  
        return isimler


isim_listesi = isim_ekle("ahmet", "ayşe", "mehmet", "fatma")
print(isim_listesi)  

#TASK 7

def kelime_sayisi (cümle): 
    kelimeler = cümle.split()
    return len(kelimeler)

cümle = "Bu bir deneme cümlesidir."
kelime_adedi = kelime_sayisi(cümle)

if kelime_adedi > 5 :
        print("Cümle Uzun")
else:
    print("Cümle Kısa")
    
print('Yazılan cümlenin kelime sayısı:',kelime_adedi)  

#TASK 8

def toplam(n):
     if n != 1:
         return n * (n + 1) // 2
     elif n == 1:
          return 1
     else :
          return "Hata: Girdiğiniz sayı 1'den küçük olamaz"

sonuç = toplam(3)  
print(' 1"den girilen sayıya kadar olan sayıların toplamı:',sonuç)
     


    

