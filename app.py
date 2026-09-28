import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
from pathlib import Path


# ============================================================
# PAGE CONFIGURATION
# ============================================================

st.set_page_config(
    page_title="AI-ML Candlestick Trading System",
    page_icon="📈",
    layout="wide"
)


# ============================================================
# PROJECT PATHS
# ============================================================

BASE_DIR = Path(__file__).resolve().parent
RESULTS_DIR = BASE_DIR / "results"


# ============================================================
# LOAD DATA
# ============================================================

@st.cache_data
def load_data():

    file_path = RESULTS_DIR / "final_trading_analysis.csv"

    if not file_path.exists():
        st.error(
            f"File not found:\n{file_path}"
        )
        st.stop()

    data = pd.read_csv(file_path)

    if "Date" in data.columns:
        data["Date"] = pd.to_datetime(data["Date"])

    return data


@st.cache_data
def load_model_comparison():

    file_path = RESULTS_DIR / "model_comparison.csv"

    if not file_path.exists():
        return pd.DataFrame()

    return pd.read_csv(file_path)


@st.cache_data
def load_best_models():

    file_path = RESULTS_DIR / "best_model_summary.csv"

    if not file_path.exists():
        return pd.DataFrame()

    return pd.read_csv(file_path)


@st.cache_data
def load_feature_importance():

    file_path = RESULTS_DIR / "random_forest_feature_importance.csv"

    if not file_path.exists():
        return pd.DataFrame()

    return pd.read_csv(file_path)


# ============================================================
# LOAD ALL DATA
# ============================================================

data = load_data()
comparison = load_model_comparison()
best_models = load_best_models()
feature_importance = load_feature_importance()


# ============================================================
# TITLE
# ============================================================

st.title("📈 AI-ML Automated Candlestick Pattern Recognition")
st.subheader("Market Trend Analysis and Trading System")

st.markdown(
    """
    This dashboard presents candlestick pattern detection, market trend
    analysis, trend reversal identification, machine learning model
    comparison, and Buy/Sell/Hold trading signals.
    """
)

st.divider()


# ============================================================
# SIDEBAR
# ============================================================

st.sidebar.title("Dashboard Controls")

# Date filter
if "Date" in data.columns:

    min_date = data["Date"].min().date()
    max_date = data["Date"].max().date()

    selected_dates = st.sidebar.date_input(
        "Select Date Range",
        value=(min_date, max_date),
        min_value=min_date,
        max_value=max_date
    )

    if isinstance(selected_dates, tuple) and len(selected_dates) == 2:

        start_date = pd.Timestamp(selected_dates[0])
        end_date = pd.Timestamp(selected_dates[1])

        filtered_data = data[
            (data["Date"] >= start_date)
            &
            (data["Date"] <= end_date)
        ].copy()

    else:

        filtered_data = data.copy()

else:

    filtered_data = data.copy()


# ============================================================
# BASIC CHECK
# ============================================================

if filtered_data.empty:

    st.warning("No data available for the selected date range.")

    st.stop()


# ============================================================
# LATEST MARKET DATA
# ============================================================

latest = filtered_data.iloc[-1]


# ============================================================
# KPI SECTION
# ============================================================

st.header("📊 Current Market Status")

col1, col2, col3, col4, col5 = st.columns(5)


# Close Price
with col1:

    if "Close" in latest.index:

        st.metric(
            "Close Price",
            f"{latest['Close']:.2f}"
        )

    else:

        st.metric(
            "Close Price",
            "N/A"
        )


# Trend
with col2:

    trend = latest.get(
        "Trend",
        "N/A"
    )

    st.metric(
        "Market Trend",
        trend
    )


# HTF Bias
with col3:

    htf_bias = latest.get(
        "HTF_Bias",
        "N/A"
    )

    st.metric(
        "HTF Bias",
        htf_bias
    )


# Trading Signal
with col4:

    signal = latest.get(
        "Trading_Signal",
        "N/A"
    )

    st.metric(
        "Trading Signal",
        signal
    )


# Trend Reversal
with col5:

    reversal = latest.get(
        "Trend_Reversal",
        "N/A"
    )

    st.metric(
        "Trend Reversal",
        reversal
    )


