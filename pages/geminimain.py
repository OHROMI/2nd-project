import streamlit as st
import folium
from streamlit_folium import folium_static

st.set_page_config(layout="wide")

st.title("🇵🇹 포르투갈 주요 관광지 가이드")

st.markdown("""
이 가이드는 Streamlit과 Folium을 활용하여 포르투갈의 아름다운 주요 관광지들을 소개합니다.
각 도시의 매력을 탐험하고, 인터랙티브 지도를 통해 위치를 확인해 보세요!
""")

# --- 서론 ---
st.header("✨ 포르투갈, 매력적인 여행지")
st.image("https://d3b39vpyptsv01.cloudfront.net/photo/1/2/fbf1131576abb61595bb83be8374c224.jpg", caption="리스본의 25 데 아브릴 다리와 크리스투 헤이 전경")
st.markdown("""
**포르투갈**은 풍부한 역사, 아름다운 해안선, 맛있는 음식, 그리고 활기찬 문화가 어우러진 매력적인 나라입니다.
고대 로마 유적부터 중세 성곽, 화려한 마누엘 양식 건축물까지 다양한 볼거리를 제공하며,
따뜻한 기후와 친절한 사람들 덕분에 방문객들에게 잊지 못할 경험을 선사합니다.
""")

# --- 주요 도시 섹션 ---

# 1. 리스본
st.header("🏰 1. 리스본 (Lisbon)")
st.subheader("포르투갈의 활기찬 수도")
col1, col2 = st.columns(2)
with col1:
    st.image("https://images.pexels.com/photos/461936/pexels-photo-461936.jpeg?auto=compress&cs=tinysrgb&w=600", caption="벨렝 탑 (Torre de Belém)")
    st.image("https://www.windsortour.co.kr/images/area_img/PT/LIS/PTLIS3201525_0001.jpg?CMD=resize&width=100%", caption="리스본 대성당 (Sé de Lisboa)")
with col2:
    st.markdown("""
    **리스본**은 포르투갈의 수도이자 가장 큰 도시입니다. 테주 강변에 위치한 언덕 도시로, 아름다운 전망과 활기찬 분위기가 특징입니다.

    **주요 관광지:**
    * **벨렝 탑 (Belém Tower):** 유네스코 세계문화유산으로 지정된 마누엘 양식의 아름다운 요새예요. 대항해시대의 상징이죠.
    * **제로니무스 수도원 (Jerónimos Monastery):** 역시 유네스코 세계문화유산으로, 포르투갈의 번성했던 시대를 보여주는 웅장한 건축물입니다. 바스쿠 다 가마의 묘지가 이곳에 있어요.
    * **알파마 지구 (Alfama District):** 리스본에서 가장 오래된 지구로, 좁은 골목길, 파두 음악, 그리고 리스본 성의 아름다운 전망을 제공합니다.
    * **상 조르제 성 (São Jorge Castle):** 리스본 시내를 한눈에 내려다볼 수 있는 고대 성곽입니다.
    * **산타 주스타 엘리베이터 (Santa Justa Lift):** 에펠탑의 제자인 라울 드 보쉬에가 설계한 철제 엘리베이터로, 리스본의 멋진 전망을 제공합니다.
    * **코메르시우 광장 (Praça do Comércio):** 테주 강변에 위치한 웅장한 광장으로, 과거 왕궁이 있던 자리입니다.
    * **트램 28 (Tram 28):** 리스본의 언덕과 좁은 골목길을 누비며 주요 관광지를 지나는 노선으로, 그 자체로도 관광 명물입니다.

    **추천 활동:**
    * 알파마 지구에서 **파두 공연** 감상하기
    * 벨렝에서 **에그타르트(Pastel de Belém)** 맛보기
    * 산타 주스타 엘리베이터를 타고 리스본 시내 전망 감상하기
    * **트램 28**을 타고 리스본 골목길 탐험하기
    """)

