import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load dataset
customers_dataset_df = pd.read_csv("customers_dataset.csv")
order_items_dataset_df = pd.read_csv("order_items_dataset.csv")

# Title of the Dashboard
st.title("Dashboard Analisis E-Commerce")

# Visualization 1: 10 Kota dengan Pelanggan Terbanyak
st.subheader("10 Kota dengan Pelanggan Terbanyak")
customer_city_counts = customers_dataset_df['customer_city'].value_counts().head(10)
fig, ax = plt.subplots(figsize=(12, 6))
sns.barplot(x=customer_city_counts.index, y=customer_city_counts.values, palette="viridis", ax=ax)
plt.xticks(rotation=45)
plt.xlabel("Kota")
plt.ylabel("Jumlah Pelanggan")
plt.title("10 Kota dengan Pelanggan Terbanyak")
st.pyplot(fig)

# Visualization 2: Distribusi Harga Produk
st.subheader("Distribusi Harga Produk")
fig, ax = plt.subplots(figsize=(10, 5))
sns.histplot(order_items_dataset_df['price'], bins=50, kde=True, color="blue", ax=ax)
plt.title("Distribusi Harga Produk")
plt.xlabel("Harga Produk")
plt.ylabel("Frekuensi")
plt.xlim(0, order_items_dataset_df['price'].quantile(0.99))  # Hindari outlier ekstrem
st.pyplot(fig)

