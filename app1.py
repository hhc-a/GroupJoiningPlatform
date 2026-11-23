import streamlit as st
from datetime import datetime, date, time

st.set_page_config(page_title="附近揪團", page_icon="🍲")
st.title("附近揪團｜第 2 步：建立活動（暫存版）")

if "activities" not in st.session_state:
    st.session_state.activities = [
    ]

with st.form("new_activity"):
    name = st.text_input("活動名稱")
    kind = st.selectbox("類別", ["美食", "桌遊", "運動", "其他"])
    selected_date = st.date_input("選擇日期",value=date.today())
    selected_time = st.time_input("選擇時間",value=datetime.now().time(), step=900)
    host = st.text_input("主揪暱稱")
    capacity = st.number_input("名額（含主揪）", min_value=2, max_value=30, value=5)
    submitted = st.form_submit_button("建立活動")

if submitted:
    if name.strip() and host.strip():
        st.session_state.activities.append({"name": name.strip(), "kind": kind, "date": selected_date, "time": selected_time , "host": host.strip(), "joined": 1, "capacity": int(capacity)})
        st.success("已加入這次執行中的活動清單。")
    else:
        st.warning("請填活動名稱和主揪暱稱。")

st.subheader("活動清單")
for activity in st.session_state.activities:
    with st.container(border=True):
        st.write(f"### {activity['name']}")
        st.write(f"{activity['kind']}｜{activity['date']}｜{activity['time']}｜主揪：{activity['host']}")
        st.write(f"名額：{activity['joined']} / {activity['capacity']}")
