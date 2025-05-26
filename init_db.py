import sqlite3

conn = sqlite3.connect("products.db")
cursor = conn.cursor()

# 建立表格（如果還沒建立）
cursor.execute("""
CREATE TABLE IF NOT EXISTS products (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL,
    price INTEGER NOT NULL
)
""")

# 清除原有資料
cursor.execute("DELETE FROM products")

# 加入新商品
products = [
    ("C羅 Cristiano Ronaldo 穿過穿過的內褲", 70000),
    ("賈伯斯用過的 iPhone 4S", 100000),
    ("蔣經國的小一生字簿", 399),
    ("毛澤東用過的牙刷", 32900),
    ("黃仁勳穿過的皮外套", 8999),
    ("郭台銘舔過的盤子", 2999),
    ("安柏赫德拉過的床單", 21000),
    ("NaNaQ 的擦X布", 99),
    ("賓賓哥的物資組合包", 50000),
    ("G-Dragon 權志龍的套頭絲巾", 1080),
    ("馬英九穿過的熱褲", 10900)
]

cursor.executemany("INSERT INTO products (name, price) VALUES (?, ?)", products)
print("✅ 資料庫已重建，商品已更新")

conn.commit()
conn.close()
