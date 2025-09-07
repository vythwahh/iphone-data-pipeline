import pandas as pd
import re
import sqlite3
 
df = pd.read_csv("/Users/vythu/Downloads/archive/iphone_results (1).csv")

 
df.rename(columns={"RAM(Random Processing memory)": "RAM"}, inplace=True)

 
df["Price"] = df["Price"].replace(",", "", regex=True).astype(float)

 
df["ReviewCount"] = df["ReviewCount"].replace("[^0-9]", "", regex=True).astype(int)
 
df["Description"] = df["Description"].str.strip()
df["RAM"] = df["RAM"].str.strip()

 
df["RAM"] = df["RAM"].str.extract(r"(\d+)").astype(int)

 
df["Rating"] = df["Rating"].astype(float)

 
def extract_model(desc):
    match = re.search(r"iPhone\s[\w\s]+(?=\s\()", desc)
    return match.group(0).strip() if match else None

def extract_storage(desc):
    match = re.search(r"\((\d+)GB\)", desc)
    return int(match.group(1)) if match else None

def extract_color(desc):
    match = re.search(r"-\s(.+)$", desc)
    return match.group(1).strip() if match else None

df["Model"] = df["Description"].apply(extract_model)
df["Storage"] = df["Description"].apply(extract_storage)
df["Color"] = df["Description"].apply(extract_color)

 
df.dropna(inplace=True)

 
print(df.head())

 
print("\n Kích thước dataset:", df.shape)
print(" Các cột có trong dataset:", df.columns.tolist())
 
output_path = "/Users/vythu/Documents/Financial Data Pipeline/cleaned_iphone_data.csv"
df.to_csv(output_path, index=False)
print(f"\n Dữ liệu đã được lưu vào: {output_path}")
 
db_path = "/Users/vythu/Documents/Financial Data Pipeline/iphone_data.db"

 
conn = sqlite3.connect(db_path)
 
df.to_sql("iphone_data", conn, if_exists="replace", index=False)

 
conn.close()

print(f"\n Đã lưu dữ liệu vào database: {db_path}")
 
db_path = "/Users/vythu/Documents/Financial Data Pipeline/iphone_data.db"
conn = sqlite3.connect(db_path)

 
query1 = """
SELECT Model, Color, Storage, Price, Rating
FROM iphone_data
ORDER BY Rating DESC, ReviewCount DESC
LIMIT 5;
"""
df1 = pd.read_sql_query(query1, conn)
print(" Top 5 iPhone được đánh giá cao nhất:")
print(df1)

 
query2 = """
SELECT Model, ROUND(AVG(Price), 2) AS AvgPrice
FROM iphone_data
GROUP BY Model
ORDER BY AvgPrice DESC;
"""
df2 = pd.read_sql_query(query2, conn)
print("\n Giá trung bình theo từng dòng iPhone:")
print(df2)

 
query3 = """
SELECT RAM, COUNT(*) AS Count
FROM iphone_data
GROUP BY RAM
ORDER BY RAM;
"""
df3 = pd.read_sql_query(query3, conn)
print("\nPhân bố sản phẩm theo RAM:")
print(df3)

 
conn.close()
import matplotlib.pyplot as plt

 
plt.figure(figsize=(10, 6))
plt.bar(df2["Model"], df2["AvgPrice"], color="skyblue")
plt.title(" Giá trung bình của từng dòng iPhone")
plt.xlabel("Model")
plt.ylabel("Giá trung bình (VND)")
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()
plt.figure(figsize=(6, 6))
plt.pie(df3["Count"], labels=df3["RAM"], autopct="%1.1f%%", startangle=140)
plt.title(" Tỷ lệ phân bố theo RAM")
plt.show()
plt.savefig("charts_file.png")
