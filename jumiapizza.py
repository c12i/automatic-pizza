from selenium import webdriver
import requests

print('You need to have a Jumia Account for this to work')
email = input('Enter Jumia Food email: ')
password = input('Enter Jumia Food password: ')
response = requests.get('https://food.jumia.co.ke/login')

url = 'https://food.jumia.co.ke/login'
url2 = 'https://food.jumia.co.ke/customer/timeline/orders'
#Debonairs Friday Thrill
url3 = 'https://food.jumia.co.ke/cart/reorder-now/k4gz-8lip'
#Debonairs Friday Thrill
url4 = 'https://food.jumia.co.ke/review-order/k4gz'

#You need to indicate the filepath of the chromedriver
driver = webdriver.Chrome('/Users/collins/Desktop/python_projects/auto_login/chromedriver')

def logintourl():
    driver.get(url)
    driver.find_element_by_id('customer_login_email').send_keys(email)
    driver.find_element_by_id('customer_login_password').send_keys(password)
    driver.find_element_by_tag_name('button').click()

def repeatorder():
    driver.get(url2)
    driver.get(url3)
    driver.get(url4)
    driver.find_element_by_id('shop_order_cart_type_checkout_primary_button').click()
    driver.find_element_by_class_name('payment-img').click()
    driver.find_element_by_id('shop_checkout_type_place_order_button').click()

    
while response.headers['Date'][0:3] == 'Fri':
    repeatorder()
    logintourl()
    break
else:
    print('Not Yet Friday')
    driver.close()
    
