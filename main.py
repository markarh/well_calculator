import pandas as pd
import numpy as np

# Читаем файл
df = pd.read_excel("data/well_input.xlsx")

# Удаляем строку с единицами
df = df.iloc[1]

# Преобразуем в словарь
data = df.to_dict()

# Преобразуем значения в float (если вдруг строка)
for key in data:
    try:
        data[key] = float(str(data[key]).replace(',', '.'))
    except:
        pass

# Теперь работаем с данными
g = 9.81

P_res = data['Pпл']
K_temp = data['Тф']
G_grad = data['G']
H_depth = data['Hф']
angle = data['угол']
D_ek = data['Dэк']
K_prod = data['К']
x_popravka = ['поправка']
P_lin = data['Pл']
Q_debit = ['Qжсу']
D_nkt = data['Dнкт']
K_sherh = ['Кэ']
P_nas = ['Pнас']
Gas_factor = ['Гн.нас']
p_gsu = ['pгсу']
y_azot = ['ya']
p_isu = ['pису']
p_tl = ['pтж']
b_vsu = ['βвсу'] # объёмная доля попутной воды в добываемой из скв. жидкости при СУ (обводненность)
p_vsu = ['pвсу']
a_g = ['аг']
m_g = ['mг']
n_g = ['nг']
m_b = ['mв']
n_b = ['nв']
m_p = ['mp']
n_p = ['np']
m_y = ['my']
n_y = ['ny']

# Объемные расходы фаз и скв продукции в целом по пути движения от фильтра до устья скважины
def volume_rate (Q_debit, Q_oil, b_vsu):
    # если обводненность <= 65%
    if b_vsu <= 0.65:
        b_water = 1
    else:
        b_water = 1 # нужно усложнить позже
    Q_oil = Q_debit * b_oil * (1-b_vsu)
    Q_water = Q_debit * b_water * b_vsu
    return Q_oil, Q_water
#  При рассчете Q_oil в насоса при P<=Pд.нас следует взять вместо b_oil b_oil_corr
def b_oil_corr():
    b_oil_corr =


