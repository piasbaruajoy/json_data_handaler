import requests
url = "https://jsonplaceholder.typicode.com/posts/"

response = requests.get(url)
if response.status_code == 200:
    currency = response.json()
    for country in currency[:5]:  # প্রথম ৫টা দেশ দেখাচ্ছে
        print(country['name']['common'])
else:
    print("Failed to fetch data.")
    print(response.status_code)
    print(response.text)
