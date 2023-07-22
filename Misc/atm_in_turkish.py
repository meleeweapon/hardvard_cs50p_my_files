import json

with open("kullanicilar.json", "r") as kullanicilar_dosyasi:
  kullanicilar = json.load(kullanicilar_dosyasi)


print("Hoşgeldiniz")

while True:
  isim = input("İsminizi giriniz: ")
  try:
    kullanici = kullanicilar[isim]
    break
  except KeyError:
    print("Kullanıcı adı bulunamamıştır.")

while True:
  sifre = input("Şifrenizi giriniz: ")
  sifre_dogru = kullanici["sifre"] == sifre
  if sifre_dogru:
    break
  else:
    print("Yanlış şifre.")

print()
print("Başarıyla giriş yapılmıştır.")
print("Merhaba " + isim + "!")

print("Bakiyeniz: " + "₺" + str(kullanici["bakiye"]))
print()

komut_bekle = True
while komut_bekle:
  while True:
    print()
    komut_girisi = input("Para yatırmak için 'y', para çekmek için 'ç' yazınız: ")
    print()

    if komut_girisi == "y":
      while True:
        yatirma_miktari = input("Lütfen yatırmak istediğiniz miktarı giriniz: ")
        try:
          yatirma_miktari = int(yatirma_miktari)
          if yatirma_miktari < 1:
            print("Lütfen 1'den büyük bir sayı giriniz.")
            continue
          break
        except ValueError:
          print("Lütfen bir sayı giriniz.")

      kullanici["bakiye"] += yatirma_miktari
      print()
      print("Para yatırma işlemi başarıyla gerçekleşmiştir")
      print("Yeni bakiye miktarı: " + "₺" + str(kullanici["bakiye"]))
      print()
      break
    elif komut_girisi == "ç":
      while True:
        cekme_miktari = input("Lütfen çekmek istediğiniz miktarı giriniz: ")
        try:
          cekme_miktari = int(cekme_miktari)
          if cekme_miktari < 1:
            print("Lütfen 1'den büyük bir sayı giriniz.")
            continue
          break
        except ValueError:
          print("Lütfen bir sayı giriniz.")


      kullanici["bakiye"] -= cekme_miktari
      print()
      print("Para çekme işlemi başarıyla gerçekleşmiştir")
      print("Yeni bakiye miktarı: " + "₺" + str(kullanici["bakiye"]))
      print("Lütfen para alma yerinden paranızı alınız.")
      print()
      break
    else:
      print("Lütfen 'y' yada 'ç' yazınız.")

  print("Başka bir işlem gerçekleştirmek istiyor musunuz?")
  while True:
    evet_hayir = input("Evet ise 'e', hayır ise 'h' yazınız: ")

    if evet_hayir == "e":
      komut_bekle = True
      break
    elif evet_hayir == "h":
      komut_bekle = False
      break
    else:
      print("Lütfen 'e' yada 'h' yazınız.")
      

print()
print("İyi günler " + isim + ".")


with open("kullanicilar.json", "w") as kullanicilar_dosyasi:
  kullanicilar_dosyasi.write(json.dumps(kullanicilar))
