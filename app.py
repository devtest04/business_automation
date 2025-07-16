import streamlit as st
import pandas as pd

# 🧾 Page Setup
st.set_page_config(page_title="📊 Business Daily Report Viewer", layout="wide")

# 🧠 Title
st.title("📊 Business Daily Report Viewer")

# 📂 Load Excel File
file_path = "master_report.xlsx"

try:
    df = pd.read_excel(file_path)

    # 📊 Show full table
    st.subheader("📋 Daily Master Report")
    st.dataframe(df, use_container_width=True)

    # 📅 Filter by DATE
    if "DATE" in df.columns:
        dates = df['DATE'].dropna().unique()
        selected_date = st.selectbox("📅 Filter by Date", options=dates)

        if selected_date:
            filtered_df = df[df['DATE'] == selected_date]
            st.success(f"Showing data for: {selected_date}")
            st.dataframe(filtered_df, use_container_width=True)

except FileNotFoundError:
    st.warning("⚠️ File 'master_report.xlsx' not found.")
except Exception as e:
    st.error(f"❌ Error: {e}")
