import tkinter as tk
from logic.save_data import save_game_result

def show_result_screen(game_state, result_message):
    """リザルト画面を表示"""
    # ゲーム結果を保存
    save_game_result(game_state, result_message)

    # リザルト画面の表示
    root = tk.Tk()
    root.title("リザルト画面")
    root.geometry("800x300")

    tk.Label(root, text="ゲーム終了", font=("Arial", 18)).pack(pady=10)

    # 結果メッセージ
    tk.Label(root, text=result_message, font=("Arial", 14), fg="blue").pack(pady=10)

    # ゲーム結果の詳細
    result_details = (
        f"総ターン数: {game_state['turn']}\n"
        f"最終資金: {game_state['funds']} 万円\n"
        f"最終従業員数: {game_state['employees']} 人\n"
        f"最終技術力: {game_state['tech_level']} 点\n"
        f"最終市場シェア: {game_state['market_share']}%"
    )
    tk.Label(root, text=result_details, font=("Arial", 12), justify="left").pack(pady=10)

    # 閉じるボタン
    tk.Button(root, text="終了", command=root.destroy).pack(pady=20)

    root.mainloop()
