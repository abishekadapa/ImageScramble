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
        
        




def decode():

    
    p=53

    q=71

    n=p*q
    print("File Name : ",filename)
    file=filename

    imageval = Image.open(file,'r')

    hieght , width = Image.open(file,'r').size
    pri_key = text1.get(0.0, END)
    pri_key = int(pri_key)

    print("Hieght : ",hieght)
    print("Width : ",width)
    dec=""
    print()
    print()
    print("Decoding is About to Start........")
    print()
    print()
    
    img = imageval.load()
    bb=0
    lb=0
    for i in range(20):
       print("->",img[lb,bb])
       bb = bb + 1

    bb=0

    lb = 0
    bb = 0
    b1 = ""
    datarecovered = 0
    tup = 0
    rec=[]
    r , g , b = img[lb,bb]

    msg_len,encoded_offset = r+g,b
    bb = bb + 1

    track_val =0

    max_track_val = msg_len * encoded_offset

    iter_val = 0
    
    if(encoded_offset % 3 == 0):
   
        while(lb <= hieght - 1):
   
            while(bb <= width - 1 ):

                r , g , b = img[lb,bb]

                print("pixel value","[",lb,",",bb,"]"," ",img[lb,bb])

                if(r % 2 == 0):
                    b1 = b1 + '0'
                if(r % 2 != 0):
                    b1 = b1 + '1'
                    
            
                iter_val = iter_val + 1
                track_val = track_val + 1

                if(g % 2 == 0):
                    b1 = b1 + '0'
                if(g % 2 != 0):
                    b1 = b1 + '1'

                iter_val = iter_val + 1
                track_val = track_val + 1
           
                if(b % 2 == 0):
                   b1 = b1 + '0'
                if(b % 2 != 0):
                   b1 = b1 + '1'
                iter_val = iter_val + 1
                track_val = track_val + 1

                if(iter_val == encoded_offset):
                   iter_val = 0
                   rec.append(b1)
                   b1=""
              
                if( track_val == max_track_val):
                   datarecovered = 1
                   break 
                bb = bb + 1

            bb=0
            lb = lb + 1

            if(datarecovered == 1):
                break
      
    print(rec)

    print("Decoding Done Successfully......")
    decoded_string = ""
    for i in rec:
        val = binary_to_decimal(i)
        decoded_string += chr(val)

    print("Decoded String is : ",decoded_string) 



    for i in decoded_string:
    
        dtt = Decimal(0) 
        dtt = pow(ord(i),pri_key) 
        dt = dtt % n

        dec = dec + chr(dt)

    print()

    print("Decrypted Secret Message : ",dec)
    text.insert(0.0, dec)


def generatekeys():
    p=53

    q=71

    n=p*q

    z= (p-1) * (q-1)

    pub_key = 0

    while(True):
        r = random.randint(2,z-1)

        print(r)
        if((not(isPrime(r))) and  (gcd(r,z) == 1)):
            pub_key = r
            break
        
        
    print("Public Key : " ,pub_key)


    pri_key = 0
    j=1
    while(True):
        d = ((j * z) + 1 )
        if(d % pub_key == 0):
            pri_key = d//pub_key
            break
        else:
            j = j + 1

    print("Private Key : ",pri_key)

    f=open("pubkey.txt", "w")
    fp=open("prikey.txt","w")
    f.write(str(pub_key))
    f.close()
    print("Public Key Updated.....")
    fp.write(str(pri_key))
    fp.close()
    print("Private Key Updated.....")
    
#Encoding and Decoding
def close_window():
    val = text.get(0.0,END)
    obj.destroy()

def getprikey():
    f=open("prikey.txt","r")
    key=f.read()
    text1.insert(0.0,str(key))
    

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

text1 = Text(obj, width=40, height=1, wrap=WORD)
tbutton = canvas.create_window(200, 600, anchor='nw', window=text1)

dialog = Button(obj, text="OPEN", width=10, height=1, borderwidth=2, command=browse, bg="pink", fg="black")
d_button = canvas.create_window(560, 500 , anchor='nw', window=dialog)

key_button = Button(obj, text="GET KEY",width=10, height=1, borderwidth=2, command=getprikey, bg="pink", fg="black")
gkey = canvas.create_window(560, 600, anchor='nw', window=key_button)

encode_button = Button(obj, text="DECODE",width=12, height=1, borderwidth=3, command=decode, bg="pink", fg="black")
encode = canvas.create_window(300, 670, anchor='nw', window=encode_button)

decode_button = Button(obj, text="GENERATE KEY",width=12, height=1, borderwidth=3, command=generatekeys, bg="pink", fg="black")
decode = canvas.create_window(480, 670, anchor='nw', window=decode_button)

width = 900
height = 740
screenw = obj.winfo_screenwidth()
screenh = obj.winfo_screenheight()

x = (screenw / 2) - (width / 2)
y = (screenh / 2) - (height / 2)
obj.geometry("%dx%d+%d+%d" % (width, height, x, y))

obj.mainloop()
