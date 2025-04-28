import csv
import os

def main():
    class Roboko(object):
        def __init__(self):
            os.makedirs('data/csv', exist_ok=True)
            self.target_file_path = 'data/csv/ranking.csv'
            self.is_file_exist = os.path.isfile(self.target_file_path)
            self.csvdata = []
            self.found = False
            name = input('こんにちは!私はRobokoです。あなたの名前は何ですか?')
            self.name = name
            self.get_csv_data()
            self.recomend_favorite_restaurant()
            favoriteFoodStore = input('{}さん。どこのレストランが好きですか?'.format(name))
            self.favoriteFoodStore = favoriteFoodStore.title()

        def recomend_favorite_restaurant(self):
            for row in self.csvdata:
                while True:
                    choice = input('私のオススメのレストランは、 {}です。\nこのレストランは好きですか? [Yes/No]'.format(row['NAME'])).lower()

                    if choice in ['y', 'yes']:
                        break
                    elif choice in ['n', 'no']:
                        break
                    print('yまたはnで答えてください')

        def get_csv_data(self):
            with open(self.target_file_path, 'r', newline='')as csvfile:
                reader = csv.DictReader(csvfile)
                for row in reader:
                    self.csvdata.append(row)

        def save_csv(self):
            if self.favoriteFoodStore == '':
                return

            if self.is_file_exist:
                with open(self.target_file_path, 'r', newline='') as csvfile:
                    reader = csv.DictReader(csvfile)
                    for row in reader:
                        if row['NAME'] == self.favoriteFoodStore:
                            row['COUNT'] = str(int(row['COUNT']) + 1)
                            found = True
                        self.csvdata.append(row)

            if not self.found:
                self.csvdata.append({
                    'NAME': self.favoriteFoodStore,
                    'COUNT': '1',
                })

            with open(self.target_file_path, 'w', newline='') as csvfile:
                fieldnames = ['NAME', 'COUNT']
                writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
                writer.writeheader()

                for row in self.csvdata:
                    writer.writerow(row)

        def final(self):
            self.save_csv()
            print('{}さん。ありがとうございました。\n良い一日を!さようなら。'.format(self.name))

    roboko = Roboko()

    try:
        roboko.ask_favorite_restaurant()
    finally:
        roboko.final()


main()