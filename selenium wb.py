from selenium import webdriver

driver = webdriver.Chrome(executable_path='C:\\Users\\Rishik\\Downloads\\chromedriver_win32\\chromedriver.exe')
driver.get('https://web.whatsapp.com')

name = input("enter the name of user or group : ")
msg = input("enter the message : ")
count = int(input('count : '))

user = driver.find_element_by_xpath('//span[@title = "{}"]'.format(name))
user.click()

msg_box = driver.find_element_by_class_name('_3u328')

for i in  range(count):
    msg_box.send_keys(msg)
    button = driver.find_element_by_class_name('_3M-N-')
    button.click()