from flask import Flask, render_template
import mysql.connector

app = Flask(__name__)

# Konfigurasi database
db_config = {
    'host': '35.227.24.242',
    'user': 'root',
    'password': 'aliya123.',
    'database': 'produk_uts'
}

# Fungsi koneksi database
def get_db_connection():
    connection = mysql.connector.connect(**db_config)
    return connection

# Route utama
@app.route('/')
def home():
    # Koneksi ke database
    connection = get_db_connection()
    cursor = connection.cursor()

    # Query ambil nama produk dan harga dari tabel 'products'
    cursor.execute('SELECT nama, harga FROM produk')
    products = cursor.fetchall()

    # Tutup koneksi
    cursor.close()
    connection.close()

    # Kirim data ke template HTML
    return render_template('index.html', products=products)

# Jalankan server
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
