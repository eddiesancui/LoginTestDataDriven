import openpyxl
import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
import os
from datetime import datetime

# Create screenshot folder
SCREENSHOT_DIR = "screenshots"
os.makedirs(SCREENSHOT_DIR, exist_ok=True)

def get_timestamp():
    return datetime.now().strftime("%Y%m%d_%H%M%S")

def take_screenshot(driver, step_name):
    filename = f"{SCREENSHOT_DIR}/step_{step_name}_{get_timestamp()}.png"
    driver.save_screenshot(filename)
    print(f"Screenshot saved: {filename}")

def get_test_data_from_excel(file_path):
    workbook = openpyxl.load_workbook(file_path)
    sheet = workbook.active
    data = []
    for row in sheet.iter_rows(min_row=2, values_only=True):
        data.append(row)
    return data

@pytest.mark.parametrize("username,password", get_test_data_from_excel("testdata.xlsx"))
def test_login(username, password):
    driver = webdriver.Chrome(ChromeDriverManager().install())
    driver.get("https://example.com/login")
    take_screenshot(driver, "01_open_login_page")

    driver.find_element(By.ID, "//input[@placeholder='Username']").send_keys(username)
    take_screenshot(driver, "02_enter_username")

    driver.find_element(By.ID, "//input[@placeholder='Password']").send_keys(password)
    take_screenshot(driver, "03_enter_password")

    driver.find_element(By.ID, "//button[normalize-space()='Login']").click()
    take_screenshot(driver, "04_after_click_login")

    # Example assertion (customize as needed)
    assert "dashboard" in driver.current_url or "error" in driver.page_source.lower()
    take_screenshot(driver, "05_after_assertion")

    driver.quit()
