import time
import os
import requests
import json

image = """⠄⠄⠄⢰⣧⣼⣯⠄⣸⣠⣶⣶⣦⣾⠄⠄⠄⠄⡀⠄⢀⣿⣿⠄⠄⠄⢸⡇⠄⠄  
⠄⠄⠄⣾⣿⠿⠿⠶⠿⢿⣿⣿⣿⣿⣦⣤⣄⢀⡅⢠⣾⣛⡉⠄⠄⠄⠸⢀⣿⠄  
⠄⠄⢀⡋⣡⣴⣶⣶⡀⠄⠄⠙⢿⣿⣿⣿⣿⣿⣴⣿⣿⣿⢃⣤⣄⣀⣥⣿⣿⠄  
⠄⠄⢸⣇⠻⣿⣿⣿⣧⣀⢀⣠⡌⢻⣿⣿⣿⣿⣿⣿⣿⣿⣿⠿⠿⠿⣿⣿⣿⠄  
⠄⢀⢸⣿⣷⣤⣤⣤⣬⣙⣛⢿⣿⣿⣿⣿⣿⣿⡿⣿⣿⡍⠄⠄⢀⣤⣄⠉⠋⣰  
⠄⣼⣖⣿⣿⣿⣿⣿⣿⣿⣿⣿⢿⣿⣿⣿⣿⣿⢇⣿⣿⡷⠶⠶⢿⣿⣿⠇⢀⣤  
⠘⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣽⣿⣿⣿⡇⣿⣿⣿⣿⣿⣿⣷⣶⣥⣴⣿⡗  
⢀⠈⢿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡟⠄  
⢸⣿⣦⣌⣛⣻⣿⣿⣧⠙⠛⠛⡭⠅⠒⠦⠭⣭⡻⣿⣿⣿⣿⣿⣿⣿⣿⡿⠃⠄  
⠘⣿⣿⣿⣿⣿⣿⣿⣿⡆⠄⠄⠄⠄⠄⠄⠄⠄⠹⠈⢋⣽⣿⣿⣿⣿⣵⣾⠃⠄  
⠄⠘⣿⣿⣿⣿⣿⣿⣿⣿⠄⣴⣿⣶⣄⠄⣴⣶⠄⢀⣾⣿⣿⣿⣿⣿⣿⠃⠄⠄  
⠄⠄⠈⠻⣿⣿⣿⣿⣿⣿⡄⢻⣿⣿⣿⠄⣿⣿⡀⣾⣿⣿⣿⣿⣛⠛⠁⠄⠄⠄  
⠄⠄⠄⠄⠈⠛⢿⣿⣿⣿⠁⠞⢿⣿⣿⡄⢿⣿⡇⣸⣿⣿⠿⠛⠁⠄⠄⠄⠄⠄  
⠄⠄⠄⠄⠄⠄⠄⠉⠻⣿⣿⣾⣦⡙⠻⣷⣾⣿⠃⠿⠋⠁⠄⠄⠄⠄⠄⢀⣠⣴  
⣿⣿⣿⣶⣶⣮⣥⣒⠲⢮⣝⡿⣿⣿⡆⣿⡿⠃⠄⠄⠄⠄⠄⠄⠄⣠⣴⣿⣿⣿
"""

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

def animate_image(image, delay=0.05):
    lines = image.splitlines()
    for i in range(len(lines) + 1):
        clear_screen()
        print('\n'.join(lines[:i]))
        time.sleep(delay)

def fetch_location(ip_address):
    url = f"http://ip-api.com/json/{ip_address}"
    try:
        response = requests.get(url)
        response.raise_for_status()
        return response.json()
    except requests.RequestException as e:
        return {'error': f'Ошибка запроса: {e}'}

def fetch_phone_info(phone_number):
    api_key = 'ВАШ_API_КЛЮЧ'  #NumVerify
    url = f"http://apilayer.net/api/validate?access_key={api_key}&number={phone_number}&country_code=&format=1"
    try:
        response = requests.get(url)
        response.raise_for_status()
        return response.json()
    except requests.RequestException as e:
        return {'error': f'Ошибка запроса: {e}'}

