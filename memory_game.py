import tkinter as tk
from PIL import Image, ImageTk
import random
import requests
from io import BytesIO


class MemoryGame:
    def __init__(self, root):
        self.root = root
        self.root.title("Funny Memory Game")

        self.rows = 4
        self.cols = 4
        self.total_pairs = (self.rows * self.cols) // 2

        self.revealed = []
        self.matched = []
        self.buttons = []
        self.lock = False

        # Back image URL
        self.back_image_url = "https://wiki.mushureport.com/images/d/d7/Card_Back_official.png"

        # Front images: 8 unique images (one for each pair)
        self.front_image_urls = [
            "https://img.freepik.com/free-photo/close-up-portrait-beautiful-cat_23-2149214419.jpg?semt=ais_hybrid&w=740",
            "https://i.pinimg.com/736x/e5/b9/81/e5b98110fcd62d6ebe0e636262170175.jpg",
            "https://t3.ftcdn.net/jpg/00/72/56/48/360_F_72564896_vWACor9JLeVk1vBarV6dQ33bvvOVNa78.jpg",
            "https://image1.masterfile.com/getImage/NzAwLTAwMTc3OTYxZW4uMDAwMDAwMDA=AAy-5L/700-00177961en_Masterfile.jpg",
            "https://i.pinimg.com/736x/6b/25/50/6b2550effe768605591fc7dedd3f8f31.jpg",
            "https://i.pinimg.com/564x/38/e8/f5/38e8f50e89c5d438c054e7d6bced3f1a.jpg",
            "https://i.pinimg.com/736x/75/d2/47/75d24724e13f083bce2c77541606f15b.jpg",
            "https://as1.ftcdn.net/jpg/05/29/25/56/1000_F_529255615_lOnG8RtMROoQNSRGH21i2SyXBB52NruU.jpg"
        ]

        self.load_images()
        self.create_board()

    def load_images(self):
        # Load back image
        response = requests.get(self.back_image_url)
        back_img = Image.open(BytesIO(response.content)).resize((120, 150))
        self.card_back = ImageTk.PhotoImage(back_img)

        # Load and pair front images
        self.card_fronts = []
        for url in self.front_image_urls:
            response = requests.get(url)
            img = Image.open(BytesIO(response.content)).resize((120, 150))
            photo = ImageTk.PhotoImage(img)
            self.card_fronts.extend([photo, photo])  # Add twice for a matching pair

        random.shuffle(self.card_fronts)

    def create_board(self):
        for i in range(self.rows):
            for j in range(self.cols):
                idx = i * self.cols + j
                btn = tk.Button(self.root, image=self.card_back, command=lambda i=idx: self.reveal_card(i))
                btn.grid(row=i, column=j, padx=5, pady=5)
                self.buttons.append(btn)

    def reveal_card(self, index):
        if self.lock or index in self.revealed or index in self.matched:
            return

        self.buttons[index].config(image=self.card_fronts[index])
        self.revealed.append(index)

        if len(self.revealed) == 2:
            self.lock = True
            self.root.after(1000, self.check_match)

    def check_match(self):
        first, second = self.revealed

        if self.card_fronts[first] == self.card_fronts[second]:
            self.matched.extend([first, second])
        else:
            self.buttons[first].config(image=self.card_back)
            self.buttons[second].config(image=self.card_back)

        self.revealed.clear()
        self.lock = False

        if len(self.matched) == len(self.card_fronts):
            self.show_win_message()

    def show_win_message(self):
        label = tk.Label(self.root, text="🎉 You Won! 🎉", font=("Arial", 18))
        label.grid(row=self.rows, column=0, columnspan=self.cols, pady=10)


if __name__ == "__main__":
    root = tk.Tk()
    game = MemoryGame(root)
    root.mainloop()