# 리스본 지도
st.subheader("🗺️ 리스본 주요 관광지 지도")
m_lisbon = folium.Map(location=[38.7088, -9.1393], zoom_start=13)
folium.Marker([38.6916, -9.2167], tooltip="벨렝 탑", icon=folium.Icon(color="blue", icon="info-sign")).add_to(m_lisbon)
folium.Marker([38.6979, -9.2062], tooltip="제로니무스 수도원", icon=folium.Icon(color="blue", icon="info-sign")).add_to(m_lisbon)
folium.Marker([38.7135, -9.1309], tooltip="상 조르제 성", icon=folium.Icon(color="red", icon="home")).add_to(m_lisbon)
folium.Marker([38.7077, -9.1367], tooltip="산타 주스타 엘리베이터", icon=folium.Icon(color="green", icon="eye-open")).add_to(m_lisbon)
folium.Marker([38.7070, -9.1360], tooltip="코메르시우 광장", icon=folium.Icon(color="purple", icon="tag")).add_to(m_lisbon)
folium_static(m_lisbon)

st.markdown("---")

# 2. 포르투
st.header("🍷 2. 포르투 (Porto)")
st.subheader("도우루 강의 도시, 포트 와인의 고향")
col1, col2 = st.columns(2)
with col1:
    st.image("https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcQPHWXbTZ5jdU3Kf8zmirvOy3vbBHL0cDwe_g&s", caption="포르투 리베이라 지구")
    st.image("https://images.pexels.com/photos/2549573/pexels-photo-2549573.jpeg?auto=compress&cs=tinysrgb&w=600", caption="동 루이스 1세 다리")
with col2:
    st.markdown("""
    **포르투갈 북부**의 주요 도시이자 **포트 와인**의 본고장인 **포르투**는 도우루 강변의 아름다운 풍경과 역사적인 건축물로 유명합니다.

    **주요 관광지:**
    * **리베이라 지구 (Ribeira District):** 유네스코 세계문화유산으로 지정된 포르투의 구시가지로, 다채로운 색깔의 건물들과 강변 카페들이 인상적입니다.
    * **동 루이스 1세 다리 (Dom Luís I Bridge):** 에펠의 제자가 설계한 철제 다리로, 포르투의 상징 중 하나입니다. 다리 위에서 아름다운 도우루 강과 포르투 시내를 조망할 수 있습니다.
    * **클레리구스 탑 (Clérigos Tower):** 포르투에서 가장 높은 건물로, 정상에 오르면 포르투 시내 전경을 파노라마로 감상할 수 있습니다.
    * **렐루 서점 (Livraria Lello):** 세계에서 가장 아름다운 서점 중 하나로 손꼽히며, 해리포터 시리즈의 영감을 준 곳으로도 알려져 있습니다.
    * **상 벤투 역 (São Bento Railway Station):** 역 내부의 아름다운 아줄레주(타일) 벽화가 인상적인 기차역입니다.
    * **포트 와인 셀러 (Port Wine Cellars):** 도우루 강 건너편 빌라 노바 데 가이아(Vila Nova de Gaia)에 위치하며, 포트 와인 시음 투어를 즐길 수 있습니다.

    **추천 활동:**
    * **도우루 강변**에서 크루즈 타기
    * **포트 와인 셀러**에서 와인 시음 투어 참여하기
    * 동 루이스 1세 다리 위에서 일몰 감상하기
    * **렐루 서점**에서 독특한 분위기 즐기기
    """)

# 포르투 지도
st.subheader("🗺️ 포르투 주요 관광지 지도")
m_porto = folium.Map(location=[41.1496, -8.6109], zoom_start=14)
folium.Marker([41.1408, -8.6110], tooltip="리베이라 지구", icon=folium.Icon(color="blue", icon="info-sign")).add_to(m_porto)
folium.Marker([41.1404, -8.6105], tooltip="동 루이스 1세 다리", icon=folium.Icon(color="red", icon="home")).add_to(m_porto)
folium.Marker([41.1458, -8.6146], tooltip="클레리구스 탑", icon=folium.Icon(color="green", icon="eye-open")).add_to(m_porto)
folium.Marker([41.1457, -8.6139], tooltip="렐루 서점", icon=folium.Icon(color="purple", icon="tag")).add_to(m_porto)
folium.Marker([41.1456, -8.6108], tooltip="상 벤투 역", icon=folium.Icon(color="orange", icon="train")).add_to(m_porto)
folium_static(m_porto)

st.markdown("---")

