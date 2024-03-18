import csv
class Archive:
    def __init__(self, path_file):
        self.path_file = path_file

    def create_archive(self):
        with open(self.path_file, "w", encoding="utf-8") as file:
            csv.writer(file, delimiter=";")

    def file_read(self):
        with open(self.path_file, "r", encoding="utf-8") as file:
            leitor = csv.reader(file, delimiter=";")