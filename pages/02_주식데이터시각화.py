import streamlit as st
import yfinance as yf
import pandas as pd
import plotly.graph_objects as go
from datetime import datetime, timedelta

def get_top_10_market_cap_tickers():
    """
    글로벌 시가총액 상위 기업의 티커를 반환합니다.
    (주의: yfinance에서 직접적으로 실시간 시가총액 순위를 제공하지 않으므로,
    일반적으로 알려진 시가총액 상위 기업들을 수동으로 지정합니다.
    실제 시가총액 순위는 변동될 수 있습니다.)
    """
    # 2024-2025년 기준 일반적으로 알려진 글로벌 시가총액 상위 기업들 (변동 가능성 있음)
    # yfinance 티커를 사용합니다.
    return {
        "Apple": "AAPL",
        "Microsoft": "MSFT",
        "NVIDIA": "NVDA",
        "Alphabet (Google)": "GOOGL", # 또는 GOOG
        "Amazon": "AMZN",
        "Meta Platforms": "META",
        "Berkshire Hathaway": "BRK.A", # 또는 BRK.B (클래스 B 주식)
        "Eli Lilly and Company": "LLY",
        "TSMC": "TSM",
        "Johnson & Johnson": "JNJ"
    }

def fetch_stock_data(ticker, period="3y"):
    """
    주가 데이터를 yfinance에서 가져옵니다.
    """
    try:
        data = yf.download(ticker, period=period)
        return data['Adj Close']
    except Exception as e:
        st.error(f"'{ticker}' 데이터를 가져오는 중 오류 발생: {e}")
        return pd.Series()

def app():
    st.set_page_config(layout="wide")
    st.title("글로벌 시가총액 Top 10 기업 주가 변화 (최근 3년)")

    st.write(
        """
        이 앱은 `yfinance`를 사용하여 글로벌 시가총액 상위 10개 기업(미리 정의된 리스트)의
        지난 3년간의 주가 변화를 시각화합니다.
        데이터 로딩에는 다소 시간이 걸릴 수 있습니다.
        """
    )

    tickers_info = get_top_10_market_cap_tickers()
    company_names = list(tickers_info.keys())
    tickers = list(tickers_info.values())

    stock_data = {}
    with st.spinner("주가 데이터를 불러오는 중..."):
        for name, ticker in tickers_info.items():
            stock_data[name] = fetch_stock_data(ticker, period="3y")

    # 모든 데이터가 성공적으로 로드되었는지 확인
    if not all(not data.empty for data in stock_data.values()):
        st.warning("일부 또는 모든 기업의 데이터를 가져오지 못했습니다. 앱을 다시 시작하거나 인터넷 연결을 확인해주세요.")
        return

    # 데이터프레임으로 통합
    df_stock = pd.DataFrame(stock_data)
    df_stock.index.name = 'Date'

    st.subheader("주가 추이")

    # 인터랙티브한 Plotly 그래프 생성
    fig = go.Figure()

    for company_name in company_names:
        if company_name in df_stock.columns:
            fig.add_trace(go.Scatter(
                x=df_stock.index,
                y=df_stock[company_name],
                mode='lines',
                name=company_name
            ))

    fig.update_layout(
        title="글로벌 시가총액 Top 10 기업의 최근 3년간 주가 변화",
        xaxis_title="날짜",
        yaxis_title="종가 (USD)",
        hovermode="x unified",
        legend_title="기업",
        height=600
    )

    st.plotly_chart(fig, use_container_width=True)

    st.subheader("데이터 테이블")
    st.dataframe(df_stock.tail()) # 최근 데이터 일부만 보여줍니다.

    st.markdown(
        """
        ---
        **참고:**
        * 표시된 시가총액 Top 10 기업 목록은 일반적인 정보를 바탕으로 하며, 실시간 시가총액 순위와 다를 수 있습니다. `yfinance`는 직접적인 실시간 시가총액 순위 API를 제공하지 않습니다.
        * 데이터는 `yfinance`에서 제공하는 '수정 종가(Adjusted Close)'를 사용합니다.
        * 주식 분할, 배당 등으로 인해 주가가 조정될 수 있습니다.
        """
    )

if __name__ == "__main__" :
    app()
