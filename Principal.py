# https://streamlit-emoji-shortcodes-streamlit-app-gwckff.streamlit.app/
import datetime
import streamlit as st
import plotly.graph_objects as go

st.set_page_config(
    page_title="Monitor Reserva Natural Urbana del Oeste - Santa Fe",
    page_icon="🍻",
    layout="wide"
)

st.write("# Monitor RNUO 🍻")

placeholder = st.empty()
with placeholder.container():
    hoy = datetime.datetime.now()
    st.write(f"#### Fecha y hora: {hoy.day}/{hoy.month}/{hoy.year} {hoy.hour}:{hoy.minute}:{hoy.second}")
    c1, c2, c3, c4 = st.columns(4)
    # fill in those three columns with respective metrics or KPIs

    c1.metric(
        label="Canal 1",
        value=11,
        delta=12,
    )
    
    c2.metric(
        label="Reservorio",
        value=21,
        delta=20,
    )
    
    c3.metric(
        label="Alcantarilla 1",
        value=31,
        delta=32,
    )

    c4.metric(
        label="Alcantarilla 2",
        value=31,
        delta=32,
    )
    fig_col1, fig_col2, fig_col3 = st.columns(3)
    with fig_col1:
        fig = go.Figure()
        fig.add_trace(go.Bar(x = ["Canal 1", "Reservorio", "Alcantarilla 1","Alcantarilla 2"], y = [50, 55, 43, 39],))
        fig.update_layout(title="Altura hidrométrica", barmode='group',legend=dict(orientation="h", yanchor="bottom", y=1.02,xanchor="right", x=0.9))

        st.plotly_chart(fig, use_container_width=True)
    
    with fig_col2:
        fig = go.Figure()
        fig.add_trace(go.Bar(x = ["Canal 1", "Reservorio", "Alcantarilla 1","Alcantarilla 2"], y = [50, 55, 43, 39],))
        fig.update_layout(title="Altura hidrométrica", barmode='group',legend=dict(orientation="h", yanchor="bottom", y=1.02,xanchor="right", x=0.9))

        st.plotly_chart(fig, use_container_width=True)

    with fig_col3:
        fig = go.Figure()
        fig.add_trace(go.Bar(x = ["Canal 1", "Reservorio", "Alcantarilla 1","Alcantarilla 2"], y = [50, 55, 43, 39],))
        fig.update_layout(title="Altura hidrométrica", barmode='group',legend=dict(orientation="h", yanchor="bottom", y=1.02,xanchor="right", x=0.9))

        st.plotly_chart(fig, use_container_width=True)