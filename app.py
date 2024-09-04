from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
import random
import os
import platform
import logging
import requests  # Library to check for internet connection
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
from selenium.common.exceptions import WebDriverException, NoSuchWindowException

# Initialize logging to store the history of runs
logging.basicConfig(filename='history.log', level=logging.INFO, 
                    format='%(asctime)s - %(message)s')

# Function to check for internet connection
def check_internet():
    """
    This function checks if the device is connected to the internet by attempting to reach Google.
    If the connection fails, the script will stop and ask the user to check their connection.
    """
    url = "http://www.google.com"
    timeout = 5
    try:
        requests.get(url, timeout=timeout)
        return True
    except (requests.ConnectionError, requests.Timeout):
        return False

# Function to set up ChromeDriver based on the OS
def setup_driver():
    """
    This function sets up the ChromeDriver with maximized window settings using WebDriver Manager 
    to automatically manage the installation of the correct driver version.
    """
    chrome_options = Options()
    chrome_options.add_argument("--start-maximized")  # Maximize the browser window
    service = Service(ChromeDriverManager().install())  # Install WebDriver Manager automatically
    driver = webdriver.Chrome(service=service, options=chrome_options)
    return driver

# Function to search for Selenium tutorials on YouTube
def search_youtube(driver):
    """
    This function searches YouTube for random Selenium tutorial videos, selects the first video 
    from the results, and logs the details of the video title.
    """
    search_terms = [
        'Selenium tutorial for beginners',
        'Selenium automation projects',
        'Selenium WebDriver examples',
        'Selenium Python guide'
    ]
    
    # Choose a random search term each time the script runs
    search_query = random.choice(search_terms)
    driver.get('https://www.youtube.com')
    time.sleep(2)

    # Find the search box, input the search query, and press Enter
    search_box = driver.find_element(By.NAME, 'search_query')
    search_box.send_keys(search_query)
    search_box.send_keys(Keys.RETURN)
    time.sleep(3)

    # Select the first video result
    try:
        first_video = driver.find_elements(By.ID, 'video-title')[0]
        video_title = first_video.get_attribute('title')
        if not video_title:
            raise ValueError("The video is unavailable or cannot be played.")
        first_video.click()
        
        # Log the run details with video title
        logging.info(f'Played video: {video_title}, Search term: {search_query}')
        print(f'Playing video: {video_title}')

    except IndexError:
        print("No videos found for the search term.")
        logging.error("No videos found for the search term.")
        return

# Function to handle potential errors and keep the browser open
def run_script():
    """
    This is the main function that runs the entire script. It checks for internet connection, sets up
    the driver, searches for YouTube videos, plays them, and handles any errors that occur. The script 
    will refresh the terminal after the browser closes.
    """
    if not check_internet():
        print("No internet connection. Please check your connection and try again.")
        return

    try:
        driver = setup_driver()  # Set up the Chrome browser
        search_youtube(driver)  # Perform a search on YouTube and play a video
        
        # Keep the video running, simulate the user watching it
        time.sleep(10)
        
        # Make the video fullscreen (YouTube's 'f' key is the shortcut for fullscreen)
        driver.find_element(By.TAG_NAME, 'body').send_keys('f')
        print('Video is now in fullscreen mode.')
        
        # Wait for the user to close the tab manually
        while True:
            try:
                driver.title  # Try to access the page title to ensure the browser is open
            except (WebDriverException, NoSuchWindowException):
                break  # If the tab is closed, break the loop
            time.sleep(1)
    except Exception as e:
        # Print the error and log it for troubleshooting
        print(f"An error occurred: {e}. Please try again or contact support.")
        logging.error(f"An error occurred: {e}")
    finally:
        # Close the driver when done
        try:
            driver.quit()
        except:
            pass
        print("Browser closed, you can re-run the script by clicking Play in VS Code.")
        
        # Refresh the terminal after browser closes
        refresh_terminal()

# Function to refresh the terminal after the browser closes
def refresh_terminal():
    """
    This function clears and refreshes the terminal window based on the operating system, 
    preparing it for another run of the script.
    """
    if platform.system() == 'Windows':
        os.system('cls')
    else:
        os.system('clear')
    print("Terminal refreshed, ready to run the script again.")

if __name__ == "__main__":
    # Run the script and handle terminal refreshing
    run_script()
