from EAL import FuncionesGralEAL, VariablesGralEAL
from EAL.FuncionesGralEAL import driver, wait, AppiumBy, EC, Log

funciones = FuncionesGralEAL.funciones()
variables = VariablesGralEAL

client_id = """ añadir id del cliente de venta de crédito"""

class VentaDeCredito:

    def ingresar_app(self):
        try:
            funciones.ingreso_app()
            Log().info("Se accedió a la app")
        except Exception as e:
            Log().error(f"No se logró acceder a la app, validar el error: {e}")
            raise

    def cargar_base(self):
        try:
            # Corrección: Agregado AppiumBy.ANDROID_UIAUTOMATOR para formar la tupla
            cargar = wait.until(
                EC.element_to_be_clickable((AppiumBy.ANDROID_UIAUTOMATOR, variables.btn_cargar)))
            cargar.click()
        except Exception as e:
            Log().error(f"No se logro dar click al botón cargar, validar el error: {e}")
            raise

    def ingresar_ruta_credito(self):
        try:
            # No es necesario llamar ingreso_app de nuevo si ya se llamó antes,
            # pero si el flujo lo requiere, está bien.
            # funciones.ingreso_app()

            # Corrección: Llamar a la función específica de CRÉDITO
            funciones.ingreso_ruta_credito()
            Log().info("Se ingresó a la ruta crédito")
        except Exception as e:
            Log().error(f"No se logró acceder a la ruta de crédito, validar el error: {e}")
            raise

    def get_id_button(self, client_id: str) -> tuple:
        """Retorna el localizador para un cliente específico por su ID."""
        locator_client_id = (AppiumBy.ANDROID_UIAUTOMATOR,
                             f'new UiSelector().className("android.widget.TextView").text("{client_id}")')
        return locator_client_id

    def escoger_cliente(self, client_id):
        try:
            locator = self.get_id_button(client_id)
            client_btn = wait.until(EC.element_to_be_clickable(locator))
            client_btn.click()
            Log().info(f"Se seleccionó el cliente {client_id}")
        except Exception as e:
            Log().error(f"No se logró hacer clic en el cliente, validar el error: {e}")
            raise

    def iniciar_visita(self):
        try:
            funciones.inicio_visita()
        except Exception as e:
            Log().error(f"No se logró iniciar visita, validar el error: {e}")
            raise

    def iniciar_venta_de_credito(self):
        try:
            funciones.venta_credito()
        except Exception as e:
            Log().error(f"No se logró iniciar venta de crédito, validar el error: {e}")
            raise

    # =======================================================================
    '''Espacio para poner funciones que falten'''

    #preventa
    el6 = driver.find_element(by=AppiumBy.ANDROID_UIAUTOMATOR, value="new UiSelector().text(\"202299\")")
    el6.click()
    el7 = driver.find_element(by=AppiumBy.ANDROID_UIAUTOMATOR, value="new UiSelector().text(\"Nuevo documento...\")")
    el7.click()
    el8 = driver.find_element(by=AppiumBy.ANDROID_UIAUTOMATOR, value="new UiSelector().text(\"Preventa Credito\")")
    el8.click()

    #mandar como pendiente
    el9 = driver.find_element(by=AppiumBy.ANDROID_UIAUTOMATOR,
                              value="new UiSelector().className(\"android.widget.ImageButton\").instance(1)")
    el9.click()
    #falla preventa
    el10 = driver.find_element(by=AppiumBy.ID, value="android:id/button2")
    el10.click()

    #revisar documentos pendientes
    el11 = driver.find_element(by=AppiumBy.CLASS_NAME, value="android.widget.ImageView")
    el11.click()
    el12 = driver.find_element(by=AppiumBy.ANDROID_UIAUTOMATOR, value="new UiSelector().text(\"Documentos\")")
    el12.click()
    el13 = driver.find_element(by=AppiumBy.ANDROID_UIAUTOMATOR,
                               value="new UiSelector().text(\"Gestionar Documentos Pendientes\")")
    el13.click()

    # =======================================================================

    def finalizar_visita(self):
        try:
            funciones.final_visita()
            Log().info("Se finalizó la visita")
        except Exception as e:
            Log().error(f"No se logró crear el documento de final de visita, validar el error: {e}")
            raise

    def descargar(self):
        try:
            btn_descargar = wait.until(EC.element_to_be_clickable((AppiumBy.ANDROID_UIAUTOMATOR, variables.btn_descargar)))
            btn_descargar.click()
            el10 = wait.until(EC.element_to_be_clickable((AppiumBy.ID, "android:id/button1")))
            el10.click()
            el11 = wait.until(EC.element_to_be_clickable((AppiumBy.ID, "android:id/button2")))
            el11.click()
        except Exception as e:
            Log().error(f"No se logró descargar la información, validar el error: {e}")
            raise

    def tomar_log(self, request):
        """Automatiza visualización de log"""
        try:
            funciones.boton_log(request)
            Log().info("Se tomó el log de la aplicación")
        except Exception as e:
            Log().error(f"No se logró dar click al botón log, validar el error: {e}")

    def test_venta_credito(self):
        self.ingresar_app()
        self.cargar_base()
        self.driver.ingresar_ruta_credito()
        self.get_id_button(client_id)
        self.escoger_cliente(client_id)
        self.iniciar_visita()
        self.iniciar_venta_de_credito()
        self.finalizar_visita()
        """espacio para las demás funciones"""
        self.descargar()
        self.tomar_log()