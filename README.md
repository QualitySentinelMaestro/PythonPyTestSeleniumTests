# 🧪 Python PyTest Selenium Test Suite

> **End-to-end UI automation** for web applications using **Page Object Model (POM)** + **PyTest** — structured, maintainable, and CI-ready.

![Python](https://img.shields.io/badge/Python-3.11+-3776AB?style=flat&logo=python&logoColor=white)
![Selenium](https://img.shields.io/badge/Selenium-4.x-43B02A?style=flat&logo=selenium)
![PyTest](https://img.shields.io/badge/PyTest-8.x-0A9EDC?style=flat&logo=pytest)
![POM](https://img.shields.io/badge/Pattern-Page%20Object%20Model-blueviolet?style=flat)

---

## 🧠 Problem → Solution

| Problem | Solution |
|--------|---------|
| UI test scripts become brittle and hard to maintain | Page Object Model separates UI locators from test logic |
| Tests tightly coupled to hardcoded credentials | Environment variables via `.env` — no secrets in code |
| No structured reporting for stakeholders | PyTest's built-in reporting + fixtures for clean setup/teardown |

---

## ⚙️ Tech Stack

| Tool | Purpose |
|------|---------|
| **Python 3.11+** | Core language |
| **Selenium 4** | Browser automation |
| **PyTest** | Test runner & fixture management |
| **Page Object Model** | Design pattern for maintainable tests |
| **python-dotenv** | Environment-based credential management |
| **ChromeDriver** | Chrome browser driver |

---

## 📁 Project Structure

```
PythonPyTestSeleniumTests/
├── Config/
│   ├── config.py          # App config loaded from environment variables
│   └── __init__.py
├── Pages/                 # Page Object classes (one per page)
├── Pytestselenium/        # Core framework utilities
├── Tests/
│   ├── conftest.py        # PyTest fixtures (WebDriver setup/teardown)
│   ├── test_Base.py       # Base test class
│   ├── test_Homepage.py   # Homepage test scenarios
│   ├── test_Loginpage.py  # Login page test scenarios
│   └── __init__.py
├── .env.example           # Template for required environment variables
├── .gitignore
└── README.md
```

---

## 🚀 Setup & Run

### 1. Clone the repository
```bash
git clone https://github.com/QualitySentinelMaestro/PythonPyTestSeleniumTests.git
cd PythonPyTestSeleniumTests
```

### 2. Create a virtual environment
```bash
python -m venv .venv
source .venv/bin/activate   # Mac/Linux
# .venv\Scripts\activate    # Windows
```

### 3. Install dependencies
```bash
pip install selenium pytest python-dotenv
```

### 4. Install ChromeDriver

Download ChromeDriver matching your Chrome version from [chromedriver.chromium.org](https://chromedriver.chromium.org/downloads) and note its path.

### 5. Configure environment variables
```bash
cp .env.example .env
# Edit .env with your values
```

`.env.example`:
```
BASE_URL=https://your-app-url.com
USERNAME=your_test_username
PASSWORD=your_test_password
CHROME_EXECUTABLE_PATH=/path/to/chromedriver
```

### 6. Run the test suite
```bash
# Run all tests
pytest Tests/

# Run with verbose output
pytest Tests/ -v

# Run a specific test file
pytest Tests/test_Loginpage.py -v
```

---

## 🧩 Design Pattern — Page Object Model

Each page of the application has its own class in `Pages/`:

```python
class LoginPage:
    def __init__(self, driver):
        self.driver = driver
        self.username_field = (By.ID, "username")
        self.password_field = (By.ID, "password")
        self.login_button   = (By.CSS_SELECTOR, "button[type='submit']")

    def login(self, username, password):
        self.driver.find_element(*self.username_field).send_keys(username)
        self.driver.find_element(*self.password_field).send_keys(password)
        self.driver.find_element(*self.login_button).click()
```

Tests import page classes — **locators never leak into test files**.

---

## 🔮 Roadmap

- [ ] Add parallel execution with `pytest-xdist`
- [ ] Integrate Allure Reports for rich HTML reports
- [ ] Add GitHub Actions CI workflow
- [ ] Extend to Firefox / Edge cross-browser testing

---

## 🪪 License

MIT License — free to use and extend.
