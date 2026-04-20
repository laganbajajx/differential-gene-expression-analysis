import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("zone_of_inhibition.csv")

print(df)

df.plot(x="Antibiotic", y="Zone_mm", kind="bar")
plt.title("Antibiotic Susceptibility")
plt.ylabel("Zone of Inhibition (mm)")
plt.tight_layout()
plt.show()
