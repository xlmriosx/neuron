import numpy as np
import pandas as pd
import matplotlib.pyplot as plt


# %%
df = np.array([
  [0, 100],
  [20, 150],
  [30, 200],
  [40, 180],
  [50, 250],
  [60, 230]
])

pd_df = pd.DataFrame(df)


# %%
print(len(pd_df))


# %%
print(pd_df)


# %%
sum_x = pd_df[0].sum()
print(sum_x)
sum_y = pd_df[1].sum()
print(sum_y)

sum_xSquared = pd_df[0].apply(lambda x : x**2).sum()
print(sum_xSquared)
sum_xy = (pd_df[0] * pd_df[1]).sum()
print(sum_xy)
n = len(pd_df)
print(n)


# %%
#Hallar la pendiente
pendiente = (n*sum_xy - sum_x*sum_y)/(n*sum_xSquared - sum_x**2)
print(pendiente)
#Hallar la intersección
interseccion = (sum_y - pendiente*sum_x)/n
print(interseccion)


# %%
def f(m, x, b):
  """Calculo de la pendiente """
  return m*x + b


# %%
print('La ecuación lineal es: ')
print(f'y = {np.round(pendiente,2)}x + {np.round(interseccion,2)}')


# %%
ecm = np.std(df)
print("El error cuadratico medio es, ECM = ", ecm)


# %%
N = 1000
x = np.linspace(0, (60), num=N)
y = f(pendiente, x, interseccion)

fig, ax = plt.subplots()
ax.plot(x, y, color='green')

ax.scatter(pd_df[0], pd_df[1], c='red')

ax.set_xlabel('Gasto en publicidad')
ax.set_ylabel('Ventas')
ax.grid()
plt.show()

# %%