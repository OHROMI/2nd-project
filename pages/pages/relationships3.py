import streamlit as st
import networkx as nx
import matplotlib.pyplot as plt

# Streamlit 기본 설정
st.set_page_config(page_title="학생 관계 맵", layout="wide")
st.title("중학교 학생 관계 시각화")

# 학생 목록
students = [str(i) for i in range(1, 30)]

# 설문 입력
st.header("친구 선택 설문")
responses = {}

for student in students:
    with st.expander(f"학생 {student}의 응답"):
        q1 = st.multiselect(
            "1. 수련회에서 함께 방을 쓰고 싶은 친구 3명 선택",
            options=[s for s in students if s != student],
            key=f"q1_{student}",
            max_selections=3
        )
        q2 = st.selectbox(
            "2. 교실에서 짝이 되고 싶은 친구 1명 선택",
            options=[s for s in students if s != student],
            key=f"q2_{student}"
        )
        q3 = st.multiselect(
            "3. 최근 3일간 대화를 나눈 친구들 모두 선택",
            options=[s for s in students if s != student],
            key=f"q3_{student}"
        )

        responses[student] = {"q1": q1, "q2": q2, "q3": q3}

# 관계 맵 생성
if st.button("관계 맵 그리기"):
    G = nx.Graph()

    # 노드 추가
    G.add_nodes_from(students)

    # 엣지 추가 (친밀도에 따라 가중치 설정)
    for student, answers in responses.items():
        for friend in answers["q1"]:
            G.add_edge(student, friend, weight=2)

        G.add_edge(student, answers["q2"], weight=3)

        for friend in answers["q3"]:
            if not G.has_edge(student, friend):
                G.add_edge(student, friend, weight=1)

    # 그래프 시각화
    pos = nx.spring_layout(G, seed=42)
    plt.figure(figsize=(12, 8))

    weights = nx.get_edge_attributes(G, 'weight')
    edge_colors = [weights[edge] for edge in G.edges()]
    color_map = {1: 'gray', 2: 'blue', 3: 'red'}

    nx.draw(G, pos, with_labels=True, node_color='skyblue', node_size=700,
            width=[weight for weight in edge_colors],
            edge_color=[color_map[weight] for weight in edge_colors],
            font_size=10)

    st.pyplot(plt)