# 3. 신트라
st.header(" fairytale 3. 신트라 (Sintra)")
st.subheader("동화 같은 성들이 있는 로맨틱한 도시")
col1, col2 = st.columns(2)
with col1:
    st.image("https://images.pexels.com/photos/30380673/pexels-photo-30380673/free-photo-of-tourists-explore-national-palace-of-pena-sintra.jpeg?auto=compress&cs=tinysrgb&w=600", caption="페나 성 (Palácio Nacional da Pena)")
    st.image("https://media.istockphoto.com/id/1167644659/ko/%EC%82%AC%EC%A7%84/%EC%8B%A0%ED%8A%B8%EB%9D%BC%EC%9D%98-%ED%80%B8%ED%83%80-%EB%8B%A4-%EB%A0%88%EA%B0%88%EB%A0%88%EC%9D%B4%EB%9D%BC-%ED%8F%AC%EB%A5%B4%ED%88%AC%EA%B0%88-%EB%A6%AC%EC%8A%A4%EB%B3%B8-%EA%B7%BC%EC%B2%98.jpg?s=170667a&w=0&k=20&c=RHzLKBn5jU-vefE5TZfvonM-Ni3_H_M3HEzEg4JQlMM=", caption="킨타 다 헤갈레이라 (Quinta da Regaleira)")
with col2:
    st.markdown("""
    **리스본 근교**에 위치한 **신트라**는 유네스코 세계문화유산으로 지정된 로맨틱한 산악 도시입니다.
    이곳은 동화 같은 궁전, 성, 그리고 울창한 정원으로 가득합니다.

    **주요 관광지:**
    * **페나 성 (Pena Palace):** 신트라의 상징이자 가장 유명한 명소입니다. 다채로운 색상과 이국적인 건축 양식이 어우러진 동화 같은 궁전입니다.
    * **신트라 국립 궁전 (Sintra National Palace):** 신트라 시내 중심에 위치한 중세 궁전으로, 독특한 원뿔형 굴뚝이 특징입니다.
    * **무어 성 (Moorish Castle):** 신트라의 산 정상에 위치한 고대 성곽 유적입니다. 리스본까지 이어지는 아름다운 전망을 제공합니다.
    * **킨타 다 헤갈레이라 (Quinta da Regaleira):** 신비로운 정원, 동굴, 지하 통로, 그리고 이니시에이션 우물(Initiation Well)로 유명한 사유지입니다.

    **추천 활동:**
    * **페나 성**에서 사진 찍고 동화 같은 분위기 만끽하기
    * **킨타 다 헤갈레이라**의 지하 통로와 우물 탐험하기
    * **무어 성**에서 신트라와 주변 경관 조망하기
    * 신트라 마을에서 현지 특산품 쇼핑하기
    """)

# 신트라 지도
st.subheader("🗺️ 신트라 주요 관광지 지도")
m_sintra = folium.Map(location=[38.7909, -9.3905], zoom_start=13)
folium.Marker([38.7876, -9.3903], tooltip="페나 성", icon=folium.Icon(color="blue", icon="info-sign")).add_to(m_sintra)
folium.Marker([38.7979, -9.3905], tooltip="신트라 국립 궁전", icon=folium.Icon(color="red", icon="home")).add_to(m_sintra)
folium.Marker([38.7937, -9.3879], tooltip="무어 성", icon=folium.Icon(color="green", icon="eye-open")).add_to(m_sintra)
folium.Marker([38.7960, -9.3938], tooltip="킨타 다 헤갈레이라", icon=folium.Icon(color="purple", icon="tag")).add_to(m_sintra)
folium_static(m_sintra)

st.markdown("---")

# 4. 파루 & 알가르베
st.header("🏖️ 4. 파루 & 알가르베 (Faro & Algarve)")
st.subheader("아름다운 해변과 햇살 가득한 남부 지역")
col1, col2 = st.columns(2)
with col1:
    st.image("https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcSbLoyJRWTfyB0b0FOmIw7s-dVyTvFeaJ2shA&s", caption="알가르베 해안선")
    st.image("https://images.pexels.com/photos/2602791/pexels-photo-2602791.jpeg?auto=compress&cs=tinysrgb&w=600", caption="파루 구시가지 (Cidade Velha de Faro)")
