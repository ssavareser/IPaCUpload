import streamlit as st
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager

URL = "http://example.com"  # Replace with your actual URL
TIMEOUT = 20

st.title("Test Selenium")

# Configure Chrome options
chrome_options = Options()
chrome_options.add_argument("--headless")
chrome_options.add_argument("--disable-gpu")
chrome_options.add_argument("--no-sandbox")
chrome_options.add_argument("--disable-dev-shm-usage")

# Set up ChromeDriver service
service = Service(ChromeDriverManager().install())

# Initialize WebDriver
driver = webdriver.Chrome(service=service, options=chrome_options)

# Open the URL
driver.get(URL)

# Optionally, you can use WebDriverWait and other Selenium features here
# Example of waiting for an element:
# wait = WebDriverWait(driver, TIMEOUT)
# element = wait.until(EC.presence_of_element_located((By.ID, "element_id")))

# Display page source in Streamlit
st.write(driver.page_source)

# Quit the browser session
driver.quit()

