import streamlit as st
import yfinance as yf
import plotly.graph_objects as go
import pandas as pd
from datetime import datetime, timedelta

# --- 글로벌 시가총액 TOP 10 기업 (예시, 실제 데이터와 다를 수 있음) ---
TOP_10_COMPANIES = {
    "AAPL": "Apple Inc.",
    "MSFT": "Microsoft Corp.",
    "NVDA": "NVIDIA Corp.",
    "GOOGL": "Alphabet Inc. (Class A)",
    "GOOG": "Alphabet Inc. (Class C)",
    "AMZN": "Amazon.com Inc.",
    "META": "Meta Platforms Inc.",
    "TSLA": "Tesla Inc.",
    "BRK.B": "Berkshire Hathaway Inc. (Class B)",  # 수정됨
    "JPM": "JPMorgan Chase & Co.",
    "XOM": "Exxon Mobil Corp.",
    "LLY": "Eli Lilly and Company",
}

st.set_page_config(layout="wide")
st.title("📈 글로벌 시가총액 TOP 기업 주가 변화 (최근 3년)")
st.markdown("현재 날짜 (2025년 6월 10일)를 기준으로 최근 3년간의 주가 변화를 시각화합니다.")

# --- 날짜 범위 설정 ---
end_date = datetime.now()
start_date = end_date - timedelta(days=3 * 365)

st.sidebar.header("설정")
selected_companies = st.sidebar.multiselect(
    "확인할 기업을 선택하세요:",
    options=list(TOP_10_COMPANIES.keys()),
    default=list(TOP_10_COMPANIES.keys())[:5]
)

st.sidebar.info(
    "기업 목록은 **예시**입니다. 실시간 시가총액 TOP 10은 변동할 수 있습니다."
    " 정확한 목록은 금융 정보 사이트를 참고해주세요."
)

if not selected_companies:
    st.warning("최소 하나 이상의 기업을 선택해주세요.")
else:
    stock_data = {}
    progress_bar = st.progress(0)
    status_text = st.empty()

    for i, ticker in enumerate(selected_companies):
        status_text.text(f"데이터 다운로드 중: {TOP_10_COMPANIES[ticker]} ({ticker})")
        try:
            data = yf.download(ticker, start=start_date, end=end_date)
            if not data.empty and "Adj Close" in data.columns:
                stock_data[ticker] = data["Adj Close"]
            else:
                st.warning(f"{TOP_10_COMPANIES[ticker]} ({ticker})의 데이터가 없거나 'Adj Close' 컬럼이 없습니다.")
        except Exception as e:
            st.error(f"{TOP_10_COMPANIES[ticker]} ({ticker}) 데이터 다운로드 중 오류 발생: {e}")
        progress_bar.progress((i + 1) / len(selected_companies))

    if stock_data:
        df_combined = pd.DataFrame(stock_data)
        df_normalized = df_combined / df_combined.iloc[0] * 100

        st.subheader("기업별 주가 변화 추이 (3년 전 대비 정규화)")
        st.write(f"기간: {start_date.strftime('%Y-%m-%d')} ~ {end_date.strftime('%Y-%m-%d')}")

        fig = go.Figure()
        for ticker in df_normalized.columns:
            fig.add_trace(go.Scatter(
                x=df_normalized.index,
                y=df_normalized[ticker],
                mode='lines',
                name=f"{TOP_10_COMPANIES[ticker]} ({ticker})"
            ))

        fig.update_layout(
            hovermode="x unified",
            xaxis_title="날짜",
            yaxis_title="정규화된 주가 (3년 전 = 100)",
            legend_title="기업",
            height=600,
            xaxis_rangeslider_visible=False
        )
        st.plotly_chart(fig, use_container_width=True)

        st.subheader("원시 주가 데이터 (조정 종가)")
        st.dataframe(df_combined.head())
    else:
        st.info("선택된 기업의 데이터를 가져오지 못했습니다.")

st.markdown("---")
st.markdown("본 앱은 교육 및 정보 제공 목적으로만 사용되며, 투자 조언이 아닙니다.")
