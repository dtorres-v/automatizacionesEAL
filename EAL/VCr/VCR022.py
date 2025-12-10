import pytest
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time


# Conectamos con tu conftest.py
@pytest.mark.usefixtures("driver_setup")
class TestRecorder:

    # ---------------------------------------------------------
    # HELPER: Función WAIT
    # ---------------------------------------------------------
    def wait_for_element(self, by, value, timeout=20):
        """
        Helper para esperar explícitamente a un elemento.
        Usa self.driver que viene inyectado desde el conftest.
        """
        wait = WebDriverWait(self.driver, timeout)
        return wait.until(EC.visibility_of_element_located((by, value)))

    def test_run_recorder(self):

        driver = self.driver

        print("\n--- Iniciando Ejecución de Pasos Grabados ---")


        # ---------------------------------------------------------
        # ESPACIO PARA PEGAR CÓDIGO (APPIUM RECORDER)
        # ---------------------------------------------------------

        # Pega aquí directamente lo que te dio el Inspector.
        # No necesitas indentar nada especial ni poner try/except.
        # Asegúrate de sí usar la función self.wait_for_element(...) cuando sea requerida
        # el1 = self.wait_for_element(by=AppiumBy.CLASS_NAME, value="android.widget.Button")
        # el1.click()

        el1 = driver.find_element(by=AppiumBy.CLASS_NAME, value="android.widget.Button")
        el1.click()
        el2 = driver.find_element(by=AppiumBy.ACCESSIBILITY_ID, value="Usuario")
        el2.click()
        el2.send_keys("anevvv003")
        el3 = driver.find_element(by=AppiumBy.ACCESSIBILITY_ID, value="Contraseña")
        el3.click()
        el3.send_keys("Pwst12345*")
        el4 = driver.find_element(by=AppiumBy.ACCESSIBILITY_ID, value="Servidor")
        el4.click()
        el4.send_keys("m.assist.com.uy/mobileservices")
        driver.execute_script('mobile:pressKey', {"keycode": 4})
        el5 = driver.find_element(by=AppiumBy.CLASS_NAME, value="android.widget.CheckBox")
        el5.click()
        el6 = driver.find_element(by=AppiumBy.ANDROID_UIAUTOMATOR, value="new UiSelector().text(\"Instalar\")")
        el6.click()

        #wait for el boton cargar to be visible
        el7 = driver.find_element(by=AppiumBy.ANDROID_UIAUTOMATOR,
                                  value="new UiSelector().resourceId(\"uy.com.assist.eaf:id/imageButtonImage\").instance(1)")
        el7.click()

        #wait for the home button
        el8 = driver.find_element(by=AppiumBy.ANDROID_UIAUTOMATOR, value="new UiSelector().text(\"inicio\")")
        el8.click()

        #wait for the start button
        el9 = driver.find_element(by=AppiumBy.ANDROID_UIAUTOMATOR, value="new UiSelector().text(\"Iniciar\")")
        el9.click()

        #escoger ruta
        el10 = driver.find_element(by=AppiumBy.ANDROID_UIAUTOMATOR, value="new UiSelector().text(\"JUEVES\")")
        el10.click()
        el11 = driver.find_element(by=AppiumBy.ANDROID_UIAUTOMATOR, value="new UiSelector().text(\"JUEVES\")")
        el11.click()

        #escoger cliente por id
        el12 = driver.find_element(by=AppiumBy.ANDROID_UIAUTOMATOR, value="new UiSelector().text(\"202299\")")
        el12.click()

        #iniciar visita
        el13 = driver.find_element(by=AppiumBy.ANDROID_UIAUTOMATOR,
                                   value="new UiSelector().text(\"Nuevo documento...\")")
        el13.click()
        el14 = driver.find_element(by=AppiumBy.ANDROID_UIAUTOMATOR, value="new UiSelector().text(\"Inicio Visita\")")
        el14.click()
        el15 = driver.find_element(by=AppiumBy.ANDROID_UIAUTOMATOR,
                                   value="new UiSelector().className(\"android.widget.TextView\").instance(6)")
        el15.click()
        el16 = driver.find_element(by=AppiumBy.ANDROID_UIAUTOMATOR,
                                   value="new UiSelector().text(\"Etiqueta PDV dañada\")")
        el16.click()
        el17 = driver.find_element(by=AppiumBy.ANDROID_UIAUTOMATOR,
                                   value="new UiSelector().className(\"android.widget.ImageButton\").instance(0)")
        el17.click()

        #Checar saldo ccd
        el18 = driver.find_element(by=AppiumBy.CLASS_NAME, value="android.widget.Button")
        el18.click()
        el19 = driver.find_element(by=AppiumBy.ANDROID_UIAUTOMATOR, value="new UiSelector().text(\"2,023.97\")")
        #get the text
        el19.click()

        driver.execute_script('mobile:pressKey', {"keycode": 4})

        #venta de credito
        el21 = driver.find_element(by=AppiumBy.ANDROID_UIAUTOMATOR, value="new UiSelector().text(\"202299\")")
        el21.click()
        el22 = driver.find_element(by=AppiumBy.ANDROID_UIAUTOMATOR,
                                   value="new UiSelector().text(\"Nuevo documento...\")")
        el22.click()
        #scroll into view
        el23 = driver.find_element(by=AppiumBy.ANDROID_UIAUTOMATOR, value="new UiSelector().text(\"Venta Credito\")")
        el23.click()

        #añadir artículos
        el24 = driver.find_element(by=AppiumBy.ANDROID_UIAUTOMATOR,
                                   value="new UiSelector().className(\"android.widget.ImageButton\").instance(0)")
        el24.click()

        #buscar artículos por código
        el25 = driver.find_element(by=AppiumBy.ANDROID_UIAUTOMATOR,
                                   value="new UiSelector().className(\"android.widget.ImageButton\").instance(2)")
        el25.click()
        el26 = driver.find_element(by=AppiumBy.ANDROID_UIAUTOMATOR,
                                   value="new UiSelector().text(\"Buscar por descripción\")")
        el26.click()
        el27 = driver.find_element(by=AppiumBy.ANDROID_UIAUTOMATOR,
                                   value="new UiSelector().text(\"Buscar por código\")")
        el27.click()
        el28 = driver.find_element(by=AppiumBy.CLASS_NAME, value="android.widget.EditText")
        el28.click()
        el28.send_keys("FA01002")
        el29 = driver.find_element(by=AppiumBy.CLASS_NAME, value="android.widget.Button")
        el29.click()
        #escoger el articulo
        el30 = driver.find_element(by=AppiumBy.ANDROID_UIAUTOMATOR, value="new UiSelector().text(\"Usr: FA01002\")")
        el30.click()
        el31 = driver.find_element(by=AppiumBy.ANDROID_UIAUTOMATOR,
                                   value="new UiSelector().text(\"MARLBORO GOLD KS BOX 20 - FA01002\")")
        el31.click()
        el32 = driver.find_element(by=AppiumBy.ANDROID_UIAUTOMATOR, value="new UiSelector().text(\"0.00\")")
        el32.click()
        el33 = driver.find_element(by=AppiumBy.ANDROID_UIAUTOMATOR,
                                   value="new UiSelector().className(\"android.widget.EditText\").instance(0)")
        el33.click()
        el33.send_keys("1")
        el34 = driver.find_element(by=AppiumBy.ANDROID_UIAUTOMATOR, value="new UiSelector().text(\"Aceptar\")")
        el34.click()
        el35 = driver.find_element(by=AppiumBy.ANDROID_UIAUTOMATOR,
                                   value="new UiSelector().className(\"android.widget.ImageButton\").instance(1)")
        el35.click()

        #continuar
        el36 = driver.find_element(by=AppiumBy.ANDROID_UIAUTOMATOR,
                                   value="new UiSelector().className(\"android.widget.ImageButton\").instance(3)")
        el36.click()

        #confirmar to/do y realizar la venta
        #dejar pendiente
        el38 = driver.find_element(by=AppiumBy.ANDROID_UIAUTOMATOR,
                                   value="new UiSelector().className(\"android.widget.ImageButton\").instance(1)")
        el38.click()

        #fiscalizar

        #revisar el ccd otra vez
        el44 = driver.find_element(by=AppiumBy.CLASS_NAME, value="android.widget.Button")
        el44.click()
        el45 = driver.find_element(by=AppiumBy.ANDROID_UIAUTOMATOR, value="new UiSelector().text(\"1,349.31\")")
        #get text
        el45.click()

        ### Revisar estado de cuenta

        #realizar recibo de pago parcial
        #nuevo doc
        el46 = driver.find_element(by=AppiumBy.ANDROID_UIAUTOMATOR, value="new UiSelector().text(\"202299\")")
        el46.click()
        el47 = driver.find_element(by=AppiumBy.ANDROID_UIAUTOMATOR,
                                   value="new UiSelector().text(\"Nuevo documento...\")")
        el47.click()

        # realizar recibo de pago
        el48 = driver.find_element(by=AppiumBy.ANDROID_UIAUTOMATOR, value="new UiSelector().text(\"Recibo de Pago\")")
        el48.click()
        el49 = driver.find_element(by=AppiumBy.ANDROID_UIAUTOMATOR,
                                   value="new UiSelector().className(\"android.widget.ImageButton\").instance(2)")
        el49.click()
        #total
        el6 = driver.find_element(by=AppiumBy.ANDROID_UIAUTOMATOR, value="new UiSelector().text(\"1,349.31\")")
        el6.click()
        el7 = driver.find_element(by=AppiumBy.ANDROID_UIAUTOMATOR, value="new UiSelector().text(\"Confirmar\")")
        el7.click()
        el8 = driver.find_element(by=AppiumBy.ANDROID_UIAUTOMATOR,
                                  value="new UiSelector().className(\"android.widget.ImageButton\").instance(0)")
        el8.click()

        #pop ups
        el56 = driver.find_element(by=AppiumBy.ID, value="android:id/button2")
        el56.click()
        el57 = driver.find_element(by=AppiumBy.ID, value="android:id/button2")
        el57.click()

        #volver a checar el saldo
        el1 = driver.find_element(by=AppiumBy.CLASS_NAME, value="android.widget.Button")
        el1.click()
        el2 = driver.find_element(by=AppiumBy.ANDROID_UIAUTOMATOR, value="new UiSelector().text(\"2,023.97\")")
        #get saldo ccd
        el2.click()

        ### Revisar estado de cuenta

        driver.execute_script('mobile:pressKey', {"keycode": 4})

        #descargar
        driver.execute_script('mobile:pressKey', {"keycode": 4})
        el8 = driver.find_element(by=AppiumBy.ID, value="android:id/button1")
        el8.click()
        #wait
        el9 = driver.find_element(by=AppiumBy.ANDROID_UIAUTOMATOR, value="new UiSelector().text(\"descargar\")")
        el9.click()
        #wait
        el10 = driver.find_element(by=AppiumBy.ID, value="android:id/button1")
        el10.click()
        #wait
        el11 = driver.find_element(by=AppiumBy.ID, value="android:id/button2")
        el11.click()

        ###Fiscalizar

        # ---------------------------------------------------------
        # FIN DEL CÓDIGO PEGADO
        # ---------------------------------------------------------

        # Pequeña pausa final opcional para que veas el resultado antes de que se cierre
        time.sleep(2)
        print("--- Fin de los pasos grabados ---")
