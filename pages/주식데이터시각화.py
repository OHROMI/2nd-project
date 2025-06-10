import streamlit as st
import yfinance as yf
import plotly.graph_objects as go
import pandas as pd
from datetime import datetime, timedelta

# --- 글로벌 시가총액 TOP 10 기업 (예시, 실제 데이터와 다를 수 있음) ---
# 2025년 6월 10일 기준 실시간 TOP 10을 가져올 수 없으므로, 일반적으로 TOP 기업들을 가정하여 사용합니다.
# 실제 배포 시에는 최신 데이터를 반영할 수 있도록 수동으로 업데이트하거나,
# 별도의 API를 통해 최신 시가총액 데이터를 가져오는 로직을 추가해야 합니다.
TOP_10_COMPANIES = {
    "AAPL": "Apple Inc.",
    "MSFT": "Microsoft Corp.",
    "NVDA": "NVIDIA Corp.",
    "GOOGL": "Alphabet Inc. (Class A)",
    "GOOG": "Alphabet Inc. (Class C)",
    "AMZN": "Amazon.com Inc.",
    "META": "Meta Platforms Inc.",
    "TSLA": "Tesla Inc.",
    "BRK-B": "Berkshire Hathaway Inc. (Class B)",
    "JPM": "JPMorgan Chase & Co.",
    "XOM": "Exxon Mobil Corp.", # 예시로 1개 더 추가 (TOP 10 변동성 고려)
    "LLY": "Eli Lilly and Company", # 예시로 1개 더 추가 (TOP 10 변동성 고려)
}

st.set_page_config(layout="wide")
st.title("📈 글로벌 시가총액 TOP 기업 주가 변화 (최근 3년)")
st.markdown("현재 날짜 (2025년 6월 10일)를 기준으로 최근 3년간의 주가 변화를 시각화합니다.")

# --- 날짜 범위 설정 ---
end_date = datetime.now() # 현재 날짜
start_date = end_date - timedelta(days=3 * 365) # 3년 전 (윤년 고려 안 함)

st.sidebar.header("설정")
selected_companies = st.sidebar.multiselect(
    "확인할 기업을 선택하세요:",
    options=list(TOP_10_COMPANIES.keys()),
    default=list(TOP_10_COMPANIES.keys())[:5] # 기본적으로 상위 5개 선택
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
            # yfinance로 주가 데이터 가져오기
            data = yf.download(ticker, start=start_date, end=end_date)
            if not data.empty:
                # 종가만 사용 (Adj Close가 분할/배당 조정된 종가)
                stock_data[ticker] = data['Adj Close']
            else:
                st.warning(f"{TOP_10_COMPANIES[ticker]} ({ticker}) 데이터가 없습니다. 티커를 확인해주세요.")
        except Exception as e:
            st.error(f"{TOP_10_COMPANIES[ticker]} ({ticker}) 데이터 다운로드 중 오류 발생: {e}")
        progress_bar.progress((i + 1) / len(selected_companies))

    if stock_data:
        # 모든 주식 데이터를 하나의 DataFrame으로 합치기 (각 기업의 종가)
        df_combined = pd.DataFrame(stock_data)

        # 기준일(3년 전)의 종가로 정규화 (모든 주가를 기준일 대비 변화율로 표시)
        # 이렇게 하면 서로 다른 가격대의 주식들을 한 그래프에서 비교하기 용이합니다.
        df_normalized = df_combined / df_combined.iloc[0] * 100 # 기준일을 100으로 설정

        st.subheader("기업별 주가 변화 추이 (3년 전 대비 정규화)")
        st.write(f"기간: {start_date.strftime('%Y-%m-%d')} ~ {end_date.strftime('%Y-%m-%d')}")

        fig = go.Figure()
        for ticker in df_normalized.columns:
            fig.add_trace(go.Scatter(x=df_normalized.index, y=df_normalized[ticker],
                                     mode='lines',
                                     name=f"{TOP_10_COMPANIES[ticker]} ({ticker})"))

        fig.update_layout(
            hovermode="x unified", # 마우스 오버 시 모든 라인의 데이터 표시
            xaxis_title="날짜",
            yaxis_title="정규화된 주가 (3년 전 = 100)",
            legend_title="기업",
            height=600,
            xaxis_rangeslider_visible=False # 아래 슬라이더 숨기기
        )
        st.plotly_chart(fig, use_container_width=True)

        st.subheader("원시 주가 데이터 (조정 종가)")
        st.dataframe(df_combined.head())
    else:
        st.info("선택된 기업의 데이터를 가져오지 못했습니다.")

st.markdown("---")
st.markdown("본 앱은 교육 및 정보 제공 목적으로만 사용되며, 투자 조언이 아닙니다.")
