from fastapi import FastAPI
import mysql.connector
import speedtest
import os

app = FastAPI()

# MySQL connection
def get_db_connection():
    conn = mysql.connector.connect(
        host=os.getenv("DB_HOST", "localhost"),
        user=os.getenv("DB_USER", "root"),
        password=os.getenv("DB_PASSWORD", "password"),
        database=os.getenv("DB_NAME", "speedtest_db")
    )
    return conn

@app.get("/api/speedtest")
def speedtest_api():
    st = speedtest.Speedtest()
    st.get_best_server()
    download_speed = st.download() / 1_000_000  # convert from bits to Mbps
    upload_speed = st.upload() / 1_000_000
    ping = st.results.ping

    # Save to DB
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute("INSERT INTO results (download, upload, ping) VALUES (%s, %s, %s)",
                   (download_speed, upload_speed, ping))
    conn.commit()
    cursor.close()
    conn.close()

    return {"download": download_speed, "upload": upload_speed, "ping": ping}
