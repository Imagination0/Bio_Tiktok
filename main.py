import asyncio
import schedule
import time
from get_views import get_total_views
from update_bio import update_tiktok_bio

USERNAME = 'your_username'

async def job():
    total_views = get_total_views(USERNAME)
    bio_text = f"Jumblah Total Views: {total_views}"
    await update_tiktok_bio(bio_text)
    print(f"[UPDATED] {bio_text}")

def run_schedule():
    schedule.every(20).minutes.do(lambda: asyncio.run(job()))
    while True:
        schedule.run_pending()
        time.sleep(1)

if __name__ == "__main__":
    run_schedule()
