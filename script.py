import json
import requests

URL_LINK : str = "https://jsonplaceholder.typicode.com/users"

response = requests.get(URL_LINK).json()

def kullanici_bul(kullanici_adi : str) -> None:
    bulundu_mu : bool = False
    for kullanici in response:
        if kullanici_adi.strip().lower() in kullanici["name"].lower():
            print("Kullanıcı Bulundu !")
            print(f"İsim : {kullanici["name"]}")
            print(f"Kullanıcı Adı : {kullanici["username"]}")
            print(f"Email : {kullanici["email"]}")
            print(f"Şehir : {kullanici["address"]["city"]}")

            bulundu_mu = True
            break
    if not bulundu_mu:
        print("Kullanıcı Bulunamadı")

def kullanici_listele():
    for kullanici in response:
        print(kullanici["name"])

while True:
    print(" 1-- Kullanıcı Ara : ")
    print(" 2-- Tüm Kullanıcıları Listele : ")
    print(" 3-- Çıkış : ")
    secim : int = int(input("Seçiniz (1-2-3) : "))
    if not secim:
        print("Lütfen Seçin : ")
        continue
    match secim:
        case 1 :
            isim : str = input("Lütfen İsmi Giriniz : ")
            if not isim.strip():
                print("İsim Girmelisiniz !")
            else: kullanici_bul(isim)
        case 2: kullanici_listele()
        case 3: 
            print("Çıkış Yapılıyor !!!")
            break
        case _ :
            print("Lütfen Geçerli Değer Giriniz !!")
