import logging
from appium import webdriver
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.common.keys import Keys
from time import sleep

# Configure logging
logging.basicConfig(level=logging.INFO, format='%(message)s')
logger = logging.getLogger(__name__)

def main():
    try:
        logger.info("🚀 Starting WebPageTest analysis...")
        
        # Firefox configuration
        firefox_options = Options()
        firefox_options.add_argument("--headless")
        firefox_options.add_argument("--no-sandbox")
        firefox_options.add_argument("--disable-dev-shm-usage")
        firefox_options.binary_location = "/usr/bin/firefox"

        # Set capabilities
        firefox_options.set_capability("platformName", "linux")
        firefox_options.set_capability("browserName", "firefox")
        firefox_options.set_capability("appium:automationName", "gecko")

        logger.info("🔌 Initializing WebDriver...")
        driver = webdriver.Remote(
            command_executor='http://localhost:4723',
            options=firefox_options
        )

        logger.info("🌐 Navigating to WebPageTest.org...")
        driver.get("https://www.webpagetest.org")
        sleep(3)

        # Scroll down to the test input section
        logger.info("🖱️ Scrolling to input section...")
        driver.execute_script("window.scrollTo(0, 500)")
        sleep(2)

        # Find the URL input field using CSS selector
        logger.info("🔍 Locating input field...")
        url_input = driver.find_element("css selector", "input#url")
        
        # Clear and enter the test URL
        logger.info("⌨️ Entering test URL...")
        url_input.clear()
        url_input.send_keys("flintlab.io")
        sleep(1)

        # Submit by pressing ENTER
        logger.info("↩️ Pressing ENTER to submit...")
        url_input.send_keys(Keys.RETURN)
        
        # Simply wait 60 seconds without any checks
        logger.info("⏳ Waiting exactly 60 seconds...")
        sleep(5)

        # Take screenshot after 60 seconds
        screenshot_path = "/tmp/webpagetest_after_60s.png"
        driver.save_screenshot(screenshot_path)
        logger.info(f"📸 Screenshot saved to {screenshot_path}")

    except Exception as e:
        logger.error(f"❌ Test failed: {str(e)}")
        raise
    finally:
        if 'driver' in locals():
            driver.quit()
        logger.info("✅ Test completed")

if __name__ == "__main__":
    main()
