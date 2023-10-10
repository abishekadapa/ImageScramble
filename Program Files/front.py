from tkinter import filedialog
from tkinter import *
from PIL import ImageTk, Image
from PIL import Image
from decimal import Decimal 
import random
import math

#Assigning Values
filename = ""
photovar = "3.jpg"

def count_largest(s):

   m = 0

   for i in s :
      if(m < len(i)):
         m = len(i)
   return m


def gcd(x, y): 
  
   while(y): 
       x, y = y, x % y 
  
   return x


def getpubkey():
    f=open("pubkey.txt","r")
    key=f.read()
    text1.insert(0.0,str(key))
    

def nearest_roundoff(n):
   if(n > 0):
      return math.ceil(n/3.0) * 3
   elif( n < 0):
      return math.floor(n/3.0) * 3
   else:
      return 3

def isPrime(n) :
    if(n in [2,3]):
        return True
    else:
        k=0
        while(True):
            if(n in [((6*k)-1),((6*k)+1)]):
                return True
            else:
                if(( ((6*k) - 1) or ((6*k) + 1) ) > n):
                    return False
                k = k + 1



def get_num_pixels(filename):
    width, height = Image.open(filename).size
    return width*height


def binary_to_decimal(v):
    v = v.strip()
    v = v[::-1]
    dec_value = 0
    i = 0 
    for j in v:
        dec_value = dec_value + (int(j)*(2**i))
        i = i + 1
    return dec_value
        
        


#Function for Opening Dialog
def browse():
    global filename
    global photovar
    global firstimg
    global image3
    filename = filedialog.askopenfilename()

    var = ""
    for i in filename:
        var = var + i
        if (i == "/"):
            var = ""
    filename = var
    photovar = var
    image3 = ImageTk.PhotoImage(Image.open(photovar))
    canvas.itemconfig(firstimg, image=image3)

#Encoding
def encode():
    p=53

    q=71

    n=p*q

    z= (p-1) * (q-1)
    msg = text.get(0.0, END)
    publickey = text1.get(0.0, END)
    
    print("Message : ",msg)
    print("Public Key : ",publickey)
    print("File Name : ",filename)

    file=filename

    imag = Image.open(file,'r')

    hieght , width = Image.open(file,'r').size

    print("Hieght : ",hieght)
    print("Width : ",width)
    pixel_value = list(imag.getdata())
    imdata = iter(imag.getdata()) 
    print(imag.getdata())
    pub_key = int(publickey)

    enc=""
    
    for i in msg:
    
        ctt = Decimal(0) 
        ctt =pow(ord(i),pub_key) 
        ct = ctt % n

        enc = enc + chr(ct)

    print("Encrypted Data : " , enc," ")

    a=[]
    for i in enc:
        w=bin(ord(i))[2:]
        w='0'*(8-len(w)) + w
        a.append(w)

    print(a)

    maxlen = count_largest(a)

    maxlen = nearest_roundoff(maxlen)

    print("Maximum Value : " , maxlen)

    for  i in range(len(a)):
        print("len(max(a)) : ",maxlen," len(a[i]) : ",len(a[i])) 
        a[i] = '0'*(maxlen - len(a[i]))  + a[i]

    print(">>>>>")


    print(a)

    print("<<<<<")

    img = imag.load()

    print(type(img))

    track = 0
    lb = 0
    bb = 0
    datadone = 0
    it = 0
    it1 = 0

    r , g , b = img[lb,bb]

    binary_value = (bin(len(msg)))[2:]

    temp = '0'*(16 - len(binary_value)) + binary_value

    r = binary_to_decimal(temp[0:8])

    g = binary_to_decimal(temp[8:])

    b = maxlen
    print(r+g)
    print(b)
    img[lb,bb] = (r,g,b)

    bb = bb + 1

    rarr = []
    garr = []
    barr = []

    for i in range(maxlen):
        if(i % 3 == 0):
            rarr.append(i)
        elif(i % 3 == 1):
            garr.append(i)
        elif(i % 3 == 2):
            barr.append(i)
      

    while(lb <= hieght - 1):

        while(bb <= width - 1 ):
            r , g , b = img[lb,bb]

            print("pixel value","[",lb,",",bb,"]"," ",img[lb,bb])
            if(it >= len(a)):
         
                print("ExitPoint")
                datadone = 1
                break
         
            t = a[it]

            t = list(t)

            print(t)
         
        

            if(it1 in rarr):

                if(t[it1] == '0' ):

                    if(r % 2 != 0):
                        r = r - 1
                        img[lb,bb] = (r,g,b)

                elif(t[it1] == '1'):

                    if(r % 2 != 1):

                        r = r - 1

                        img[lb,bb] = (r,g,b) 


                it1 = it1 + 1

            track = track + 1

            if(it1 >= len(t)):

                it1 = 0
                t = a[it]
                t = list(t)
                it = it + 1

            if(track > maxlen * len(msg)):
                print("ExitPoint1")
                datadone = 1
                break

            if(it1 in garr):

                    if(t[it1] == '0' ):
    
                        if(g % 2 != 0):

                            g = g - 1

                            img[lb,bb] = (r,g,b)

                    elif(t[it1] == '1'):

                        if(g % 2 != 1):

                            g = g - 1

                            img[lb,bb] = (r,g,b)

                    it1 = it1 + 1

            track = track + 1
             

            if(it1 >= len(t)):

                 it1 = 0
                 t = a[it]
                 t = list(t)
                 it = it + 1

            if(track > maxlen * len(msg)):
                 print("ExitPoint2")
                 datadone = 1
                 break
         
            if(it1 in barr):

                 if(t[it1] == '0' ):

                     if(b % 2 != 0):

                          b = b - 1

                          img[lb,bb] = (r,g,b)

                 elif(t[it1] == '1'):

                    if(b % 2 != 1):

                        b = b - 1

                        img[lb,bb] = (r,g,b)

                 it1 = it1 + 1

            track = track + 1

            if(it1 >= len(t)):

                 it1 = 0
                 t = a[it]
                 t = list(t)
                 it = it + 1

            if(track > maxlen * len(msg)):
                 print("ExitPoint3")
                 datadone = 1
                 break

            print("pixel value","[",lb,",",bb,"]"," ",img[lb,bb])

            print()
         

            bb = bb + 1

        bb = 0

        lb = lb + 1
        if(datadone == 1):
            break

    print("Encoding is Done Successfully......")

    r,g,b = img[0,0]

    print(r,g,b)

    lb = 0
    bb=0
    for i in range(20):
       print("->",img[lb,bb])
       bb = bb + 1
    imag.save(file, "png")
    
    
