from abc import ABC, abstractmethod
import random

# Abstract Player sınıfı
class Player(ABC):
    def __init__(self, name):
        self.name = name
        self.score = 0
        self.moves = []

    @abstractmethod
    def make_move(self):
        pass

# HumanPlayer sınıfı
class HumanPlayer(Player):
    def make_move(self):
        move = input(f"{self.name}, hamlenizi seçin (taş, kağıt, makas): ").lower()
        while move not in ["taş", "kağıt", "makas"]:
            print("Geçersiz hamle. Lütfen tekrar deneyin.")
            move = input(f"{self.name}, hamlenizi seçin (taş, kağıt, makas): ").lower()
        self.moves.append(move)
        return move

# RandomComputerPlayer sınıfı
class RandomComputerPlayer(Player):
    def make_move(self):
        move = random.choice(["taş", "kağıt", "makas"])
        self.moves.append(move)
        print(f"{self.name} (Bilgisayar) seçimi: {move}")
        return move

# Oyun sınıfı
class RockPaperScissorsGame:
    def __init__(self, player1, player2):
        self.player1 = player1
        self.player2 = player2
        self.round = 0

    @staticmethod
    def decide_winner(move1, move2):
        if move1 == move2:
            return "draw"
        elif (move1 == "taş" and move2 == "makas") or \
             (move1 == "kağıt" and move2 == "taş") or \
             (move1 == "makas" and move2 == "kağıt"):
            return "player1"
        else:
            return "player2"

    def play_round(self):
        self.round += 1
        print(f"\n--- {self.round}. Tur ---")
        move1 = self.player1.make_move()
        move2 = self.player2.make_move()
        winner = self.decide_winner(move1, move2)

        if winner == "draw":
            print("Berabere!")
        elif winner == "player1":
            print(f"{self.player1.name} kazandı!")
            self.player1.score += 1
        else:
            print(f"{self.player2.name} kazandı!")
            self.player2.score += 1

        print(f"Skor: {self.player1.name} {self.player1.score} - {self.player2.score} {self.player2.name}")

    def display_history(self):
        print("\n--- Hamle Geçmişi ---")
        for i in range(len(self.player1.moves)):
            print(f"Tur {i+1}: {self.player1.name} {self.player1.moves[i]} - {self.player2.moves[i]} {self.player2.name}")

    def play_game(self):
        while True:
            self.play_round()
            cont = input("Oyuna devam etmek istiyor musunuz? (e/h): ").lower()
            if cont != 'e':
                break
        self.display_history()
        print("\nOyun Bitti!")
        print(f"Son Skor: {self.player1.name} {self.player1.score} - {self.player2.score} {self.player2.name}")

# Oyun Başlatıcı
if __name__ == "__main__":
    print("Taş-Kağıt-Makas Oyununa Hoşgeldiniz!")
    player_name = input("Oyuncu adınızı girin: ")
    human = HumanPlayer(player_name)
    computer = RandomComputerPlayer("Bilgisayar")
    game = RockPaperScissorsGame(human, computer)
    game.play_game()
