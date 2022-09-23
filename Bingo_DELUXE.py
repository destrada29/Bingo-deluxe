import time
from tkinter import *
import tkinter
import pygame
pygame.mixer.init()
from tkinter import ttk
from PIL import ImageTk,Image
from tkVideoPlayer import TkinterVideo
from io import BytesIO
from gtts import gTTS

Xo = int(time.time())
a = (1103515245)
c = (12345)
m = (32768)   
Lim_1=("1")
Lim_2=("75")
Numeros = (int(Lim_2)-int(Lim_1))+1 
repeated = False
Base=10**(len(str(Numeros))+1)
I=1
total=[]
conteo=[]
fila=100
columna=200


def metodo(Xo,c,m,Lim_1,Lim_2,repeated,Base,I,pes1,pes2):
    

    pygame.mixer.music.load(r"cub1.mp3")
    pygame.mixer.music.play()

    video= TkinterVideo(master=pes2,scaled=True)
    video.load(r'VIDEO_RULETA.mp4')

    video.pack(expand=YES,fill='both')
    video.play()
    video.after(1000,lambda: (video.destroy(),pygame.mixer.music.stop(),bolas(Xo,c,m,Lim_1,Lim_2,repeated,Base,I,pes1,pes2)))

def bolas(Xo,c,m,Lim_1,Lim_2,repeated,Base,I,pes1,pes2):
      global total,columna,fila,imagen_bol,conteo,imagen_x
      lenguaje= 'es-us'
      mp3_fp = BytesIO()
      while I==1:
        Xn=(a*Xo + c) % m
        Aleatorio=Xn/m
        Xo = int(Xn)
        Entero=round(Aleatorio*(Base))
        repeated = Entero in total
        if (not repeated):
          if Entero>=int(Lim_1) and Entero<=int(Lim_2):
            total.append(Entero)
            Resultado=Entero
            image3 =Image.open(str(Resultado)+'.png')
            image3=image3.resize((300,300), Image.Resampling.LANCZOS)
            imagen_bol = ImageTk.PhotoImage(image3)
            imagen_bola=tkinter.Label(pes2,image=imagen_bol) 
            imagen_bola.place(x=350,y=270)


            image4 =Image.open(r"x.jpg")
            image4=image4.resize((20,20), Image.Resampling.LANCZOS)
            imagen_x = ImageTk.PhotoImage(image4)

            if Resultado<=15:
              read= gTTS(text=("B"+str(Resultado)),lang=lenguaje,slow=False)
              read.write_to_fp(mp3_fp)
              conteo.append("B"+str(Resultado))
              pygame.mixer.music.load(mp3_fp,'mp3')
              pygame.mixer.music.play()
              print('B',Resultado)
            if Resultado>15 and Resultado<=30:
              read= gTTS(text=("I"+str(Resultado)),lang=lenguaje,slow=False)
              read.write_to_fp(mp3_fp)
              conteo.append("I"+str(Resultado))
              pygame.mixer.music.load(mp3_fp,'mp3')
              pygame.mixer.music.play()     
              print('I',Resultado)
            if Resultado>30 and Resultado<=45:
              read= gTTS(text=("N"+str(Resultado)),lang=lenguaje,slow=False)
              read.write_to_fp(mp3_fp)
              conteo.append("N"+str(Resultado))
              pygame.mixer.music.load(mp3_fp,'mp3')
              pygame.mixer.music.play()       
              print('N',Resultado)
            if Resultado>45 and Resultado<=60:
              read= gTTS(text=("G"+str(Resultado)),lang=lenguaje,slow=False)
              read.write_to_fp(mp3_fp)
              conteo.append("G"+str(Resultado))
              pygame.mixer.music.load(mp3_fp,'mp3')
              pygame.mixer.music.play()         
              print('G',Resultado)
            if Resultado>60 and Resultado<=75:
              read= gTTS(text=("O"+str(Resultado)),lang=lenguaje,slow=False)
              read.write_to_fp(mp3_fp)
              conteo.append("O"+str(Resultado))
              pygame.mixer.music.load(mp3_fp,'mp3')
              pygame.mixer.music.play()        
              print('O',Resultado)
            I=0
            fila+=40
            if fila == 900:
              fila=100
              columna+=40

            if Resultado==1:
              imagen_x1=tkinter.Label(pes1,image=imagen_x,background='#662A91') 
              imagen_x1.place(x=260,y=141)
            if Resultado==2:
              imagen_x1=tkinter.Label(pes1,image=imagen_x,background='#662A91') 
              imagen_x1.place(x=260,y=175)
            if Resultado==3:
              imagen_x1=tkinter.Label(pes1,image=imagen_x,background='#662A91') 
              imagen_x1.place(x=260,y=205)
            if Resultado==4:
              imagen_x1=tkinter.Label(pes1,image=imagen_x,background='#662A91') 
              imagen_x1.place(x=260,y=236)
            if Resultado==5:
              imagen_x1=tkinter.Label(pes1,image=imagen_x,background='#662A91') 
              imagen_x1.place(x=260,y=264)
            if Resultado==6:
              imagen_x1=tkinter.Label(pes1,image=imagen_x,background='#662A91') 
              imagen_x1.place(x=260,y=291)
            if Resultado==7:
              imagen_x1=tkinter.Label(pes1,image=imagen_x,background='#662A91') 
              imagen_x1.place(x=260,y=318)
            if Resultado==8:
              imagen_x1=tkinter.Label(pes1,image=imagen_x,background='#662A91') 
              imagen_x1.place(x=260,y=347)
            if Resultado==9:
              imagen_x1=tkinter.Label(pes1,image=imagen_x,background='#662A91') 
              imagen_x1.place(x=260,y=377)
            if Resultado==10:
              imagen_x1=tkinter.Label(pes1,image=imagen_x,background='#662A91') 
              imagen_x1.place(x=260,y=407)
            if Resultado==11:
              imagen_x1=tkinter.Label(pes1,image=imagen_x,background='#662A91') 
              imagen_x1.place(x=260,y=438)
            if Resultado==12:
              imagen_x1=tkinter.Label(pes1,image=imagen_x,background='#662A91') 
              imagen_x1.place(x=260,y=470)
            if Resultado==13:
              imagen_x1=tkinter.Label(pes1,image=imagen_x,background='#662A91') 
              imagen_x1.place(x=260,y=503)
            if Resultado==14:
              imagen_x1=tkinter.Label(pes1,image=imagen_x,background='#662A91') 
              imagen_x1.place(x=260,y=539)
            if Resultado==15:
              imagen_x1=tkinter.Label(pes1,image=imagen_x,background='#662A91') 
              imagen_x1.place(x=260,y=574)
            

            if Resultado==16:
              imagen_x1=tkinter.Label(pes1,image=imagen_x,background='#662A91') 
              imagen_x1.place(x=370,y=141)
            if Resultado==17:
              imagen_x1=tkinter.Label(pes1,image=imagen_x,background='#662A91') 
              imagen_x1.place(x=370,y=175)
            if Resultado==18:
              imagen_x1=tkinter.Label(pes1,image=imagen_x,background='#662A91') 
              imagen_x1.place(x=370,y=205)
            if Resultado==19:
              imagen_x1=tkinter.Label(pes1,image=imagen_x,background='#662A91') 
              imagen_x1.place(x=370,y=236)
            if Resultado==20:
              imagen_x1=tkinter.Label(pes1,image=imagen_x,background='#662A91') 
              imagen_x1.place(x=370,y=264)
            if Resultado==21:
              imagen_x1=tkinter.Label(pes1,image=imagen_x,background='#662A91') 
              imagen_x1.place(x=370,y=291)
            if Resultado==22:
              imagen_x1=tkinter.Label(pes1,image=imagen_x,background='#662A91') 
              imagen_x1.place(x=370,y=318)
            if Resultado==23:
              imagen_x1=tkinter.Label(pes1,image=imagen_x,background='#662A91') 
              imagen_x1.place(x=370,y=347)
            if Resultado==24:
              imagen_x1=tkinter.Label(pes1,image=imagen_x,background='#662A91') 
              imagen_x1.place(x=370,y=377)
            if Resultado==25:
              imagen_x1=tkinter.Label(pes1,image=imagen_x,background='#662A91') 
              imagen_x1.place(x=370,y=407)
            if Resultado==26:
              imagen_x1=tkinter.Label(pes1,image=imagen_x,background='#662A91') 
              imagen_x1.place(x=370,y=438)
            if Resultado==27:
              imagen_x1=tkinter.Label(pes1,image=imagen_x,background='#662A91') 
              imagen_x1.place(x=370,y=470)
            if Resultado==28:
              imagen_x1=tkinter.Label(pes1,image=imagen_x,background='#662A91') 
              imagen_x1.place(x=370,y=503)
            if Resultado==29:
              imagen_x1=tkinter.Label(pes1,image=imagen_x,background='#662A91') 
              imagen_x1.place(x=370,y=539)
            if Resultado==30:
              imagen_x1=tkinter.Label(pes1,image=imagen_x,background='#662A91') 
              imagen_x1.place(x=370,y=574)





            if Resultado==31:
              imagen_x1=tkinter.Label(pes1,image=imagen_x,background='#662A91') 
              imagen_x1.place(x=480,y=141)
            if Resultado==32:
              imagen_x1=tkinter.Label(pes1,image=imagen_x,background='#662A91') 
              imagen_x1.place(x=480,y=175)
            if Resultado==33:
              imagen_x1=tkinter.Label(pes1,image=imagen_x,background='#662A91') 
              imagen_x1.place(x=480,y=205)
            if Resultado==34:
              imagen_x1=tkinter.Label(pes1,image=imagen_x,background='#662A91') 
              imagen_x1.place(x=480,y=236)
            if Resultado==35:
              imagen_x1=tkinter.Label(pes1,image=imagen_x,background='#662A91') 
              imagen_x1.place(x=480,y=264)
            if Resultado==36:
              imagen_x1=tkinter.Label(pes1,image=imagen_x,background='#662A91') 
              imagen_x1.place(x=480,y=291)
            if Resultado==37:
              imagen_x1=tkinter.Label(pes1,image=imagen_x,background='#662A91') 
              imagen_x1.place(x=480,y=318)
            if Resultado==38:
              imagen_x1=tkinter.Label(pes1,image=imagen_x,background='#662A91') 
              imagen_x1.place(x=480,y=347)
            if Resultado==39:
              imagen_x1=tkinter.Label(pes1,image=imagen_x,background='#662A91') 
              imagen_x1.place(x=480,y=377)
            if Resultado==40:
              imagen_x1=tkinter.Label(pes1,image=imagen_x,background='#662A91') 
              imagen_x1.place(x=480,y=407)
            if Resultado==41:
              imagen_x1=tkinter.Label(pes1,image=imagen_x,background='#662A91') 
              imagen_x1.place(x=480,y=438)
            if Resultado==42:
              imagen_x1=tkinter.Label(pes1,image=imagen_x,background='#662A91') 
              imagen_x1.place(x=480,y=470)
            if Resultado==43:
              imagen_x1=tkinter.Label(pes1,image=imagen_x,background='#662A91') 
              imagen_x1.place(x=480,y=503)
            if Resultado==44:
              imagen_x1=tkinter.Label(pes1,image=imagen_x,background='#662A91') 
              imagen_x1.place(x=480,y=539)
            if Resultado==45:
              imagen_x1=tkinter.Label(pes1,image=imagen_x,background='#662A91') 
              imagen_x1.place(x=480,y=574)



            if Resultado==46:
              imagen_x1=tkinter.Label(pes1,image=imagen_x,background='#662A91') 
              imagen_x1.place(x=590,y=141)
            if Resultado==47:
              imagen_x1=tkinter.Label(pes1,image=imagen_x,background='#662A91') 
              imagen_x1.place(x=590,y=175)
            if Resultado==48:
              imagen_x1=tkinter.Label(pes1,image=imagen_x,background='#662A91') 
              imagen_x1.place(x=590,y=205)
            if Resultado==49:
              imagen_x1=tkinter.Label(pes1,image=imagen_x,background='#662A91') 
              imagen_x1.place(x=590,y=236)
            if Resultado==50:
              imagen_x1=tkinter.Label(pes1,image=imagen_x,background='#662A91') 
              imagen_x1.place(x=590,y=264)
            if Resultado==51:
              imagen_x1=tkinter.Label(pes1,image=imagen_x,background='#662A91') 
              imagen_x1.place(x=590,y=291)
            if Resultado==52:
              imagen_x1=tkinter.Label(pes1,image=imagen_x,background='#662A91') 
              imagen_x1.place(x=590,y=318)
            if Resultado==53:
              imagen_x1=tkinter.Label(pes1,image=imagen_x,background='#662A91') 
              imagen_x1.place(x=590,y=347)
            if Resultado==54:
              imagen_x1=tkinter.Label(pes1,image=imagen_x,background='#662A91') 
              imagen_x1.place(x=590,y=377)
            if Resultado==55:
              imagen_x1=tkinter.Label(pes1,image=imagen_x,background='#662A91') 
              imagen_x1.place(x=590,y=407)
            if Resultado==56:
              imagen_x1=tkinter.Label(pes1,image=imagen_x,background='#662A91') 
              imagen_x1.place(x=590,y=438)
            if Resultado==57:
              imagen_x1=tkinter.Label(pes1,image=imagen_x,background='#662A91') 
              imagen_x1.place(x=590,y=470)
            if Resultado==58:
              imagen_x1=tkinter.Label(pes1,image=imagen_x,background='#662A91') 
              imagen_x1.place(x=590,y=503)
            if Resultado==59:
              imagen_x1=tkinter.Label(pes1,image=imagen_x,background='#662A91') 
              imagen_x1.place(x=590,y=539)
            if Resultado==60:
              imagen_x1=tkinter.Label(pes1,image=imagen_x,background='#662A91') 
              imagen_x1.place(x=590,y=574)





            if Resultado==61:
              imagen_x1=tkinter.Label(pes1,image=imagen_x,background='#662A91') 
              imagen_x1.place(x=696,y=141)
            if Resultado==62:
              imagen_x1=tkinter.Label(pes1,image=imagen_x,background='#662A91') 
              imagen_x1.place(x=696,y=175)
            if Resultado==63:
              imagen_x1=tkinter.Label(pes1,image=imagen_x,background='#662A91') 
              imagen_x1.place(x=696,y=205)
            if Resultado==64:
              imagen_x1=tkinter.Label(pes1,image=imagen_x,background='#662A91') 
              imagen_x1.place(x=696,y=236)
            if Resultado==65:
              imagen_x1=tkinter.Label(pes1,image=imagen_x,background='#662A91') 
              imagen_x1.place(x=696,y=264)
            if Resultado==66:
              imagen_x1=tkinter.Label(pes1,image=imagen_x,background='#662A91') 
              imagen_x1.place(x=696,y=291)
            if Resultado==67:
              imagen_x1=tkinter.Label(pes1,image=imagen_x,background='#662A91') 
              imagen_x1.place(x=696,y=318)
            if Resultado==68:
              imagen_x1=tkinter.Label(pes1,image=imagen_x,background='#662A91') 
              imagen_x1.place(x=696,y=347)
            if Resultado==69:
              imagen_x1=tkinter.Label(pes1,image=imagen_x,background='#662A91') 
              imagen_x1.place(x=696,y=377)
            if Resultado==70:
              imagen_x1=tkinter.Label(pes1,image=imagen_x,background='#662A91') 
              imagen_x1.place(x=696,y=407)
            if Resultado==71:
              imagen_x1=tkinter.Label(pes1,image=imagen_x,background='#662A91') 
              imagen_x1.place(x=696,y=438)
            if Resultado==72:
              imagen_x1=tkinter.Label(pes1,image=imagen_x,background='#662A91') 
              imagen_x1.place(x=696,y=470)
            if Resultado==73:
              imagen_x1=tkinter.Label(pes1,image=imagen_x,background='#662A91') 
              imagen_x1.place(x=696,y=503)
            if Resultado==74:
              imagen_x1=tkinter.Label(pes1,image=imagen_x,background='#662A91') 
              imagen_x1.place(x=696,y=539)
            if Resultado==75:
              imagen_x1=tkinter.Label(pes1,image=imagen_x,background='#662A91') 
              imagen_x1.place(x=696,y=574)


            


