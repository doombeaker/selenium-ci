from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# 初始化 WebDriver，这里以 Chrome 为例
driver = webdriver.Chrome()
print("selenium test in Python!!!")
# # 打开网页
# driver.get("http://127.0.0.1:8188")

# # 等待按钮加载完成
# queue_button = WebDriverWait(driver, 10).until(
#     EC.element_to_be_clickable((By.ID, "queue-button"))
# )

# # 点击按钮
# queue_button.click()

# 关闭浏览器
driver.quit()