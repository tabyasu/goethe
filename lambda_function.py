import random
import requests

def lambda_handler(event, context):
    url = generate_url()
    while check_http_status_code(url) != 200:
        url = generate_url()
    return url

def generate_url():
    max_num = 507
    image_prefix = "gazou_"

    if random.randint(0, 1):
      max_num = 50
      image_prefix = "shun_"

    number = "{0:04d}".format(random.randint(1, max_num))
    return "http://e-village.main.jp/gazou/image_gazou/" + image_prefix + number + ".jpg"

def check_http_status_code(url):
    return requests.get(url).status_code
