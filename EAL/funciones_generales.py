from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

#aqui se debe de poner la función que saca los logs
#aqui se debe de poner la funcion que saca las capturas de pantalla
#aqui se debe de poner la función para esperar


class BasePage:
    def __init__(self, driver):
        self.driver = driver
        # Tiempo de espera general de 10 segundos
        self.wait = WebDriverWait(self.driver, 10)

    def encontrar_elemento(self, locator):
        """Espera a que el elemento sea visible y lo devuelve"""
        return self.wait.until(EC.visibility_of_element_located(locator))

    def clic(self, locator):
        """Hace clic en un elemento de forma segura"""
        elemento = self.encontrar_elemento(locator)
        elemento.click()

    def escribir_texto(self, locator, texto):
        """Limpia el campo y escribe el texto"""
        elemento = self.encontrar_elemento(locator)
        elemento.clear()
        elemento.send_keys(texto)

    def obtener_texto(self, locator):
        """Devuelve el texto de un elemento"""
        return self.encontrar_elemento(locator).text