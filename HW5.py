# %%
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns
from matplotlib.ticker import MultipleLocator

# %%
#1
df = pd.read_csv(r"D:\william\OneDrive - UW-Madison\UW-Madison\718\5\SOCR-HeightWeight.csv")
#1-1
df.drop(columns=['Index'], inplace=True)
df.plot.scatter(x='Height(Inches)', y='Weight(Pounds)')
plt.legend()
plt.title('Matplotllib Scatter Plot')
plt.xlabel('Height (Inches)')
plt.ylabel('Weight (Pounds)')
plt.savefig(r"1-1.png")
#1-2
sns.scatterplot(data=df, x='Height(Inches)', y='Weight(Pounds)')
plt.title('Seaborn Scatter Plot')
plt.xlabel('Height (Inches)')
plt.ylabel('Weight (Pounds)')
plt.savefig(r"1-2.png")

# %%
#2
fig, ax = plt.subplots(1,2)
ax[0].hist(df['Height(Inches)'],  edgecolor='black')
ax[0].set_title('Matplotlib Histogram- Height')
ax[0].set_xlabel('Height (Inches)')
ax[0].set_ylabel('Frequency')
ax[1].hist(df['Weight(Pounds)'],  edgecolor='black')
ax[1].set_title('Matplotlib Histogram- Weight')
ax[1].set_xlabel('Weight (Pounds)')
fig.suptitle("Matplotlib Histograms")
plt.tight_layout()
plt.savefig(r"2-1.png")
#2-2
sns.histplot(df['Height(Inches)'],  ax=ax[0])
ax[0].set_title('Seaborn Histogram- Height')
ax[0].set_xlabel('Height (Inches)')
ax[0].set_ylabel('Frequency')
sns.histplot(df['Weight(Pounds)'],  ax=ax[1])
ax[1].set_title('Seaborn Histogram- Weight')
ax[1].set_xlabel('Weight (Pounds)')
ax[1].set_ylabel('')
fig.suptitle("Seaborn Histograms")
plt.tight_layout()
plt.savefig(r"2-2.png")





# %%
sd1 = df['Height(Inches)'].std()
sd2 = df['Weight(Pounds)'].std()
diff = sd1 - sd2
(sd1, sd2, diff)

# %%
#3
fig, ax = plt.subplots(figsize=(8, 4.5))
sns.scatterplot(data=df, x='Height(Inches)', y='Weight(Pounds)',s=5, ax=ax, color='k')
sns.regplot(data=df, x='Height(Inches)', y='Weight(Pounds)', ax=ax,line_kws={"linewidth": 2}, scatter=False, color='b', ci=95)
ax.set_xlabel("Height (Inches)")
ax.set_ylabel("Weight (Pounds)")
ax.set_title("Height vs. Weight with Linear Fit")
ax.grid(color='gray', alpha=.3, linestyle='--')
ax.set_facecolor("whitesmoke")
ax.xaxis.set_major_locator(MultipleLocator(5))
ax.yaxis.set_major_locator(MultipleLocator(25))
plt.tight_layout()
plt.show()
plt.savefig(r"3.png")

# %%
#4
df = pd.read_csv(r"D:\william\OneDrive - UW-Madison\UW-Madison\718\5\company_sales_data.csv")
#4-1
sns.barplot(data=df, x='month_number', y='total_profit')
plt.title('Total Profit by Month')
plt.tight_layout()
plt.xlabel('Month Number')
plt.ylabel('Total Profit')
plt.savefig(r"4-1.png")
#4-2
fig, ax = plt.subplots(2, 3, figsize=(15, 8))
sns.barplot(data=df, x='month_number', y='facecream', ax=ax[0,0])
ax[0,0].set_title('Face Cream Sales by Month')
ax[0,0].set_xlabel('')
ax[0,0].set_ylabel('Units Sold')
sns.barplot(data=df, x='month_number', y='facewash', ax=ax[0,1])
ax[0,1].set_title('Face Wash Sales by Month')
ax[0,1].set_xlabel('')
ax[0,1].set_ylabel('')
sns.barplot(data=df, x='month_number', y='toothpaste', ax=ax[0,2])
ax[0,2].set_title('Toothpaste Sales by Month')
ax[0,2].set_xlabel('')
ax[0,2].set_ylabel('')
sns.barplot(data=df, x='month_number', y='bathingsoap', ax=ax[1,0])
ax[1,0].set_title('Bathing Soap Sales by Month')
ax[1,0].set_xlabel('')
ax[1,0].set_ylabel('Units Sold')
sns.barplot(data=df, x='month_number', y='shampoo', ax=ax[1,1])
ax[1,1].set_title('Shampoo Sales by Month')
ax[1,1].set_xlabel('Month Number')
ax[1,1].set_ylabel('')
sns.barplot(data=df, x='month_number', y='moisturizer', ax=ax[1,2])
ax[1,2].set_title('Moisturizer Sales by Month')
ax[1,2].set_xlabel('')
ax[1,2].set_ylabel('')
fig.suptitle("Sales by Month for Each Products")
plt.tight_layout()
plt.savefig(r"4-2.png")
#4-3
fig, ax = plt.subplots(figsize=(10, 6))
sns.scatterplot(data=df, x='facewash', y='facecream', color='b', ax=ax)
sns.regplot(data=df, x='facewash', y='facecream', ax=ax, scatter=False, color='r', line_kws={"linewidth": 2}, ci=95)
ax.set_title('Face Wash vs. Face Cream Sales')
ax.set_xlabel('Face Wash Sales')
ax.set_ylabel('Face Cream Sales')
ax.grid(color='gray', alpha=.3, linestyle='--')
ax.set_facecolor("whitesmoke")
plt.tight_layout()
plt.savefig(r"4-3.png")



# %%
#5
df = pd.read_csv(r"D:\william\OneDrive - UW-Madison\UW-Madison\718\5\crop_production.csv")
#5-1
df_rice = df[df["SUBJECT"] == "RICE"].copy()
df_rice_grouped = df_rice.groupby("TIME")["Value"].sum().reset_index()
sns.barplot(data=df_rice_grouped, x='TIME', y='Value')
plt.title('Total Rice Production Over Years')
plt.xlabel('Year')
plt.ylabel('Production (in tons)')
plt.xticks(rotation=45)
plt.tight_layout()
ax = plt.gca()
ax.xaxis.set_major_locator(MultipleLocator(5))  
plt.savefig(r"5-1.png")
#5-2
df_wheat = df[df["SUBJECT"] == "WHEAT"].copy()
df_wheat_grouped = df_wheat.groupby("LOCATION")["Value"].sum().reset_index()
fig, ax = plt.subplots(figsize=(10, 6))
sns.barplot(data=df_wheat_grouped, x='LOCATION', y='Value', ax=ax)
plt.title('Total Wheat Production by Location Since 1990')
plt.xlabel('Location')
plt.ylabel('Production (in tons)')
plt.xticks(rotation=60)
plt.tight_layout()
plt.savefig(r"5-2.png")



# %%



