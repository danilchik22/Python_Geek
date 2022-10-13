import hashlib


class InternetService:
    def __init__(self):
        self.cache = {}
        self.pages = set()

    def show_cache(self):
        for url, hash in self.cache.items():
            print(f'{url} : {hash}')

    def check_page_in_cache(self, url):
        salt = 'kdl 233 wekel'
        if url in self.cache:
            print(hashlib.sha512((url+salt).encode()).hexdigest())
        else:
            hash_url = hashlib.sha512((url+salt).encode()).hexdigest()
            self.cache[url] = hash_url

    def add_page(self, url):
        self.check_page_in_cache(url)
        self.pages.add(url)


if __name__ == '__main__':
    service = InternetService()
    service.add_page('www.winter.ru')
    service.add_page('www.winter.ru')
    service.add_page('www.winter.ru/home')
    service.show_cache()
    print(service.pages)
