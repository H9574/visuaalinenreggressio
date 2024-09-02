from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.common.exceptions import TimeoutException
from webdriver_manager.chrome import ChromeDriverManager
import os
from pathlib import Path

#example:
#capture_screenshot('https://www.punainenristi.fi', 'screenshots/testi5.png')
def capture_screenshot(url, path):
    try:
        options = webdriver.ChromeOptions()
        options.add_argument('--headless')
        options.add_argument('--disable-gpu')
        #options.add_argument('--window-size=1920,1080')

        driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()), options=options)
        driver.get(url)
        # define a function to get scroll dimensions
        def get_scroll_dimension(axis):
            return driver.execute_script(f"return document.body.parentNode.scroll{axis}")
        # get the page scroll dimensions
        width = get_scroll_dimension("Width")
        height = get_scroll_dimension("Height")
        # set the browser window size
        driver.set_window_size(width, height)
        # Wait for the page to fully load by checking document readiness
        try:
            WebDriverWait(driver, 10).until(
                lambda driver: driver.execute_script("return document.readyState") == "complete"
            )
        except TimeoutException:
            print("Timeout, page took too long to load!")
            print(url)
            driver.quit()
        driver.save_screenshot(path)
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
    finally:
        # Close the browser
        driver.quit()

def screenshots_didnt_match(current_file_path, new_file_path, directory):
    # Rename the file
    try:
        # Create a new directory
        Path(directory).mkdir(parents=True, exist_ok=True)
        # add screenshots to directory
        os.rename(current_file_path, new_file_path)
        print(f"Screenshot renamed successfully to {new_file_path}")
    except FileNotFoundError:
        print(f"Error: The screenshot {current_file_path} was not found.")
    except PermissionError:
        print(f"Error: Permission denied for renaming {current_file_path}.")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
