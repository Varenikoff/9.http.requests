import requests


class superHero:
    url = ' https://superheroapi.com/api/'
    access_token = '2619421814940190'

    def __init__(self, name):
        self.name = name
        self.id = ''
        self.intell = ''

    def get_id(self):
        self.id = requests.get(self.url + self.access_token + '/search/' + self.name).json()['results'][0]['id']
        return self.id

    def get_intell(self):
        if not self.id:
            self.get_id()
        self.intell = requests.get(self.url + self.access_token + '/' + self.id + '/powerstats').json()[
            'intelligence']
        return self.intell


def best_intell(heroes):
    for hero in heroes:
        if not hero.intell:
            hero.get_intell()
    sorted_list_of_intell = sorted(heroes, key=lambda hero: hero.intell)
    return sorted_list_of_intell[0]


if __name__ == "__main__":
    superHeroes = [superHero('Hulk'),
                    superHero('Captain America'),
                    superHero('Thanos')]
    winner = best_intell(superHeroes)
    print(f"Самый умный - {winner.name},  интеллект - {winner.intell}")