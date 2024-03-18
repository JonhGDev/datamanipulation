import csv


class Arquivo:
    def __init__(self, path_file):
        self.path_file = path_file

      def create_Arquivo(self):
        with open(self.path_file, "W", encoding="utf-8") as file:
          csv.writer(file, delimiter=";")
