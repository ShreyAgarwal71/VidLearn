import time
import numpy as np
import cv2
import pyautogui
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

# this works 
screenshot = pyautogui.screenshot()
screenshot.save("test_screenshot.png")


# this does not work 
def start_screen_recording(output_file="recording.mp4", screen_size=(1920, 1080), fps=20):
    fourcc = cv2.VideoWriter_fourcc(*'mp4v')  
    out = cv2.VideoWriter(output_file, fourcc, fps, screen_size)
    
    return out

# this also does not work 
def capture_screen(out, screen_size):
    screenshot = pyautogui.screenshot()  
    frame = np.array(screenshot)  
    frame = cv2.cvtColor(frame, cv2.COLOR_RGB2BGR)  
    out.write(frame) 

# this works well
def automate_website(url):
    options = webdriver.ChromeOptions()
    options.add_argument("--start-maximized")
    
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)
    actions = ActionChains(driver)
    
    try:
        out = start_screen_recording()  # also does not work 
        driver.get(url)
        time.sleep(2)
        
        for _ in range(3):
            driver.execute_script("window.scrollBy(0, 800);")
            time.sleep(1)
        
        # clicks 3 buttons (i think it does more)
        buttons = driver.find_elements(By.TAG_NAME, "button")
        for button in buttons[:3]: 
            try:
                actions.move_to_element(button).click().perform()
                time.sleep(1)
            except:
                pass
        
        # none of the recording works 
        start_time = time.time()
        while time.time() - start_time < 30:
            capture_screen(out, (1920, 1080)) 
            time.sleep(1 / 20)  

    finally:
        out.release()  # stops recording 
        driver.quit()

# website 
automate_website("https://www.snackpass.co/")
