from pages.base_page import BasePage
from pages.locators import HomeLocators


class HomePage(BasePage):

    def __init__(self, driver):
        super().__init__(driver)  # Inicializa la clase padre

    def realizar_login(self, usuario):
        """Función única que agrupa pasos lógicos"""
        # Usamos los métodos generales que creamos en BasePage
        self.escribir_texto(HomeLocators.INPUT_USUARIO, usuario)
        self.clic(HomeLocators.BTN_LOGIN)

    def es_mensaje_visible(self):
        """Verifica si el login fue exitoso leyendo un texto"""
        return self.obtener_texto(HomeLocators.TXT_BIENVENIDA)