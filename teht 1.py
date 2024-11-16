import requests


def hae_chuck_norris_vitsi():
    try:

        vastaus = requests.get("https://api.chucknorris.io/jokes/random")
        vastaus.raise_for_status()

        data = vastaus.json()

        vitsi = data.get("value")
        if vitsi:
            print("Chuck Norris -vitsi:")
            print(vitsi)
        else:
            print("Vitsiä ei voitu hakea.")

    except requests.RequestException as e:
        print(f"Virhe haettaessa vitsiä: {e}")



if __name__ == "__main__":
    hae_chuck_norris_vitsi()
