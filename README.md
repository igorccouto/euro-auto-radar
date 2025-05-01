# Euro Auto Radar

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE) 
[![Python](https://img.shields.io/badge/Python-3.12+-blue.svg)](https://www.python.org/downloads/release/python-370/) ![GitHub last commit](https://img.shields.io/github/last-commit/igorccouto/euro-auto-radar)

A Python project to help car buyers in Portugal (and later other countries) find the best car for their needs. It automates data gathering and filtering from multiple car listing websites.

## Features
- Scrape car data from OLX, StandVirtual, PiscaPisca, Carmine, and more
- Modular browser automation using Selenium
- Car data model and filtering
- Easily extendable to other countries (e.g., Germany)
- Statistics like mean price value

## Setup
1. Create and activate a virtual environment:
   ```bash
   python3 -m venv venv
   source venv/bin/activate
   ```
2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

## Usage
- Implement specific browser classes in `euro_auto_radar/browsers/` for each website.
- Use the `Car` and `CarFilter` models to manage and filter car data.

## Project Structure
- `browsers/`: Selenium automation for each car website
- `models/`: Data models for cars and filters
- `utils/`: Utility functions
- `tests/`: Unit tests

---

## License
MIT
