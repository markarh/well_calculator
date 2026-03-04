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

        H = st.number_input("Длина подвески / ESP depth (m)", value=2500.0)

        P_head = st.number_input(
            "Устьевое давление / Head pressure (MPa)", value=10.0
        )

        P_annulus = st.number_input(
            "Затрубное давление / Annulus pressure (MPa)", value=10
        )

        calculate = st.button("Calculate dynamic level", key="calc_dyn")

    # ---- Расчёт ----

    with col2:

        st.subheader("Results")

        if calculate:

            P_head_pa = P_head * mpa_to_pa                                                                              # Перевод в Па
            P_annulus_pa = P_annulus * mpa_to_pa

            P_wellhead_pa = mean_density * g * H + P_head_pa                                                            # Нахождение забойного давления с учетом устьевого (Необходима проверка)

            if P_annulus >= P_wellhead_pa:                                                                              # Проверка, чтобы затрубное давление не оказалось больше, чем забойное
                st.warning("Annulus pressure must be lower than wellhead pressure")
                st.stop()

            h = (P_wellhead_pa - P_annulus_pa) / (mean_density * g)                                                     # Формула нахождения гидростатического уровня
            H_dyn = H - h                                                                                               # Формула нахождения динамического уровня

            st.metric("Уровень водяного столба / Fluid column height (m)", f"{h:.2f}")
            st.metric(" Динамический уровень / Dynamic level (m)", f"{H_dyn:.2f}")

































# содержимое второй вкладки
with tab2:
    st.header("Dupuit Flow")

# содержимое третьей вкладки
with tab3:
    st.header("Productivity Index")

