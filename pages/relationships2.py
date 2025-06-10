import streamlit as st
import pandas as pd
import networkx as nx
from pyvis.network import Network
import streamlit.components.v1 as components
import tempfile
import os

st.set_page_config(page_title="학생 관계 시각화", layout="wide")

# ------------------ 초기 세팅 ------------------
NUM_STUDENTS = 29
student_ids = [str(i) for i in range(1, NUM_STUDENTS + 1)]
DATA_FILE = "student_relationships.csv"

# 데이터 초기화
def init_data():
    if not os.path.exists(DATA_FILE):
        df = pd.DataFrame(columns=["student", "q1", "q2", "q3"])
        df.to_csv(DATA_FILE, index=False)

# 데이터 저장
def save_response(student, q1, q2, q3):
    df = pd.read_csv(DATA_FILE)
    new_row = {
        "student": student,
        "q1": ",".join(q1),
        "q2": q2,
        "q3": ",".join(q3),
    }
    df = df[df["student"] != student]  # 중복 제출 방지
    df = pd.concat([df, pd.DataFrame([new_row])], ignore_index=True)
    df.to_csv(DATA_FILE, index=False)

# 친밀도 그래프 생성
def create_graph(df):
    G = nx.Graph()

    for sid in student_ids:
        G.add_node(sid)

    for _, row in df.iterrows():
        src = row["student"]
        q1_list = row["q1"].split(",") if row["q1"] else []
        q2 = row["q2"]
        q3_list = row["q3"].split(",") if row["q3"] else []

        for tgt in q1_list:
            if tgt and tgt != src:
                G.add_edge(src, tgt, weight=2, color="blue")

        if q2 and q2 != src:
            G.add_edge(src, q2, weight=3, color="red")

        for tgt in q3_list:
            if tgt and tgt != src:
                if G.has_edge(src, tgt):
                    G[src][tgt]["weight"] += 1
                else:
                    G.add_edge(src, tgt, weight=1, color="gray")

    return G

# 시각화 함수
def show_graph(G):
    net = Network(height="600px", width="100%", bgcolor="#ffffff", font_color="black")
    net.from_nx(G)

    for node in net.nodes:
        node["label"] = f"{node['id']}번"

    for edge in net.edges:
        w = edge["value"]
        edge["title"] = f"친밀도 {w}"
        edge["width"] = w

    with tempfile.NamedTemporaryFile(delete=False, suffix=".html") as f:
        net.save_graph(f.name)
        html_path = f.name

    components.html(open(html_path, "r", encoding="utf-8").read(), height=650)

# ------------------ 앱 시작 ------------------
st.title("🧭 중학생 친밀도 맵")

init_data()

tab1, tab2 = st.tabs(["👥 설문 참여", "📊 관계 시각화"])

with tab1:
    st.subheader("친구 관계 설문")
    selected_student = st.selectbox("당신의 번호를 선택하세요", student_ids)

    q1 = st.multiselect("수련회에서 함께 방을 사용하고 싶은 친구 3명을 선택하세요", options=[x for x in student_ids if x != selected_student], max_selections=3)
    q2 = st.selectbox("교실에서 짝이 되고 싶은 친구 1명을 선택하세요", options=[x for x in student_ids if x != selected_student])
    q3 = st.multiselect("최근 3일간 대화한 친구들을 모두 선택하세요", options=[x for x in student_ids if x != selected_student])

    if st.button("제출하기"):
        save_response(selected_student, q1, q2, q3)
        st.success("응답이 저장되었습니다!")

with tab2:
    st.subheader("학생들 간의 관계 시각화")
    df = pd.read_csv(DATA_FILE)
    if df.empty:
        st.info("아직 제출된 설문이 없습니다.")
    else:
        G = create_graph(df)
        show_graph(G)
