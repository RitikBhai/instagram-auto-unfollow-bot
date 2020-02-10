from selenium import webdriver
import time
import stdiomask
print("    ██║░░░██║████╗░██║██╔════╝██╔══██╗██║░░░░░██║░░░░░██╔══██╗░██║░░██╗░░██║")
print("    ██║░░░██║██╔██╗██║█████╗░░██║░░██║██║░░░░░██║░░░░░██║░░██║░╚██╗████╗██╔╝")
print("    ██║░░░██║██║╚████║██╔══╝░░██║░░██║██║░░░░░██║░░░░░██║░░██║░░████╔═████║░")
print("    ╚██████╔╝██║░╚███║██║░░░░░╚█████╔╝███████╗███████╗╚█████╔╝░░╚██╔╝░╚██╔╝░")
print("    ░╚═════╝░╚═╝░░╚══╝╚═╝░░░░░░╚════╝░╚══════╝╚══════╝░╚════╝░░░░╚═╝░░░╚═╝░░")
print("  --STEPS")
print("  1 ENTER YOUR USERNAME OR EMAIL ID ")
print("  2 ENTER YOUR PASSWORD  ")
print("  3 ENTER UNFOLLOW VALUE")
usr=input("username or email id: ")
password =stdiomask.getpass("password: ", mask='X')
numbers_of_following = int(input("value: "))
driver = webdriver.Chrome()
driver.get('https://www.instagram.com/accounts/login/')
time.sleep(2)
driver.maximize_window()
time.sleep(1)
login_field = driver.find_element_by_name('username')
login_field.send_keys(usr)
password_field = driver.find_element_by_xpath("//input[@name=\"password\"]")
password_field.send_keys(password)
login_box = driver.find_element_by_xpath('//button[@type="submit"]')
login_box.click()
time.sleep(4)
not_now = driver.find_element_by_xpath("//button[contains(text() , 'Not Now')]") 
not_now.click()
def unfollow():
    name = driver.find_element_by_xpath('/html/body/div[1]/section/main/section/div[3]/div[1]/div/div[2]/div[1]/a')
    name.click()
    time.sleep(2)
    following_lable= driver.find_element_by_xpath('/html/body/div[1]/section/main/div/header/section/ul/li[3]/a')
    following_lable.click()
    time.sleep(1)
    i = 1
    while i <= numbers_of_following:
         time.sleep(2)
         following_box = driver.find_element_by_xpath("//button[contains(text() , 'Following')]")
         following_box.click()
         unfollow_box = driver.find_element_by_xpath("//button[contains(text() , 'Unfollow')]")
         unfollow_box.click()
         driver.execute_script('arguments[0].scrollIntoView()', following_box)
         i += 1  
    time.sleep(0.5)     
    close_button = driver.find_element_by_xpath('/html/body/div[4]/div/div[1]/div/div[2]/button') 
    close_button.click()
    setting_button = driver.find_element_by_xpath('/html/body/div[1]/section/main/div/header/section/div[1]/div/button/span')
    setting_button.click()
    time.sleep(0.5)
    log_out = driver.find_element_by_xpath("//button[contains(text() , 'Log Out')]")
    log_out.click()
    
    
   
  
    

        
unfollow()       

