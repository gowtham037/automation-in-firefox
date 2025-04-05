import logging
from appium import webdriver
from selenium.webdriver.firefox.options import Options
from time import sleep

# Configure logging
logging.basicConfig(level=logging.INFO, format='%(message)s')
logger = logging.getLogger(__name__)

def main():
    try:
        logger.info("🚀 Starting test...")
        
        # Firefox configuration (same structure as Chrome)
        firefox_options = Options()
        firefox_options.add_argument("--headless")
        firefox_options.add_argument("--no-sandbox")
        firefox_options.add_argument("--disable-dev-shm-usage")
        firefox_options.binary_location = "/usr/bin/firefox"

        # Set REQUIRED capabilities as options (same structure)
        firefox_options.set_capability("platformName", "linux")
        firefox_options.set_capability("browserName", "firefox")
        firefox_options.set_capability("appium:automationName", "gecko")

        logger.info("🔌 Initializing WebDriver...")
        driver = webdriver.Remote(
            command_executor='http://localhost:4723',
            options=firefox_options  # Using ONLY options
        )

        logger.info("🌐 Navigating to YouTube...")
        driver.get("https://www.youtube.com")
        sleep(3)

        screenshot_path = "/tmp/firefox_success.png"
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
