import time
import numpy as np
import pyscreenrec
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager


# this works well
def automate_website(url):
    options = webdriver.ChromeOptions()
    options.add_argument("--start-maximized")
    
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)
    actions = ActionChains(driver)
    
    try:
        driver.get(url)
        time.sleep(2)
        
        for _ in range(3):
            driver.execute_script("window.scrollBy(0, 800);")
            time.sleep(1)
        
        # does not click buttons 
        buttons = driver.find_elements(By.TAG_NAME, "button")
        for button in buttons[:3]: 
            try:
                actions.move_to_element(button).click().perform()
                time.sleep(1)
            except:
                pass
        

    finally:
        driver.quit()


recorder = pyscreenrec.ScreenRecorder()
time.sleep(2) 
recorder.start_recording("websiteRecording.mp4", 10)

# website 
# automate_website("https://www.snackpass.co/")
time.sleep(5)  # Let it record for a few seconds

recorder.stop_recording()