def fetch_email_info(email):
    url = f"https://emailrep.io/{email}"
    try:
        response = requests.get(url)
        response.raise_for_status()
        return response.json()
    except requests.RequestException as e:
        return {'error': f'Ошибка запроса: {e}'}

def ip_lookup():
    clear_screen()
    animate_image(image)
    ip = input("Введите IP-адрес: ")
    location_data = fetch_location(ip)
    if location_data.get('status') == 'fail':
        print(f"Ошибка: {location_data.get('message', 'Не удалось определить местоположение')}")
    else:
        print(f"Страна: {location_data.get('country', 'Неизвестно')}")
        print(f"Регион: {location_data.get('regionName', 'Неизвестно')}")
        print(f"Город: {location_data.get('city', 'Неизвестно')}")
        print(f"Широта: {location_data.get('lat', 'Неизвестно')}")
        print(f"Долгота: {location_data.get('lon', 'Неизвестно')}")
        print(f"Провайдер: {location_data.get('isp', 'Неизвестно')}")
    input("Нажмите Enter для продолжения...")

def phone_lookup():
    clear_screen()
    animate_image(image)
    phone = input("Введите номер телефона: ")
    phone_info = fetch_phone_info(phone)
    if phone_info.get('valid'):
        print(f"Номер: {phone_info.get('number', 'Неизвестно')}")
        print(f"Местоположение: {phone_info.get('location', 'Неизвестно')}")
        print(f"Страна: {phone_info.get('country_name', 'Неизвестно')}")
        print(f"Оператор: {phone_info.get('carrier', 'Неизвестно')}")
    else:
        print("Номер телефона недействителен.")
    input("Нажмите Enter для продолжения...")

def email_lookup():
    clear_screen()
    animate_image(image)
    email = input("Введите email: ")
    email_info = fetch_email_info(email)
    if email_info.get('error'):
        print(f"Ошибка: {email_info.get('error')}")
    else:
        print(f"Email: {email_info.get('email', 'Неизвестно')}")
        print(f"Репутация: {email_info.get('reputation', 'Неизвестно')}")
        print(f"Подозрительный: {'Да' if email_info.get('suspicious', False) else 'Нет'}")
        print(f"Временный: {'Да' if email_info.get('disposable', False) else 'Нет'}")
        print(f"Домен: {email_info.get('details', {}).get('domain', 'Неизвестно')}")
        print(f"Последний раз видели: {email_info.get('details', {}).get('last_seen', 'Неизвестно')}")
    input("Нажмите Enter для продолжения...")

def show_instructions():
    clear_screen()
    animate_image(image)
    instruction = """Инструкция как узнать айпи:
1. Установите Node.js.
2. Создайте сервер:
const express = require('express');
const app = express();
const PORT = 3000;
app.get('/', (req, res) => {
    console.log(`IP: ${req.ip}`);
    res.send(':)');
});
app.listen(PORT, () => {
    console.log(`Сервер на http://localhost:${PORT}`);
});
3. Получите IP и используйте его в программе.
    """
    print(instruction)
    input("Нажмите Enter для продолжения...")

def main_menu():
    while True:
        clear_screen()
        animate_image(image)
        print("\nВыберите действие:\n1. Инструкция по пробиву IP\n2. Пробив по IP\n3. Пробив по номеру телефона\n4. Пробив по email\n5. Выход")
        choice = input("Введите номер: ")
        if choice == '1':
            show_instructions()
        elif choice == '2':
            ip_lookup()
        elif choice == '3':
            phone_lookup()
        elif choice == '4':
            email_lookup()
        elif choice == '5':
            print("Выход из программы...")
            break
        else:
            print("Некорректный выбор. Пожалуйста, выберите 1, 2, 3, 4 или 5.")
            input("Нажмите Enter для продолжения...")

if __name__ == "__main__":
    main_menu()