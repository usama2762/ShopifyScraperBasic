import json, requests, time, webbrowser

url = raw_input("Please enter Shopify URL: ")
keyword = raw_input("Keyword: ")
size = raw_input("Size: ")

delay = 1

def get_products(url):
  while True:
    r = requests.get(url)
    response = r.json()

    for i in response['products']:
      yield i

    time.sleep(delay)

def get_cart_link(url, id):
  return url + '/cart/add?&id=' + str(id) + '&quantity=1&add=add'

def get_products_url(url):
  return url + '/products.json'

def find_products(keyword):
  for product in get_products(get_products_url(url)):
    if not keyword.lower() in product['title'].lower():
      continue

    for variant in product['variants']:
      if variant['title'] == str(size):
        webbrowser.open(get_cart_link(url, variant['id']))
        return

find_products(keyword)
