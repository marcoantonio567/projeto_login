# Login Project (Flask) + Automation (Selenium)

A simple Python project with:

- A Flask web app with a login screen and an “index” page.
- A Selenium automation script that logs in and fills the form using data from an Excel spreadsheet.

## Tech Stack

- Python
- Flask ([app.py](file:///c:/Users/marco/Desktop/update_repositorio/projeto%20login/projeto_login/app.py))
- Selenium + OpenPyXL ([automatizacao.py](file:///c:/Users/marco/Desktop/update_repositorio/projeto%20login/projeto_login/automatizacao.py))
- HTML/CSS in [templates](file:///c:/Users/marco/Desktop/update_repositorio/projeto%20login/projeto_login/templates) and [static](file:///c:/Users/marco/Desktop/update_repositorio/projeto%20login/projeto_login/static)

## Project Structure

- [app.py](file:///c:/Users/marco/Desktop/update_repositorio/projeto%20login/projeto_login/app.py): Flask app and routes
- [templates/html/login.html](file:///c:/Users/marco/Desktop/update_repositorio/projeto%20login/projeto_login/templates/html/login.html): login screen
- [templates/html/index.html](file:///c:/Users/marco/Desktop/update_repositorio/projeto%20login/projeto_login/templates/html/index.html): form page (UI)
- [automatizacao.py](file:///c:/Users/marco/Desktop/update_repositorio/projeto%20login/projeto_login/automatizacao.py): browser automation
- [produtos.xlsx](file:///c:/Users/marco/Desktop/update_repositorio/projeto%20login/projeto_login/produtos.xlsx): data used by the automation
- [requirements.txt](file:///c:/Users/marco/Desktop/update_repositorio/projeto%20login/projeto_login/requirements.txt): dependencies

## Run the App (Flask)

1. (Optional) Create and activate a virtual environment.
```bash
python -m venv venv
```
2. Install dependencies:

```bash
pip install -r requirements.txt
```

3. Run the server:

```bash
python app.py
```

1. Open:

- <http://127.0.0.1:5000>

## Test Credentials

Users are defined directly in code in [app.py](file:///c:/Users/marco/Desktop/update_repositorio/projeto%20login/projeto_login/app.py):

- `saitama` / `1234`
- `usuario2` / `senha2`
- `user1` / `bota00`

## Run the Automation (Selenium)

Prerequisites:

- The Flask server must be running at <http://127.0.0.1:5000>
- Firefox installed
- `geckodriver` available in your PATH (required for Selenium to control Firefox)

Run:

```bash
python automatizacao.py
```

The script:

- Opens the browser
- Logs in with `saitama` / `1234`
- Reads [produtos.xlsx](file:///c:/Users/marco/Desktop/update_repositorio/projeto%20login/projeto_login/produtos.xlsx) and fills the index page form

## Notes

- This is a demo/learning project: credentials are stored in plain text in the code and there is no database persistence.

