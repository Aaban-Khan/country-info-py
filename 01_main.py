import requests
import webbrowser


country = input("Enter a Country Name: ")

try:
    url = f"https://restcountries.com/v3.1/name/{country}?fullText=true"
    r = requests.get(url)

    if r.status_code == 200:
        data = r.json()[0]

        country_name = data['name']['common']
        capital = data.get('capital', "N/A")[0]
        population = data.get('population', "N/A")
        currencies = ", ".join(data['currencies'].keys()) if "currencies" in data else "N/A"
        region = data.get('region', "N/A")
        languages = ", ".join(data['languages'].values()) if 'languages' in data else "N/A"

        maps_url = f"https://www.google.com/maps/place/indore"
        webbrowser.open(maps_url)

        print(f"\n📍 Country Name: {country_name}")
        print(f"🏙️ Capital: {capital}")
        print(f"👥 Population: {population}")
        print(f"💰 Currencies: {currencies}")
        print(f"🌍 Region: {region}")
        print(f"🗣️ Common Languages: {languages}")

    else:
        print("❌ Invalid country name or not found.")
except Exception as e:
    print(f"❗Something went Wrong: {e}")