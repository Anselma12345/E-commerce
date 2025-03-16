import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load dataset
customers_dataset_df = pd.read_csv("customers_dataset.csv")
order_items_dataset_df = pd.read_csv("order_items_dataset.csv")

# Title of the Dashboard
st.title("Dashboard Analisis E-Commerce")

# Sidebar untuk interaktivitas
st.sidebar.header("Filter Data")

# Filter: Jumlah kota yang ditampilkan
num_cities = st.sidebar.slider("Jumlah Kota Teratas:", min_value=5, max_value=20, value=10, step=1)

# Visualization 1: Kota dengan Pelanggan Terbanyak
st.subheader(f"{num_cities} Kota dengan Pelanggan Terbanyak")
customer_city_counts = customers_dataset_df['customer_city'].value_counts().head(num_cities)
fig, ax = plt.subplots(figsize=(12, 6))
sns.barplot(x=customer_city_counts.index, y=customer_city_counts.values, palette="viridis", ax=ax)
plt.xticks(rotation=45)
plt.xlabel("Kota")
plt.ylabel("Jumlah Pelanggan")
plt.title(f"{num_cities} Kota dengan Pelanggan Terbanyak")
st.pyplot(fig)

# Filter: Rentang harga produk
min_price, max_price = st.sidebar.slider(
    "Pilih Rentang Harga Produk:",
    float(order_items_dataset_df['price'].min()),
    float(order_items_dataset_df['price'].max()),
    (float(order_items_dataset_df['price'].min()), float(order_items_dataset_df['price'].quantile(0.99)))
)

# Filter dataset berdasarkan harga
filtered_df = order_items_dataset_df[(order_items_dataset_df['price'] >= min_price) & (order_items_dataset_df['price'] <= max_price)]

# Visualization 2: Distribusi Harga Produk setelah Filtering
st.subheader("Distribusi Harga Produk (Setelah Filtering)")
fig, ax = plt.subplots(figsize=(10, 5))
sns.histplot(filtered_df['price'], bins=50, kde=True, color="blue", ax=ax)
plt.title("Distribusi Harga Produk")
plt.xlabel("Harga Produk")
plt.ylabel("Frekuensi")
st.pyplot(fig)

st.write(f"Menampilkan data produk dengan harga antara **{min_price:.2f}** dan **{max_price:.2f}**")
