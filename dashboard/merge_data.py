import pandas as pd

# Step 1: Membaca data dari file CSV
order_items_df = pd.read_csv('C:/Users/User/Documents/Submission/data/order_items_dataset.csv')
orders_df = pd.read_csv('C:/Users/User/Documents/Submission/data/orders_dataset.csv')
product_df = pd.read_csv('C:/Users/User/Documents/Submission/data/products_dataset.csv')
order_payment_df = pd.read_csv('C:/Users/User/Documents/Submission/data/order_payments_dataset.csv')
reviews_df = pd.read_csv('C:/Users/User/Documents/Submission/data/order_reviews_dataset.csv')

# Step 2: Menggabungkan DataFrame
merged_df = (
    order_items_df
    .merge(orders_df, on='order_id', how='inner')
    .merge(order_payment_df, on='order_id', how='inner')
    .merge(reviews_df, on='order_id', how='inner')
    .merge(product_df, on='product_id', how='inner')
)

# Step 3: Menyimpan hasil ke main_data.csv
merged_df.to_csv('C:/Users/User/Documents/Submission/dashboard/main_data.csv', index=False)

print("Data telah digabungkan dan disimpan sebagai main_data.csv")
