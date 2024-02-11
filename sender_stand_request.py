import configurations
import requests
import data

def get_docs():
    return requests.get(configurations.URL_SERVICE + configurations.DOC_PATH)

def get_logs():
    return requests.get(configurations.URL_SERVICE + configurations.LOG_MAIN_PATH, params={'count': 20})

def get_users_table():
    return requests.get(configurations.URL_SERVICE + configurations.USER_TABLE_PATH)

def post_new_user(body):
    return requests.post(configurations.URL_SERVICE + configurations.CREATE_USER_PATH,
                         json=body,
                         headers=data.headers)

def post_products_kits(product_ids):
    return requests.post(configurations.URL_SERVICE + configurations.PRODUCTS_KITS_PATH,
                         json=product_ids,
                         headers=data.headers)

# response = get_docs()
# print(response.status_code)

# response = get_logs()
# print(response.status_code)
# print(response.headers)

# response = get_users_table()
# print(response.status_code)

# response = post_new_user(data.user_body)
# print(response.status_code)
# print(response.json())

# response = post_products_kits(data.product_ids)
# print(response.status_code)
# print(response.json())