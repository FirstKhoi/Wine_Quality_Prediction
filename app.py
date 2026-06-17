import streamlit as st
import pandas as pd
import numpy as np
import joblib

# 1. Cấu hình giao diện ứng dụng
st.set_page_config(page_title="Wine Quality Predictor", page_icon="🍷", layout="centered")

st.title("🍷 Hệ Thống Dự Đoán Chất Lượng Rượu Vang")
st.write("Ứng dụng Machine Learning (XGBoost + SMOTE) để đánh giá chất lượng rượu dựa trên các chỉ số hóa học.")
st.markdown("---")

# 2. Tải mô hình đã đóng gói về
@st.cache_resource # Dòng này giúp Streamlit lưu cấu hình mô hình vào bộ nhớ đệm, không bị load lại mỗi lần click
def load_model():
    return joblib.load('./Wine_Quality_Prediction/wine_model_pipeline.pkl')

try:
    model = load_model()
except Exception as e:
    st.error("Không tìm thấy file 'wine_model_pipeline.pkl'. Hãy đảm bảo bạn đã chạy bước lưu mô hình trong Notebook!")
    st.stop()

# 3. Tạo các thanh trượt (Sliders) để người dùng nhập thông tin
st.subheader("📊 Nhập các chỉ số hóa học của mẫu rượu:")

col1, col2 = st.columns(2)

with col1:
    wine_type = st.selectbox("Loại rượu (type)", options=["Vang Trắng (White)", "Vang Đỏ (Red)"])
    fixed_acidity = st.slider("Axit cố định (fixed acidity)", 3.8, 15.9, 7.0, step=0.1)
    volatile_acidity = st.slider("Axit bay hơi (volatile acidity)", 0.08, 1.58, 0.3, step=0.01)
    citric_acid = st.slider("Axit citric (citric acid)", 0.0, 1.66, 0.3, step=0.01)
    residual_sugar = st.slider("Lượng đường dư (residual sugar)", 0.6, 65.8, 5.0, step=0.1)
    chlorides = st.slider("Lượng muối (chlorides)", 0.009, 0.611, 0.05, step=0.001)

with col2:
    free_sulfur_dioxide = st.slider("SO2 tự do (free sulfur dioxide)", 1.0, 289.0, 30.0, step=1.0)
    pH = st.slider("Độ pH", 2.72, 4.01, 3.2, step=0.01)
    sulphates = st.slider("Chất Sulphates", 0.22, 2.0, 0.5, step=0.01)
    alcohol = st.slider("Nồng độ cồn (alcohol %)", 8.0, 14.9, 10.5, step=0.1)

# Chuyển đổi lựa chọn loại rượu về lại số 0/1 giống như lúc train model
type_numeric = 1 if "White" in wine_type else 0

# 4. Gom dữ liệu người dùng nhập thành một DataFrame chuẩn cấu trúc
# Lưu ý: Sắp xếp đúng thứ tự các cột như tập x_train ban đầu (đã bỏ density và total SO2)
input_data = pd.DataFrame([{
    'type': type_numeric,
    'fixed acidity': fixed_acidity,
    'volatile acidity': volatile_acidity,
    'citric acid': citric_acid,
    'residual sugar': residual_sugar,
    'chlorides': chlorides,
    'free sulfur dioxide': free_sulfur_dioxide,
    'pH': pH,
    'sulphates': sulphates,
    'alcohol': alcohol
}])

st.markdown("---")

# 5. Nút bấm kích hoạt AI dự đoán
if st.button("🔮 Kiểm Tra Chất Lượng Rượu", use_container_width=True):
    # Luồng dữ liệu tự chui vào pipeline: tự điền median nếu thiếu, tự đoán
    prediction = model.predict(input_data)
    prediction_proba = model.predict_proba(input_data)[0][1] # Lấy xác suất đạt điểm cao
    
    # Hiển thị kết quả đẹp mắt ra màn hình
    if prediction[0] == 1:
        st.success(f"🎉 **KẾT QUẢ: RƯỢU NGON (PREMIUM)!** (Độ tin cậy: {prediction_proba:.2%})")
        st.balloons() # Hiệu ứng bóng bay chúc mừng cho sinh động
    else:
        st.warning(f"📉 **KẾT QUẢ: RƯỢU THƯỜNG / CHƯA ĐẠT CHUẨN.** (Xác suất ngon chỉ có: {prediction_proba:.2%})")