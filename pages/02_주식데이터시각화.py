import streamlit as st
import yfinance as yf
import pandas as pd
import plotly.graph_objects as go
from datetime import datetime, timedelta

# 글로벌 시가총액 TOP 10 기업 티커 (2025년 기준 예시)
TOP_10_COMPANIES = {
    "AAPL": "Apple Inc.",
    "MSFT": "Microsoft Corp.",
    "NVDA": "NVIDIA Corp.",
    "GOOGL": "Alphabet Inc. (Class A)",
    "GOOG": "Alphabet Inc. (Class C)",
    "AMZN": "Amazon.com Inc.",
    "META": "Meta Platforms Inc.",
    "TSLA": "Tesla Inc.",
    "BRK.B": "Berkshire Hathaway Inc. (Class B)",  # 주의: Yahoo Finance에서는 점(.) 사용
    "JPM": "JPMorgan Chase & Co.",
}

# 페이지 설정
st.set_page_config(page_title="글로벌 시가총액 TOP10 주가 분석", layout="wide")
st.title("🌎 글로벌 시가총액 TOP 10 기업의 최근 3년간 주가 변화")
st.markdown("데이터 출처: Yahoo Finance (yfinance)")

# 날짜 범위 설정 (최근 3년)
end_date = datetime.today()
start_date = end_date - timedelta(days=3 * 365)

# 기업 선택
st.sidebar.header("기업 선택")
selected_tickers = st.sidebar.multiselect(
    "분석할 기업을 선택하세요:",
    options=list(TOP_10_COMPANIES.keys()),
    default=list(TOP_10_COMPANIES.keys())[:5]
)

if not selected_tickers:
    st.warning("최소 하나의 기업을 선택해야 합니다.")
    st.stop()

# 주가 데이터 수집
@st.cache_data(show_spinner=True)
def fetch_data(ticker: str):
    df = yf.download(ticker, start=start_date, end=end_date)
    return df["Adj Close"] if "Adj Close" in df.columns else pd.Series()

st.info("💾 주가 데이터를 다운로드 중입니다...")
all_data = {}
for ticker in selected_tickers:
    series = fetch_data(ticker)
    if not series.empty:
        all_data[ticker] = series
    else:
        st.warning(f"{TOP_10_COMPANIES[ticker]} ({ticker}) 데이터 없음.")

# 데이터프레임으로 정리
if not all_data:
    st.error("유효한 데이터를 가져오지 못했습니다.")
    st.stop()

df_prices = pd.DataFrame(all_data)

# 정규화: 기준일 종가 = 100
df_normalized = df_prices / df_prices.iloc[0] * 100

# 그래프 그리기
fig = go.Figure()
for ticker in df_normalized.columns:
    fig.add_trace(go.Scatter(
        x=df_normalized.index,
        y=df_normalized[ticker],
        mode="lines",
        name=f"{TOP_10_COMPANIES[ticker]} ({ticker})"
    ))

fig.update_layout(
    title="📈 최근 3년간 정규화된 주가 변화 (기준일 = 100)",
    xaxis_title="날짜",
    yaxis_title="정규화된 주가",
    hovermode="x unified",
    legend_title="기업",
    height=600
)

st.plotly_chart(fig, use_container_width=True)

# 원시 데이터 표
st.subheader("📊 원시 주가 데이터 (Adj Close)")
st.dataframe(df_prices.tail())
