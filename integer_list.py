class IntegerList:
    def __init__(self):
        self.numbers = []

    def add_integer(self, num):
        if isinstance(num, int):
            self.numbers.append(num)
        else:
            raise ValueError("Seuls les entiers sont autorisés.")

    def remove_integer(self, num):
        if num in self.numbers:
            self.numbers.remove(num)
        else:
            raise ValueError(f"{num} n'est pas dans la liste.")

    def get_average(self):
        if not self.numbers:
            raise ValueError("La liste est vide.")
        return sum(self.numbers) / len(self.numbers)

    def get_max(self):
        if not self.numbers:
            raise ValueError("La liste est vide.")
        return max(self.numbers)

    def get_min(self):
        if not self.numbers:
            raise ValueError("La liste est vide.")
        return min(self.numbers)
