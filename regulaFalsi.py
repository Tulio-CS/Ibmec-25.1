from numpy import linspace
from matplotlib.pyplot import figure , plot, ylim, show,legend
from math import e

f=lambda x: (1- e**(-0.4*x))-0.25

# Creating array of x
x=linspace(0.1,10,50)

# Drawing function
figure(1,dpi=200)
plot(x,f(x))
ylim(0,5)
plot([-4,4],[0,0],'k--')

# Selecting false positions x1 and x2
x1=0.1
x2=10

# Evaluating corresponding y1 and y2
y1=f(x1)
y2=f(x2)

# Initial check
if y1*y2>0:
   print("on the same side of x axis, Correct the Range")
   exit
else:
   # Plotting line joining (x1,y1) and (x2,y2)
   plot([x1,x2],[y1,y2])
   
   # Iteration counter
   count=1
   
   # Iterations
   while True:
      xn=x1-y1*(x2-x1)/(y2-y1)
      plot([xn],[0],'o',label=f'{xn}')
      yn=f(xn)
      if abs(y1)<1.E-5:
         print("Root= ",x1)
         break
      elif y1*yn<0:
         x2=xn
         y2=yn
         plot([x1,x2],[y1,y2])
      else:
         x1=xn
         y1=yn
         plot([x1,x2],[y1,y2])
         
      # printing few xn in legend
      if count<6:
         legend()
         
      # Increasing iteration counter
      count +=1

show()