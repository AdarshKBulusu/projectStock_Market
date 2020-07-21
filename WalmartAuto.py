from selenium import webdriver #gets the driver executes actions
from selenium.webdriver.common.action_chains import ActionChains #puts actions together (click)
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options
import time


driver = webdriver.Chrome(ChromeDriverManager().install()) # runs the program 
action = webdriver.common.action_chains.ActionChains(driver) #clicks, drops, send_keys 


def cart(): # this will get all of the user's inputs  
    grocery_list = []
    num = input("How many items do you want to put in your cart: ").strip() # this is string 
    
    while not(num.isnumeric()):
        num = input("Please enter a numerical input: ").strip()
    
    num = int(num)
    
    for i in range(num):
        
        item = input("What is the #" + str(i + 1) + " item you want: ").strip() 
        while item.isnumeric() or not(item.isalpha()):
            item = input("Please enter a word: ").strip()
        
        grocery_list.append(item)
    
    return grocery_list 
           


def WalmartLogin():
    driver.get('https://www.walmart.com/account/login?ref=domain') # driver.get(gets the website inside)
    driver.find_element_by_id("email").send_keys("georgedebbie23@gmail.com")
    driver.find_element_by_id("password").send_keys('64robin')
    driver.find_element_by_xpath('//*[@id="sign-in-form"]/button[1]').click() #logs into the account
    time.sleep(3) #based on your home wifi speed 
    driver.find_element_by_xpath('/html/body/div[1]/div[2]/div/header/div/a[2]').click()
    driver.find_element_by_xpath('//*[@id="header-tabs"]/div/a[1]').click()
    time.sleep(8)
    action.move_by_offset(0,0).click().perform() #eliminates pop ups
    for i in range(len(cart())):
        driver.find_element_by_xpath('/html/body/div[1]/div[1]/div/div/header/div[2]/div[2]/form/input').send_keys(cart()[i])
        driver.find_element_by_xpath('/html/body/div[1]/div[1]/div/div/header/div[2]/div[2]/form/input').submit()
        driver.find_element_by_xpath('//*[@id="item-44390948"]/div/div[3]/div/div/button').click()
    
    driver.find_element_by_xpath('/html/body/div/div[1]/div/div/header/ul/li[1]/a/span').click()
    driver.find_element_by_xpath('/html/body/div/div[1]/div/div/section/div[2]/div/div[2]/button').click()
    time.sleep(4)
    driver.save_screenshot('/Users/UserName/Desktop/Python_Projects/WalmartAuto/Updates/Updates.jpeg') 
    
    
    
if __name__ == "__main__":  
    cart()
    WalmartLogin() 

