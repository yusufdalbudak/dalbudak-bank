# -*- coding: utf-8 -*-
import os
import time

class Musteri:
    def __init__(self, tc, isim, sifre):
        self.tc = tc
        self.isim = isim
        self.sifre = sifre
        self.bakiye = 0
        self.hareketler = []

    def bakiye_goster(self):
        print(f"Bakiyeniz: {self.bakiye} TL")

    def para_yatir(self, miktar):
        self.bakiye += miktar
        self.hareketler.append(f"+{miktar} TL")
        print(f"Bakiyenize {miktar} TL eklenmiştir. Güncel bakiyeniz: {self.bakiye} TL")

    def para_cek(self, miktar):
        if self.bakiye >= miktar:
            self.bakiye -= miktar
            self.hareketler.append(f"-{miktar} TL")
            print(f"Hesabınızdan {miktar} TL çekilmiştir. Güncel bakiyeniz: {self.bakiye} TL")
        else:
            print("Yetersiz bakiye.")

    def faiz_hesapla(self):
        faiz_orani = 0.05
        faiz_miktari = self.bakiye * faiz_orani
        print(f"Yıllık tahmini faiz getirisi: {faiz_miktari} TL")

    def hesap_ozeti(self):
        print(f"{self.isim} adına kayıtlı hesap hareketleri:")
        for hareket in self.hareketler:
            print(hareket)

class Banka:
    def __init__(self):
        self.musteriler = []

    def musteri_ekle(self, yeni_musteri):
        self.musteriler.append(yeni_musteri)
        print(f"{yeni_musteri.isim}, bankamıza hoşgeldiniz!")

    def musteri_bul(self, tc):
        for m in self.musteriler:
            if m.tc == tc:
                return m
        return None

    def para_transferi(self, gonderen_tc, alici_tc, miktar):
        gonderen = self.musteri_bul(gonderen_tc)
        alici = self.musteri_bul(alici_tc)
        if gonderen and alici and gonderen.bakiye >= miktar:
            gonderen.bakiye -= miktar
            alici.bakiye += miktar
            gonderen.hareketler.append(f"-{miktar} TL (Transfer)")
            alici.hareketler.append(f"+{miktar} TL (Transfer)")
            print(f"{miktar} TL {alici.isim} adlı müşteriye başarıyla transfer edildi.")
        else:
            print("Transfer işlemi başarısız.")

def ekran_temizle():
    os.system('cls' if os.name == 'nt' else 'clear')

def ana_menu():
    ekran_temizle()
    print("""
    DALBUDAK BANK'a HOŞGELDİNİZ

    1) Giriş Yap
    2) Yeni Müşteri Kaydı
    Q) Çıkış
    """)
    return input("Lütfen bir seçenek giriniz: ")

def musteri_menu():
    ekran_temizle()
    print("""
    MÜŞTERİ MENÜSÜ

    1) Bakiye Sorgula
    2) Para Yatır
    3) Para Çek
    4) Para Transferi
    5) Şifre Değiştir
    6) Hesap Özeti
    7) Faiz Hesapla
    Q) Çıkış
    """)
    return input("Lütfen bir işlem seçiniz: ")

def sifre_degistir(musteri):
    yeni_sifre = input("Yeni şifrenizi giriniz: ")
    musteri.sifre = yeni_sifre
    print("Şifreniz başarıyla değiştirildi.")

def uygulama():
    banka = Banka()
    while True:
        secim = ana_menu()
        if secim == "1":
            tc = input("TC kimlik numaranızı giriniz: ")
            sifre = input("Şifrenizi giriniz: ")
            musteri = banka.musteri_bul(tc)
            if musteri and musteri.sifre == sifre:
                while True:
                    islem = musteri_menu()
                    if islem == "1":
                        musteri.bakiye_goster()
                    elif islem == "2":
                        miktar = int(input("Yatırılacak miktar: "))
                        musteri.para_yatir(miktar)
                    elif islem == "3":
                        miktar = int(input("Çekilecek miktar: "))
                        musteri.para_cek(miktar)
                    elif islem == "4":
                        alici_tc = input("Alıcı TC kimlik numarası: ")
                        miktar = int(input("Transfer miktarı: "))
                        banka.para_transferi(tc, alici_tc, miktar)
                    elif islem == "5":
                        sifre_degistir(musteri)
                    elif islem == "6":
                        musteri.hesap_ozeti()
                    elif islem == "7":
                        musteri.faiz_hesapla()
                    elif islem.upper() == "Q":
                        break
                    else:
                        print("Geçersiz işlem.")
            else:
                print("Giriş bilgileri hatalı.")
        elif secim == "2":
            tc = input("TC kimlik numaranızı giriniz: ")
            isim = input("Adınız ve soyadınız: ")
            sifre = input("Bir şifre belirleyiniz: ")
            yeni_musteri = Musteri(tc, isim, sifre)
            banka.musteri_ekle(yeni_musteri)
        elif secim.upper() == "Q":
            print("Çıkış yapılıyor...")
            break
        else:
            print("Geçersiz seçenek.")

if __name__ == "__main__":
    uygulama()
