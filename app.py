
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
FEATURE_DIR = RESULTS_DIR / "feature_importance"

# ============================================================
# DATA LOADING FUNCTIONS
# ============================================================

@st.cache_data
def load_csv(file_path):
    if not file_path.exists():
        return pd.DataFrame()

    return pd.read_csv(file_path)


@st.cache_data
def load_data():
    file_path = RESULTS_DIR / "final_trading_analysis.csv"

    if not file_path.exists():
        return pd.DataFrame()

    data = pd.read_csv(file_path)

    if "Date" not in data.columns:
        return pd.DataFrame()

    data["Date"] = pd.to_datetime(
        data["Date"], errors="coerce"
    )

    data = data.dropna(subset=["Date"]).copy()
    data = data.sort_values("Date").reset_index(drop=True)

    if "Close" in data.columns:
        data["Close"] = pd.to_numeric(
            data["Close"], errors="coerce"
        )

    return data


data = load_data()

comparison = load_csv(
    RESULTS_DIR / "model_comparison.csv"
)

best_models = load_csv(
    RESULTS_DIR / "best_model_summary.csv"
)

feature_importance = load_csv(
    FEATURE_DIR / "xgboost_feature_importance_all_patterns.csv"
)

# ============================================================
# CHECK DATA AVAILABILITY
# ============================================================

st.title("📈 AI-ML Automated Candlestick Pattern Recognition")
st.subheader("Market Trend Analysis and Trading System")

st.markdown(
    """
    This dashboard presents candlestick pattern detection, market
    trend analysis, trend reversal identification, machine learning
    model comparison, feature importance, and rule-based
    Buy/Sell/Hold trading signals.
    """
)

st.divider()

if data.empty:
    st.error(
        "Trading dataset is unavailable or contains no valid dates. "
        "Run Steps 10 and 11 before starting the dashboard."
    )
    st.stop()

# ============================================================
# SIDEBAR — DATE FILTER
# ============================================================

st.sidebar.title("Dashboard Controls")

min_date = data["Date"].min().date()
max_date = data["Date"].max().date()

selected_dates = st.sidebar.date_input(
    "Select Date Range",
    value=(min_date, max_date),
    min_value=min_date,
    max_value=max_date
)

if isinstance(selected_dates, (tuple, list)):
    if len(selected_dates) == 2:
        start_date = pd.Timestamp(selected_dates[0])
        end_date = pd.Timestamp(selected_dates[1])
    elif len(selected_dates) == 1:
        start_date = pd.Timestamp(selected_dates[0])
        end_date = start_date
    else:
        start_date = pd.Timestamp(min_date)
        end_date = pd.Timestamp(max_date)
else:
    start_date = pd.Timestamp(selected_dates)
    end_date = start_date

filtered_data = data[
    (data["Date"] >= start_date)
    & (data["Date"] < end_date + pd.Timedelta(days=1))
].copy()

if filtered_data.empty:
    st.warning("No data available for the selected date range.")
    st.stop()

latest = filtered_data.iloc[-1]

# ============================================================
# CURRENT MARKET STATUS
# ============================================================

st.header("📊 Current Market Status")

col1, col2, col3, col4, col5 = st.columns(5)

with col1:
    close_value = latest.get("Close", None)
    st.metric(
        "Close Price",
        f"{close_value:.2f}"
        if pd.notna(close_value) else "N/A"
    )

with col2:
    st.metric("Market Trend", str(latest.get("Trend", "N/A")))

with col3:
    st.metric("HTF Bias", str(latest.get("HTF_Bias", "N/A")))

with col4:
    st.metric(
        "Trading Signal",
        str(latest.get("Trading_Signal", "N/A"))
    )

with col5:
    st.metric(
        "Trend Reversal",
        str(latest.get("Trend_Reversal", "N/A"))
    )

st.caption(
    "The displayed status is the latest record within the selected date range."
)

st.divider()

# ============================================================
# PRICE CHART WITH BUY / SELL SIGNALS
# ============================================================

st.header("📈 Price Movement and Trading Signals")

