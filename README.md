# function-example

1. "Merhaba, Python!" Yazdıran Fonksiyon
Bir merhaba_de adında fonksiyon yazın. Bu fonksiyon, ekrana "Merhaba, Python!" yazdırmalıdır.
2. İsim ve Soyisim Yazdıran Fonksiyon
Bir fonksiyon oluşturun. Bu fonksiyon, isim ve soyisim olmak üzere iki parametre alsın ve ekrana tam adınızı yazdırsın.
3. Listeden Tek Sayıları Bulan Fonksiyon
Aşağıdaki liste içindeki tek sayıları bulan bir fonksiyon yazın.
sayilar = [10, 15, 20, 25, 30, 35]
4. Dört İşlem Yapan Fonksiyonlar
Aşağıdaki matematiksel işlemleri gerçekleştiren fonksiyonları eksiksiz bir şekilde yazın.
Fonksiyon Açıklamaları:
•
topla(sayi1, sayi2) → İki sayının toplamını döndürür.
•
bolme(sayi1, sayi2) → İlk sayıyı ikinci sayıya böler. Eğer bölen 0 ise "Bölen kısım 0 olamaz" mesajını döndürür.
•
carpma(sayi1, sayi2) → İki sayının çarpımını döndürür.
•
cikarma(sayi1, sayi2) → İlk sayıdan ikinciyi çıkarıp sonucu döndürür.
•
mod(sayi1, sayi2) → İlk sayının ikinci sayıya göre modunu döndürür.
5. Metin Üzerinde Farklı İşlemler Yapan Fonksiyon
Bir fonksiyon yazın. Bu fonksiyon iki parametre almalıdır:
•
metin → İşlem yapılacak string
•
islem_tipi → Yapılacak işlem türü ("ters", "buyuk", "kucuk", "uzunluk")
Fonksiyon, islem_tipi parametresine göre şu işlemleri yapmalıdır:
•
"ters" → Metni ters çevirir.
•
"buyuk" → Tüm harfleri büyük yapar.
•
"kucuk" → Tüm harfleri küçük yapar.
•
"uzunluk" → Metnin karakter uzunluğunu döndürür.
•
Geçersiz bir işlem girilirse "Geçersiz işlem" mesajı döndürmelidir.
6. Birden Fazla İsim Ekleyen Fonksiyon
Aşağıdaki özelliklere sahip bir fonksiyon yazın:
•
isim_ekle adlı fonksiyon, birden fazla isim alabilmelidir.
•
Fonksiyon, isimlerin saklandığı boş bir liste olan isimler adlı bir liste kullanmalıdır.
•
args kullanarak, parametre olarak verilen tüm isimleri büyük harf formatında isimler listesine eklemelidir.
•
Fonksiyon en son olarak isimler listesini döndürmelidir.
7. Metindeki Kelime Sayısını Analiz Eden Fonksiyon
Aşağıdaki iki fonksiyonu oluşturun:
1.
kelime_sayisi(metin)
a.
Verilen metindeki kelime sayısını döndürmelidir.
2.
cumle_analiz(metin)
a.
kelime_sayisi fonksiyonunu kullanarak metindeki kelime sayısını hesaplamalıdır.
b.
Cümlede 5 veya daha fazla kelime varsa "Cümle uzun", aksi takdirde "Cümle kısa" çıktısını döndürmelidir.
İpucu: Kelime sayısını bulmak için .split() metodunu kullanabilirsiniz.
8. Recursive Toplam Hesaplayan Fonksiyon
1’den verilen sayıya kadar olan sayıların toplamını hesaplayan recursive fonksiyon yazın.
Kurallar:
•
toplam(n) fonksiyonu, 1’den n’e kadar olan sayıların toplamını döndürmelidir.
•
Durdurma koşulu → n == 1 olduğunda fonksiyon durmalıdır.
