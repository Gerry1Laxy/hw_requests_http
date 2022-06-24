import requests


def compare_heroes(hero_names: list, parameter: str) -> None:
    url = 'https://akabab.github.io/superhero-api/api/all.json'
    response = requests.get(url)

    target_heroes = {name: None for name in hero_names}
    for hero in response.json():
        if hero['name'] in target_heroes:
            target_heroes[hero['name']] = hero['powerstats'][parameter]

    max_power = max(target_heroes.values())
    for hero_name, power in target_heroes.items():
        if power == max_power:
            print(f'{hero_name} has {power} {parameter}.')


if __name__ == '__main__':
    heroes = ['Thanos', 'Hulk', 'Captain America', 'Ant-Man']
    compare_heroes(heroes, 'intelligence')
    compare_heroes(heroes, 'speed')
