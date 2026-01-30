import pandas as pd #install pandas(used to work with tables (dataframes))
import numpy as np #used for numerical operations (not heavily used here but commonly included)
import matplotlib.pyplot as plt #used to create charts/graphs
import os #used to work with folders and file paths

df = pd.read_csv("sales_data.csv") #Reads the file sales_data.csv Stores it in a dataframe called df

# Clean column names
df.columns = df.columns.str.strip().str.lower() #Removes extra spaces in column names Converts all column names to lowercase

print("Columns:", df.columns.tolist()) #Prints all column names as a list so you can verify them
df.rename(columns={ #Renames columns
    'orderid': 'order_id',
    'customer': 'customer_id',
    'prize': 'price'
}, inplace=True)
df['sales'] = df['quantity'] * df['price'] #Creates a new column sales Formula: Sales = Quantity × Price
print("Total Sales:", df['sales'].sum()) #Adds all sales values → gives total revenue
print("Average Order Value:", df['sales'].mean()) #Finds average sales per row/order
print("Total Orders:", df['order_id'].nunique()) #Counts unique order IDs
print("Unique Customers:", df['customer_id'].nunique()) #Counts different customers
top_products = df.groupby('product')['sales'].sum().sort_values(ascending=False) #Group data by product Add total sales for each product Sort from highest to lowest
print(top_products.head()) #Shows Top 5 selling products
city_sales = df.groupby('city')['sales'].sum().sort_values(ascending=False)#Groups by city Calculates total sales in each city Sorts highest to lowest
print(city_sales)#Displays sales performance city-wise
os.makedirs("output", exist_ok=True)#Creates a folder named output exist_ok=True prevents error if folder already exists

# Top products chart
top_products.head(5).plot(kind='bar') #Creates bar chart Adds title & Y-axis label Saves image as top_products.png Closes the plot"""
plt.title("Top 5 Products by Sales")
plt.ylabel("Sales")
plt.tight_layout()
plt.savefig("output/top_products.png")
plt.close()

# City sales chart 
city_sales.plot(kind='bar') #Bar chart for sales by city Saved as city_sales.png
plt.title("Sales by City")
plt.ylabel("Sales")
plt.tight_layout()
plt.savefig("output/city_sales.png")
plt.close()
summary = pd.DataFrame({   # Creates a new table with one row Contains key business metrics
    "Total Sales": [df['sales'].sum()], 
    "Total Orders": [df['order_id'].nunique()],
    "Unique Customers": [df['customer_id'].nunique()], 
    "Average Order Value": [df['sales'].mean()]
})

summary.to_excel("output/sales_summary.xlsx", index=False) #Saves summary as an Excel file index=False removes row numbers column
print("Report saved!") #Confirms everything is completed


