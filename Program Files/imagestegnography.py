from PIL import Image
from decimal import Decimal 
import random
import math


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
        
        



file = input("Open a File with Extension : ")

image = Image.open(file,'r')

hieght , width = Image.open(file,'r').size

print("Height : ",hieght)
print("Width : ",width)

pixel_value = list(image.getdata())

imdata = iter(image.getdata()) 

print(image.getdata())

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

msg = input("Enter a Message : ")

enc = ""
dec = ""

for i in msg:
    
    ctt = Decimal(0) 
    ctt =pow(ord(i),pub_key) 
    ct = ctt % n

    enc = enc + chr(ct)

print("Encrypted Data : " , enc," ")

print()

print("Number o pixels : " , get_num_pixels(file))

pixels_required = 3 * len(enc)

if(get_num_pixels(file) + 9 >= pixels_required ):
    print("Encoding can be done.......")

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

img = image.load()

track = 0
lb = 0
bb = 0
datadone = 0
it = 0
it1 = 0
print(img[0,0])
r , g , b = img[lb,bb]

binary_value = (bin(len(msg)))[2:]

temp = '0'*(16 - len(binary_value)) + binary_value

r = binary_to_decimal(temp[0:8])

g = binary_to_decimal(temp[8:])

b = maxlen

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

print()






lb = 0
bb = 0
b1 = ""
datarecovered = 0
tup = 0
rec=[]
print()
print()
print()
print()
print("Decoding is About to Start........")
print()
print()

r , g , b = img[lb,bb]

msg_len = r + g

encoded_offset = b

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
