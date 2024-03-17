import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("data.csv")
products = df["Product"].to_list()
product_name = input("Please enter the product's name: ")

if product_name in products:
    selected_data = df[df['Product'] == product_name]
    grouped_data = selected_data.groupby('Month').agg(
        {'Count': 'sum', 'Price': 'mean'})

    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(12, 6))

    ax1.bar(grouped_data.index, grouped_data['Count'], width=0.1)
    ax1.set_xlabel('Month')
    plt.xticks(range(1, 13))
    ax1.set_ylabel('Count')
    ax1.set_title('Count(sum)/Month for selected product')

    ax2.plot(grouped_data.index,
             grouped_data['Price'], marker='o', color='orange')
    ax2.set_xlabel('Month')
    plt.xticks(range(1, 13))
    ax2.set_ylabel('Price')
    ax2.set_title('Price(mean)/Month for selected product')

    plt.tight_layout()

    plt.show()
else:
    print("The product's name is not correct !!")
