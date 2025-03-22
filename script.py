import requests
from bs4 import BeautifulSoup

url = input('Ingrese el host: ')
response = requests.get(url=url)

if response.status_code == 200:
    soup = BeautifulSoup(response.text, 'html.parser')
    machines = soup.find_all('div', onclick=True)
    for machine in machines:
        onclick_text = machine['onclick']
        machine_name = onclick_text.split("'")[1]
        print('Machine is ====>', machine_name)