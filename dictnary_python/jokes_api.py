import requests

pj_jokes = "https://official-joke-api.appspot.com/random_joke"

dad_jokes = "https://icanhazdadjoke.com/"


def get_joke(url_type,mood):
    headers = {
        "Accept": "application/json"
    }
    joke = requests.get(url=url_type,headers=headers)
    if mood == "dad":
        final_joke = joke.json()["joke"]
    if mood == "pj":
        final_joke = joke.json()["setup"] + joke.json()["punchline"]
        
    return final_joke

mood = input("Enter what kind of jokes you want eg.(dad,pj): ")

if mood == "dad":
    url_type = dad_jokes
else:
    url_type = pj_jokes

jokes = get_joke(url_type,mood)

print(jokes)