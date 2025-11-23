import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

# ---------------------------
# PREMIUM UI SETTINGS
# ---------------------------
st.set_page_config(
    page_title="ETL Dashboard",
    page_icon="📊",
    layout="wide"
)

st.markdown("""
    <style>
        .main {
            background-color: #0F1220;
            color: white;
        }
        h1, h2, h3, h4 {
            color: #00E6A8;
        }
        .css-1n76uvr, .css-10trblm {
            color: white !important;
        }
    </style>
""", unsafe_allow_html=True)

# ---------------------------
# HEADER
# ---------------------------
st.markdown("<h1 style='text-align: center;'>📊 VIP ETL Analytics Dashboard</h1>", unsafe_allow_html=True)
st.write("### Luxury Visualization Panel | Powered by Streamlit")

# ---------------------------
# LOAD DATA
# ---------------------------
st.sidebar.header("📂 Upload Your CSV")
uploaded = st.sidebar.file_uploader("Choose TRANSFORMED DATA.csv", type="csv")

if uploaded:
    df = pd.read_csv(uploaded, encoding="latin1")
    st.success("✅ Data Loaded Successfully!")
else:
    st.warning("⚠ Please upload your CSV file to continue.")
    st.stop()

# ---------------------------
# DATA PREVIEW
# ---------------------------
st.write("## 📄 Dataset Preview")
st.dataframe(df, height=300)

# Clean numeric columns
df['Price'] = pd.to_numeric(df['Price'], errors='coerce')
df['Rating'] = pd.to_numeric(df['Rating'], errors='coerce')

# ---------------------------
# VISUAL 1 – PRICE DISTRIBUTION
# ---------------------------
st.write("## 1️⃣ Price Distribution per Category")

fig1, ax1 = plt.subplots(figsize=(10,5))
for cat, data in df.groupby('Category'):
    data['Price'].plot(kind='kde', label=cat, ax=ax1)

ax1.set_title("Price Distribution per Category")
ax1.set_xlabel("Price")
ax1.legend()

st.pyplot(fig1)


# ---------------------------
# VISUAL 2 – RATING vs PRICE
# ---------------------------
st.write("## 2️⃣ Rating vs Price Scatter Plot")

fig2, ax2 = plt.subplots(figsize=(7,5))
ax2.scatter(df['Price'], df['Rating'])
ax2.set_xlabel("Price")
ax2.set_ylabel("Rating")
ax2.set_title("Rating vs Price Correlation")

st.pyplot(fig2)


# ---------------------------
# VISUAL 3 – AVERAGE PRICE PER CATEGORY
# ---------------------------
st.write("## 3️⃣ Average Price per Category")

avg_price = df.groupby('Category')['Price'].mean()

fig3, ax3 = plt.subplots(figsize=(10,5))
avg_price.plot(kind='bar', ax=ax3, color='skyblue')

ax3.set_title("Average Price per Category")
ax3.set_ylabel("Average Price")
ax3.set_xlabel("Category")

st.pyplot(fig3)


# ---------------------------
# VISUAL 4 – BEST VALUE SCORE
# ---------------------------
st.write("## 4️⃣ Best Value Score per Category (Rating/Price)")

df['value_score'] = df['Rating'] / df['Price']
best_value = df.groupby('Category')['value_score'].mean().sort_values(ascending=False)

fig4, ax4 = plt.subplots(figsize=(8,5))
best_value.plot(kind='bar', ax=ax4, color='orange')

ax4.set_title("Best Value Score per Category")
ax4.set_ylabel("Value Score")
ax4.set_xlabel("Category")

st.pyplot(fig4)


# ---------------------------
# FOOTER
# ---------------------------
st.markdown("<br><hr><center>Made with ❤️ | Premium Streamlit ETL Dashboard</center>", unsafe_allow_html=True)
