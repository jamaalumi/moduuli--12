import requests


def hae_saatiedot(paikkakunta, api_avain):
    try:
        # Rakennetaan rajapintapyyntö
        url = f"http://api.openweathermap.org/data/2.5/weather"
        params = {
            "q": paikkakunta,
            "appid": api_avain,
            "units": "metric",  # Celsius-asteet
            "lang": "fi"  # Suomi
        }

        # Lähetetään pyyntö
        vastaus = requests.get(url, params=params)
        vastaus.raise_for_status()  # Virheenhallinta

        # Muutetaan vastaus JSON-muotoon
        data = vastaus.json()

        # Haetaan tarvittavat tiedot
        lampotila = data["main"]["temp"]
        saakuvaus = data["weather"][0]["description"]

        # Tulostetaan sää
        print(f"Sää paikkakunnalla {paikkakunta.capitalize()}:")
        print(f"  {saakuvaus.capitalize()}, {lampotila:.1f}°C")

    except requests.exceptions.RequestException as e:
        print(f"Virhe haettaessa säätietoja: {e}")
    except KeyError:
        print(f"Paikkakuntaa '{paikkakunta}' ei löytynyt. Tarkista nimi ja yritä uudelleen.")


# Pääohjelma
if __name__ == "__main__":
    # Käyttäjä antaa paikkakunnan ja API-avaimen
    paikkakunta = input("Anna paikkakunnan nimi: ")
    api_avain = input("Syötä OpenWeather API-avain: ").strip()

    # Kutsutaan sääfunktiota
    hae_saatiedot(paikkakunta, api_avain)
