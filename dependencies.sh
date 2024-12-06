#!/bin/bash

# Обновление списка пакетов
echo "Обновляем список пакетов..."
sudo apt update -y

# Установка Python и инструментов сборки
echo "Устанавливаем Python и инструменты для сборки..."
sudo apt install -y python3 python3-pip python3-venv python3-dev build-essential

# Установка OpenCV и его зависимостей
echo "Устанавливаем OpenCV и зависимости..."
sudo apt install -y libopencv-dev python3-opencv

# Установка инструментов для создания скриншотов
echo "Устанавливаем инструменты для скриншотов..."
sudo apt install -y scrot gnome-screenshot

# Установка X11 и дополнительных инструментов
echo "Устанавливаем X11 и дополнительные инструменты..."
sudo apt install -y x11-utils x11-apps

# Настройка переменной DISPLAY
if ! grep -q "export DISPLAY=:0" ~/.bashrc; then
    echo "Настраиваем переменную DISPLAY..."
    echo 'export DISPLAY=:0' >> ~/.bashrc
    export DISPLAY=:0
fi

# Завершение
echo "Все зависимости успешно установлены. Перезапустите терминал или выполните 'source ~/.bashrc' для применения переменных окружения."