with col2:
    st.markdown("""
    **포르투갈 최남단**에 위치한 **알가르베** 지역은 세계적으로 유명한 아름다운 해변과 골프 코스로 명성이 높습니다.
    주요 도시인 **파루**는 이 지역의 관문 역할을 합니다.

    **주요 관광지:**
    * **파루 구시가지 (Faro Old Town):** 로마 시대 유적과 아름다운 바로크 양식의 건축물들이 어우러진 매력적인 구시가지입니다.
    * **카페도 뼈 예배당 (Capela dos Ossos):** 파루의 카르무 교회(Igreja do Carmo)에 위치한 독특한 예배당으로, 수천 개의 해골과 뼈로 장식되어 있습니다.
    * **폰타 다 피에다데 (Ponta da Piedade, 라고스):** 라고스 근처에 있는 절벽과 동굴 지형으로, 보트 투어를 통해 탐험할 수 있는 아름다운 해안 절경입니다.
    * **베나길 동굴 (Benagil Cave, 알망실):** 알가르베 해안의 상징적인 명소 중 하나로, 자연적으로 형성된 거대한 해식 동굴입니다. 보트나 카약으로 접근할 수 있습니다.
    * **세비야 (Seville, 스페인):** 파루에서 차로 약 2시간 거리에 스페인의 아름다운 도시 세비야가 있어 당일치기 여행도 가능합니다.

    **추천 활동:**
    * **알가르베 해변**에서 일광욕 및 해수욕 즐기기
    * 보트 투어를 통해 **폰타 다 피에다데**와 **베나길 동굴** 탐험하기
    * **파루 구시가지**의 역사적인 골목길 산책하기
    * 골프를 즐기는 사람이라면 세계적인 수준의 골프 코스에서 라운딩하기
    """)

# 파루 & 알가르베 지도 (중심은 파루)
st.subheader("🗺️ 파루 & 알가르베 주요 관광지 지도")
m_algarve = folium.Map(location=[37.0194, -7.9360], zoom_start=10)
folium.Marker([37.0163, -7.9352], tooltip="파루 대성당 & 구시가지", icon=folium.Icon(color="blue", icon="info-sign")).add_to(m_algarve)
folium.Marker([37.0177, -7.9383], tooltip="카페도 뼈 예배당", icon=folium.Icon(color="red", icon="home")).add_to(m_algarve)
folium.Marker([37.0858, -8.6723], tooltip="폰타 다 피에다데 (라고스)", icon=folium.Icon(color="green", icon="eye-open")).add_to(m_algarve)
folium.Marker([37.1009, -8.4259], tooltip="베나길 동굴 (알망실)", icon=folium.Icon(color="purple", icon="tag")).add_to(m_algarve)
folium_static(m_algarve)

st.markdown("---")

# 5. 아베이루
st.header("🛶 5. 아베이루 (Aveiro)")
st.subheader("포르투갈의 베네치아")
col1, col2 = st.columns(2)
with col1:
    st.image("https://images.pexels.com/photos/10312658/pexels-photo-10312658.jpeg?auto=compress&cs=tinysrgb&w=1260&h=750&dpr=2", caption="아베이루 몰리세이루스 보트")
    st.image("https://images.pexels.com/photos/10313098/pexels-photo-10313098.jpeg?auto=compress&cs=tinysrgb&w=1260&h=750&dpr=2", caption="아베이루 운하와 아르누보 건물")
with col2:
    st.markdown("""
    **포르투갈 중부**에 위치한 **아베이루**는 "포르투갈의 베네치아"라고 불리며,
    아름다운 운하와 독특한 모양의 배인 **'몰리세이루스(Moliceiros)'**로 유명합니다.

    **주요 관광지:**
    * **아베이루 운하 (Aveiro Canals):** 도시를 가로지르는 운하를 몰리세이루스 배를 타고 유람하는 것이 아베이루의 주요 매력입니다.
    * **코스타 노바 (Costa Nova):** 아베이루 근처 해변 마을로, 줄무늬 패턴의 알록달록한 집들로 유명합니다.
    * **아르누보 건축물 (Art Nouveau Buildings):** 아베이루 시내에는 아름다운 아르누보 양식의 건물들이 많이 남아 있어 독특한 분위기를 자아냅니다.
    * **아베이루 박물관 (Aveiro Museum):** 과거 수도원이었던 곳으로, 아베이루의 역사와 예술 작품을 전시하고 있습니다.

    **추천 활동:**
    * **몰리세이루스 배**를 타고 운하 유람하기
    * **코스타 노바**의 줄무늬 집들 앞에서 기념사진 찍기
    * 아베이루의 특산품인 **'오보스 몰레스(Ovos Moles)'** 맛보기 (계란 노른자와 설탕으로 만든 달콤한 디저트)
    * 아르누보 건축물 감상하며 도시 산책하기
    """)

