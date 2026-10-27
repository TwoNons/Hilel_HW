import requests

BASE_URL = "https://images-api.nasa.gov"

# Пошук зображень
search_url = f"{BASE_URL}/search"
search_params = {
    "q": "Curiosity rover Mars",  # пошуковий запит
    "media_type": "image",  # тільки зображення
    "page_size": 20  # щоб було з чого вибрати
}
response = requests.get(search_url, params=search_params)
response.raise_for_status()
data = response.json()

# Отримання nasa_id з data
items = data["collection"]["items"]
nasa_ids = []
for item in items:
    nasa_id = item['data'][0]['nasa_id']
    nasa_ids.append(nasa_id)

# Отримання файлів по nasa_id
asset_url_template = f"{BASE_URL}/asset/{{nasa_id}}"
count = 0
for nasa_id in nasa_ids:
    if count == 2:
        break
    asset_url = asset_url_template.format(nasa_id=nasa_id)
    asset_response = requests.get(asset_url)
    asset_response.raise_for_status()
    asset_data = asset_response.json()
    file_urls = asset_data["collection"]["items"]

    for file in file_urls:
        image_url = file["href"]
        if image_url.lower().split("?")[0].endswith(".jpg"):
            image_response = requests.get(image_url)
            image_response.raise_for_status()
            filename = f'mars_photo{count + 1}.jpg)'
            with open(filename, "wb") as f:
                f.write(image_response.content)
            print(f'Зображення збережено {filename}')
            count += 1
            break
if count < 2:
    print(f'Вдалось завантажити лише {count} зображень')
