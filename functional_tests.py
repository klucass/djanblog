from selenium import webdriver


browser = webdriver.Firefox(executable_path='C:\geckodriver\geckodriver.exe')
browser.get('http://localhost:8000')

# Testa se o django foi instalado com sucesso
assert 'successfully' in browser.title