# 아베이루 지도
st.subheader("🗺️ 아베이루 주요 관광지 지도")
m_aveiro = folium.Map(location=[40.6405, -8.6538], zoom_start=13)
folium.Marker([40.6405, -8.6540], tooltip="아베이루 운하", icon=folium.Icon(color="blue", icon="info-sign")).add_to(m_aveiro)
folium.Marker([40.6133, -8.7567], tooltip="코스타 노바", icon=folium.Icon(color="red", icon="home")).add_to(m_aveiro)
folium.Marker([40.6416, -8.6545], tooltip="아르누보 박물관 (아르누보 건물 밀집 지역)", icon=folium.Icon(color="green", icon="eye-open")).add_to(m_aveiro)
folium_static(m_aveiro)

st.markdown("---")

# 6. 코임브라
st.header(" 🎓 6. 코임브라 (Coimbra)")
st.subheader("유서 깊은 대학 도시")
col1, col2 = st.columns(2)
with col1:
    st.image("https://images.pexels.com/photos/10313093/pexels-photo-10313093.jpeg?auto=compress&cs=tinysrgb&w=1260&h=750&dpr=2", caption="코임브라 대학교 전경")
    st.image("https://images.pexels.com/photos/10313101/pexels-photo-10313101.jpeg?auto=compress&cs=tinysrgb&w=1260&h=750&dpr=2", caption="코임브라 구 대성당 (Sé Velha de Coimbra)")
with col2:
    st.markdown("""
    **포르투갈 중부**에 위치한 **코임브라**는 오랜 역사와 전통을 자랑하는 대학 도시입니다.
    포르투갈의 옛 수도였으며, 유네스코 세계문화유산으로 등재된 **코임브라 대학교**가 유명합니다.

    **주요 관광지:**
    * **코임브라 대학교 (University of Coimbra):** 1290년에 설립된 포르투갈에서 가장 오래된 대학으로, 바로크 양식의 **조아니나 도서관(Biblioteca Joanina)**이 특히 유명합니다.
    * **조아니나 도서관 (Biblioteca Joanina):** 코임브라 대학교 내에 위치한 세계에서 가장 아름다운 도서관 중 하나입니다. 화려한 장식과 수많은 고서들이 인상적입니다.
    * **코임브라 구 대성당 (Sé Velha de Coimbra):** 로마네스크 양식의 견고한 요새형 대성당으로, 오랜 역사를 간직하고 있습니다.
    * **산타 크루즈 수도원 (Santa Cruz Monastery):** 포르투갈의 초대 왕인 아폰수 1세의 묘지가 있는 곳입니다.
    * **소규모 포르투갈 (Portugal dos Pequenitos):** 포르투갈의 역사, 문화, 건축물을 미니어처로 재현해 놓은 테마파크입니다.

    **추천 활동:**
    * **코임브라 대학교** 캠퍼스 투어하기
    * **조아니나 도서관**의 웅장함 감상하기
    * 포르투갈 전통 의상을 입은 대학생들의 모습 구경하기
    * 몬데고 강변에서 여유로운 시간 보내기
    """)

# 코임브라 지도
st.subheader("🗺️ 코임브라 주요 관광지 지도")
m_coimbra = folium.Map(location=[40.2056, -8.4196], zoom_start=14)
folium.Marker([40.2081, -8.4277], tooltip="코임브라 대학교 (조아니나 도서관 포함)", icon=folium.Icon(color="blue", icon="info-sign")).add_to(m_coimbra)
folium.Marker([40.2087, -8.4260], tooltip="코임브라 구 대성당", icon=folium.Icon(color="red", icon="home")).add_to(m_coimbra)
folium.Marker([40.2078, -8.4239], tooltip="산타 크루즈 수도원", icon=folium.Icon(color="green", icon="eye-open")).add_to(m_coimbra)
folium.Marker([40.2001, -8.4275], tooltip="소규모 포르투갈", icon=folium.Icon(color="purple", icon="tag")).add_to(m_coimbra)
folium_static(m_coimbra)

st.markdown("---")

