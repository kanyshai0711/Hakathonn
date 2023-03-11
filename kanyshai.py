import requests
from bs4 import BeautifulSoup
import lxml 
import csv

def write_to_csv(data):
    with open('data.csv', 'a') as file:
        write = csv.writer(file)
        write.writerow([data['title'], data['price'], data['image']])

def get_html(url):
    response = requests.get(url)
    return response.text

def get_total_pages(html):
    soup = BeautifulSoup(html,'lxml')
    # page_list = soup.find('div', "pager-wrap").find('ul', class_="pagination pagination-sm").find_all('li')
    # print(page_list)

get_total_pages(get_html('https://www.kivano.kg/mobilnye-telefony'))

def get_data(html):
    soup = BeautifulSoup(html, 'lxml')
    products= soup.find('div',class_="list-view" ).find_all('div', class_ = "item")
    # print(products)
    
    for product in products:
        title = product.find('div',class_ = "listbox_title oh").find('strong').text
        price = product.find('div',class_='listbox_price').find('strong').text
        image = 'https://www.kivano.kg/' + product.find('img').get('src')
        dict = {'price':price,'title':title,'image':image}
        write_to_csv(dict)

with open('data.csv', 'w') as file:
    write = csv.writer(file)
    write.writerow(['title         ','                                   price        ', '            image           '])
    

def main():
    url = 'https://www.kivano.kg/mobilnye-telefony'
    html = get_html(url)
    get_data(html)
    pages = '?page'
    number = 25
    i = 1
    while i <= number:
        url_page = url + pages + str(i)
        i+= 1
        html = get_html(url_page)
        get_data(html)
        print(i)

main()
    
import time
while True:
    main()
    time.sleep(3600)


