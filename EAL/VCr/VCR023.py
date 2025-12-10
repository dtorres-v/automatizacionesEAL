from EAL import FuncionesGralEAL, VariablesGralEAL
from FuncionesGralEAL import *
from VariablesGralEAL import *

funciones = FuncionesGralEAL.funciones
variables = VariablesGralEAL

client_id = "278170"


class VentadeCredito:

    def ingresar_app(self):
        try:
            funciones.ingreso_app()
            Log().info("Se accedió a la app")
        except Exception as e:  # pragma: no cover
            Log().error(f"No se logró acceder a la app, validar el error: {e}")
            raise

    def cargar_base(self):
        try:
            cargar = wait.until(
                EC.element_to_be_clickable((AppiumBy.ANDROID_UIAUTOMATOR, ConfiguracionEAL.btn_cargar)))
            cargar.click()
        except Exception as e:  # pragma: no cover
            Log().error(f"No se logro dar click al botón cargar, validar el error: {e}")
            raise

    def ingresar_ruta_credito(self):

        try:
            funciones.ingreso_app()
            Log().info("Se accedió a la app")
        except Exception as e:  # pragma: no cover
            Log().error(f"No se logró acceder a la app, validar el error: {e}")
            raise
        try:
            funciones.ingreso_ruta()
            Log().info("Se ingresó a la ruta crédito")
        except Exception as e:  # pragma: no cover
            Log().error(f"No se logró acceder a la ruta de crédito, validar el error: {e}")
            raise

    def get_id_button(self, client_id: str) -> tuple:
        """Retorna el localizador para un cliente específico por su ID."""
        locator_client_id = (AppiumBy.ANDROID_UIAUTOMATOR,
                             f'new UiSelector().className("android.widget.TextView").text("{client_id}")')
        return locator_client_id

    def escoger_cliente(self, client_id):
        try:
            client_btn = self.get_id_button(client_id)
            client_btn.click()
        except Exception as e:  # pragma: no cover
            Log().error(f"No se logró hacer clic en el cliente, validar el error: {e}")
            raise

    def iniciar_visita(self):
        try:
            funciones.inicio_visita()
        except Exception as e:  # pragma: no cover
            Log().error(f"No se logró iniciar visita, validar el error: {e}")
            raise

    def iniciar_venta_de_credito(self):
        try:
            funciones.venta_credito()
        except Exception as e:  # pragma: no cover
            Log().error(f"No se logró iniciar venta de crédito, validar el error: {e}")
            raise

    # =======================================================================

    '''Espacio para poner funciones que falten'''


    #añadir articulos buscando por código
    el6 = driver.find_element(by=AppiumBy.ANDROID_UIAUTOMATOR,
                              value="new UiSelector().className(\"android.widget.ImageButton\").instance(0)")
    el6.click()
    el7 = driver.find_element(by=AppiumBy.ANDROID_UIAUTOMATOR,
                              value="new UiSelector().className(\"android.widget.ImageButton\").instance(2)")
    el7.click()
    el8 = driver.find_element(by=AppiumBy.ANDROID_UIAUTOMATOR,
                              value="new UiSelector().text(\"Buscar por descripción\")")
    el8.click()
    el9 = driver.find_element(by=AppiumBy.ANDROID_UIAUTOMATOR, value="new UiSelector().text(\"Buscar por código\")")
    el9.click()
    el10 = driver.find_element(by=AppiumBy.CLASS_NAME, value="android.widget.EditText")
    el10.send_keys("FA01002")
    el11 = driver.find_element(by=AppiumBy.CLASS_NAME, value="android.widget.Button")
    el11.click()
    el12 = driver.find_element(by=AppiumBy.ANDROID_UIAUTOMATOR, value="new UiSelector().text(\"Usr: FA01002\")")
    el12.click()
    el13 = driver.find_element(by=AppiumBy.ANDROID_UIAUTOMATOR,
                               value="new UiSelector().text(\"MARLBORO GOLD KS BOX 20 - FA01002\")")
    el13.click()
    el15 = driver.find_element(by=AppiumBy.ANDROID_UIAUTOMATOR,
                               value="new UiSelector().className(\"android.widget.EditText\").instance(0)")
    el15.click()
    el15.send_keys("3")
    el16 = driver.find_element(by=AppiumBy.ANDROID_UIAUTOMATOR, value="new UiSelector().text(\"Aceptar\")")
    el16.click()
    el17 = driver.find_element(by=AppiumBy.ANDROID_UIAUTOMATOR,
                               value="new UiSelector().className(\"android.widget.ImageButton\").instance(1)")
    el17.click()


    el18 = driver.find_element(by=AppiumBy.ANDROID_UIAUTOMATOR,
                               value="new UiSelector().className(\"android.widget.ImageButton\").instance(3)")
    el18.click()

    #get total

    # Emitir
    el19 = driver.find_element(by=AppiumBy.ANDROID_UIAUTOMATOR,
                               value="new UiSelector().className(\"android.widget.ImageButton\").instance(0)")
    el19.click()

    #popups
    el20 = driver.find_element(by=AppiumBy.ID, value="android:id/button2")
    el20.click()
    el21 = driver.find_element(by=AppiumBy.ID, value="android:id/button2")
    el21.click()

    #Revisar en documentos emitidos
    el22 = driver.find_element(by=AppiumBy.CLASS_NAME, value="android.widget.ImageView")
    el22.click()
    el23 = driver.find_element(by=AppiumBy.ANDROID_UIAUTOMATOR, value="new UiSelector().text(\"Documentos\")")
    el23.click()
    el24 = driver.find_element(by=AppiumBy.ANDROID_UIAUTOMATOR,
                               value="new UiSelector().text(\"Gestionar Documentos Emitidos\")")
    el24.click()
    #todo rear variable para el total
    el25 = driver.find_element(by=AppiumBy.ANDROID_UIAUTOMATOR, value="new UiSelector().text(\"2023.97\")")
    el25.click()

    #regresar a la pantalla anterior
    driver.execute_script('mobile:pressKey', {"keycode": 4})

    #regresar a HomePage
    driver.execute_script('mobile:pressKey', {"keycode": 4})
    el26 = driver.find_element(by=AppiumBy.ID, value="android:id/button1")
    el26.click()

    #actualizar
    el27 = driver.find_element(by=AppiumBy.ANDROID_UIAUTOMATOR,
                               value="new UiSelector().className(\"android.widget.RelativeLayout\").instance(4)")
    el27.click()
    #esperar explicitamente
    #aceptar confirmacion de la descarga
    el28 = driver.find_element(by=AppiumBy.ID, value="android:id/button2")
    el28.click()

    # esperar explicitamente
    #aceptar carga
    el29 = driver.find_element(by=AppiumBy.ID, value="android:id/button1")
    el29.click()

    # esperar explicitamente
    #aceptar finalizacion de la carga
    el30 = driver.find_element(by=AppiumBy.ID, value="android:id/button2")
    el30.click()
    el31 = driver.find_element(by=AppiumBy.ID, value="android:id/button2")
    el31.click()








    # =======================================================================

    def finalizar_visita(self):
        try:
            funciones.final_visita()
            Log().info("Se finalizó la visita")
        except Exception as e:  # pragma: no cover
            Log().error(f"No se logró crear el documento de final de visita, validar el error: {e}")
            raise

    def descargar(self):
        try:
            btn_descargar = wait.until(EC.element_to_be_clickable(VariablesGralEAL.btn_descargar))
            btn_descargar.click()
            el10 = driver.find_element(by=AppiumBy.ID, value="android:id/button1")
            el10.click()
            el11 = driver.find_element(by=AppiumBy.ID, value="android:id/button2")
            el11.click()
        except Exception as e:  # pragma: no cover
            Log().error(f"No se logró descargar la información, validar el error: {e}")
            raise

    def tomar_log(self, request):
        """Automatiza visualización de log"""
        try:
            funciones.boton_log(request)
            Log().info("Se tomó el log de la aplicación")
        except Exception as e:  # pragma: no cover
            Log().error(f"No se logró dar click al botón log, validar el error: {e}")




