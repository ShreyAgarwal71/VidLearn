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
    "https://www.amazon.com/ref=nav_logo",
    "https://www.microsoft.com/en-us/windows?r=1",
    "https://www.boringcompany.com/",
    "https://www.celsius.com/",
    "https://www.hotels.com/"
]

output_folder = "websiteImages"

if not os.path.exists(output_folder):
    os.makedirs(output_folder)

i = 1
for url in urls:
    output_file = os.path.join(output_folder, "version_" + str(i) + ".png")
    
    capture_and_crop_screenshot(url, output_file, crop_height=0)
    
    i += 1
