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
    "기업 목록은 **예시**입니다. 실시간 시가총액 TOP 10은 변동할 수 있습니다
