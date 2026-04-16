import streamlit as st
import pandas as pd

st.title("📊 Food Vibe Analysis")
st.subheader("오늘 선택한 메뉴의 '행복 지수' 분석")
# 간단한 차트 데이터 생성 (맛, 영양, 행복도)
chart_data = pd.DataFrame({"Category": ["맛", "영양", "행복도"], "Score": [95, 70, 100]})
st.bar_chart(chart_data.set_index("Category"))
st.info("💡 Tip: 행복도가 100점입니다! 고민하지 말고 지금 당장 드세요.")
