import requests
from bs4 import BeautifulSoup
from tools.mod_helpers import transform_date, get_last_page, get_html_from_url
from tpscrapping import tools

base_url = 'https://www.quebec.ca/en/health/health-system-and-services/service-organization/quebec-health-system-and-its-services/situation-in-emergency-rooms-in-quebec'\

params = {
    'id': '24981',
    'tx_solr[location]': 'H4L3A2',
    'tx_solr[pt]': '45.5213056,-73.6985088',
    'tx_solr[sfield]': 'geolocation_location',
    'tx_solr[page]': 1
}

soup = get_html_from_url(base_url, params)
last_page = int(get_last_page(soup))
print(f"Last page: {last_page}")

last_update = transform_date(soup.find('div', class_='last-update-info').find_all("span")[1].text)
print(f"Last update: {last_update}")

for page_number in range(1, last_page + 1):
    params['tx_solr[page]'] = page_number
    print(f"Page number: {page_number}")

    soup = get_html_from_url(base_url, params)

    if len(soup) > 0 :

        hospitals = soup.find('ul', class_='results-list list-group').find_all('div', class_='hospital_element')

        for hospital in hospitals:
            data_hospital = hospital.find(name='ul', class_='hospital-info')
            title = data_hospital.find('li', class_='title')
            name = title.find('div', class_='font-weight-bold').text

            address = title.find('div', class_='adresse')

            address_details = address.contents[0].strip()
            street = address_details.split(',')[0]
            city = address_details.split(',')[1]
            code_postal = address_details.split(',')[2]
            region = address.contents[2].strip()

            fiche = title.find('div', class_='lien-fiche-sante')
            id = fiche.find('a').get("href").split('?nofiche=')[1]

            print(f"id: {id}")
            print(f"Name: {name}")
            print(f"Street: {street}")
            print(f"City: {city}")
            print(f"Postal Code: {code_postal}")
            print(f"Region: {region}")

            items = data_hospital.find_all('li', class_='hopital-item')

            wait_non_priority = items[0].find_all('div')[1].find('span', class_='font-weight-bold').text.strip()
            waiting_to_see_doctor = items[1].find_all('div')[1].find('span', class_='font-weight-bold').text.strip()
            total_people = items[2].find_all('div')[1].find('span', class_='font-weight-bold').text.strip()
            occupancy_rate = items[3].find_all('div')[1].find('span', class_='font-weight-bold').text.strip()
            avg_wait_room = items[4].find_all('div')[1].find('span', class_='font-weight-bold').text.strip()
            avg_wait_stretcher = items[5].find_all('div')[1].find('span', class_='font-weight-bold').text.strip()
            print(f"Estimated wait time for non-priority cases: {wait_non_priority}")
            print(f"Number of people waiting to see a doctor: {waiting_to_see_doctor}")
            print(f"Total number of people in the emergency room: {total_people}")
            print(f"Occupancy rate of stretchers: {occupancy_rate}")
            print(f"Average stay time in the waiting room (previous day): {avg_wait_room}")
            print(f"Average stay time on a stretcher (previous day): {avg_wait_stretcher}")
            print('-' * 40)

    else:
        print("Failed to retrieve the webpage")