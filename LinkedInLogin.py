from selenium import webdriver
from bs4 import BeautifulSoup
import time
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support.wait import WebDriverWait


path = "C:\\Users\\Amit\\PycharmProjects\\PythonScript(selenium, beautiful soup )\\PythonScript\\chromedriver.exe"

driver = webdriver.Chrome(path)
driver.implicitly_wait(10)
driver.maximize_window()
driver.get('https://www.linkedin.com/login')

file = open('config.txt')
lines = file.readlines()
username = lines[0]
password = lines[1]

Title = driver.title
print(Title)

EmailIdText = driver.find_element_by_id('username').send_keys(username)
PasswordText = driver.find_element_by_id('password').send_keys(password)
print("Login Successfully")
time.sleep(2)

driver.get("https://www.linkedin.com/search/results/people/?geoUrn=%5B%22103644278%22%5D&keywords=sumithra%20jonnalagadda&network=%5B%22F%22%2C%22S%22%2C%22O%22%5D&origin=FACETED_SEARCH")
time.sleep(2)
soup = BeautifulSoup(driver.page_source, features="lxml")
# print(soup.text)
# print(soup.contents)
# all_buttons = soup.find_all('div', {'class':'entity-result', 'class':'entity-result__actions entity-result__divider'})
# print(all_buttons)
all_buttons = driver.find_elements_by_tag_name('button')
Button = soup.find('all_buttons', {'id':'ember80'})
# print(Button)
# print(soup.find_all('button'))
# message_button = soup.find_all('span', {'class':'artdeco-button__text'})
# print(message_button)
message_button = [btn for btn in all_buttons if btn.text == "Message"]
message_Button = soup.find_all('message_button', {'class':'artdeco-button__text'})
for i in range(0, len(message_button)):
    driver.execute_script("arguments[0].click();", message_button[i])
    time.sleep(2)

    subject_button = driver.find_element_by_name('subject').send_keys("Testing")
    message = "Hi Sumithra Jonnalagadda. " \
              "This message has to do with testing the project."
    messageattributevalue = driver.find_element_by_xpath('//div[@role="textbox"]')
    messageattributevalue.send_keys(message)
    print(message)
    submit_Button = driver.find_element_by_xpath("//button[@type='submit']").click()
    time.sleep(2)
    close_button = driver.find_element_by_id('ember125').click()
    # close_button = driver.find_element_by_xpath("//button[@id='ember125']").click()
    time.sleep(2)
driver.close()