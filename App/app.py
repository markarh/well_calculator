import streamlit as st

# настройка страницы
st.set_page_config(layout="wide")

# Заголовок приложения
st.title("Well Engineering Calculator")

# создаём вкладки
tab1, tab2, tab3 = st.tabs([
    "Dynamic Level",
    "Dupuit Flow",
    "Productivity Index"
])

# содержимое первой вкладки
with tab1:
    st.header("Dynamic Level Calculation")
    # ---- Ввод параметров ----

    H = st.number_input("Well depth H (m)", value=2500.0)

    P_ann = st.number_input(
        "Annulus pressure P_ann (MPa)", value=3.0
    )

    P_g = st.number_input(
        "Gas pressure P_g (MPa)", value=0.2
    )

    rho = st.number_input(
        "Fluid density (kg/m³)", value=850.0
    )

    # ---- Константа ----

    g = 9.81

    # ---- Расчёт ----

    if st.button("Calculate dynamic level"):

        # перевод MPa → Pa
        P_ann_pa = P_ann * 1_000_000
        P_g_pa = P_g * 1_000_000

        # высота жидкостного столба
        h = (P_ann_pa - P_g_pa) / (rho * g)

        # динамический уровень
        H_dyn = H - h

        st.subheader("Results")

        st.write(f"Fluid column height: {h:.2f} m")

        st.write(f"Dynamic level: {H_dyn:.2f} m")


# содержимое второй вкладки
with tab2:
    st.header("Dupuit Flow")

# содержимое третьей вкладки
with tab3:
    st.header("Productivity Index")

