import datetime
from time import sleep
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select  # this is for drop down lists
from selenium.webdriver import Keys
from faker import Faker
fake = Faker(locale=['en_Ca', 'en_US'])


from selenium.webdriver.chrome.options import Options

options = Options()
options.add_argument("--headless")
options.add_argument("window-size=1400,1500")
options.add_argument("--disable-gpu")
options.add_argument("--no-sandbox")
options.add_argument("start-maximized")
options.add_argument("enable-automation")
options.add_argument("--disable-infobars")
options.add_argument("--disable-dev-shm-usage")

driver = webdriver.Chrome(options=options)

app = 'Parabank'
parabank_url ='https://parabank.parasoft.com/parabank/index.htm'
parabank_title = 'ParaBank | Welcome | Online Banking'
register_page_url = 'https://parabank.parasoft.com/parabank/register.htm'
register_page_title = 'ParaBank | Register for Free Online Account Access'

username = f'{fake.user_name()}{fake.pyint(111,999)}{fake.century()}'
password1 = fake.password()
password2= password1
first_name = fake.first_name()
last_name = fake.last_name()
email = fake.email()
full_name = f'{first_name} {last_name}'
address = fake.address().replace("\n", " ")
city = fake.city()
state = fake.state_abbr()
zipcode = fake.zipcode()
phonenumber = fake.bothify(text='1-(###)-###-####')
ssn = fake.ssn()


def setUp():
    print(f'-----Launch {app} App.')
    driver.maximize_window()
    driver.implicitly_wait(30)
    driver.get(parabank_url)
    print(driver.current_url)
    if driver.current_url == parabank_url and driver.title == parabank_title:
        print(f'-----Yey! {app} App website launched successfully!')
        print(f'-----{app} homepage URL: {driver.current_url}, homepage title: {driver.title}')
        sleep(0.25)

    else:
        print(f'-----{app} did not launched, check your code or application.')
        print(f'-----Current URL: {driver.current_url}, page title: {driver.title}')
        tearDown()


def tearDown():
    if driver is not None:
        print('------------------------------------~*~------------------------------------------------')
        print(f'-----The test is completed at: {datetime.datetime.now()}')
        sleep(2)
        driver.close()
        driver.quit()


def register():
    driver.find_element(By.XPATH, '//a[contains(.,"Register")]').click()
    print(driver.current_url)
    if register_page_url in driver.current_url:
        print('You are were are suppose to be.')
    else:
        print('Something is not working.')

    assert driver.find_element(By.XPATH, '//h1[contains(., "Signing up is easy!")]').is_displayed()
    sleep(0.25)
    driver.find_element(By.ID, 'customer.firstName').send_keys(first_name)
    sleep(0.25)
    driver.find_element(By.ID, 'customer.lastName').send_keys(last_name)
    sleep(0.25)
    driver.find_element(By.ID, 'customer.address.street').send_keys(address)
    sleep(0.25)
    driver.find_element(By.ID, 'customer.address.city').send_keys(city)
    sleep(0.25)
    driver.find_element(By.ID, 'customer.address.state').send_keys(state)
    sleep(0.25)
    driver.find_element(By.ID, 'customer.address.zipCode').send_keys(zipcode)
    sleep(0.25)
    driver.find_element(By.ID, 'customer.phoneNumber').send_keys(phonenumber)
    sleep(0.25)
    driver.find_element(By.ID, 'customer.ssn').send_keys(ssn)
    sleep(0.25)
    driver.find_element(By.ID, 'customer.username').send_keys(username)
    sleep(0.25)
    driver.find_element(By.ID, 'customer.password').send_keys(password1)
    sleep(0.25)
    driver.find_element(By.ID, 'repeatedPassword').send_keys(password2)
    driver.find_element(By.XPATH, '//input[contains(@value, "Register")]').click()
    sleep(0.25)

    assert driver.find_element(By.XPATH, f'//h1[contains(., "Welcome {username}")]').is_displayed()
    sleep(0.25)
    user_name = driver.find_element(By.XPATH, f'//h1[contains(., "Welcome {username}")]').is_displayed()
    print(f'The user name {username} is diplayed: {user_name}')
    sleep(0.25)

    assert driver.find_element(By.XPATH, f'//p[contains(., "Welcome {full_name}")]').is_displayed()
    fullname = driver.find_element(By.XPATH, f'//p[contains(., "Welcome {full_name}")]').is_displayed()
    print(f'The full name {full_name }is displayed too: {fullname}')
    sleep(0.25)



def logout():
    driver.find_element(By.LINK_TEXT, 'Log Out').click()
    sleep(0.25)
    assert driver.find_element(By.XPATH, '//h2[contains(., "Customer Login")]').is_displayed()


def login():
    driver.get(parabank_url)
    driver.find_element(By.XPATH, '//input[contains(@name, "username")]').send_keys(username)
    sleep(0.25)
    driver.find_element(By.XPATH, '//input[contains(@name,"password")]').send_keys(password2)
    sleep(0.25)
    driver.find_element(By.XPATH, '//input[contains(@value, "Log In")]').click()
    sleep(0.25)

    assert driver.find_element(By.XPATH, '//p[contains(., "Welcome")]').text
    sleep(0.5)
    success_login = driver.find_element(By.XPATH, '//p[contains(., "Welcome")]').text
    print(success_login)
    if full_name in success_login:
        print(f'You have successfully log in: {success_login}')
    else:
        print('Something is not working.')




#
# setUp()
# register()
# logout()
# login()
# logout()
# tearDown()