# 7. 오비두스
st.header(" medieval 7. 오비두스 (Óbidos)")
st.subheader("중세 성벽 마을")
col1, col2 = st.columns(2)
with col1:
    st.image("https://images.pexels.com/photos/10312678/pexels-photo-10312678.jpeg?auto=compress&cs=tinysrgb&w=1260&h=750&dpr=2", caption="오비두스 성곽 마을")
    st.image("https://images.pexels.com/photos/10312680/pexels-photo-10312680.jpeg?auto=compress&cs=tinysrgb&w=1260&h=750&dpr=2", caption="오비두스 성벽에서 바라본 마을 전경")
with col2:
    st.markdown("""
    **리스본에서 북쪽**으로 약 1시간 거리에 위치한 **오비두스**는 완벽하게 보존된 중세 성벽 마을입니다.
    아름다운 하얀 집들과 꽃으로 장식된 골목길이 매력적인 곳입니다.

    **주요 관광지:**
    * **오비두스 성 (Óbidos Castle):** 마을 전체를 둘러싸고 있는 견고한 성벽과 아름다운 성곽입니다. 성벽 위를 걸으며 마을 전체를 조망할 수 있습니다.
    * **산타 마리아 교회 (Igreja de Santa Maria):** 오비두스 중심부에 위치한 아름다운 교회로, 아줄레주 장식이 인상적입니다.
    * **포우사다 드 오비두스 (Pousada de Óbidos):** 성 내에 위치한 고급 호텔로, 성의 일부를 개조하여 만들었습니다.
    * **좁은 골목길과 상점들:** 성벽 안의 좁은 골목길을 따라 아기자기한 상점과 카페들이 줄지어 있습니다.

    **추천 활동:**
    * **성벽 위**를 걸으며 마을 전체와 주변 풍경 감상하기
    * 마을 골목길을 거닐며 아기자기한 상점 구경하기
    * 오비두스의 특산품인 **'진자(Ginja)'** 맛보기 (체리 리큐어)
    * 로맨틱한 분위기에서 식사 즐기기
    """)

# 오비두스 지도
st.subheader("🗺️ 오비두스 주요 관광지 지도")
m_obidos = folium.Map(location=[39.3621, -9.1578], zoom_start=16)
folium.Marker([39.3662, -9.1574], tooltip="오비두스 성", icon=folium.Icon(color="blue", icon="info-sign")).add_to(m_obidos)
folium.Marker([39.3649, -9.1572], tooltip="산타 마리아 교회", icon=folium.Icon(color="red", icon="home")).add_to(m_obidos)
folium_static(m_obidos)

st.markdown("---")

# 8. 파티마
st.header("🙏 8. 파티마 (Fátima)")
st.subheader("성모 발현지, 종교적 순례지")
col1, col2 = st.columns(2)
with col1:
    st.image("https://images.pexels.com/photos/10313103/pexels-photo-10313103.jpeg?auto=compress&cs=tinysrgb&w=1260&h=750&dpr=2", caption="파티마 성모 발현 기념 성당 광장")
    st.image("https://images.pexels.com/photos/10313102/pexels-photo-10313102.jpeg?auto=compress&cs=tinysrgb&w=1260&h=750&dpr=2", caption="파티마 지성모 삼위일체 대성당")
with col2:
    st.markdown("""
    **파티마**는 1917년 성모 마리아가 세 명의 어린 목동에게 발현했다고 전해지는 **가톨릭 순례지**입니다.
    매년 수백만 명의 순례자들이 이곳을 방문합니다.

    **주요 관광지:**
    * **파티마 성모 발현 기념 성당 (Sanctuary of Our Lady of Fátima):** 성모 발현이 이루어졌다고 알려진 곳에 세워진 거대한 광장과 성당들로 이루어진 단지입니다.
    * **로사리오의 성모 대성당 (Basilica of Our Lady of the Rosary):** 성모 발현을 목격한 세 어린 목동의 묘지가 있는 곳입니다.
    * **지성모 삼위일체 대성당 (Basilica of the Most Holy Trinity):** 2007년에 완공된 현대적인 대성당으로, 매우 큰 규모를 자랑합니다.
    * **발현의 작은 예배당 (Chapel of the Apparitions):** 성모 마리아가 처음 발현했다고 전해지는 자리에 세워진 작은 예배당입니다.

    **추천 활동:**
    * **성모 발현 기념 성당**에서 미사 참여하기
    * **십자가의 길** 걷기 (Via Sacra)
    * 기도하고 묵상하는 시간 가지기
    * 성물 구매하기
    """)

