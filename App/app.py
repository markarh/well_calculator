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
    "Динамический уровень",
    "Время подачи",
    "Скорость притока к скважине"
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

        P_inlet = st.number_input(
            "Давление на приёме насоса / Inlet pressure (MPa)", value=10.0, step=0.1, format="%.2f", min_value=0.0
        )

        P_annulus = st.number_input(
            "Затрубное давление / Annulus pressure (MPa)", value=10.0, step=0.1, format="%.2f", min_value=0.0
        )

        calculate = st.button("Calculate dynamic level", key="calc_dyn")

    # ---- Расчёт ----

    with col2:

        st.subheader("Results")

        if calculate:

            P_inlet_pa = P_inlet * mpa_to_pa                                                                            # Перевод в Па
            P_annulus_pa = P_annulus * mpa_to_pa
                                                                                                                        # Необходимо рассмотреть случаи, когда P_annulus >= P_inlet
            if P_annulus_pa >= P_inlet_pa:                                                                              # Проверка, чтобы затрубное давление не оказалось больше, чем на приёме насоса
                st.warning("Annulus pressure must be lower than wellhead pressure")
                st.stop()

            h = (P_inlet_pa - P_annulus_pa) / (mean_density * g)                                                     # Формула нахождения гидростатического уровня
            H_dyn = H - h                                                                                               # Формула нахождения динамического уровня

            st.metric("Высота столба жидкости / Fluid column height (m)", f"{h:.2f}")
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


            t_flow = H_static * B_nkt / Q_esp

            st.metric("Время появления подачи на устье (min)", f"{t_flow:.2f}")
            st.caption("t = H_static × B_nkt / Q_esp × 1440")



# содержимое третьей вкладки
with tab3:
    st.header("Определение притока из пласта / Inflow rate")

    col1, col2 = st.columns(2)

    with col1:
        st.subheader("Inputs")

        Q_agzu = st.number_input(
            'дебит скважины замеренный по АГЗУ за время T (m3/day)', value=100.0, step=0.1, format="%.2f", min_value=0.0
        )
        H_dyn1 = st.number_input(
            'Начальный динамический уровень в скважине при определении притока (m)', value=1000.0, step=0.1, format="%.2f", min_value=0.0         #
        )
        H_dyn2 = st.number_input(
            'Конечный динамический уровень в скважине за время T (m)', value=1000.0, step=0.1, format="%.2f", min_value=0.0
        )



