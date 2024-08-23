import requests
import re

def goods_parser(url: str) -> list:
    req = requests.get(url)
    text = req.text
    pattern = r'(?<=woocommerce-loop-product__title"\>)[\w ]{1,45}'
    products_list = re.findall(pattern, text)

    return products_list


print(goods_parser('https://www.itfree.com.ua/product-category/tekhnika-dlya-kukhni/refrigerators/freezers/'))
