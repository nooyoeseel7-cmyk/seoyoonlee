import streamlit as st

st.set_page_config(page_title="Vibe Welcome", page_icon="✨")
name = st.text_input("당신의 닉네임을 입력해 주세요!", placeholder="예: 코딩장인")
if name:
    st.success(f"🔥 반갑습니다, {name}님! 오늘 당신의 바이브에 딱 맞는 메뉴를 제안해 드릴게요.")
    pick = st.radio("지금 당장 당기는 맛은?", ["스트레스 풀리는 매운맛", "깔끔한 담백함", "달달한 디저트"])
    st.write(f"👉 **{name}**님을 위한 추천: " + {"매운맛": "마라탕 3단계", "담백함": "연어 포케", "디저트": "탕후루"}.get(pick[-3:], "맛있는 한 끼"))
