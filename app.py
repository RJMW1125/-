from flask import Flask, request, render_template, send_from_directory
import sqlite3
import os

# 指定 templates 資料夾
app = Flask(__name__, template_folder='網頁/templates')

# 首頁：讀取 網頁/index.html
@app.route('/')
@app.route('/index.html')
def index():
    return send_from_directory('網頁', 'index.html')

# 搜尋功能：讀取 網頁/templates/search.html
@app.route('/search')
def search():
    keyword = request.args.get('keyword', '').strip()
    results = []

    if keyword:
        conn = sqlite3.connect('products.db')
        cursor = conn.cursor()
        cursor.execute("SELECT name, price FROM products WHERE name LIKE ?", ('%' + keyword + '%',))
        results = cursor.fetchall()
        conn.close()

    return render_template('search.html', keyword=keyword, results=results)

# 其他 HTML：如 member.html、custom.html 等
@app.route('/<path:filename>')
def other_html(filename):
    return send_from_directory('網頁', filename)

if __name__ == '__main__':
    app.run(debug=True)