# 파티마 지도
st.subheader("🗺️ 파티마 주요 관광지 지도")
m_fatima = folium.Map(location=[39.6300, -8.6710], zoom_start=15)
folium.Marker([39.6310, -8.6720], tooltip="파티마 성모 발현 기념 성당", icon=folium.Icon(color="blue", icon="info-sign")).add_to(m_fatima)
folium.Marker([39.6318, -8.6738], tooltip="로사리오의 성모 대성당", icon=folium.Icon(color="red", icon="home")).add_to(m_fatima)
folium.Marker([39.6293, -8.6698], tooltip="지성모 삼위일체 대성당", icon=folium.Icon(color="green", icon="eye-open")).add_to(m_fatima)
folium.Marker([39.6309, -8.6706], tooltip="발현의 작은 예배당", icon=folium.Icon(color="purple", icon="tag")).add_to(m_fatima)
folium_static(m_fatima)

st.markdown("---")

# 9. 에보라
st.header("🏛️ 9. 에보라 (Évora)")
st.subheader("알렌테주 지방의 역사 도시")
col1, col2 = st.columns(2)
with col1:
    st.image("https://images.pexels.com/photos/10313083/pexels-photo-10313083.jpeg?auto=compress&cs=tinysrgb&w=1260&h=750&dpr=2", caption="에보라 로마 신전 (Templo Romano de Évora)")
    st.image("https://images.pexels.com/photos/10313097/pexels-photo-10313097.jpeg?auto=compress&cs=tinysrgb&w=1260&h=750&dpr=2", caption="에보라 뼈 예배당 (Capela dos Ossos)")
with col2:
    st.markdown("""
    **알렌테주 지방**의 중심부에 위치한 **에보라**는 유네스코 세계문화유산으로 지정된 고대 도시입니다.
    로마 시대부터 중세, 르네상스 시대에 이르는 다양한 역사적 유적을 간직하고 있습니다.

    **주요 관광지:**
    * **에보라 로마 신전 (Roman Temple of Évora):** 로마 시대에 건설된 신전의 유적으로, 에보라의 상징 중 하나입니다.
    * **에보라 대성당 (Évora Cathedral):** 로마네스크 양식과 고딕 양식이 혼합된 웅장한 대성당입니다.
    * **뼈 예배당 (Capela dos Ossos):** 상 프란시스쿠 교회(Igreja de São Francisco) 내에 위치하며, 수천 명의 유골로 장식된 독특한 예배당입니다.
    * **아구아 드 프라타 수로 (Aqueduto da Água de Prata):** 로마 시대부터 이어져 온 거대한 수로 유적입니다.
    * **에보라 대학교 (University of Évora):** 아름다운 건물과 역사적인 분위기를 자랑하는 대학입니다.

    **추천 활동:**
    * **로마 신전** 앞에서 고대 로마의 흔적 느끼기
    * **뼈 예배당**에서 삶과 죽음에 대해 성찰하기
    * 에보라 구시가지의 좁은 골목길 산책하며 역사 탐험하기
    * 알렌테주 지방의 맛있는 와인과 올리브 오일 맛보기
    """)

# 에보라 지도
st.subheader("🗺️ 에보라 주요 관광지 지도")
m_evora = folium.Map(location=[38.5667, -7.9094], zoom_start=15)
folium.Marker([38.5727, -7.9070], tooltip="에보라 로마 신전", icon=folium.Icon(color="blue", icon="info-sign")).add_to(m_evora)
folium.Marker([38.5714, -7.9079], tooltip="에보라 대성당", icon=folium.Icon(color="red", icon="home")).add_to(m_evora)
folium.Marker([38.5684, -7.9091], tooltip="뼈 예배당 (상 프란시스쿠 교회)", icon=folium.Icon(color="green", icon="eye-open")).add_to(m_evora)
folium_static(m_evora)

st.markdown("---")

