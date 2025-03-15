import streamlit as st
import numpy as np
import pandas as pd
from PIL import Image

st.title('Streamlit 超入門')

st.write('Interactive Widgets')

# 条件によって表示を変える
# チェックボックス
# if st.checkbox('Show Image'):
#     img = Image.open('sample.png')
#     st.image(img, caption='sample', use_container_width=True)

# セレクトボックス
# option = st.selectbox(
#     'あなたが好きな数字を教えてください。',
#     list(range(1, 11))
# )

# 'あなたの好きな数字は', option, 'です。'


# テキスト入力
text = st.text_input('あなたの趣味を教えてください。')

'あなたの趣味：', text

# スライダー
condition = st.slider('あなたの今の調子は？', 0, 100, 50)
'コンディション：', condition