if "Close" in filtered_data.columns:

    chart_data = filtered_data.dropna(subset=["Close"])

    fig, ax = plt.subplots(figsize=(14, 6))

    ax.plot(
        chart_data["Date"],
        chart_data["Close"],
        label="Close Price",
        linewidth=1.3
    )

    if "Trading_Signal" in chart_data.columns:

        buy_data = chart_data[
            chart_data["Trading_Signal"] == "BUY"
        ]

        sell_data = chart_data[
            chart_data["Trading_Signal"] == "SELL"
        ]

        if not buy_data.empty:
            ax.scatter(
                buy_data["Date"],
                buy_data["Close"],
                marker="^",
                s=65,
                label="BUY"
            )

        if not sell_data.empty:
            ax.scatter(
                sell_data["Date"],
                sell_data["Close"],
                marker="v",
                s=65,
                label="SELL"
            )

    ax.set_xlabel("Date")
    ax.set_ylabel("Close Price")
    ax.set_title("Price Chart with Trading Signals")
    ax.legend()
    ax.grid(alpha=0.3)

    fig.autofmt_xdate()
    fig.tight_layout()

    st.pyplot(fig)
    plt.close(fig)

# ============================================================
# MARKET TREND AND SIGNAL DISTRIBUTIONS
# ============================================================

st.header("📊 Market and Trading Signal Analysis")

col1, col2 = st.columns(2)

with col1:
    if "Trend" in filtered_data.columns:

        trend_counts = (
            filtered_data["Trend"]
            .fillna("Unknown")
            .value_counts()
        )

        fig, ax = plt.subplots(figsize=(7, 5))
        trend_counts.plot(kind="bar", ax=ax)

        ax.set_title("Market Trend Distribution")
        ax.set_xlabel("Trend")
        ax.set_ylabel("Number of Records")
        ax.tick_params(axis="x", rotation=0)

        fig.tight_layout()
        st.pyplot(fig)
        plt.close(fig)

with col2:
    if "Trading_Signal" in filtered_data.columns:

        signal_counts = (
            filtered_data["Trading_Signal"]
            .value_counts()
            .reindex(["BUY", "SELL", "HOLD"], fill_value=0)
        )

        fig, ax = plt.subplots(figsize=(7, 5))
        signal_counts.plot(kind="bar", ax=ax)

        ax.set_title("Trading Signal Distribution")
        ax.set_xlabel("Signal")
        ax.set_ylabel("Number of Records")
        ax.tick_params(axis="x", rotation=0)

        fig.tight_layout()
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
    pattern for pattern in pattern_columns
    if pattern in filtered_data.columns
]

if available_patterns:

    for pattern in available_patterns:
        filtered_data[pattern] = pd.to_numeric(
            filtered_data[pattern], errors="coerce"
        )

    pattern_counts = (
        filtered_data[available_patterns]
        .sum()
        .sort_values(ascending=False)
    )

    fig, ax = plt.subplots(figsize=(12, 6))
    pattern_counts.plot(kind="bar", ax=ax)

    ax.set_title("Candlestick Pattern Distribution")
    ax.set_xlabel("Candlestick Pattern")
    ax.set_ylabel("Number of Occurrences")
    ax.tick_params(axis="x", rotation=45)

    fig.tight_layout()
    st.pyplot(fig)
    plt.close(fig)

    st.subheader("Latest Detected Candlestick Patterns")

    latest_patterns = [
        pattern
        for pattern in available_patterns
        if latest.get(pattern, 0) == 1
    ]

    if latest_patterns:
        st.success(
            "Detected Pattern(s): " + ", ".join(latest_patterns)
        )
    else:
        st.info(
            "No candlestick pattern detected in the latest record."
        )

else:
    st.info("Candlestick pattern columns are unavailable.")

# ============================================================
# TREND REVERSAL ANALYSIS
# ============================================================

st.header("🔄 Trend Reversal Analysis")

