import streamlit as st
import numpy as np
import pandas as pd
from PIL import Image

st.title('Streamlit 超入門')

st.write('Interactive Widgets')

# サイドバー
# st.sidebar.write('Interactive Widgets')
# text = st.sidebar.text_input('あなたの趣味を教えてください。')
# condition = st.sidebar.slider('あなたの今の調子は？', 0, 100, 50)

# 'あなたの趣味：', text
# 'コンディション：', condition


# 2カラムレイアウト
left_column, right_column = st.columns(2)

button = left_column.button('右カラムに文字を表示')
if button:
    right_column.write('ここは右カラムです')

# expander
# AttributeError: module 'streamlit' has no attribute 'beta_expander'
# expander = st.beta_expander('問い合わせ')
expander1 = st.expander('問い合わせ1')
expander1.write('問い合わせ1の内容を書く')
expander2 = st.expander('問い合わせ2')
expander2.write('問い合わせ2の内容を書く')
expander3 = st.expander('問い合わせ3')
expander3.write('問い合わせ3の内容を書く')

# 授業メモ
# 同様の名前のものを選択し、Ctrl + D で一括選択し、一括変更、削除ができる