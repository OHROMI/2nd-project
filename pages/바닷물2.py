import streamlit as st
import plotly.graph_objs as go
import numpy as np
import pandas as pd

# -----------------------
# 데이터 생성
# -----------------------
np.random.seed(0)
years = np.arange(1995, 2025)
base_temp = 15 + 0.02 * (years - 1995)  # 약간씩 오르는 수온
noise = np.random.normal(0, 0.1, len(years))  # 약간의 잡음
temps = base_temp + noise

df = pd.DataFrame({'Year': years, 'SeaTemperature': temps})

# -----------------------
# 앱 UI
# -----------------------
st.title("📊 30년간 바닷물 수온 변화 시각화")
st.markdown("""
이 시각화는 **축 범위 설정에 따라 동일한 데이터가 어떻게 다르게 보일 수 있는지**를 보여줍니다.
""")

col1, col2 = st.columns(2)

# -----------------------
# 좁은 축 범위: 변화가 커 보임
# -----------------------
with col1:
    st.subheader("1️⃣ 좁은 Y축 범위 (수온 변화가 커 보임)")
    fig1 = go.Figure()
    fig1.add_trace(go.Scatter(x=df['Year'], y=df['SeaTemperature'],
                              mode='lines+markers', name='Temp'))
    fig1.update_layout(
        yaxis=dict(range=[14.5, 16.5]),
        title="Sea Surface Temperature (Zoomed In)",
        xaxis_title="Year",
        yaxis_title="Temperature (°C)"
    )
    st.plotly_chart(fig1, use_container_width=True)

# -----------------------
# 넓은 축 범위: 변화가 작아 보임
# -----------------------
with col2:
    st.subheader("2️⃣ 넓은 Y축 범위 (수온 변화가 작아 보임)")
    fig2 = go.Figure()
    fig2.add_trace(go.Scatter(x=df['Year'], y=df['SeaTemperature'],
                              mode='lines+markers', name='Temp'))
    fig2.update_layout(
        yaxis=dict(range=[0, 30]),
        title="Sea Surface Temperature (Full Range)",
        xaxis_title="Year",
        yaxis_title="Temperature (°C)"
    )
    st.plotly_chart(fig2, use_container_width=True)

# -----------------------
# 요약 메시지
# -----------------------
st.markdown("""
🔍 **생각해 볼 거리:**
- 두 그래프의 데이터는 완전히 동일하지만, 그래프의 인상은 다릅니다.
- 언론, 보고서, 광고에서 축의 범위를 조정하여 특정 메시지를 강화하려는 시도가 있을 수 있습니다.
- 데이터를 해석할 때는 항상 축 범위, 맥락, 단위 등을 주의 깊게 살펴보아야 합니다.
""")
