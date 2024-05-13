from yandex_music import Client


class YaMusic:
    def __init__(self, token:str=None):
        self.token: str = token
        self.__client = Client(token=token)
    
    def like_track(self, n: int):
        return self.__client.users_likes_tracks()[n].fetch_track()
    
    def search_track(self, title: str):
        data = self.__client.search(text=title).tracks.results
        if len(data):
            return data[0]
        return None  




if __name__ == "__main__":
    token = "YOUR_TOKEN"
    ya_mus = YaMusic(token=token)
    m = ya_mus.search_track("снова я напиваюсь")
    m.download("hello.mp3")