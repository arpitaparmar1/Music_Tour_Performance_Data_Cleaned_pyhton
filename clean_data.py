import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

df=pd.read_csv("F:/python/numpy/Music_Tour_Performance_Data_Cleaned/messy_data.csv")


df.columns=[col.replace('\xa0',' ').strip()for col in df.columns]

def remove_bracket(val):
    if pd.isna(val):
        return val
    val=str(val)
    return val.split('[')[0].strip()

def clean_numeric_string(val):
    if pd.isna(val):
        return np.nan
    val=str(val)
    val=val.split('[')[0].replace('$','').replace(',','').strip()
    return val if val not in['','-'] else np.nan
    

df['Peak']=pd.to_numeric(df['Peak'].apply(remove_bracket),errors='coerce')
df['All Time Peak']=pd.to_numeric(df['All Time Peak'].apply(remove_bracket),errors='coerce')

columns=['Actual gross', 'Adjusted gross (in 2022 dollars)', 'Average gross']
for col in columns:
    df[col]=pd.to_numeric(df[col].apply(clean_numeric_string),errors='coerce')


df['Tour title']=df['Tour title'].apply(remove_bracket).str.replace('†','').str.replace('‡','')
df['Ref.'] = df['Ref.'].str.split('[').str[1].str.replace(']','')

# df.to_csv("F:/python/numpy/Music_Tour_Performance_Data_Cleaned/clean_data.csv")

print(df.head(10))

#----data visualization----

df_top5 = df.nlargest(5, 'Shows')
plt.figure(figsize=(10, 6))
sns.barplot(x='Tour title',y='Shows',hue='Artist',data=df_top5,dodge=False)
plt.xticks(rotation=45, ha='right')
plt.title('Top 5 Tours by Number of Shows')
plt.tight_layout()


yearly_data = df.groupby('Year(s)')['Shows'].sum().reset_index()
# 2. Extract the start year to use for sorting
# This takes '2002-2005' and creates a numeric value 2002
yearly_data['start_year'] = yearly_data['Year(s)'].str.extract('(\d{4})').astype(int)
# 3. Sort by that numeric year
yearly_data = yearly_data.sort_values('start_year')
# 4. Plot
plt.figure(figsize=(12, 6))
sns.lineplot(x='Year(s)', y='Shows', data=yearly_data, marker='o', linewidth=3)
# 5. Formatting
plt.title('Total Shows by Year (Ascending Order)', fontsize=14)
plt.xticks(rotation=45)
plt.grid(axis='y', linestyle='--', alpha=0.7)
plt.tight_layout()
plt.show()


plt.figure(figsize=(10, 6))
sns.regplot(x='Shows', y='Actual gross', data=df, line_kws={'color':'red'})
plt.title('Shows vs. Actual Gross Revenue')
plt.show()

artist_revenue=df.groupby('Artist')['Actual gross'].sum().nlargest(5)
plt.figure(figsize=(8,8))
plt.pie(artist_revenue,labels=artist_revenue.index,autopct='%1.1f%%',startangle=140)
plt.title('Total Revenue Share by Top 5 Artists')
plt.tight_layout()


sns.set_style("darkgrid")
plt.figure(figsize=(12, 6))
df['Artist'] = df['Artist'].str.strip()
top_5_atrist=df['Artist'].value_counts().nlargest(5).index
df_top=df[df['Artist'].isin(top_5_atrist)]  
print(df_top.head())
sns.violinplot(x='Artist',y='Actual gross',data=df_top,inner="point",palette='GnBu')

plt.title('Gross Revenue Density by Artist')
plt.show()



