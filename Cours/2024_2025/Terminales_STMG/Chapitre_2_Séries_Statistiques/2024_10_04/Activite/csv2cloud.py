import pandas as pd
import matplotlib.pyplot as plt



videogame = pd.read_csv(r"C:\Users\quentincanu\Desktop\Enseignement\Cours\2024_2025\Terminales_STMG\Chapitre_2_Séries_Statistiques\2024_10_04\Activite\vgsales.csv")

videogame["GenreFactor"]=videogame["Genre"].astype("category")

print(videogame.head())
videogame["Genre"].value_counts().plot.bar()


# print(max(videogame["Year"]))
# videogame.plot.scatter(x="EU_Sales", y="NA_Sales", c="GenreFactor", colormap="tab20")
# plt.xlabel("Ventes des jeux en Europe (en millions)")
# plt.ylabel("Ventes des jeux en Amérique du Nord (en millions)")
plt.show()