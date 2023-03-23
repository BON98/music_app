from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver import ActionChains
import time
driver=webdriver.Chrome(executable_path="C:\DRIVERS\chromedriver32\chromedriver.exe")
driver.implicitly_wait(15) #implicit wait
driver.get("https://164.92.150.242/staff/staff")
driver.maximize_window()
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
#Departments -> Courses
Departments=driver.find_element("xpath", "//span[normalize-space()='Departments']")
Courses=driver.find_element("xpath", "//a[@href='#'][normalize-space()='Courses']")
courses=driver.find_element("xpath", "//a[@href='/staff/courses']")
#mousehover navbar
act=ActionChains(driver)
act.move_to_element(Departments).move_to_element(Courses).move_to_element(courses).click().perform()
time.sleep(10)
driver.find_element(By.XPATH, "//button[normalize-space()='Create Course']").click()#Click on create course button
time.sleep(5)
drpcourse_ele=driver.find_element(By.XPATH, "//body[1]/div[5]/div[1]/div[1]/div[2]/div[2]/div[1]/div[1]/div[1]/div[1]/div[1]/form[1]/div[1]/div[1]/div[1]/div[1]/div[2]").click()#select course pre-requisites
time.sleep(5)
course=driver.find_element("xpath", "//div[@id='react-select-2-option-0']").click()
time.sleep(5)

#select a department
drpdep_ele=driver.find_element(By.XPATH, "//body[1]/div[5]/div[1]/div[1]/div[2]/div[2]/div[1]/div[1]/div[1]/div[1]/div[1]/form[1]/div[1]/div[2]/div[1]/div[1]/div[2]").click()#select department
time.sleep(5)
dep=driver.find_element("xpath", "//div[@id='react-select-3-option-1']").click()
time.sleep(5)
#select Timetablable option
drptimetablable_ele=driver.find_element(By.XPATH, "//select[@id='timetablable']")#select timetablable option
drptimetablable = Select(drptimetablable_ele)# pass drop down element
time.sleep(5)
# select option from dropdown
drptimetablable.select_by_value("true") #value
time.sleep(5)
#select technical assistance
drptechnical_ele=driver.find_element(By.XPATH, "//body[1]/div[5]/div[1]/div[1]/div[2]/div[2]/div[1]/div[1]/div[1]/div[1]/div[1]/form[1]/div[1]/div[5]/div[1]/div[1]/div[2]").click()#select technical assistance option
time.sleep(5)
dep=driver.find_element("xpath", "//div[@id='react-select-4-option-0']").click()
time.sleep(5)

driver.quit()





