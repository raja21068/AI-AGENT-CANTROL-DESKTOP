from selenium import webdriver
from selenium.webdriver.common.by import By

def fill_form_and_upload_document(url, form_data, file_path, driver_path='path_to_driver'):
    driver = webdriver.Chrome(executable_path=driver_path)
    driver.get(url)
    for field, value in form_data.items():
        input_element = driver.find_element(By.NAME, field)
        input_element.send_keys(value)
    upload_field = driver.find_element(By.NAME, 'file_upload')
    upload_field.send_keys(file_path)
    driver.find_element(By.CSS_SELECTOR, 'button[type="submit"]').click()
    print("Form submitted and file uploaded!")
    driver.quit()
