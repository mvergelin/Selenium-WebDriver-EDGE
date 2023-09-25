from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.edge.options import Options
import time

# Configura opciones de Edge
edge_options = webdriver.EdgeOptions()

# Acepta certificados no seguros
edge_options.accept_insecure_certs = True

# Crea una instancia del navegador Edge con las capacidades personalizadas
driver = webdriver.Edge(options=edge_options)

#Accede a MCP CIENA con la config precargada en el link
driver.get('https://172.22.52.20/alarms/#/?autoRefresh=false&contextState=TIME%20SEARCH&filters=%7B%22allTime%22%3A%222023-05-01T17%3A00%3A52-03%3A00%2C2023-09-21T17%3A07%3A52-03%3A00%22%2C%22state%22%3A%5B%22ACTIVE%22%2C%22CLEARED%22%2C%22SUPERSEDED%22%5D%2C%22additionalText%22%3A%5B%7B%22label%22%3A%22Loss%20Of%20Signal%22%2C%22value%22%3A%22Loss%20Of%20Signal%22%7D%5D%7D')

#Ejemplo que permite usar el buscador de bing y dar search
#element = driver.find_element(By.ID, 'sb_form_q')
#element.send_keys('DatoBuscar')
#element.submit()

#### PROCESO DE LOGIN DE MCP
# Encuentra los campos de usuario y contraseña por su nombre o etiqueta HTML
username_field = WebDriverWait(driver, 5).until(
    EC.presence_of_element_located((By.ID, "ember24"))
)
password_field = WebDriverWait(driver, 5).until(
    EC.presence_of_element_located((By.ID, "ember32"))
)

# Ingresa tu nombre de usuario y contraseña
username_field.send_keys("mvergelin")
password_field.send_keys("Vida.Linda.26")

# Envía el formulario de inicio de sesión por busqueda de ID
login_button = WebDriverWait(driver, 5).until(
    EC.presence_of_element_located((By.ID, "ember13"))
)
login_button.click()

# Espera unos segundos para que la página de inicio de sesión procese la información
driver.implicitly_wait(5)

##### FIN LOGIN

##### ESPERA Y DESCARGA REPORTE CSV
time.sleep(10)

export_csv = WebDriverWait(driver, 5).until(
    EC.presence_of_element_located((By.ID, "ember109"))
)
export_csv.click()

time.sleep(10)

#links = driver.find_elements("xpath", "//a[@href]")
#for link in links:
#    print(link.get_attribute("innerHTML"))

#driver.quit()