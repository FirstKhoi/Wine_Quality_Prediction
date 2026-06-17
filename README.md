# 🍷 Wine Quality Prediction System

A machine learning-based web application that predicts wine quality using advanced algorithms (XGBoost + SMOTE) based on chemical properties.

[winequalitypredictionbykhoi.streamlit.app](https://winequalitypredictionbykhoi.streamlit.app/)

## 📋 Overview

This project implements a intelligent system to assess the quality of wine by analyzing chemical indicators. The application uses a trained machine learning model to classify wines as premium quality or standard grade based on chemical composition features.

## ✨ Features

- **🎯 Accurate Predictions**: Uses XGBoost algorithm with SMOTE for balanced classification
- **🌐 Web Interface**: User-friendly Streamlit interface for real-time predictions
- **📊 Multiple Features**: Analyzes 10 chemical indicators of wine quality
- **⚡ Fast Processing**: Cached model loading for quick response times
- **🔮 Confidence Scores**: Displays prediction confidence percentages
- **🎨 Interactive UI**: Intuitive sliders for easy feature input

## 🔬 Model Features

The prediction model analyzes the following wine chemical properties:

| Feature | Description | Unit |
|---------|-------------|------|
| Type | Red or White wine | Categorical |
| Fixed Acidity | Concentration of fixed acids | g/dm³ |
| Volatile Acidity | Concentration of volatile acids | g/dm³ |
| Citric Acid | Citric acid concentration | g/dm³ |
| Residual Sugar | Remaining sugar after fermentation | g/dm³ |
| Chlorides | Salt concentration | g/dm³ |
| Free Sulfur Dioxide | Unbound SO₂ | mg/dm³ |
| pH | Acidity level (0-14 scale) | pH |
| Sulphates | Potassium sulphate concentration | g/dm³ |
| Alcohol | Alcohol content | % |

## 📦 Installation

### Prerequisites

- Python 3.7 or higher
- pip (Python package manager)

### Setup

1. **Clone the repository**
   ```bash
   git clone https://github.com/FirstKhoi/Wine_Quality_Prediction.git
   cd Wine_Quality_Prediction
   ```

2. **Create a virtual environment (optional but recommended)**
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

## 🚀 Usage

### Running the Application

Start the Streamlit web application:

```bash
streamlit run app.py
```

The application will open in your default browser at `http://localhost:8501`

### Making Predictions

1. **Select wine type**: Choose between Red or White wine
2. **Adjust chemical properties**: Use the sliders to input the chemical indicators
3. **Click the prediction button**: Press "🔮 Kiểm Tra Chất Lượng Rượu" to get the prediction
4. **View results**: The system displays the quality classification and confidence score

## 📦 Dependencies

The project uses the following Python libraries:

- **streamlit** (1.32.0) - Web application framework
- **pandas** - Data manipulation and analysis
- **numpy** - Numerical computing
- **scikit-learn** - Machine learning utilities
- **xgboost** - Gradient boosting algorithm
- **imbalanced-learn** - SMOTE for handling imbalanced data
- **joblib** - Model serialization and caching

See `requirements.txt` for the complete list.

## 🤖 Model Architecture

The project uses:

- **Algorithm**: XGBoost (eXtreme Gradient Boosting)
- **Data Handling**: SMOTE (Synthetic Minority Over-sampling Technique) for balanced dataset
- **Model Storage**: Serialized as `wine_model_pipeline.pkl`

## 📊 Dataset

The model is trained on wine quality data containing:
- Red and white wine samples
- Chemical composition features
- Quality ratings

## 🔧 Project Structure

```
Wine_Quality_Prediction/
├── app.py                          # Main Streamlit application
├── requirements.txt                # Python dependencies
├── wine_model_pipeline.pkl         # Trained ML model
└── README.md                       # This file
```

## 🎯 Prediction Output

The system provides:

- **Classification**: Premium Quality (Good Wine) or Standard Quality
- **Confidence Score**: Percentage confidence in the prediction
- **Visual Feedback**: Success/warning messages with emoji indicators

### Example Results:
- ✅ **Premium Quality**: "🎉 KẾT QUẢ: RƯỢU NGON (PREMIUM)! (Độ tin cậy: 85%)"
- ⚠️ **Standard Quality**: "📉 KẾT QUẢ: RƯỢU THƯỜNG / CHƯA ĐẠT CHUẨN. (Xác suất ngon chỉ có: 45%)"

## 🛠️ Troubleshooting

### Model File Not Found Error

If you see "Không tìm thấy file 'wine_model_pipeline.pkl'":

1. Ensure `wine_model_pipeline.pkl` exists in the project root directory
2. Verify the file path in `app.py` matches your setup
3. Check file permissions

### Port Already in Use

If port 8501 is already in use:

```bash
streamlit run app.py --server.port 8502
```

## 📝 Notes

- The application uses Vietnamese interface labels and messages
- The model requires exactly 10 chemical features for prediction
- Input sliders are pre-configured with realistic ranges based on wine dataset

## 🚧 Future Enhancements

Potential improvements:
- [ ] Add model performance metrics visualization
- [ ] Implement model retraining functionality
- [ ] Add data export/download feature
- [ ] Support for batch predictions
- [ ] Mobile-responsive design
- [ ] Database integration for prediction history

## 📄 License

This project is available for educational and research purposes.

## 👤 Author

FirstKhoi

## 🤝 Contributing

Contributions are welcome! Please feel free to:

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/amazing-feature`)
3. Commit your changes (`git commit -m 'Add amazing feature'`)
4. Push to the branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request

## ❓ Questions or Issues?

If you encounter any issues or have questions about the project, please open an issue on the GitHub repository.

---

**Made with ❤️ for wine enthusiasts and ML practitioners**
