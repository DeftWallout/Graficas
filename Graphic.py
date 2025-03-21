import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

Acos = 2
Fcos = 3
Facos = 1
#Primera gráfica de X vs Y
x=[2,3,4,5,6,7]
y=[4,9,16,25,36,49]
#Coseno
xcos = np.linspace(0,2*np.pi,100)
ycos = Acos*np.cos(Fcos*xcos + Facos)
#Seno
xsen = np.linspace(0,2*np.pi,100)
ysen = Acos*np.sin(Fcos*xsen + Facos)
#Gráfica de exponencial
z = np.linspace(-10,10,50)
v = 1/z

plt.figure(figsize=(12,8))
plt.subplot(3,1,(1,2))
plt.plot(x, y, color='black', marker='*')
plt.xlabel("Puntos en x", fontsize=10)
plt.ylabel("Puntos en y", fontsize=10)
plt.title(f"Gráfica X vs Y", fontsize=8)
plt.grid(True)
plt.xlim(0,10)

# Second subplot
plt.subplot(3, 1, 3)
plt.plot(xcos,ycos, color ='blue', marker = '*')
plt.title('Función coseno')


#Third subplot
plt.subplot(3, 3, 7)
plt.plot(xsen, ysen, color = 'red', marker = '*')
plt.title('Función seno')

#Cuarto subplot
plt.subplot(3, 3, 9)
plt.plot(z, v)
plt.title('Gráfica de 1/z')

plt.grid(True)






plt.show()

