import pyautogui
import time

# Дайте время переключиться на окно для теста
time.sleep(5)

# Сделайте скриншот
pyautogui.screenshot('/tmp/test_pyautogui.png')

print("Скриншот успешно сохранён в /tmp/test_pyautogui.png")
