import streamlit as st

def playgame()

st.title("동전 던지기 게임")
st.divider()

st.image("assets/coin_head.png")
st.image("assets/coin_tail.png")

st.header('동전 던지기 게임에 오신 것을 환영합니다.')
st.subheader('앞면일까요? 뒷면일까요?')

st.button('앞면')
st.button('뒷면')

if st.button('앞면'):
  playgame(0)
if st.button('뒷면'):
 playgame(1)
