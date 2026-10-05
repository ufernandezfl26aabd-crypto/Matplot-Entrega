import pandas as pd
import matplotlib.pyplot as plt
import numpy as np 
# df = pd.read_csv("/home/unai/Programazioa/Python oinarriak/matplot/eguraldia.csv") 

df = pd.read_csv(r"C:\Users\UNAI\Desktop\entrega\matplot\eguraldia.csv")

plt.plot(df["eguna"], df["tenperatura"] , label = "Tenperatura " )
plt.plot(df["eguna"], df["euria_mm"] , label = "Precipitazioak" )
plt.title("Eguraldia ")

plt.xlabel("eguna")
plt.ylabel("Tenpertura")
plt.legend()
plt.savefig("grafikoatemperatura.png", dpi=300)
plt.show()

# 2 ikasleak.csv 
df = pd.read_csv(r"C:\Users\UNAI\Desktop\entrega\matplot\ikasleak_Matplot.csv")
ikasleak = df["ikasgela"].value_counts().sort_index()

plt.subplot(1, 2, 2)
plt.bar(ikasleak.index, ikasleak, label = "klasea ikaslerekiko")

plt.title("ikasle dauden klaserekiko")
plt.xlabel("Klasea")
plt.ylabel("Ikasle kopurua")
plt.legend()




plt.subplot(1, 2, 1)
notak = df.groupby("ikasgela")["nota"].mean()
plt.bar(notak.index, notak, label = "Media")

plt.title("klase bakoitzeko batazbesteko nota.")
plt.xlabel("Klasea")
plt.ylabel("nota")
plt.legend()
plt.savefig("grafikoamedia.png", dpi=300)

plt.show()
