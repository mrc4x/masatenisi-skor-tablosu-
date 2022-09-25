import tkinter as tk
from turtle import width
from PIL import Image, ImageTk
 # değerler
pencere=tk.Tk()
pencere.geometry("1920x1080")
pencere.title("MASA TENİSİ")
ayar=tk.Tk()
ayar.geometry("500x500")
ayar.title("MASA TENİSİ")
ayar.config(bg="purple")
score=0
score2=0
set=0
setsonu=11
sayac=0

#
resim=ImageTk.PhotoImage(Image.open('massa.png'))

label=tk.Label(pencere,image=resim)
label.pack()
def ekle():          # 1. oyuncu puan ekleme fonksiyonu
    global score
    global set
    global score2
    score +=1
    yazi.config(text= score)
    if score >=setsonu:
        set +=1
        yazi2.config(text= set)
        score2 -= score2
        score -= score
        yazi.config(text= score)
        yazii.config(text=score2)
    yazi2.place(x=715, y=500)
    

def cıkar():                         # 1. oyuncu puan cıkarma fonksiyonu
    global score
    score-=1
    yazi.config(text= score)
yazi=tk.Label(pencere,font=("courier", 62))
yazi.place(x=173, y=300)


dugme=tk.Button(pencere)                 # 1. oyuncu puan ekleme
dugme.config(text="puan ekle",width=9,height=2,font=("Courier", 9, "italic"))
dugme.config(command=ekle)
dugme.place(x=100, y=700)

dugme2=tk.Button(pencere)               # 1. oyuncu puan cıkarma
dugme2.config(text="puan çıkar",width=9,height=2,font=("Courier", 9, "italic"))
dugme2.config(command=cıkar)
dugme2.place(x=200, y=700)
#
yazii=tk.Label(pencere,font=("courier", 62), bg="black", fg="white")        # oyuncu 2 yazı fontu
yazii.pack()

def ekle2():                    # 2. oyuncu puan ekleme fonksiyonu
    global score2
    global score
    global set
    score2 +=1
    yazii.config(text= score2)
    if score2 >=setsonu:
        set +=1
        yazi2.config(text=set)
        score2 -= score2
        score -= score
        yazi.config(text= score2)
        yazii.config(text=score)
    yazii.place(x=1250, y=300)
    yazi2.place(x=715, y=500)
    

def cıkar2():                   # 2. oyuncu puan cıkarma fonksiyonu
    global score2
    score2 -=1
    yazii.config(text= score2)
    yazii.place(x=1250, y=300)
    
dugme3=tk.Button(pencere)                   # 2. oyuncu puan ekleme
dugme3.config(text="puan ekle",width=9,height=2,font=("Courier", 9, "italic"))
dugme3.config(command=ekle2)
dugme3.place(x=1200, y=700)

dugme4=tk.Button(pencere)                   # 2. oyuncu puan cıkarma
dugme4.config(text="puan cıkar",width=9,height=2,font=("Courier", 9, "italic"))
dugme4.config(command=cıkar2)
dugme4.place(x=1300, y=700)

yazi2=tk.Label(pencere,font=("courier", 52), bg="orange")            # puan fontu
yazi2.place(x=715, y=500)
yazi2.pack()

def setekle():          #set ekleme fonksiyonu
    global set
    set +=1
    yazi2.config(text=set)
    yazi2.place(x=715, y=500)

def setcıkar():         #set cıkarma fonksiyonu
    global set
    set-=1
    yazi2.config(text=set)
    yazi2.place(x=715, y=500)


dugme5=tk.Button(pencere)           # set ekleme tuşu
dugme5.config(text="set ekle",width=9,height=2,font=("Courier", 9, "italic"))
dugme5.config(command=setekle)
dugme5.place(x=660, y=700)

dugme6=tk.Button(pencere)           # set çıkarma tuşu
dugme6.config(text="set cıkar",width=9,height=2,font=("Courier", 9, "italic"))
dugme6.config(command=setcıkar)
dugme6.place(x=760, y=700)
##############################
sayachata=0
sayacozum=0
eskisüre=0
sayac=1
def ilerisay():         # ileri sayma fonksiyonu
    global sayac, sayachata
    if sayachata==0:
        sayachata==1
        sayacozum==1

    if sayac>0:
        sayım_lbl.config(text=sayac)
        sayac=sayac+1
        sayım_lbl.after(1000, ilerisay)

    if sayac==0:
        sayac+=1
def durdur():               # durdurma fonksiyonu
    global sayac, eskisüre
    eskisüre=sayac-1
    sayım2_lbl.config(text=eskisüre)
    sayac-=sayac
    sayım_lbl.config(text=sayac)

button3=tk.Button(pencere,text="durdur",activebackground="red",command=durdur)          # durudrma butonu 
button3.place(x=755, y=150)

button2=tk.Button(pencere,text="başlat",activebackground="red",command=ilerisay)             # başlatma butonu
button2.place(x=670, y=150)

sayım_lbl=tk.Label(bg="white",font=("courier",50))            # sayaç değeri
sayım_lbl.place(x=708, y=30)

sayım2_lbl=tk.Label(bg="white",font=("courier",40))           # eski sayac değeri
sayım2_lbl.place(x=1430, y=30)


###### ayar sayfası
giris1=tk.Entry(ayar)
giris1.place(x=150,y=150)

giris2=tk.Entry(ayar)
giris2.place(x=150,y=170)
oyuncudegeri=0
oyuncu2degeri=0


def degerleriata():
    global oyuncudegeri, oyuncu2degeri
    oyuncudegeri=giris1.get()
    oyuncu2degeri=giris2.get()
    yazdırılanoyuncu2.config(text=oyuncu2degeri)
    yazdırılanoyuncu.config(text=oyuncudegeri)
    ayar.destroy()

######
yazdırılanoyuncu=tk.Label(pencere, font=("Courier", 36, "italic"),bg="light blue")
yazdırılanoyuncu.place(x=173, y=165)

yazdırılanoyuncu2=tk.Label(pencere,font=("Courier", 36, "italic"),bg="light blue")
yazdırılanoyuncu2.place(x=1250, y=165)

kaydet=tk.Button(ayar)
kaydet.config(text="kaydet",command=degerleriata)
kaydet.place(x=150,y=200)


oyuncuyazı=tk.Label(ayar)
oyuncuyazı.config(text="oyuncu 1: ",bg="black",fg="white")
oyuncuyazı.place(x=90,y=150)


oyuncuyazı2=tk.Label(ayar)
oyuncuyazı2.config(text="oyuncu 2: ",bg="black",fg="white")
oyuncuyazı2.place(x=90,y=170)

teknokent=tk.Label(ayar)
teknokent.config(text="""
ANTAKYA TEKNOKENT KOLEJİ
""",bg="purple",font=("Nirmala UI",25))
teknokent.place(x=150,y=250)

ekyazı=tk.Label(ayar)
ekyazı.config(text="Oyuncu Adlarını girin..")

pencere.mainloop()
ayar.mainloop()










