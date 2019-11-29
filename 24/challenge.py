from abc import ABC, abstractmethod


class Challenge(ABC):
    def __init__(self, number, title):
        self.number = number
        self.title = title

    @abstractmethod
    def verify(self, ver):
        pass

    @property
    @abstractmethod
    def pretty_title(self):
        pass


class BlogChallenge(Challenge):
    def __init__(self, number, title, merged_prs):
        super().__init__(number, title)
        self.merged_prs = merged_prs

    @property
    def pretty_title(self):
        return f"PCC{self.number} - {self.title}"

    def verify(self, ver):
        return ver in self.merged_prs


class BiteChallenge(Challenge):
    def __init__(self, number, title, result):
        super().__init__(number, title)
        self.result = result

    @property
    def pretty_title(self):
        return f"Bite {self.number}. {self.title}"

    def verify(self, ver):
        return self.result == ver