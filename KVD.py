import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression

# === 1. Чтение файла ===
df = pd.read_excel("kvd_data.xlsx")

# предполагаем колонки: time, pressure
t = df["time"].values
P = df["pressure"].values

# === 2. Определяем пластовое давление ===
P_pl = max(P)

# === 3. Считаем депрессию ===
delta_P = P_pl - P

# === 4. Берем логарифм времени ===
ln_t = np.log(t)

# === 5. Линейная регрессия ===
X = ln_t.reshape(-1, 1)
y = delta_P

model = LinearRegression()
model.fit(X, y)

A = model.coef_[0]
B = model.intercept_

print("Коэффициент A:", A)
print("Коэффициент B:", B)

# === 6. Строим график ===
plt.figure()
plt.scatter(ln_t, delta_P, label="Эксперимент")
plt.plot(ln_t, model.predict(X), color="red", label="Линейная аппроксимация")
plt.xlabel("ln(t)")
plt.ylabel("ΔP")
plt.title("Линеаризация КВД")
plt.legend()
plt.show()