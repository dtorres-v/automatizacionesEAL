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