st.divider()


# ============================================================
# PRICE CHART
# ============================================================

st.header("📈 Price Movement and Trading Signals")

if "Date" in filtered_data.columns and "Close" in filtered_data.columns:

    fig, ax = plt.subplots(figsize=(14, 6))

    ax.plot(
        filtered_data["Date"],
        filtered_data["Close"],
        label="Close Price"
    )

    # BUY signals
    if "Trading_Signal" in filtered_data.columns:

        buy_data = filtered_data[
            filtered_data["Trading_Signal"] == "BUY"
        ]

        if not buy_data.empty:

            ax.scatter(
                buy_data["Date"],
                buy_data["Close"],
                marker="^",
                s=70,
                label="BUY"
            )

        # SELL signals
        sell_data = filtered_data[
            filtered_data["Trading_Signal"] == "SELL"
        ]

        if not sell_data.empty:

            ax.scatter(
                sell_data["Date"],
                sell_data["Close"],
                marker="v",
                s=70,
                label="SELL"
            )

    ax.set_xlabel("Date")
    ax.set_ylabel("Close Price")
    ax.set_title("Price Chart with Trading Signals")
    ax.legend()
    ax.grid(alpha=0.3)

    plt.xticks(rotation=45)

    st.pyplot(fig)

    plt.close(fig)


# ============================================================
# TREND AND SIGNAL DISTRIBUTION
# ============================================================

st.header("📊 Market and Trading Signal Analysis")

col1, col2 = st.columns(2)


# Market Trend Distribution
with col1:

    if "Trend" in filtered_data.columns:

        trend_counts = filtered_data[
            "Trend"
        ].value_counts()

        fig, ax = plt.subplots(figsize=(7, 5))

        trend_counts.plot(
            kind="bar",
            ax=ax
        )

        ax.set_title("Market Trend Distribution")
        ax.set_xlabel("Trend")
        ax.set_ylabel("Number of Records")

        plt.xticks(rotation=0)

        st.pyplot(fig)

        plt.close(fig)


# Trading Signal Distribution
with col2:

    if "Trading_Signal" in filtered_data.columns:

        signal_counts = filtered_data[
            "Trading_Signal"
        ].value_counts()

        fig, ax = plt.subplots(figsize=(7, 5))

        signal_counts.plot(
            kind="bar",
            ax=ax
        )

        ax.set_title("Trading Signal Distribution")
        ax.set_xlabel("Signal")
        ax.set_ylabel("Number of Records")

        plt.xticks(rotation=0)

        st.pyplot(fig)

        plt.close(fig)


# ============================================================
# CANDLESTICK PATTERN ANALYSIS
# ============================================================

st.header("🕯️ Candlestick Pattern Analysis")

pattern_columns = [
    "Hammer",
    "Inverted_Hammer",
    "Doji",
    "Bullish_Engulfing",
    "Bearish_Engulfing",
    "Shooting_Star",
    "Morning_Star",
    "Evening_Star"
]

available_patterns = [
    pattern
    for pattern in pattern_columns
    if pattern in filtered_data.columns
]


if available_patterns:

    pattern_counts = filtered_data[
        available_patterns
    ].sum()

    fig, ax = plt.subplots(figsize=(12, 6))

    pattern_counts.plot(
        kind="bar",
        ax=ax
    )

    ax.set_title(
        "Candlestick Pattern Distribution"
    )

    ax.set_xlabel(
        "Candlestick Pattern"
    )

    ax.set_ylabel(
        "Number of Occurrences"
    )

    plt.xticks(rotation=45)

    st.pyplot(fig)

    plt.close(fig)


# ============================================================
# LATEST DETECTED PATTERNS
# ============================================================

st.subheader("Latest Detected Candlestick Patterns")

latest_patterns = []

for pattern in available_patterns:

    if latest[pattern] == 1:

        latest_patterns.append(pattern)


if latest_patterns:

    st.success(
        "Detected Pattern(s): "
        + ", ".join(latest_patterns)
    )

else:

    st.info(
        "No candlestick pattern detected in the latest record."
    )


# ============================================================
# TREND REVERSAL ANALYSIS
# ============================================================

