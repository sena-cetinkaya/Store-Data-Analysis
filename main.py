# Import the libraries.
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Read the dataset.
data = pd.read_excel("Vrinda_Store_Data_Analysis.xlsx")

# Display the first few rows of the data.
print(data.head)

# Learning columns.
print(data.columns)

# Data types of columns.
print(data.dtypes)

# Learning the size of the dataset.
print(data.shape)

# Check for missing values.
print(data.isnull().sum())

# Summary statistics.
print(data.describe)

# DATA VISUALIZATION

# Ratio of number of men and women with pie chart
men_women = data["Gender"].value_counts()
men_women.plot.pie(figsize=(4, 4), title="Men Vs. Women", ylabel="", autopct="%.0f%%")
plt.show()

# Pie chart by order status
order_status = data.groupby("Status")["Status"].value_counts().head(2)
order_status.plot.pie(figsize=(4, 4), title="Order Status",explode=(0,0.2), ylabel = "", autopct="%.0f%%")
plt.show()

# top sales" bar chart according to "ship-state" data
top_sales = data["ship-state"].value_counts()
top_sales_filter = top_sales[top_sales > 2000]
top_sales_filter.plot.barh(figsize=(15, 8), title="Top Sales")
plt.show()

# Countplot chart according to "Age Group" and "Gender" data
sns.countplot(x = "Age Group", hue = 'Gender',data = data)
sns.set(rc={'figure.figsize':(8,8)})
plt.title("Orders:Age Vs Gender")
plt.show()

# Pie chart by Channels
channel = data.groupby("Channel ")["Channel "].value_counts()
channel_filter = channel.drop({"Ajio","Flipkart"}).head(2)
channel_filter.plot.pie(figsize=(4, 4), title="Orders: Channels", ylabel = "", autopct="%.0f%%")
plt.show()

# Combine graphics
plt.subplot(2, 3, 1)
men_women = data["Gender"].value_counts()
men_women.plot.pie(title="Men vs. Women", ylabel="" ,autopct="%.0f%%")

plt.subplot(2, 3, 2)
order_status = data.groupby("Status")["Status"].value_counts().head(2)
order_status.plot.pie(title="Order Status",explode=(0,0.2), ylabel = "", autopct="%.0f%%")

plt.subplot(2, 3, 3)
channel = data.groupby("Channel ")["Channel "].value_counts()
channel_filter = channel.drop({"Ajio","Flipkart"}).head(2)
channel_filter.plot.pie(title="Orders: Channels", ylabel = "", autopct="%.0f%%")

plt.subplot(2, 3, 4)
sns.countplot(x = "Age Group", hue = 'Gender',data = data)
#sns.set(rc={'figure.figsize':(10,10)})
plt.title("Orders:Age Vs Gender")

plt.subplot(2, 3, 6)
top_sales = data["ship-state"].value_counts()
top_sales_filter = top_sales[top_sales > 2000]
top_sales_filter.plot.barh()

plt.suptitle("REPORT")
plt.show()

