import numpy as np
import pandas as pd

# Function to generate random data
def generate_random_data(n_samples=600):
    np.random.seed(42)     # For reproducibility

    # Random inputs
    advertising_budget = np.random.uniform(50, 150, n_samples)  # 50-150 thousands
    customers_visited = np.random.randint(100, 501, n_samples)  # 100-500 customers
    discount_percentage = np.random.uniform(10, 35, n_samples)  # 10-35%
    store_size = np.random.uniform(500, 2000, n_samples)  # 500-2000 sq.ft
    employee_count = np.random.randint(5, 21, n_samples)  # 5-20 employees
    product_variety = np.random.randint(50, 201, n_samples)  # 50-200 products
    weekend_sales_days = np.random.randint(4, 9, n_samples)  # 4-8 days
    competitor_distance = np.random.uniform(1, 10, n_samples)  # 1-10 km
    customer_rating = np.random.uniform(1, 5, n_samples)  # 1-5 rating

    # Sales (linear combination of inputs + noise)
    sales = (0.2 * advertising_budget) + (0.05 * customers_visited) + (0.1 * discount_percentage) + \
            (0.01 * store_size) + (0.3 * employee_count) + (0.02 * product_variety) + \
            (1.5 * weekend_sales_days) + (-0.5 * competitor_distance) + (2.0 * customer_rating) + \
            np.random.normal(0, 5, n_samples) + 20  # Base 20 + noise ±5

    # Create DataFrame
    df = pd.DataFrame({
        'Advertising_Budget': advertising_budget,
        'Customers_Visited': customers_visited,
        'Discount_Percentage': discount_percentage,
        'Store_Size': store_size,
        'Employee_Count': employee_count,
        'Product_Variety': product_variety,
        'Weekend_Sales_Days': weekend_sales_days,
        'Competitor_Distance': competitor_distance,
        'Customer_Rating': customer_rating,
        'Sales': sales
    })
    return df


# Generate data
data = generate_random_data()

data.to_csv('store_sales_data.csv',index=False)
print("Data generated Successfully!!","Data saved to'Store_sales_data.csv",sep="\n")

