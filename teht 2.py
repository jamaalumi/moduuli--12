import requests


def hae_saatiedot(paikkakunta, api_avain):
    try:
        url = f"http://api.openweathermap.org/data/2.5/weather"
        params = {
            "q": paikkakunta,
            "appid": api_avain,
            "units": "metric",  # Celsius-asteet
            "lang": "fi"  # Suomi
        }

        vastaus = requests.get(url, params=params)
        vastaus.raise_for_status()

        data = vastaus.json()

        lampotila = data["main"]["temp"]
        saakuvaus = data["weather"][0]["description"]

        print(f"Sää paikkakunnalla {paikkakunta.capitalize()}:")
        print(f"  {saakuvaus.capitalize()}, {lampotila:.1f}°C")

    except requests.exceptions.RequestException as e:
        print(f"Virhe haettaessa säätietoja: {e}")
    except KeyError:
        print(f"Paikkakuntaa '{paikkakunta}' ei löytynyt. Tarkista nimi ja yritä uudelleen.")


if __name__ == "__main__":
    paikkakunta = input("Anna paikkakunnan nimi: ")
    api_avain = input("Syötä OpenWeather API-avain: ").strip()


    hae_saatiedot(paikkakunta, api_avain)
