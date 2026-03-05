import streamlit as st

# -------- constants --------
g = 9.81
mean_density = 850
mpa_to_pa = 1_000_000

# таблица коэффициентов
tubing_table = {
    60: 2.8,
    73: 4.4,
    89: 6.5
}
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
    "Время подачи",
    "Productivity Index"
])

# содержимое первой вкладки
with tab1:
    st.header("Dynamic Level Calculation")

    col1, col2 = st.columns(2)

    # ---- Ввод параметров ----

    with col1:
        st.subheader("Inputs")

        H = st.number_input(
            "Длина подвески / ESP depth (m)", value=2500.0, step=0.1, format="%.2f", min_value=0.0
        )

        P_head = st.number_input(
            "Устьевое давление / Head pressure (MPa)", value=10.0, step=0.1, format="%.2f", min_value=0.0
        )

        P_annulus = st.number_input(
            "Затрубное давление / Annulus pressure (MPa)", value=10.0, step=0.1, format="%.2f", min_value=0.0
        )

        calculate = st.button("Calculate dynamic level", key="calc_dyn")

    # ---- Расчёт ----

    with col2:

        st.subheader("Results")

        if calculate:

            P_head_pa = P_head * mpa_to_pa                                                                              # Перевод в Па
            P_annulus_pa = P_annulus * mpa_to_pa

            P_wellhead_pa = mean_density * g * H + P_head_pa                                                            # Нахождение забойного давления с учетом устьевого (Необходима проверка)

            if P_annulus_pa >= P_wellhead_pa:                                                                              # Проверка, чтобы затрубное давление не оказалось больше, чем забойное
                st.warning("Annulus pressure must be lower than wellhead pressure")
                st.stop()

            h = (P_wellhead_pa - P_annulus_pa) / (mean_density * g)                                                     # Формула нахождения гидростатического уровня
            H_dyn = H - h                                                                                               # Формула нахождения динамического уровня

            st.metric("Уровень водяного столба / Fluid column height (m)", f"{h:.2f}")
            st.metric(" Динамический уровень / Dynamic level (m)", f"{H_dyn:.2f}")




# содержимое второй вкладки
with tab2:
    st.header("Время подачи")

    col1, col2 = st.columns(2)

    with col1:
        st.subheader("Inputs")

        H_static = st.number_input(
            "Статический уровень / Static level (m)", value=1500.0, step=0.1, format="%.2f", min_value=0.0
        )

        # выбор диаметра НКТ
        Q_nkt = st.selectbox(
            "Nominal tubing diameter / Номинальный диаметр НКТ (mm)",
            [60, 73, 89]
        )

        Q_esp = st.number_input(
            "Производительность насоса  / ESP performance (m3/day)", value=10.0, step=0.1, format="%.2f", min_value=0.0
        )

        calculate_flow = st.button("Calculate flow time", key="calc_flow")

    with col2:

        st.subheader("Results")


        # получение коэффициента
        B_nkt = tubing_table[Q_nkt]
        st.metric("B coefficient", B_nkt)

        if calculate_flow:

            if Q_esp <= 0:
                st.warning("Производительность насоса не может равняться 0 / ESP performance must be greater than zero")
                st.stop()


            t_flow = H_static * B_nkt / Q_esp * 1440

            st.metric("Время появления подачи на устье (min)", f"{t_flow:.2f}")
            st.caption("t = H_static × B_nkt / Q_esp × 1440")

































# содержимое третьей вкладки
with tab3:
    st.header("Productivity Index")

