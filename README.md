# 🛒 Walmart Weekly Sales Forecasting

This project is part of a time series forecasting challenge using the Walmart dataset. The objective is to forecast weekly sales for **Department 3** using a variety of models ranging from statistical techniques to advanced deep learning and machine learning methods.

---

## 📦 Dataset

- Cleaned Walmart dataset with multiple departments
- Filtered to use only **Department 3**
- Target: `Weekly_Sales`
- Features: `Temperature`, `IsHoliday`, `Date`, etc.

---

## 🔧 Project Workflow

### 1. Data Preparation
- Filtered for `Dept == 3`
- Handled dates and set time index
- Visualized weekly sales and moving averages

### 2. Time Series Analysis
- Identified trend and seasonality
- Analyzed ACF and PACF
- Evaluated external regressors (e.g., temperature, holidays)

### 3. Classical Time Series Models
- **Holt’s Linear Trend**
- **Holt-Winters Seasonal Method**
- **ARIMA**, **SARIMA**, **SARIMAX**

### 4. Machine Learning Regressors
- Feature engineering with lags, time components
- Trained:
  - Random Forest
  - XGBoost

### 5. Deep Learning Models
- ANN (Feedforward)
- LSTM (Sequential Memory Model)

### 6. Facebook Prophet
- Trended and seasonal forecasts
- Component-based interpretation

### 7. Innovative Model
- Implemented **N-BEATS** using the Darts library

---

## 🧪 Evaluation Metrics

| Model           | RMSE      | MAE       | MAPE    |
|----------------|-----------|-----------|---------|
| Holt           | 21953.99  | 19526.56  | 156.18% |
| Holt-Winters   | 9821.14   | 5804.87   | 21.20%  |
| ARIMA          | 12157.13  | 6707.45   | 23.88%  |
| SARIMA         | 9707.89   | 5719.02   | 21.03%  |
| SARIMAX        | 9716.27   | 5605.42   | 20.70%  |
| Random Forest  | 6170.51   | 4158.73   | 15.77%  |
| **XGBoost**    | **2373.46** | **1673.63** | **8.27%** |
| ANN            | 11196.41  | 7999.86   | 36.31%  |
| LSTM           | 11710.75  | 7301.32   | 29.92%  |
| Prophet        | 5984.16   | 4059.01   | 17.21%  |

✅ **Best Performing Model:** **XGBoost**

---

## 🚀 Deployment

- Deployed the XGBoost model using **Streamlit**
- Simple interactive interface allows:
  - Inputting lag features, temperature, holiday, date
  - Viewing weekly sales predictions

### Run Locally:
```bash
streamlit run app.py
