import streamlit as st

st.title('📝OSS HW2 퀴즈')

# 객관식 문제
st.subheader('객관식 1번')
    
p1 = st.radio('정보융합학부는 어느 단과대학소속 인가요?', ['답을 고르시오.', '1. 전자정보공과대학', '2. 공과대학', '3. 인공지능융합대학', '4. 자연과학대학학'])

if p1 != '답을 고르시오.':
    if p1 == '3. 인공지능융합대학':
        st.success("✅정답입니다!")
        st.balloons()
    else:
        st.error("❌오답입니다.")
else:
    st.info("아직 보기에서 선택하지 않았습니다.")

st.divider()

# 주관식 문제
st.subheader('주관식 1번')

p2 = st.text_input('오픈소스소프트웨어 담당교수님의 이름을 쓰시오.')
if p2 !="":
    if p2 == "박규동":
        st.success("✅정답입니다!")
        st.balloons()
    else:
        st.error("❌오답입니다.")
else:
    st.info("아직 답을 작성하지 않았습니다.")