def close_window():
    val = text.get(0.0,END)
    print(val)
    obj.destroy()

#Creating Window
obj = Tk()
obj.title("Concealing Images")
photo = PhotoImage(file="download.png")
obj.iconphoto(False, photo)
obj.resizable(0, 0)

#Creating Canvas to draw
canvas = Canvas(obj, width=900, height=780)
canvas.pack()

#Displaying Background Image
image=ImageTk.PhotoImage(Image.open("1.jpg"))
canvas.create_image(0,0,anchor=NW,image=image)

image1=ImageTk.PhotoImage(Image.open(photovar))
firstimg = canvas.create_image(100,50,anchor=NW,image=image1)

text = Text(obj, width=40, height=1, wrap=WORD)
button2 = canvas.create_window(200, 500, anchor='nw', window=text)
text.insert(0.0, "Enter Secret Message")

text1 = Text(obj, width=40, height=1, wrap=WORD)
key = canvas.create_window(200, 590, anchor='nw', window=text1)

dialog = Button(obj, text="OPEN", width=10, height=1, borderwidth=2, command=browse, bg="pink", fg="black")
d_button = canvas.create_window(560, 500 , anchor='nw', window=dialog)

key_button = Button(obj, text="GET KEY",width=10, height=1, borderwidth=2, command=getpubkey, bg="pink", fg="black")
gkey = canvas.create_window(560, 590, anchor='nw', window=key_button)


encode_button = Button(obj, text="ENCODE",width=12, height=1, borderwidth=3, command=encode, bg="pink", fg="black")
encode = canvas.create_window(300, 650, anchor='nw', window=encode_button)

decode_button = Button(obj, text="SEND",width=12, height=1, borderwidth=3, command=close_window, bg="pink", fg="black")
decode = canvas.create_window(480, 650, anchor='nw', window=decode_button)

width = 900
height = 780
screenw = obj.winfo_screenwidth()
screenh = obj.winfo_screenheight()

x = (screenw / 2) - (width / 2)
y = (screenh / 2) - (height / 2)
obj.geometry("%dx%d+%d+%d" % (width, height, x, y))

obj.mainloop()
