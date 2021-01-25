import numpy as np
import matplotlib.pyplot as plt
xlist = np.linspace(-3.0, 3.0, 100)
ylist = np.linspace(-3.0, 3.0, 100)
X, Y = np.meshgrid(xlist, ylist)
Z = np.sqrt(X**2 + Y**2)
fig,ax=plt.subplots(1,1)
cp = ax.contourf(X, Y, Z)
fig.colorbar(cp) # Add a colorbar to a plot
ax.set_title('Filled Contours Plot')
#ax.set_xlabel('x (cm)')
ax.set_ylabel('y (cm)')
plt.show()


x=pd.read_csv('x.csv', sep=',',header=None)
t=pd.read_csv('t.csv', sep=',',header=None)
u=pd.read_csv('u.csv', sep=',',header=None)
sol=pd.read_csv('sol.csv', sep=',',header=None)
