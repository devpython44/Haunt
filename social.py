import requests
from bs4 import BeautifulSoup
from colorama import Fore, Style

class SocialDeanon:
    def __init__(self, nickname):
        self.nickname = nickname.replace('@', '')
        self.red = Fore.RED
        self.green = Fore.GREEN
        self.magenta = Fore.MAGENTA

    def telegram(self):
        url = f'https://t.me/{self.nickname}'
        response = requests.get(url)
        soup = BeautifulSoup(response.text, 'lxml')
        quote = soup.find('div', class_="tgme_page_description")

        if quote is None:
            return ""

        temp = quote.text.strip()
        if temp != f"If you have Telegram, you can contact @{self.nickname} right away.":
            return f"  {url}\n"
        else:
            return ""

    def availability(self):
        req_list = [
            'https://www.instagram.com/',
            'https://github.com/',
            'https://rt.pornhub.com/users/',
            'https://ok.ru/',
            'https://vk.com/',
            'https://soundcloud.com/',
            'https://www.tumblr.com/blog/view/',
            'https://twitter.com/',
            'https://ask.fm/',
            'https://znanija.com/app/profile/',
            'https://www.deviantart.com/',
            'https://www.flickr.com/',
            'https://ru.linkedin.com/in/',
            'https://myspace.com/',
            'https://www.pinterest.com/',
            'https://www.reddit.com/r/',
            'https://www.reddit.com/user/'
        ]

        req_answer = []
        for req_url in req_list:
            social_req = req_url + self.nickname
            try:
                res = requests.get(social_req)
                if res.ok:
                    req_answer.append(social_req)
            except:
                continue
        return req_answer
