import csv
import os.path

# TODO оформить в тест, добавить ассерты и использовать универсальный путь

from conftest import resources_path


def test_csv():
    with open(os.path.join(resources_path, 'eggs.csv'), 'w', newline='') as csvfile:
        csvwriter = csv.writer(csvfile, delimiter=',')
        csvwriter.writerow(['Anna', 'Pavel', 'Peter'])
        csvwriter.writerow(['Alex', 'Serj', 'Yana'])

        assert os.path.exists(os.path.join(resources_path, 'eggs.csv'))
    eggs_name = []
    with open(os.path.join(resources_path, 'eggs.csv')) as csvfile:
        csvreader = csv.reader(csvfile)
        for row in csvreader:
            print(row)
            eggs_name.extend(row)

    names = ['Anna', 'Pavel', 'Peter', 'Alex', 'Serj', 'Yana']

    assert eggs_name == names
