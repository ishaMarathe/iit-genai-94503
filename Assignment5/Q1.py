from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import json

driver = webdriver.Chrome()

driver.get("https://www.sunbeaminfo.in/internship")
time.sleep(3)  

print("\n_____________Page Title_____________\n", driver.title)

driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
time.sleep(2)

plus_button = driver.find_element(By.XPATH,"//a[@href='#collapseSix']")
driver.execute_script("arguments[0].scrollIntoView(true);", plus_button)
time.sleep(1)
plus_button.click()

time.sleep(2)

print("\n_____________Internship Information_____________\n")
para = driver.find_elements(By.CSS_SELECTOR,".main_info.wow.fadeInUp")
for p in para:
    print(p.text)

print("\n______________Internship Batches_____________\n")
rows = driver.find_elements(By.TAG_NAME,"tr")

batches = []

for row in rows:
    cols = row.find_elements(By.TAG_NAME,"td")
    if len(cols) < 8:
        continue

    batches.append({
        "sr": cols[0].text,
        "batch": cols[1].text,
        "batch duration": cols[2].text,
        "start date": cols[3].text,
        "end date": cols[4].text,
        "time": cols[5].text,
        "fees": cols[6].text,
        "download": cols[7].text
    })

print(json.dumps(batches, indent=4))

time.sleep(5) 
driver.quit()
