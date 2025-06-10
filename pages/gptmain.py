import streamlit as st
import folium
from streamlit_folium import st_folium

# 포르투갈 주요 관광지 데이터
tourist_spots = [
    {
        "name": "리스본 - 벨렘 타워",
        "location": [38.6916, -9.2163],
        "description": "벨렘 타워는 16세기에 지어진 방어탑으로, 리스본의 상징적인 건축물 중 하나입니다. 유네스코 세계유산으로 등재되어 있으며, 마누엘 양식의 대표적인 예입니다.",
        "image": "https://images.pexels.com/photos/461936/pexels-photo-461936.jpeg?auto=compress&cs=tinysrgb&w=600"
    },
    {
        "name": "포르투 - 루이스 1세 다리",
        "location": [41.1406, -8.6110],
        "description": "포르투의 상징적인 철교로, 도루 강을 가로지르며 위층과 아래층 모두 보행과 차량이 이용 가능합니다. 야경이 특히 아름답습니다.",
        "image": "https://images.pexels.com/photos/2549573/pexels-photo-2549573.jpeg?auto=compress&cs=tinysrgb&w=600"
    },
    {
        "name": "신트라 - 페나 궁전",
        "location": [38.7876, -9.3904],
        "description": "동화 속 궁전 같은 페나 궁전은 다양한 건축 양식이 혼합된 아름다운 궁전으로, 신트라 산 정상에 위치해 멋진 전망을 자랑합니다.",
        "image": https://images.pexels.com/photos/30109751/pexels-photo-30109751/free-photo-of-pena-palace-architectural-beauty-in-sintra-portugal.jpeg?auto=compress&cs=tinysrgb&w=600"
    },
    {
        "name": "라구스 - 포르투갈 남부 해안",
        "location": [37.1016, -8.6742],
        "description": "라구스는 아름다운 해변과 해식 동굴, 그리고 절벽 경관으로 유명한 알가르브 지역의 대표적인 휴양지입니다.",
        "image": "https://images.pexels.com/photos/1368502/pexels-photo-1368502.jpeg?auto=compress&cs=tinysrgb&w=600"
    }
]

# Streamlit 앱 설정
st.set_page_config(page_title="포르투갈 관광 가이드", layout="wide")

st.title("🇵🇹 포르투갈 주요 관광지 가이드")
st.markdown("포르투갈의 아름다운 도시들과 명소를 지도와 함께 탐험해보세요!")

# Folium 지도 생성
m = folium.Map(location=[39.5, -8.0], zoom_start=6)

for spot in tourist_spots:
    popup_html = f"""
    <strong>{spot['name']}</strong><br>
    <img src="{spot['image']}" width="200"><br>
    <p>{spot['description']}</p>
    """
    folium.Marker(
        location=spot["location"],
        popup=folium.Popup(popup_html, max_width=250),
        tooltip=spot["name"]
    ).add_to(m)

# 지도 출력
st_folium(m, width=1000, height=600)

# 상세 설명
st.header("📍 관광지 상세 정보")
for spot in tourist_spots:
    st.subheader(spot["name"])
    col1, col2 = st.columns([1, 2])
    with col1:
        st.image(spot["image"], use_column_width=True)
    with col2:
        st.write(spot["description"])
