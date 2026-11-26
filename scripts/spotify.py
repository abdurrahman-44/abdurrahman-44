import os, json, base64, urllib.request, urllib.parse, urllib.error
from pathlib import Path
from html import escape

def fetch(url, headers, data=None):
    with urllib.request.urlopen(urllib.request.Request(url, data=data, headers=headers), timeout=20) as r:
        return json.load(r) if r.status != 204 else {}

label, detail = "Lab radio offline", "Spotify authorization required"
if all(os.getenv(k) for k in ("SPOTIFY_CLIENT_ID", "SPOTIFY_CLIENT_SECRET", "SPOTIFY_REFRESH_TOKEN")):
    try:
        auth = base64.b64encode((os.environ["SPOTIFY_CLIENT_ID"]+":"+os.environ["SPOTIFY_CLIENT_SECRET"]).encode()).decode()
        token = fetch("https://accounts.spotify.com/api/token", {"Authorization":"Basic "+auth,"Content-Type":"application/x-www-form-urlencoded"}, urllib.parse.urlencode({"grant_type":"refresh_token","refresh_token":os.environ["SPOTIFY_REFRESH_TOKEN"]}).encode())["access_token"]
        item = fetch("https://api.spotify.com/v1/me/player/currently-playing", {"Authorization":"Bearer "+token})
        track = item.get("item") or {}
        if item.get("is_playing") and track.get("name"):
            label = track["name"]
            detail = ", ".join(a["name"] for a in track.get("artists", [])) or "Spotify playback"
        else:
            label, detail = "Between tracks", "Nothing playing at last check"
    except (OSError, ValueError, KeyError):
        label, detail = "Lab radio unavailable", "Check Spotify authorization or API access"
def clean(v):
    return escape(''.join(c for c in v if ord(c)>=32)[:65])
svg = f'''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 800 110"><rect width="800" height="110" rx="12" fill="#101323"/><circle cx="55" cy="55" r="29" fill="#1ed760"/><path d="M36 48q19 -8 38 3M39 57q16 -6 31 3M43 65q12 -4 23 2" fill="none" stroke="#101323" stroke-width="4" stroke-linecap="round"/><g font-family="monospace"><text x="100" y="27" fill="#818cf8" font-size="12">LAB RADIO / SPOTIFY SNAPSHOT</text><text x="100" y="56" fill="#f8fafc" font-size="17">{clean(label)}</text><text x="100" y="80" fill="#c7d2fe" font-size="13">{clean(detail)}</text></g></svg>'''
Path("dist").mkdir(exist_ok=True)
Path("dist/spotify.svg").write_text(svg)