def bingo():
  pygame.mixer.music.stop()
  window=Toplevel(window_1)
  window.iconbitmap("icon.ico")
  imagen_recuento =Image.open(r'fondo_recuento.jpg')
  imagen_recuento=imagen_recuento.resize((1000,800), Image.Resampling.LANCZOS)


  image1 = ImageTk.PhotoImage(imagen_recuento)

  imagen_bolas =Image.open(r'fondo_bolas.jpg')
  imagen_bolas=imagen_bolas.resize((1000,800), Image.Resampling.LANCZOS)

  
  image2 = ImageTk.PhotoImage(imagen_bolas)

  imagen_casillero =Image.open(r"casilleros.jpg")
  imagen_casillero=imagen_casillero.resize((530,500), Image.Resampling.LANCZOS)

  
  image3 = ImageTk.PhotoImage(imagen_casillero)






  notebook=ttk.Notebook(window)
  notebook.pack(fill='both',expand='yes')
  pes1 =tkinter.Frame(notebook)
  pes2 =ttk.Frame(notebook)
  width = 1000 
  height = 800 
 
  screen_width = window.winfo_screenwidth()  
  screen_height = window.winfo_screenheight() 
 
  x = (screen_width/2) - (width/2)
  y = (screen_height/2) - (height/2)
 
  window.geometry('%dx%d+%d+%d' % (width, height, x, y))
  window.title("lest's play")
  imagen=tkinter.Label(pes1,image=image1)
  imagen.place(x = 0, y = 0)
  imagen_1=tkinter.Label(pes2,image=image2)
  imagen_1.place(x = 0, y = 0)
  
  imagen_2=tkinter.Label(pes1,image=image3)
  imagen_2.place(x = 200, y = 100)

  notebook.add(pes2,text='Bingo!')
  notebook.add(pes1,text='Recuento')
  
  respuesta=botton=tkinter.Button(pes2,text="Generar Numeros",command=lambda:metodo(Xo,c,m,Lim_1,Lim_2,repeated,Base,I,pes1,pes2), relief="raised", borderwidth=5, background='red').place(x=450,y=680)
  respuesta=botton=tkinter.Button(pes1,text="Contar",command=lambda:contar(), relief="raised", borderwidth=5, background='red').place(x=450,y=650)
  respuesta=botton=tkinter.Button(pes2,text="Reset Game",command=lambda:reset(window), relief="raised", borderwidth=5, background='blue').place(x=450,y=640)

  window.mainloop()