st.header("🔄 Trend Reversal Analysis")

if "Trend_Reversal" in filtered_data.columns:

    reversal_counts = filtered_data[
        "Trend_Reversal"
    ].value_counts()

    fig, ax = plt.subplots(figsize=(9, 5))

    reversal_counts.plot(
        kind="bar",
        ax=ax
    )

    ax.set_title(
        "Trend Reversal Distribution"
    )

    ax.set_xlabel(
        "Trend Reversal"
    )

    ax.set_ylabel(
        "Number of Records"
    )

    plt.xticks(rotation=30)

    st.pyplot(fig)

    plt.close(fig)


# ============================================================
# MARKET STRUCTURE TABLE
# ============================================================

st.header("📋 Market Structure")

market_columns = [
    "Date",
    "Close",
    "Trend",
    "Market_Control",
    "HTF_Bias",
    "Trend_Reversal",
    "Reversal_Confirmed"
]

available_market_columns = [
    column
    for column in market_columns
    if column in filtered_data.columns
]

if available_market_columns:

    st.dataframe(
        filtered_data[
            available_market_columns
        ].tail(20),
        use_container_width=True
    )


# ============================================================
# RECENT TRADING SIGNALS
# ============================================================

st.header("💹 Recent Trading Signals")

signal_columns = [
    "Date",
    "Close",
    "Trend",
    "HTF_Bias",
    "Trend_Reversal",
    "Trading_Signal",
    "Signal_Reason"
]

available_signal_columns = [
    column
    for column in signal_columns
    if column in filtered_data.columns
]

if available_signal_columns:

    st.dataframe(
        filtered_data[
            available_signal_columns
        ].tail(20),
        use_container_width=True
    )


# ============================================================
# MACHINE LEARNING MODEL COMPARISON
# ============================================================

st.header("🤖 Machine Learning Model Comparison")

if not comparison.empty:

    st.dataframe(
        comparison,
        use_container_width=True,
        hide_index=True
    )

    # Select numeric metric
    metric_columns = [
        "Accuracy",
        "Precision",
        "Recall",
        "F1_Score"
    ]

    available_metrics = [
        column
        for column in metric_columns
        if column in comparison.columns
    ]

    if available_metrics:

        selected_metric = st.selectbox(
            "Select Performance Metric",
            available_metrics,
            index=available_metrics.index("F1_Score")
            if "F1_Score" in available_metrics
            else 0
        )

        chart_data = comparison[
            ["Model", selected_metric]
        ].set_index("Model")

        st.bar_chart(chart_data)


else:

    st.info(
        "Model comparison file is not available."
    )


# ============================================================
# BEST MODEL SUMMARY
# ============================================================

st.header("🏆 Model Performance Summary")

if not best_models.empty:

    st.dataframe(
        best_models,
        use_container_width=True,
        hide_index=True
    )

else:

    st.info(
        "Best model summary is not available."
    )


# ============================================================
# FEATURE IMPORTANCE
# ============================================================

st.header("🌳 Random Forest Feature Importance")

if not feature_importance.empty:

    st.dataframe(
        feature_importance,
        use_container_width=True,
        hide_index=True
    )

    if (
        "Feature" in feature_importance.columns
        and "Importance" in feature_importance.columns
    ):

        importance_chart = feature_importance[
            ["Feature", "Importance"]
        ].set_index("Feature")

        st.bar_chart(
            importance_chart
        )

else:

    st.info(
        "Feature importance file is not available."
    )


# ============================================================
# DOWNLOAD FINAL DATASET
# ============================================================

st.header("⬇️ Export Trading Analysis")

csv_data = filtered_data.to_csv(
    index=False
).encode("utf-8")

st.download_button(
    label="Download Trading Analysis CSV",
    data=csv_data,
    file_name="trading_analysis.csv",
    mime="text/csv"
)


# ============================================================
# FOOTER
# ============================================================

st.divider()

st.caption(
    "AI-ML Automated Candlestick Pattern Recognition "
    "with Market Trend Analysis and Trading System"
)

st.caption(
    "Streamlit Dashboard | Historical Market Data Analysis"
)