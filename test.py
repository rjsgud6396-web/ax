import streamlit as st
    
    # 제목
    
st.title("📘 Streamlit 문서 작성 예제")
    
    # 섹션
    
st.header("1. 기본 텍스트 출력")
    
    # 표 출력
    
st.header("2. 표 출력")
import pandas as pd
df = pd.DataFrame({
"이름": ["홍길동", "이몽룡"],
"나이": [29, 34]
})
st.dataframe(df)