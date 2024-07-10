import random


class EmojiGenerator:
    def __init__(self):
        self.emojis = ["😊", "😎", "🚀", "🌟", "🎉", "🐱‍🏍"]

    def get_random_emoji(self):
        return random.choice(self.emojis)
