import csv
import os

def main():
    class Roboko(object):
        def __init__(self):
            name = input('こんにちは!私はRobokoです。あなたの名前は何ですか?')
            self.name = name
            favoriteFoodStore = input('{}さん。どこのレストランが好きですか?'.format(name))
            self.favoriteFoodStore = favoriteFoodStore
        def ask_favorite_restaurant(self):
            print(self.name, self.favoriteFoodStore)

        def save_csv(self):
            os.makedirs('data/csv', exist_ok=True)
            target_file_path = 'data/csv/rankink.csv'
            is_file_exist = os.path.isfile(target_file_path)
            mode = 'a' if is_file_exist else 'w'

            with open('data/csv/ranking.csv', 'w+', newline='') as csvfile:
                fieldnames = ['NAME', 'COUNT']
                writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

                if not is_file_exist:
                    writer.writeheader()

                writer.writerow({
                    'NAME': self.favoriteFoodStore,
                    'COUNT': 0
                })

        def final(self):
            self.save_csv()
            print('{}さん。ありがとうございました。\n良い一日を!さようなら。'.format(self.name))

    roboko = Roboko()

    try:
        roboko.ask_favorite_restaurant()
    finally:
        roboko.final()


main()