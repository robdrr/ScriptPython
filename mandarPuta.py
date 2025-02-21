import pyautogui
import time
import pyperclip

# Tiempo de espera para abrir el chat en WhatsApp Web (ajustar según sea necesario)
time.sleep(5)

# Mensaje a enviar
mensaje = "descargate el left 4 dead"

# Número de veces que se enviará el mensaje
repeticiones = 10  

for i in range(repeticiones):
    pyperclip.copy(mensaje)  # Copia el mensaje al portapapeles
    pyautogui.hotkey("ctrl", "v")  # Pega el mensaje
    pyautogui.press("enter")  # Envía el mensaje
    time.sleep(0.1)  # Espera un poco antes de enviar el siguiente mensaje

print("Mensajes enviados.")
