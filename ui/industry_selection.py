import tkinter as tk
from ui.main_game_screen import show_main_game_screen

def show_industry_selection():
    def select_industry(industry):
        print(f"選択した業界: {industry}")
        root.destroy()
        show_main_game_screen(industry)

    root = tk.Tk()
    root.title("業界選択")
    industries = ["テクノロジー", "消費財", "製造業", "エネルギー"]
    tk.Label(root, text="業界を選択してください:", font=("Arial", 16)).pack(pady=20)
    for industry in industries:
        tk.Button(root, text=industry, command=lambda i=industry: select_industry(i)).pack(pady=10)
    root.mainloop()
