import requests
import json
from datetime import date


def get_horoscope(horoscope):
    horoscope = horoscope.lower()
    url = f"https://burc-yorumlari.vercel.app/get/{horoscope}"

    try:
        response = requests.get(url, timeout=10)
        response.raise_for_status()

        data = response.json()

        if not data:
            return None

        comment = data[0]
        today = date.today().strftime("%d.%m.%Y")

        message = f"{comment['Burc']} Burcu Günlük Yorumu {today}🗓️\n\n"
        message += f"Motto✍️: {comment.get('Mottosu', 'Bilgi yok')}\n"
        message += f"Gezegen🪐: {comment.get('Gezegeni', 'Bilgi yok')}\n"
        message += f"Element: {comment.get('Elementi', 'Bilgi yok')}\n\n"
        message += f"Günlük Yorum⤵️:\n{comment.get('GunlukYorum', 'Yorum bulunamadı')}"

        return message

    except requests.exceptions.RequestException:
        return None

    except json.JSONDecodeError:
        return None

    except Exception:
        return None