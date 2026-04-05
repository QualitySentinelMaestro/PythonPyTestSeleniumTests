import os
from dotenv import load_dotenv

load_dotenv()


class TestDat:
    CHROME_EXECUTABLE_PATH = os.getenv("CHROME_EXECUTABLE_PATH", "/usr/local/bin/chromedriver")
    BASE_URL = os.getenv("BASE_URL", "https://app.hubspot.com/login")
    USERNAME = os.getenv("TEST_USERNAME")
    PASSWORD = os.getenv("TEST_PASSWORD")