# 10. 마데이라 제도
st.header("🌺 10. 마데이라 제도 (Madeira Islands)")
st.subheader("대서양의 진주, 꽃과 절경의 섬")
col1, col2 = st.columns(2)
with col1:
    st.image("https://images.pexels.com/photos/10313105/pexels-photo-10313105.jpeg?auto=compress&cs=tinysrgb&w=1260&h=750&dpr=2", caption="마데이라 카보 지랑 (Cabo Girão) 절벽")
    st.image("https://images.pexels.com/photos/10313084/pexels-photo-10313084.jpeg?auto=compress&cs=tinysrgb&w=1260&h=750&dpr=2", caption="푼샬 (Funchal) 항구와 도시 전경")
with col2:
    st.markdown("""
    **대서양**에 위치한 **마데이라 제도**는 '대서양의 진주'라고 불리며,
    아름다운 자연 경관, 독특한 식물군, 그리고 온화한 기후로 유명합니다.

    **주요 관광지:**
    * **푼샬 (Funchal):** 마데이라 제도의 수도로, 아름다운 항구와 오래된 건물들, 그리고 활기찬 시장이 있습니다.
    * **몬테 케이블카 (Monte Cable Car):** 푼샬에서 몬테 언덕으로 올라가며 아름다운 도시와 바다 경치를 감상할 수 있습니다.
    * **몬테 궁전 열대 정원 (Monte Palace Tropical Garden):** 세계 각지의 식물과 예술 작품이 어우러진 아름다운 정원입니다.
    * **카보 지랑 (Cabo Girão):** 유럽에서 가장 높은 해안 절벽 중 하나로, 투명한 스카이워크에서 아찔한 경험과 함께 멋진 경치를 즐길 수 있습니다.
    * **피코 아레이로 (Pico Ruivo & Pico do Areeiro):** 마데이라에서 가장 높은 봉우리들로, 하이킹을 통해 웅장한 산악 경관을 감상할 수 있습니다.
    * **레바다 (Levadas):** 섬 전체에 퍼져 있는 관개 수로를 따라 걷는 하이킹 코스입니다.

    **추천 활동:**
    * **몬테 케이블카**를 타고 푼샬 전경 감상하기
    * **카보 지랑 스카이워크**에서 아찔한 사진 찍기
    * **레바다 하이킹**을 통해 마데이라의 아름다운 자연 속으로 들어가기
    * **마데이라 와인** 시음하기
    * 전통 **토보간(썰매)** 체험하기
    """)

# 마데이라 지도 (중심은 푼샬)
st.subheader("🗺️ 마데이라 제도 주요 관광지 지도")
m_madeira = folium.Map(location=[32.6568, -16.9080], zoom_start=11)
folium.Marker([32.6483, -16.9081], tooltip="푼샬 (몬테 케이블카)", icon=folium.Icon(color="blue", icon="info-sign")).add_to(m_madeira)
folium.Marker([32.6657, -16.9015], tooltip="몬테 궁전 열대 정원", icon=folium.Icon(color="red", icon="home")).add_to(m_madeira)
folium.Marker([32.6599, -17.0097], tooltip="카보 지랑", icon=folium.Icon(color="green", icon="eye-open")).add_to(m_madeira)
folium.Marker([32.7483, -16.9537], tooltip="피코 아레이로", icon=folium.Icon(color="purple", icon="tag")).add_to(m_madeira)
folium_static(m_madeira)

st.markdown("---")

st.header("✈️ 여행 팁")
st.markdown("""
* **언어:** 포르투갈어 (주요 관광지에서는 영어가 잘 통합니다.)
* **통화:** 유로 (EUR)
* **교통:** 도시간 이동은 기차나 버스를 이용하고, 도시 내에서는 대중교통(트램, 지하철, 버스)을 이용하는 것이 편리해요. 렌터카는 알가르베 지역이나 근교 여행에 좋습니다.
* **음식:** **해산물 요리**, 바칼라우(대구 요리), **에그타르트(Pastel de Nata)**, 포트 와인 등 다양한 미식을 즐겨보세요.
* **날씨:** 연중 온화한 기후를 보이지만, 여름에는 덥고 겨울에는 비가 올 수 있으니 여행 시기에 맞춰 옷을 준비하세요.
* **아줄레주(Azulejo):** 포르투갈을 대표하는 아름다운 타일 예술입니다. 건물 외벽이나 실내 장식에서 쉽게 찾아볼 수 있습니다.
""")

st.success("포르투갈 여행 계획에 이 가이드가 도움이 되기를 바랍니다! 즐거운 여행 되세요! 🇵🇹")
