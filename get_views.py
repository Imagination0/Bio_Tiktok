import requests
import re

def get_total_views(username):
    url = f"https://www.tiktok.com/@{username}"
    headers = {
        "User-Agent": "Mozilla/5.0",
    }
    res = requests.get(url, headers=headers)
    matches = re.findall(r'"playCount":(\\d+)', res.text)
    total_views = sum(map(int, matches))
    return total_views