def contar():
  mp3_fp = BytesIO()
  lenguaje= 'es-us'
  read= gTTS(text='Las bolas que llevamos son',lang=lenguaje,slow=False)
  read.write_to_fp(mp3_fp)
  pygame.mixer.music.load(mp3_fp,'mp3')
  pygame.mixer.music.play()
  time.sleep(2)
  for i in conteo:
    mp3_fp = BytesIO()
    lenguaje= 'es-us'
    read= gTTS(text=i,lang=lenguaje,slow=False)
    read.write_to_fp(mp3_fp)
    pygame.mixer.music.load(mp3_fp,'mp3')
    pygame.mixer.music.play()
    time.sleep(2)






def reset(window):
  window.destroy()



window_1 = Tk()
width = 1366 
height = 768 
window_1.title("The Bingo Game")
window_1.iconbitmap(r"icon.ico")
screen_width = window_1.winfo_screenwidth()  
screen_height = window_1.winfo_screenheight() 
 

x = (screen_width/2) - (width/2)
y = (screen_height/2) - (height/2)
 
window_1.geometry('%dx%d+%d+%d' % (width, height, x, y))
image2 =Image.open(r'fondo_principal.jpg')
image2=image2.resize((1366,768), Image.Resampling.LANCZOS)

image1 = ImageTk.PhotoImage(image2)
imagen=tkinter.Label(window_1,image=image1)
imagen.place(x = 0, y = 0)

play =Image.open(r'play.png')
play_1=play.resize((200,50), Image.Resampling.LANCZOS)
play_time=ImageTk.PhotoImage(play_1)





boton_bingo=tkinter.Button(window_1,command=bingo,background='#FF68BD', borderwidth=5,image = play_time,compound=BOTTOM ).place(x=600,y=680)
pygame.mixer.music.load(r'audio.mp3')
pygame.mixer.music.play()

window_1.mainloop()