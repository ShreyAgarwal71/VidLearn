from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options
import time
import os
from PIL import Image

def capture_and_crop_screenshot(url, output_file, crop_height):
    options = Options()
    options.add_argument("--headless") 
    options.add_argument("--window-size=1280x1024") 

    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)
    
    try:
        driver.get(url) 
        time.sleep(3)  
        screenshot_path = "temp_screenshot.png" 
        
        driver.save_screenshot(screenshot_path)  
        print(f"Screenshot saved as {screenshot_path}")

        img = Image.open(screenshot_path)
        cropped_img = img.crop((0, crop_height, img.width, img.height))  
        
        cropped_img.save(output_file)
        print(f"Cropped image saved as {output_file}")
        
    finally:
        driver.quit()  
        if os.path.exists(screenshot_path): 
            os.remove(screenshot_path)

urls = [
    "https://web.archive.org/web/20170222065327/https://openai.com/about/",
    "https://web.archive.org/web/20191004192957/https://openai.com/about/",
    "https://web.archive.org/web/20201231050128/https://openai.com/about/",
    "https://web.archive.org/web/20220208123344/https://openai.com/about/",
    "https://web.archive.org/web/20240501003757/https://openai.com/about/"
]

output_folder = "websiteImages"

if not os.path.exists(output_folder):
    os.makedirs(output_folder)

i = 1
for url in urls:
    output_file = os.path.join(output_folder, "version" + str(i) + ".png")
    
    capture_and_crop_screenshot(url, output_file, crop_height=135)
    
    i += 1
