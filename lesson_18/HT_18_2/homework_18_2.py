import requests
from urllib.parse import quote

url = 'http://127.0.0.1:8080'
image = 'mars_photo2.jpg'
with open(image, 'rb') as file:
    files = {'image':(image, file, "image/jpeg")}
    response = requests.post(f'{url}/upload', files=files)
response.raise_for_status()
data = response.json()
image_url = data['image_url']
print("Зображення завантажено", image_url)

file = image_url.rsplit('/', 1)[-1]
encoded_file = quote(file, safe='')

response = requests.get(f"{url}/image/{encoded_file}", headers={"Content-Type": "text"})
response.raise_for_status()
data = response.json()
print("URL зображення:", data['image_url'])

response = requests.delete(f'{url}/delete/{encoded_file}')
response.raise_for_status()
print("Результат видалення:", response.json())