import streamlit as st

# -------- constants --------
g = 9.81
mean_density = 850
mpa_to_pa = 1_000_000
# ---------------------------

# настройка страницы
st.set_page_config(
    page_title="Well Calculator",
    page_icon="🛢️",
    layout="centered"
)

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

    H = st.number_input("ESP depth (m)", value=2500.0)

    P_wellhead = st.number_input(
        "Wellhead pressure (MPa)", value=10.0
    )

    P_annulus = st.number_input(
        "Annulus pressure (MPa)", value=0.2
    )



    # ---- Константа ----


    # ---- Расчёт ----

    if st.button("Calculate dynamic level", key="calc_dyn"):

        result_box = st.container()

        if P_annulus >= P_wellhead:
            st.warning("Annulus pressure must be lower than wellhead pressure")
            st.stop()

        # перевод MPa → Pa
        P_wellhead_pa = P_wellhead * mpa_to_pa
        P_annulus_pa = P_annulus * mpa_to_pa

        # высота жидкостного столба
        h = (P_wellhead_pa - P_annulus_pa) / (mean_density * g)

        # динамический уровень
        H_dyn = H - h

        with result_box:
            st.subheader("Results")
            st.write(f"Fluid column height: {h:.2f} m")
            st.write(f"Dynamic level: {H_dyn:.2f} m")

































# содержимое второй вкладки
with tab2:
    st.header("Dupuit Flow")

# содержимое третьей вкладки
with tab3:
    st.header("Productivity Index")

