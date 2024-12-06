import os
import time
import pyautogui

def open_calculator():
    """Открывает приложение 'Калькулятор'."""
    os.system("gnome-calculator &")
    time.sleep(2)  # Дать время приложению загрузиться

def find_and_click(image_path):
    """Ищет элемент на экране и кликает по нему."""
    button = pyautogui.locateOnScreen(image_path, confidence=0.94)
    if button:
        pyautogui.click(pyautogui.center(button))
    else:
        raise ValueError(f"Не удалось найти элемент: {image_path}")

def main():
    # Открываем калькулятор
    open_calculator()

    # Пути к изображениям кнопок
    buttons = {
        "1": "buttons/1.png",
        "2": "buttons/2.png",
        "+": "buttons/plus.png",
        "7": "buttons/7.png",
        "=": "buttons/equals.png"
    }

    # Последовательность действий
    try:
        find_and_click(buttons["1"])
        time.sleep(0.5)
        find_and_click(buttons["2"])
        time.sleep(0.5)
        find_and_click(buttons["+"])
        time.sleep(0.5)
        find_and_click(buttons["7"])
        time.sleep(0.5)
        find_and_click(buttons["="])
        time.sleep(2)
    except ValueError as e:
        print(e)

    # Закрываем калькулятор
    os.system("pkill -f gnome-calculator")

if __name__ == "__main__":
    main()
