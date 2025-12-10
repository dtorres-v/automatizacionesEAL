


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


# ruta_auto_credito = get_ruta_au()

def get_client_id_button(self, client_id: str) -> tuple:
    client_id = data.CLIENT_ID
    return (AppiumBy.ANDROID_UIAUTOMATOR,
            f'new UiSelector().className("android.widget.TextView")'
            f'text("{client_id}")')


btn_client_id = get_client_id_button()