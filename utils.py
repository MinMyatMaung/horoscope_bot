import requests

def get_daily_horoscope(sign: str, day: str) -> dict:
    """Get daily horoscope for a zodiac sign.
    Keyword arguments:
    sign:str - Zodiac sign
    day:str - Date in format (YYYY-MM-DD) OR TODAY OR TOMORROW OR YESTERDAY
    Return:dict - JSON data
    """
    
    allowed_days = ["today", "tomorrow", "yesterday"]

    if day.lower() in allowed_days:
        url = "https://horoscope-app-api.vercel.app/api/v1/get-horoscope/daily"
        params = {"sign": sign, "day": day}
        response = requests.get(url, params)

        # Handling failed response
        if response.status_code == 200:
            return response.json()
        else:
            return {
                "data": {
                    "horoscope_data": f"⚠️ Couldn't fetch horoscope for {sign} on {day}. Please try again.",
                    "date": day
                }
            }

    # Return message for days other than today, tomorrow, and yesterday
    return {
        "data": {
            "horoscope_data": f"{sign},expect surprises on {day}. Stay open-minded!",
            "date": day
        }
    }
