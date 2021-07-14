import math
import numpy as np
import matplotlib.pylab as plt
import matplotlib.animation as animation

yy = [290,291,291,290,290,289,289,288,288,287,286,285,284,283,281,280,279,277,275,273,272,270,268,265,264,262,260,257,254,250,245,240,230,220,200,185,180,177,175,173,171,170,170,169,168,168,168,167,166,166,165,165,164,163,163,162,161,161,160,159,158,157,156,154,153,152,150,149,147,146,144,142,139,136,133,129,124,120,115,110,104,99,90,81,73,55,36,30,25,20,18,16,14,12,9,8,7,6,6,5,5,4,4,4,4,4,3,3,4,4,4,4,5,5,5,6,6,7,8,10,11,12,13,14,16,17,19,20,22,23,25,27,28,30,32,33,36,37,39,41,43,45,47,50,51,54,56,58,61,64,67,70,73,77,80,82,86,90,94,98,102,106,110,113,116,120,124,128,131,135,140,144,149,153,160,166,170,174,179,184,189,194,198,203,208,213,218,222,227,231,235,240,243,247,250,254,257,260,262,265,267,269,272,274,276,276]
xx = []
for n in range(len(yy)):
 xx.append(int (2*n))

fig=plt.figure()
x_b=[]
y_b=[]
mas_speed = []
mass_time = []
xbobomba=[]

x= float(input("Введите координату х: "))
if(x<=3 or x>=408):
 print("В этой точке график неопределён")
 exit(0)

def y(x):
 x0=round(x)
 xi=x0-(x0 % 2)
 yi=yy[xi//2]
 yii=yy[xi//2+1]
 return (float (yi-(yi-yii)*(x-xi)/2))

def movement(x_forv, v, n):
  a=9.8*(y(x_forv)-y(x_forv+0.1))/pow(pow(y(x_forv)-y(x_forv+0.1),2)+pow(0.1,2),0.5)
  vv=v+a*0.1
  s=vv*0.1
  fx=x_forv+s/pow(((pow((y(x_forv+0.1)-y(x_forv))/0.1,2))+1),0.5)
  vv=vv-s*0.09
  fy=y(fx)
  x_b.append(fx)
  y_b.append(fy)
  mas_speed.append(vv)
  xbobomba.append(x_forv)
  mass_time.append(float(n))
  return(fx,vv)

def init():
 redDot.set_data([],[])
 return redDot,
i=0
def animate(i):
    redDot.set_data(x_b[i], y_b[i])
    return redDot,

def plot_ball():
   x_forv=x
   vv=0
   x_b.append(x)
   y_b.append(y(x))
   n = 0.1
   mas_speed.append(vv)
   mass_time.append(float(n))
   xbobomba.append(x_forv)
   while(abs(vv)>1 or (y(x_forv+0.1)-y(x_forv))/0.1!=0):
       n += 0.1
       (x_forv,vv)=movement(x_forv,vv, n)

pit=plt.grid()
plt.plot(xx,yy,'m')
plot_ball()

plt.ylabel('У[ММ]')
plt.xlabel('Х[ММ]')
plt.title('График движения материальной точки', fontsize=15)
plt.xlabel('x,mm', color='magenta')
plt.ylabel('y,mm', color='magenta')
redDot, = plt.plot([0], [0], marker = 'o', color = 'black')

ani = animation.FuncAnimation(fig, animate, init_func=init,  interval=10, blit=True, repeat=True)

plt.show()

pit = plt.grid()
plt.title('График зависимости скорости от времени', fontsize=15)
plt.plot(mass_time, mas_speed)
plt.xlabel('t,mm', color='magenta')
plt.ylabel('v,mm/c', color='magenta')
plt.show()

pit = plt.grid()
plt.title('График зависимости скорости от координаты', fontsize=15)
plt.plot(xbobomba, mas_speed)
plt.xlabel('x,mm', color='magenta')
plt.ylabel('v,mm/c', color='magenta')
plt.show()