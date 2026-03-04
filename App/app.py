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

    col1, col2 = st.columns(2)

    # ---- Ввод параметров ----

    with col1:
        st.subheader("Inputs")

        H = st.number_input("ESP depth (m)", value=2500.0)

        P_wellhead = st.number_input(
            "Wellhead pressure (MPa)", value=10.0
        )

        P_annulus = st.number_input(
            "Annulus pressure (MPa)", value=0.2
        )

        calculate = st.button("Calculate dynamic level", key="calc_dyn")

    # ---- Расчёт ----

    with col2:
        st.subheader("Results")

        if calculate:

            if P_annulus >= P_wellhead:
                st.warning("Annulus pressure must be lower than wellhead pressure")
                st.stop()

            P_wellhead_pa = P_wellhead * mpa_to_pa
            P_annulus_pa = P_annulus * mpa_to_pa

            h = (P_wellhead_pa - P_annulus_pa) / (mean_density * g)
            H_dyn = H - h

            st.metric("Fluid column height (m)", f"{h:.2f}")
            st.metric("Dynamic level (m)", f"{H_dyn:.2f}")

































# содержимое второй вкладки
with tab2:
    st.header("Dupuit Flow")

# содержимое третьей вкладки
with tab3:
    st.header("Productivity Index")

