
calisanlar = [
    {"ad": "Zeynep", "departman": "Yazılım", "maas": 45000},
    {"ad": "Ali", "departman": "Pazarlama", "maas": 32000},
    {"ad": "Ayşe", "departman": "Yazılım", "maas": 62000},
    {"ad": "Mehmet", "departman": "İK", "maas": 38000},
    {"ad": "Elif", "departman": "Yazılım", "maas": 51000},
    {"ad": "Can", "departman": "Pazarlama", "maas": 29000}
]

def calisan_sayisi(calisanlar):
   return len(calisanlar)

print("Çalışan sayısı:" , calisan_sayisi(calisanlar))

def toplam_maas(calisanlar):
   toplam=0
   for calisan in calisanlar:
      toplam +=calisan["maas"]
   return toplam

print("Çalışan Toplam Maas: " , toplam_maas(calisanlar))

def ortalama_maas(calisanlar):
   return toplam_maas(calisanlar)/calisan_sayisi(calisanlar)

print("Ortalama Maaş:" , ortalama_maas(calisanlar))

def en_yuksek_maas(calisanlar):
   en_yuksek=calisanlar[0]
   for calisan in calisanlar:
      if calisan["maas"] > en_yuksek["maas"]:
        en_yuksek=calisan

   return en_yuksek

print("En yüksek Maaaşı Alan Çalışan:" , en_yuksek_maas(calisanlar)) 


def departman_calisan_sayisi(calisanlar,departman):
   calisan_sayisi=0
   for calisan in calisanlar:
      if calisan["departman"] ==departman:
         calisan_sayisi+=1
   return calisan_sayisi

print("Çalışan sayısı:" , departman_calisan_sayisi(calisanlar,"Yazılım"))
   
def departman_toplam_maas(calisanlar,departman):
   toplam_maas=0
   for calisan in calisanlar:
      if calisan["departman"] == departman:
        toplam_maas +=calisan["maas"]
   return toplam_maas

print("Toplam Maaş:", departman_toplam_maas(calisanlar,"Yazılım"))


def departman_maas_ort(calisanlar,departman):
   try:
    return departman_toplam_maas(calisanlar,departman) / departman_calisan_sayisi(calisanlar,departman)
   except ZeroDivisionError:
      return "Departmanda çalışan bulunamadı. Bölme hatası.."

print(departman_maas_ort(calisanlar , "yazılım"))


def maası_yuksek_olan(calisanlar,maas):
   m=[]
   for calisan in calisanlar:
      if calisan["maas"]>maas:
         m.append({"ad": calisan["ad"], "departman" : calisan["departman"], "maas": calisan["maas"]})

   return m

print("Maaşı yüksek olanlar:", maası_yuksek_olan(calisanlar,50000))
         

def yüksek_maas_ort(calisanlar,maas):
   toplam=0
   sayi=0
   try:
    for calisan in calisanlar:
      if calisan["maas"]>maas:
         toplam+= calisan["maas"]
         sayi+=1
    ortalama= toplam/sayi
    return ortalama
         
   except ZeroDivisionError:
      return("Bu maaş seviyesinin üzerinde çalışan bulunamadı.. ")

print(yüksek_maas_ort(calisanlar,100000))
    
   
def departman_ortalamaları(calisanlar):
  
  yazılım  = departman_toplam_maas(calisanlar,"Yazılım") / departman_calisan_sayisi(calisanlar,"Yazılım")
  pazarlama= departman_toplam_maas(calisanlar,"Pazarlama") / departman_calisan_sayisi(calisanlar,"Pazarlama")  
  İK = departman_toplam_maas(calisanlar,"İK") / departman_calisan_sayisi(calisanlar,"İK")

  return ({"Yazılım":yazılım , "Pazarlama": pazarlama , "İK": İK })

print(departman_ortalamaları(calisanlar))


def departmanlar(calisanlar):
   dep=[]
   for calisan in calisanlar:
      dep.append(calisan["departman"])
   
   return set(dep)

print(departmanlar(calisanlar))
      

#incele tekrarla çünkü analmdım bu kısmı
def departmanlar_en_yuksek_maas(calisanlar):

    sonuc = {}

    for d in departmanlar(calisanlar):

        en_yuksek = None

        for calisan in calisanlar:

            if calisan["departman"] == d:

                if en_yuksek is None or calisan["maas"] > en_yuksek["maas"]:
                    en_yuksek = calisan

        sonuc[d] = en_yuksek

    return sonuc

      
print(departmanlar_en_yuksek_maas(calisanlar))

def maas_degerlendir(maas):
    if maas >= 50000:
        return "yüksek"
    elif maas >= 30000:
        return "orta"
    else:
        return "düşük"


def calisan_raporu(calisanlar):
   sonuc=[]
   for calisan in calisanlar:

      durum=maas_degerlendir(calisan["maas"])

      sonuc.append({"ad": calisan["ad"] , "maas": calisan["maas"], "durum": durum})

   return sonuc

print(calisan_raporu(calisanlar))


def genel_rapor(calisanlar):
   sayi= calisan_sayisi(calisanlar)
   toplammaas=toplam_maas(calisanlar)
   ort_maas=ortalama_maas(calisanlar)
   en_yuksek =en_yuksek_maas(calisanlar)
   departman_ort=departman_ortalamaları(calisanlar)

   return(f"""         GENEL RAPOR 
   Çalışan sayısı: {sayi}
   Toplam Maaş : {toplammaas}
   Ortalama Maaş : {ort_maas}
   En Yüksek Maaş : 
   {en_yuksek["ad"]} - {en_yuksek["maas"]} TL
   
   Departman Ortalamaları:
   {departman_ort}
   """)

print(genel_rapor(calisanlar))


def departman_calisan_sayilari(calisanlar):
    sonuc = {}

    for departman in departmanlar(calisanlar):
        sonuc[departman] = departman_calisan_sayisi(calisanlar, departman)

    return sonuc


print(departman_calisan_sayilari(calisanlar))


print(maası_yuksek_olan(calisanlar,50000))



import matplotlib.pyplot as plt

# 1. Departmanlara göre ortalama maaş
departman_ort = departman_ortalamaları(calisanlar)

departman_isimleri = list(departman_ort.keys())
ortalama_maaslar = list(departman_ort.values())

plt.bar(departman_isimleri, ortalama_maaslar)
plt.title("Departmanlara Göre Ortalama Maaş")
plt.xlabel("Departman")
plt.ylabel("Ortalama Maaş")
plt.savefig("departman_ortalama_maas.png")
plt.show()


# 2. Departmanlara göre çalışan sayısı
departman_sayilari = departman_calisan_sayilari(calisanlar)

departman_isimleri = list(departman_sayilari.keys())
calisan_sayilari = list(departman_sayilari.values())

plt.bar(departman_isimleri, calisan_sayilari)
plt.title("Departmanlara Göre Çalışan Sayısı")
plt.xlabel("Departman")
plt.ylabel("Çalışan Sayısı")
plt.savefig("departman_calisan_sayisi.png")
plt.show()

