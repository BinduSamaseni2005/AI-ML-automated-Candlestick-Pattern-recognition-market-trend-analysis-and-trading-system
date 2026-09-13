# AI/ML Automated Candlestick Pattern Recognition, Market Trend Analysis and Trading System

## Project Overview

This project focuses on:

- Candlestick Pattern Recognition
- Market Structure Analysis
- Trend Analysis
- Trend Reversal Identification
- Machine Learning Prediction
- Buy/Sell Signal Generation

---

## Project Flow

Stock Data
↓
OHLCV Dataset
↓
Data Preprocessing
↓
Feature Engineering
↓
Market Structure Analysis
↓
Trend Analysis
↓
Trend Reversal Identification
↓
Candlestick Pattern Recognition
↓
ML Dataset Preparation
↓
Machine Learning Models
↓
Model Evaluation
↓
Buy/Sell Recommendations
↓
Dashboard

---

## Completed Modules

### Step 1: Data Collection and Understanding

Implemented:

- Yahoo Finance Data Collection
- OHLCV Dataset Generation
- Dataset Exploration
- Statistical Analysis
- Data Inspection

Output:
- `nse_ohlcv_raw.csv`

---

### Step 2: Data Preprocessing

Implemented:

- Missing Value Handling
- Duplicate Removal
- Date Conversion
- Sorting and Cleaning
- Dataset Validation

Output:
- `nse_ohlcv_clean.csv`

---

### Step 3: Feature Engineering

Implemented:

- Candle Body
- Candle Range
- Upper Wick
- Lower Wick
- Body Ratio
- Upper Wick Ratio
- Lower Wick Ratio

Output:
- `candlestick_features.csv`

---

### Step 4: Market Structure & Trend Analysis

Implemented:

- Pivot High Detection
- Pivot Low Detection
- Higher High (HH)
- Higher Low (HL)
- Lower High (LH)
- Lower Low (LL)
- Trend Classification
- Market Control Detection
- Higher Timeframe Bias (HTF Bias)
- Market Structure Visualization

Output:
- `market_structure_analysis.csv`

---

### Step 5: Candlestick Pattern Recognition

Implemented:

- Hammer
- Inverted Hammer
- Doji
- Bullish Engulfing
- Bearish Engulfing
- Shooting Star
- Morning Star
- Evening Star

Output:
- `candlestick_pattern_dataset.csv`

---

### Step 6: Trend Reversal Identification

Implemented:

- Bullish Reversal Detection
- Bearish Reversal Detection
- Bullish Breakout Detection
- Bearish Breakdown Detection
- Previous Trend Tracking
- Reversal Confirmation using Candlestick Patterns

Output:
- `trend_reversal_dataset.csv`

---

### Step 7: Multi-Pattern ML Dataset Preparation

Implemented:

- Current Candle Features
- Previous Candle Features
- Previous Two Candle Features
- Multi-Pattern Label Creation
- Feature Selection
- ML Dataset Generation
- Dataset Formatting and Export

Target Patterns:

- Hammer
- Inverted Hammer
- Doji
- Bullish Engulfing
- Bearish Engulfing
- Shooting Star
- Morning Star
- Evening Star

Output:
- `multi_pattern_ml_dataset.csv`

---

## Upcoming Modules

### Step 8: Machine Learning Model Development

Planned:

- Random Forest
- XGBoost
- Logistic Regression
- Pattern Classification Models
- Trend Prediction Models

---

### Step 9: Model Evaluation

Planned:

- Accuracy
- Precision
- Recall
- F1 Score
- Confusion Matrix
- Feature Importance Analysis

---

### Step 10: Trading Signal Generation

Planned:

- Buy Signal Detection
- Sell Signal Detection
- Confidence Score Calculation
- Risk Management Rules

---

### Step 11: Visualization Dashboard

Planned:

- Market Structure Dashboard
- Trend Dashboard
- Pattern Dashboard
- Signal Dashboard
- Interactive Charts

---

### Step 12: Automated Trading System (Future Scope)

Planned:

- Real-Time Data Integration
- Live Pattern Detection
- Automated Trade Execution
- Portfolio Monitoring
- Performance Analytics

---

## Technologies Used

- Python
- Pandas
- NumPy
- Matplotlib
- Scikit-Learn
- Yahoo Finance API (yfinance)

---

## Current Status

Completed:
- Data Collection
- Data Preprocessing
- Feature Engineering
- Market Structure Analysis
- Trend Analysis
- Trend Reversal Identification
- Candlestick Pattern Recognition
- Multi-Pattern ML Dataset Preparation

Next Step:
- Machine Learning Model Development
