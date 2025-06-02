from dotenv import load_dotenv  # Memuat variabel lingkungan dari file .env
import os  # Untuk mengakses environment variable

load_dotenv()  # Jalankan fungsi untuk memuat .env ke dalam os.environ

# Ambil variabel dari .env, jika tidak ada pakai default
APP_NAME = os.getenv("APP_NAME", "FastAPI App")  
API_PREFIX = os.getenv("API_PREFIX", "/api")  # Digunakan sebagai prefix route (misal: /api/ping)
