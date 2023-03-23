#Test Login
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver import ActionChains

import time
serv_obj = Service("C:\DRIVERS\chromedriver32\chromedriver.exe")
#driver=webdriver.Chrome(executable_path="C:\DRIVERS\chromedriver32\chromedriver.exe")
driver.implicitly_wait(15) #implicit wait
driver.get("https://164.92.150.242/staff/staff")
driver.maximize_window()

act_title = driver.title
exp_title="SIMS"

if act_title==exp_title:
    print("pass")
else:
    print("fail")
class LoginTest():
    def login_test (self):
        serv_obj = Service("C:\DRIVERS\chromedriver32\chromedriver.exe")
        driver.get("https://164.92.150.242/staff/staff")
        driver.maximize_window()
        driver.find_element(By.ID, "").click
        var1=driver.find_element(By.ID, "").click()
        print(var1)
        var2=driver.find_element(By.ID, "").click
        print(var2)

Login = LoginTest()
Login.login_test()



driver.close()

driver.find_element("xpath", ' //*[@id="details-button"]').click()

# storing the current window handle to get back to dashboard
main_page = driver.current_window_handle

driver.find_element(By.LINK_TEXT, "Proceed to 164.92.150.242 (unsafe)").click()

driver.find_element("xpath", '//*[@id="root"]/div/div/button').click()
time.sleep(5)

# changing the handles to access login page
for handle in driver.window_handles:
    if handle != main_page:
        login_page = handle

# change the control to signin page
driver.switch_to.window(login_page)

# enter the email
driver.find_element("xpath", '//*[@id="i0116"]').send_keys("svc-miogsims@kpc.co.ke")
time.sleep(5)
#Click on next
driver.find_element("xpath", '//*[@id="idSIButton9"]').click()
time.sleep(5)
#enter password
driver.find_element("xpath", '//*[@id="i0118"]').send_keys("Lgemo!4745")
time.sleep(5)
#Click on signin
driver.find_element("xpath", '//*[@id="idSIButton9"]').click()
time.sleep(2)
driver.find_element("xpath", '//*[@id="idSIButton9"]').click()
time.sleep(0)
# change control to main page
driver.switch_to.window(main_page)
time.sleep(0)
#Resources -> Users
Resources=driver.find_element("xpath", "//span[normalize-space()='Resources']")
users=driver.find_element("xpath", '//*[@id="sidenav-horizontal"]/li[3]/ul/li[4]/a')
#mousehover navbar
act=ActionChains(driver)
act.move_to_element(Resources).move_to_element(users).click().perform()
time.sleep(5)
#click on create staff button
driver.find_element("xpath", '//*[@id="root"]/div/div/div/div/div/div/div/div[1]/div[2]/div/button').click()
time.sleep(5)
#provide values to textbox
driver.find_element(By.ID, 'email').send_keys("bornfaceotieno@gmail.com")
driver.find_element(By.ID, 'name').send_keys("bornfaceotieno")
driver.find_element(By.ID, 'identification').send_keys("39184237")
time.sleep(5)
#Click on from react component
dropdown = driver.find_element("xpath", "//body[1]/div[7]/div[1]/div[1]/div[2]/div[1]/div[1]/div[1]/div[1]/form[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]").click()
#Select user from react component
user=driver.find_element("xpath", "//div[@id='react-select-4-option-0']").click()

time.sleep(5)
#count number of options
#print(len(dropdown))

#capture all options
#all_options=dropdown.options
#for option in all_options:
   # print(option.text)

#Select identification type
dropdown_id = driver.find_element("xpath", "//body[1]/div[7]/div[1]/div[1]/div[2]/div[1]/div[1]/div[1]/div[1]/form[1]/div[1]/div[4]/div[1]/div[1]").click()
id_type = driver.find_element("xpath", "//div[@id='react-select-5-option-0']").click()
time.sleep(10)

#count number of options
#print(len(drpd.options)) #True

#capture all options
#all_options=drpd.options
#for option in all_options:
    #print(option.text)

# closing the window
driver.quit()
