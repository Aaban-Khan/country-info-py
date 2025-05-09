import requests
import webbrowser
import pyttsx3 
engine = pyttsx3.init('sapi5')


country = input("Enter a Country Name: ")

def speak(details):
    for label, value in details:
        print(f"{label} {value}")
        clean_label = label.encode('ascii', 'ignore').decode().replace(":", " ").strip()
        engine.say(f"{clean_label} {value}")
        engine.runAndWait()

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

        # maps_url = f"https://www.google.com/maps/place/dhar"
        # webbrowser.open(maps_url)
        print("\n--------------------------------")
        speak([
        ("📍Country Name:", country_name),
        ("🏙️ Capital:", capital),
        ("👥 Population:", str(population)),
        ("💰 Currencies:", str(currencies)),
        ("🌍 Region:", region),
        ("🗣️ Common Languages:", languages),
        ])

    else:
        print("❌ Invalid country name or not found.")
except Exception as e:
    print(f"❗Something went Wrong: {e}")

#  python -m venv .venv                                               
# PS C:\Users\asus\Desktop\Python-Projects\Python-Projects\robo_speaker> .venv/Scripts/activate                                             
# (.venv) PS C:\Users\asus\Desktop\Python-Projects\Python-Projects\robo_speaker> .venv/Scripts/activate                                     
# (.venv) PS C:\Users\asus\Desktop\Python-Projects\Python-Projects\robo_speaker> pip install pyttsx3 
# 