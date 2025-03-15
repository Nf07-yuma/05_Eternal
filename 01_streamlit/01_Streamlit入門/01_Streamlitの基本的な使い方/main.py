import streamlit as st
import numpy as np
import pandas as pd
from PIL import Image

st.title('Streamlit 超入門')

# st.write('DataFrame')

# テーブル
# df = pd.DataFrame({
#     # '1列目': [1, 2, 3, 4],
#     # '2列目': [10, 20, 30, 40],
# })

# st.write(df)
# 動的なテーブルを作成できる
# st.dataframe(df)
# st.dataframe(df, width=100, height=100)
# st.dataframe(df.style.highlight_max(axis=0), width=100, height=100)
# st.dataframe(df.style.highlight_max(axis=0))
# 静的なテーブルを作成できる
# st.table(df.style.highlight_max(axis=0))

# グラフ
# df = pd.DataFrame(
#     np.random.rand(20, 3),
#     columns=['a', 'b', 'c']
# )

# 折れ線グラフ
# st.line_chart(df)
# エリアチャート
# st.area_chart(df)
# 棒グラフ
# st.bar_chart(df)

# マップ
# 東京(新宿)付近のランダムな座標を生成
# df = pd.DataFrame(
#     np.random.rand(100, 2)/ [50, 50] + [35.69, 139.70],
#     columns=['lat', 'lon']
# )
# 地図  
# st.map(df)


st.write('Display Image')

# 画像
img = Image.open('sample.png')

# The use_column_width parameter has been deprecated and will be removed in a future release. Please utilize the use_container_width parameter instead.
# st.image(img, caption='sample', use_column_width=True)
st.image(img, caption='sample', use_container_width=True)

# マジックコマンド
# """
# # 章
# ## 節
# ### 項

# ```python
# import streamlit as st
# import numpy as np
# import pandas as pd
# ```

# """


