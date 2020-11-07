from selenium import webdriver

driver = webdriver.Chrome()
driver.get('http://web.whatsapp.com')

name = raw_input('Enter the name of user or group : ')
msg = raw_input('Enter the message : ')
count = int(raw_input('Enter the count : '))

#Scan the code before proceeding further
raw_input('Enter anything after scanning QR code')

user = driver.find_element_by_xpath('//span[@title = "{}"]'.format(name))
user.click()

msg_box = driver.find_element_by_xpath('//*[@id="main"]/footer/div[1]/div[2]/div/div[2]')

for i in range(count):
    msg_box.send_keys(msg)
    driver.find_element_by_class_name('_2lkdt').click()


