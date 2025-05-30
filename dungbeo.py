import streamlit as st
import pandas as pd

# Title of the app
st.title("📊 Interactive Excel Data Viewer - TABLE-T12-2024")

# Load Excel file
@st.cache_data
def load_data():
    # Let pandas use its default engine, which avoids openpyxl
    df = pd.read_excel("TABLE-T12-2024.xlsx")
    return df

df = load_data()

# Show raw data
if st.checkbox("Show full raw data"):
    st.dataframe(df, use_container_width=True)

# Column filter
st.subheader("🔍 Filter by Column")

column = st.selectbox("Select a column to filter by", df.columns)

if pd.api.types.is_numeric_dtype(df[column]):
    # Numeric filter
    min_val, max_val = st.slider(
        f"Select range for {column}",
        float(df[column].min()),
        float(df[column].max()),
        (float(df[column].min()), float(df[column].max()))
    )
    filtered_df = df[(df[column] >= min_val) & (df[column] <= max_val)]
else:
    # Categorical/text filter
    unique_vals = df[column].dropna().unique()
    selected_val = st.selectbox(f"Select value from {column}", unique_vals)
    filtered_df = df[df[column] == selected_val]

# Display filtered results
st.subheader("📄 Filtered Results")
st.dataframe(filtered_df, use_container_width=True)

# Download button for filtered data
csv_data = filtered_df.to_csv(index=False).encode('utf-8')
st.download_button(
    label="⬇️ Download filtered data as CSV",
    data=csv_data,
    file_name='filtered_data.csv',
    mime='text/csv'
)








 