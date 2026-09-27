import pandas as pd

customer_data = pd.read_csv(
    r"C:\Users\haris\OneDrive\Desktop\ecommerce-data-engineeering\data\customers.csv"
)

products_data = pd.read_csv(
    r"C:\Users\haris\OneDrive\Desktop\ecommerce-data-engineeering\data\products.csv"
)

payments_data = pd.read_csv(
    r"C:\Users\haris\OneDrive\Desktop\ecommerce-data-engineeering\data\payments.csv"
)

orders_data = pd.read_csv(
    r"C:\Users\haris\OneDrive\Desktop\ecommerce-data-engineeering\data\orders.csv"
)


def inspect_data(df, name):

    print("\n" + "=" * 50)
    print(name)
    print("=" * 50)

    print("Shape:")
    print(df.shape)

    print("\nData Types:")
    print(df.dtypes)

    print("\nMissing Values:")
    print(df.isnull().sum())

    print("\nDuplicate Rows:")
    print(df.duplicated().sum())


inspect_data(customer_data, "CUSTOMERS")
inspect_data(products_data, "PRODUCTS")
inspect_data(orders_data, "ORDERS")
inspect_data(payments_data, "PAYMENTS")