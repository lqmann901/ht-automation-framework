# 🎭 Playwright Mini Framework

A lightweight and modular UI automation framework built using **Playwright** + **Pytest** in Python. Ideal for personal projects, learning purposes, and small-to-mid scale UI testing.

---

## 📁 Project Structure

ht-automation-framework/
├── pages/ # Page Object classes (e.g., LoginPage)
├── tests/ # Pytest test scripts
├── utils/ # Driver factory, base test setup
├── data/ # Test data (JSON)
├── reports/ # Test output (optional)
├── conftest.py # Pytest config & fixtures
├── requirements.txt # Dependencies
└── README.md

🧪 Features
✅ Built with Page Object Model (POM)

✅ Support for Chromium and Firefox

✅ Reusable driver setup using factory pattern

✅ Works in headless and headed mode

✅ Lightweight, readable, and easy to extend

🙋‍♂️ Author
Le Quang Man
📧 lequangman9001@gmail.com
🔗 https://github.com/lqmann901

---

## 📌 Future Improvements

- [ ] Add Allure report integration
- [ ] Add API testing module using `requests` + `pytest`
- [ ] Improve test data management (CSV/YAML)
- [ ] Introduce test tagging and filtering (`pytest -m`)
- [ ] Add browser/device emulation presets (mobile/tablet)

---

## 🔄 CI/CD Integration (Planned)

- GitHub Actions workflow for:
  - ✅ Auto-run tests on push & pull request
  - ✅ Run on both Chromium and Firefox
  - ✅ Collect artifacts & test reports

> CI/CD setup will be added soon for automated testing and reporting.
