import matplotlib.pyplot as plt 

x=[1,2,3,4]
y =[10,45,25,30]

plt.subplot(1,2,1)
plt.plot(x,y)
plt.title('First Subplot')

plt.subplot(1,2,2)
plt.bar(x,y)
plt.title('Second Subplot')

plt.tight_layout()
plt.show()
