import os
import requests
from colorama import Fore, init
import social as sd  # Импортируем модуль social, где определен класс SocialDeanon

# Инициализация colorama для поддержки цветного вывода
init(autoreset=True)

# Кэширование для хранения результатов запросов
cache = {}

# Функция для получения информации об IP
def get_ip_info(ip):
    if ip in cache:
        print("Данные из кэша...")
        return cache[ip]
    
    url = f"http://ip-api.com/json/{ip}"
    try:
        response = requests.get(url, timeout=5)
        response.raise_for_status()
        data = response.json()

        if data.get("status") == "success":
            cache[ip] = data
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
██╗░░██╗░█████╗░██╗░░░██╗███╗░░██╗████████╗
██║░░██║██╔══██╗██║░░░██║████╗░██║╚══██╔══╝
███████║███████║██║░░░██║██╔██╗██║░░░██║░░░
██╔══██║██╔══██║██║░░░██║██║╚████║░░░██║░░░
██║░░██║██║░░██║╚██████╔╝██║░╚███║░░░██║░░░
╚═╝░░╚═╝╚═╝░░╚═╝░╚═════╝░╚═╝░░╚══╝░░░╚═╝░░░
""")
    print("Выберите действие:")
    print("1. Поиск информации по IP")
    print("2. Поиск в социальных сетях")
    print("3. Выход")

# Функция для отображения результатов поиска в соцсетях
def display_social_search():
    nickname = input("Введите никнейм для поиска: ").strip()
    deanon = sd.SocialDeanon(nickname)

    clear_screen()
    print(Fore.RED + f"Результаты поиска для никнейма '{nickname}':\n")
    profiles = deanon.availability()

    if profiles:
        print("Найдены профили:")
        for profile in profiles:
            print(f"  {profile}")
    else:
        print("Профили с таким ником не найдены.")

    post_search_menu()

# Функция для меню дальнейших действий
def post_search_menu():
    while True:
        print("\nЧто вы хотите сделать дальше?")
        print("1. Повторить поиск")
        print("2. Вернуться в главное меню")
        print("3. Выйти")
        choice = input("Выберите действие: ")

        if choice == "1":
            return  # Повторит поиск, вернется в функцию
        elif choice == "2":
            break  # Вернется в главное меню
        elif choice == "3":
            print("Выход из программы...")
            exit()
        else:
            print("Неверный выбор. Попробуйте снова.")

# Главная функция
def main():
    running = True  # Флаг для работы основного цикла

    while running:
        clear_screen()
        display_menu()
        choice = input("Выберите ваше действие: ")

        if choice == "1":
            ip = input("Введите IP адрес: ").strip()
            
            if not validate_ip(ip):
                print("Неверный формат IP адреса.")
                continue

            ip_info = get_ip_info(ip)
            clear_screen()
            print(Fore.RED + "Информация о IP:\n")
            print_ip_info(ip_info)
            post_search_menu()

        elif choice == "2":
            clear_screen()
            display_social_search()

        elif choice == "3":
            print("Выход из программы...")
            running = False  # Устанавливаем флаг для завершения основного цикла
        else:
            print("Неверный выбор. Пожалуйста, попробуйте снова.")

if __name__ == "__main__":
    main()