if "Trend_Reversal" in filtered_data.columns:

    reversal_counts = (
        filtered_data["Trend_Reversal"]
        .fillna("None")
        .value_counts()
    )

    fig, ax = plt.subplots(figsize=(9, 5))
    reversal_counts.plot(kind="bar", ax=ax)

    ax.set_title("Trend Reversal Distribution")
    ax.set_xlabel("Trend Reversal")
    ax.set_ylabel("Number of Records")
    ax.tick_params(axis="x", rotation=30)

    fig.tight_layout()
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
    col for col in market_columns
    if col in filtered_data.columns
]

if available_market_columns:
    st.dataframe(
        filtered_data[available_market_columns].tail(20),
        use_container_width=True,
        hide_index=True
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
    col for col in signal_columns
    if col in filtered_data.columns
]

if available_signal_columns:
    st.dataframe(
        filtered_data[available_signal_columns].tail(20),
        use_container_width=True,
        hide_index=True
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

    metric_columns = [
        "Accuracy",
        "Precision",
        "Recall",
        "F1_Score"
    ]

    available_metrics = [
        col for col in metric_columns
        if col in comparison.columns
    ]

    if "Model" in comparison.columns and available_metrics:

        selected_metric = st.selectbox(
            "Select Performance Metric",
            available_metrics,
            index=(
                available_metrics.index("F1_Score")
                if "F1_Score" in available_metrics
                else 0
            )
        )

        chart_data = comparison[["Model", selected_metric]].copy()
        chart_data[selected_metric] = pd.to_numeric(
            chart_data[selected_metric], errors="coerce"
        )
        chart_data = chart_data.dropna()

        if not chart_data.empty:
            st.bar_chart(
                chart_data.set_index("Model")
            )

else:
    st.info(
        "Model comparison file is unavailable. Run Step 9.1 first."
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
        "Best model summary is unavailable. Run Step 9.2 first."
    )

# ============================================================
# XGBOOST FEATURE IMPORTANCE
# ============================================================

st.header("🌳 XGBoost Feature Importance")

if not feature_importance.empty:

    st.dataframe(
        feature_importance,
        use_container_width=True,
        hide_index=True
    )

    if {"Feature", "Importance", "Pattern"}.issubset(
        feature_importance.columns
    ):

        available_importance_patterns = sorted(
            feature_importance["Pattern"].dropna().unique()
        )

        selected_pattern = st.selectbox(
            "Select Pattern for Feature Importance",
            available_importance_patterns
        )

        selected_importance = feature_importance[
            feature_importance["Pattern"] == selected_pattern
        ].sort_values("Importance", ascending=True)

        fig, ax = plt.subplots(figsize=(10, 6))

        ax.barh(
            selected_importance["Feature"],
            selected_importance["Importance"]
        )

        ax.set_title(
            f"XGBoost Feature Importance - {selected_pattern}"
        )
        ax.set_xlabel("Feature Importance")
        ax.set_ylabel("Feature")

        fig.tight_layout()
        st.pyplot(fig)
        plt.close(fig)

else:
    st.info(
        "XGBoost feature importance is unavailable. "
        "Run Step 9.4 first."
    )

# ============================================================
# DISPLAY SAVED STEP 9.4 GRAPHS
# ============================================================

st.subheader("Saved Feature Importance Graphs")

if FEATURE_DIR.exists():

    graph_files = sorted(
        FEATURE_DIR.glob("xgboost_*_feature_importance.png")
    )

    if graph_files:

        selected_graph = st.selectbox(
            "Choose a saved feature importance graph",
            graph_files,
            format_func=lambda path: path.name
        )

        st.image(
            str(selected_graph),
            caption=selected_graph.name,
            use_container_width=True
        )

    else:
        st.info(
            "No saved XGBoost feature importance graphs found. "
            "Run Step 9.4 to generate them."
        )

else:
    st.info("Feature importance output folder is unavailable.")

# ============================================================
# DOWNLOAD TRADING ANALYSIS
# ============================================================

st.header("⬇️ Export Trading Analysis")

csv_data = filtered_data.to_csv(index=False).encode("utf-8")

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
