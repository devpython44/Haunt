import os
import requests
from colorama import Fore, init

# Инициализация colorama для поддержки цветного вывода
init(autoreset=True)

# Кэширование для хранения результатов запросов
cache = {}

# Функция для получения информации об IP
def get_ip_info(ip):
    # Проверка на наличие IP в кэше
    if ip in cache:
        print("Данные из кэша...")
        return cache[ip]
    
    # Запрос к API
    url = f"http://ip-api.com/json/{ip}"
    try:
        response = requests.get(url, timeout=5)
        response.raise_for_status()  # Проверка на успешный статус запроса
        data = response.json()

        # Проверка успешности данных
        if data.get("status") == "success":
            cache[ip] = data  # Сохраняем данные в кэш
            return data
        else:
            print("Ошибка: Невозможно получить информацию по IP.")
            return None
    except requests.exceptions.RequestException as e:
        print(f"Ошибка запроса: {e}")
        return None

# Функция для вывода информации по IP
def print_ip_info(ip_info):
    if ip_info:
        print("├Страна:", ip_info["country"])
        print("├Код страны:", ip_info["countryCode"])
        print("├Регион:", ip_info["regionName"])
        print("├Город:", ip_info["city"])
        print("├Почтовый индекс:", ip_info["zip"])
        print("├Широта:", ip_info["lat"])
        print("├Долгота:", ip_info["lon"])
        print("├Часовой пояс:", ip_info["timezone"])
        print("└Интернет-провайдер:", ip_info["isp"])
    else:
        print("Информация по этому IP не найдена.")

# Функция для проверки корректности IP адреса
def validate_ip(ip):
    parts = ip.split(".")
    if len(parts) != 4:
        return False
    for part in parts:
        if not part.isdigit() or not 0 <= int(part) <= 255:
            return False
    return True

# Функция для очистки экрана
def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

# Функция для вывода ASCII-арт и меню выбора
def display_menu():
    print(Fore.RED + """
██╗░░██╗░█████╗░██╗░░░██╗███╗░░██╗████████╗  ██╗██████╗░
██║░░██║██╔══██╗██║░░░██║████╗░██║╚══██╔══╝  ██║██╔══██╗
███████║███████║██║░░░██║██╔██╗██║░░░██║░░░  ██║██████╔╝
██╔══██║██╔══██║██║░░░██║██║╚████║░░░██║░░░  ██║██╔═══╝░
██║░░██║██║░░██║╚██████╔╝██║░╚███║░░░██║░░░  ██║██║░░░░░
╚═╝░░╚═╝╚═╝░░╚═╝░╚═════╝░╚═╝░░╚══╝░░░╚═╝░░░  ╚═╝╚═╝░░░░░
    """)
    print("Выберите действие:")
    print("1. Поиск информации по IP")
    print("2. Выход")

# Функция для показа меню после получения информации по IP
def post_ip_info_menu():
    print("\nЧто вы хотите сделать дальше?")
    print("1. Дальше")
    print("2. Выход")

# Главная функция
def main():
    while True:
        clear_screen()  # Очищаем экран при каждом запуске цикла
        display_menu()
        choice = input(": ")

        if choice == "1":
            ip = input("Введите IP адрес: ").strip()
            
            # Убедимся, что введен правильный формат IP
            if not validate_ip(ip):
                print("Неверный формат IP адреса.")
                continue

            # Получаем информацию по IP
            ip_info = get_ip_info(ip)

            # Очистка экрана перед выводом информации
            clear_screen()
            print(Fore.RED + "Информация о IP:\n")
            print_ip_info(ip_info)

            # Показать меню с дальнейшими действиями
            post_ip_info_menu()
            next_action = input("Введите цифру для выбора действия: ")
            
            if next_action == "2":
                print("Выход из программы...")
                break

        elif choice == "2":
            print("Выход из программы...")
            break
        else:
            print("Неверный выбор. Пожалуйста, попробуйте снова.")

if __name__ == "__main__":
    main()
