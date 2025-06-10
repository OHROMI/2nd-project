import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px

st.set_page_config(layout="wide")

st.title("🌊 30년간 바닷물 수온 변화 시각화")
st.subheader("통계적 자료 분석과 비판적 사고의 중요성")

st.markdown("""
이 애플리케이션은 30년간 가상의 바닷물 수온 데이터를 시각화합니다.
**Y축의 범위(최소/최대 수온)를 조절해보면서 동일한 데이터가 어떻게 다르게 해석될 수 있는지 확인해보세요.**
이를 통해 그래프의 축 간격이 데이터의 **시각적 메시지**에 얼마나 큰 영향을 미치는지 이해하고,
통계적 자료를 접할 때 **비판적인 사고**를 갖는 것이 왜 중요한지 생각해보시기 바랍니다.
""")

# 30년간 가상의 수온 데이터 생성 (월별 데이터)
np.random.seed(42) # 재현성을 위해 시드 설정
start_year = 1995
end_year = 2024
years = range(start_year, end_year + 1)
months = range(1, 13)

# 기준 수온 (예: 15도)과 연간 변동성, 장기적인 미세한 변화 경향 추가
base_temp = 15.0
annual_variation = np.sin(np.linspace(0, 2 * np.pi, 12)) * 3 # 계절 변화 (예: -3 ~ +3 도)
long_term_trend = np.linspace(0, 0.5, (end_year - start_year + 1) * 12) # 30년간 0.5도 상승 경향

dates = []
temperatures = []

for year in years:
    for month in months:
        dates.append(f"{year}-{month:02d}-01")
        # 기준 수온 + 계절 변화 + 랜덤 노이즈 + 장기적 경향
        temp = base_temp + annual_variation[month-1] + np.random.normal(0, 0.5) + \
               long_term_trend[(year - start_year) * 12 + (month - 1)]
        temperatures.append(temp)

df = pd.DataFrame({
    '날짜': pd.to_datetime(dates),
    '수온': temperatures
})

st.sidebar.header("📈 그래프 설정")
st.sidebar.markdown("Y축의 최소/최대 수온을 조절하여 그래프를 다르게 보여주세요.")

# Y축 범위 조절 슬라이더
min_temp_slider = st.sidebar.slider(
    "Y축 최소 수온",
    min_value=float(df['수온'].min() - 2),
    max_value=float(df['수온'].min()),
    value=float(df['수온'].min() - 0.5), # 초기값 설정
    step=0.1
)

max_temp_slider = st.sidebar.slider(
    "Y축 최대 수온",
    min_value=float(df['수온'].max()),
    max_value=float(df['수온'].max() + 2),
    value=float(df['수온'].max() + 0.5), # 초기값 설정
    step=0.1
)

# Plotly 그래프 생성
fig = px.line(
    df,
    x='날짜',
    y='수온',
    title="30년간 바닷물 수온 변화",
    labels={'날짜': '연도', '수온': '수온 (°C)'},
    height=500
)

# Y축 범위 설정
fig.update_yaxes(range=[min_temp_slider, max_temp_slider])

# 레이아웃 개선
fig.update_layout(
    title_font_size=24,
    xaxis_title_font_size=18,
    yaxis_title_font_size=18,
    hovermode="x unified",
    margin=dict(l=40, r=40, t=80, b=40)
)

st.plotly_chart(fig, use_container_width=True)

st.markdown("""
---
### 🤔 토론을 위한 질문:
* Y축 범위를 좁게 설정했을 때와 넓게 설정했을 때, 수온 변화가 어떻게 다르게 느껴지나요?
* 뉴스나 보고서에서 특정 그래프를 보았을 때, 어떤 점을 비판적으로 생각해야 할까요?
* 데이터 시각화가 때로는 의도적으로 정보를 왜곡하거나 특정 메시지를 강조하는 데 사용될 수 있다는 것을 알고 있나요?

**결론적으로, 통계적 자료를 시각화할 때는 데이터를 정직하게 표현하고, 해석할 때는 다양한 관점에서 비판적으로 접근하는 것이 매우 중요합니다.**
""")
