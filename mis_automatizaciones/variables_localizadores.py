import AppiumBy

import data


class LocatorsEAL:
    # Install page
    btn_ingresar = (AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().className("android.widget.Button").text("Aceptar")')
    campo_usuario = (AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().description("Usuario")')
    campo_contraseña = (AppiumBy.ANDROID_UIAUTOMATOR, 'newUiSelector().description("Contraseña")')
    campo_servidor = (AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().description("Servidor")')
    check_ssl = (AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().className("android.widget.CheckBox").text("Usar SSL")')
    btn_instalar = (AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().className("android.widget.Button").text("Instalar")')

    # Charge page
    btn_cargar = (AppiumBy.ANDROID_UIAUTOMATOR, 'new Ui Selector().text("cargar")')
    btn_descargar = (AppiumBy.ANDROID_UIAUTOMATOR, 'new Ui Selector().text("descargar")')
    btn_config = (AppiumBy.ANDROID_UIAUTOMATOR, 'new Ui Selector().text("configuración")')
    btn_log = (AppiumBy.ANDROID_UIAUTOMATOR, 'new Ui Selector().text("log")')
    btn_inicio = (AppiumBy.ANDROID_UIAUTOMATOR, 'new Ui Selector().text("inicio")')

    #login page
    btn_inicio = (AppiumBy.ANDROID_UIAUTOMATOR, 'new Ui Selector().className("android.widget.Button").text("Iniciar")')
    # btn_regresar = ???

    # Home page


    def get_ruta_dropdown(self, ruta_default: str) -> tuple:
        ruta_default = data.RUTA_DEFAULT
        return (AppiumBy.ANDROID_UIAUTOMATOR,
           f"new UiSelector().className('android.widget.TextView')"
           f".text('{ruta_default.upper()}')")

    ruta_dropdown = get_ruta_dropdown()

    def get_ruta_au(self, nombre_ruta: str) -> tuple:
        nombre_ruta = data.RUTA_AUTOMATIZADA
        return (AppiumBy.ANDROID_UIAUTOMATOR,
                f'new UiSelector().className("android.widget.TextView")'
                f'.text("{nombre_ruta}")')

    ruta_auto = get_ruta_au()
    #ruta_auto_credito = get_ruta_au()

    def get_client_id_button(self, client_id: str) -> tuple:
        client_id = data.CLIENT_ID
        return (AppiumBy.ANDROID_UIAUTOMATOR,
                f'new UiSelector().className("android.widget.TextView")'
                f'text("{client_id}")')

    btn_client_id = get_client_id_button()

    #inicio visita
    nuevo_doc = (AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().text("Nuevo documento...")')
    doc_inicio_visita = (AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().text("Inicio Visita")')
    rubro_visita = (AppiumBy.XPATH, "//android.view.ViewGroup/android.widget.TextView[5]")
    rubro_1 = (AppiumBy.ANDROID_UIAUTOMATOR,
               'new UiSelector().resourceId("uy.com.assist.eaf:id/contextmenu_item_text").text("Etiqueta no accesible")')
    start_visit_button = (AppiumBy.XPATH, "//android.view.ViewGroup/android.widget.ImageButton[1]")

    #client info
    client_info = (AppiumBy.ANDROID_UIAUTOMATOR, f'new UiSelector().className("android.widget.Button").text("...")')
    











