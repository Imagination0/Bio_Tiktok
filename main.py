import time
import schedule
from get_views import get_total_views
from update_bio import update_tiktok_bio

USERNAME = 'your_username'  # Ganti dengan username TikTok kamu

def job():
    total_views = get_total_views(USERNAME)
    bio_text = f"Total Views Seluruh Video : {total_views}"
    update_tiktok_bio(bio_text)
    print(f"[UPDATED] {bio_text}")

if __name__ == "__main__":
    schedule.every(20).minutes.do(job)
    job()
    while True:
        schedule.run_pending()
        time.sleep(1)
