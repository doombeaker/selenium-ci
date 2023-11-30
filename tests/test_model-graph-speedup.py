from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

options = webdriver.ChromeOptions()
driver = webdriver.Remote(
    command_executor="http://127.0.0.1:4444/wd/hub", options=options
)

try:
    # 打开网页
    driver.get("http://127.0.0.1:8188")

    queue_button = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.ID, "queue-button"))
    )

    queue_button.click()

except Exception as e:
    print(e)
    print("exit with error: 1")
    exit(1)
finally:
    driver.quit()
