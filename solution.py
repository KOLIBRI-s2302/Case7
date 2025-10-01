#Case 7
#Developers: Shatalov Alexander, Svilin Andrey, Haidukhov Stepan 

import requests
import bs4
import time
import locale as loc

def main():

    
    def parsing(product_url):
    '''
    :param: product_url it is a Product page URL
        
    :Returns: Product info like name, price, color, etc.
        If data not found, value is 'Not found'
    '''
    
        response = requests.get(product_url)
        soup = bs4.BeautifulSoup(response.text, 'html.parser')
        product_data = {
            'Name': None,
            'Type of shoes': None,
            'Season': None,
            'Price': None,
            'Sizes': None,
            'Upper material': None,
            'Colour': None,
            'Country of origin': None
        }

        # Name
        name = soup.find('h1')
        if name:
            product_data['Name'] = name.text.strip()
        else:
            product_data['Name'] = 'Not found'

        # Colour

        color_title = soup.find('div', class_='param-title', string=loc.MAIN_COLOUR)
        if color_title:
            color_value = color_title.find_next_sibling('div', class_='param-body')
            if color_value:
                product_data['Colour'] = color_value.text.strip()
        else:
            product_data['Colour'] = 'Not found'

        # Type of shoes
        type_of_shoe_title = soup.find('div', class_='param-title', string=loc.TYPE_OF_SHOE)
        if type_of_shoe_title:
            type_of_shoe_value = type_of_shoe_title.find_next_sibling('div', class_='param-body')
            if type_of_shoe_value:
                product_data['Type of shoes'] = type_of_shoe_value.text.strip()
        else:
            product_data['Type of shoes'] = 'Not found'

        # SEASON
        season_title = soup.find('div', class_='param-title', string=loc.SEASON)
        if season_title:
            season_value = season_title.find_next_sibling('div', class_='param-body')
            if season_value:
                product_data['Season'] = season_value.text.strip()
        else:
            product_data['Season'] = 'Not found'

        # Sizes
        size_title = soup.find('div', class_='param-title', string=loc.SIZE)
        if size_title:
            size_value = size_title.find_next_sibling('div', class_='param-body')
            if size_value:
                product_data['Sizes'] = size_value.text.strip()
        else:
            product_data['Sizes'] = 'Not found'


        # Upper material
        upper_material_title = soup.find('div', class_='param-title', string=loc.UPPER_MATERIAL)
        if upper_material_title:
            upper_material_value = upper_material_title.find_next_sibling('div', class_='param-body')
            if upper_material_value:
                product_data['Upper material'] = upper_material_value.text.strip()
        else:
            product_data['Upper material'] = 'Not found'


        # Country_of_origin
        country_of_origin_title = soup.find('div', class_='param-title', string=loc.COUNTRY_OF_ORIGIN)
        if country_of_origin_title:
            country_of_origin_value = country_of_origin_title.find_next_sibling('div', class_='param-body')
            if country_of_origin_value:
                product_data['Country of origin'] = country_of_origin_value.text.strip()
        else:
            product_data['Country of origin'] = 'Not found'

        # Article
        article_span = soup.find('span', string=loc.ARTICLE)
        if article_span:
            article_text = article_span.next_sibling
            if article_text:
                product_data['Article'] = article_text.strip()
        else:
            product_data['Article'] = 'Not found'

        # Price
        price = soup.find('div', class_='price-current')
        if price:
            strong_tag = price.find('strong')
            if strong_tag:
                product_data['Price'] = strong_tag.text.strip()
        else:
            product_data['Price'] = 'Not found'

        return product_data

    
    def get_price_number(product):   
        '''
        :param: product it is a dictionary with product data. Have 'Price' key
        :Returns:
            int: Price as number without spaces, or 0 if price is missing/invalid
        '''
        
        if product['Price']:
            return int(product['Price'])

        return 0

    url = 'https://obuv-tut2000.ru/magazin/search'
    search_query = input("Введите поисковый запрос: ")

    page = 0
    all_links = set()

    while True:
        page_links = []
        response = requests.get(url, params={
            'p': page,
            'gr_smart_search': 1,
            'search_text': search_query
        })

        soup = bs4.BeautifulSoup(response.text, features='html.parser')
        all_forms = soup.find_all(name='form', method='post')

        for form in all_forms:
            links = form.find_all('a')
            for link in links:
                if 'product' in link['href']:
                    full_url = link['href']
                    if full_url.startswith('/'):
                        full_url = 'https://obuv-tut2000.ru' + full_url
                    all_links.add(full_url)
                    page_links.append(full_url)

        if not page_links:
            break

        
        page += 1

    all_products = []

    for product_url in all_links:
        product_data = parsing(product_url)
        all_products.append(product_data)
        time.sleep(2)

    sorted_products = sorted(all_products, key=get_price_number)

    with open('products_data.txt', 'w', encoding='utf-8') as txt_file:

        for product in sorted_products:
            txt_file.write(f"  Название: {product['Name']}\n")
            txt_file.write(f"  Артикул: {product.get('Article')}\n")
            txt_file.write(f"  Цена: {product['Price']}\n")
            txt_file.write(f"  Цвет: {product['Colour']}\n")
            txt_file.write(f"  Тип обуви: {product['Type of shoes']}\n")
            txt_file.write(f"  Сезон: {product['Season']}\n")
            txt_file.write(f"  Размеры: {product['Sizes']}\n")
            txt_file.write(f"  Материал верха: {product['Upper material']}\n")
            txt_file.write(f"  Страна производства: {product['Country of origin']}\n")
            txt_file.write("\n\n")


if __name__ == '__main__':
    main()
