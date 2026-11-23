import streamlit as st

st.set_page_config(page_title="附近揪團", page_icon="🍲")
st.title("附近揪團｜第 1 步：顯示活動")
st.write("先讓網頁顯示資料，還沒有連上雲端資料庫。")

activities = [
    {"name": "下課一起吃飯", "kind": "美食", "date": "週五 18:30", "host": "小安", "seats": "2 / 5"     ,"place":"思源樓221"},
    {"name": "週末桌遊新手團", "kind": "桌遊", "date": "週六 14:00", "host": "阿哲", "seats": "4 / 6"     ,"place":"鳥居咖啡館"},
    {"name": "周末與球團", "kind": "運動", "date": "週日 14:00", "host": "凌晨", "seats": "1 / 4"     ,"place":"六仰羽球館"},
    {"name": "週日電影團", "kind": "電影", "date": "週日 10:00", "host": "白紙", "seats": "1 / 4"     ,"place":"中港新光影城"},
]

for activity in activities:
    with st.container(border=True):
        st.subheader(activity["name"])
        st.write(f"類別：{activity['kind']}　時間：{activity['date']}")
        st.write(f"主揪：{activity['host']}　報名：{activity['seats']}")
        st.write(f"地點：{activity['place']}")
