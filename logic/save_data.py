import os
import json
from datetime import datetime

def save_game_result(game_state, result_message):
    """
    ゲーム結果をテキストファイルに保存
    """
    # 保存ディレクトリを設定
    save_dir = "saved_results"
    os.makedirs(save_dir, exist_ok=True)  # ディレクトリがなければ作成

    # 保存ファイル名を生成
    timestamp = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
    file_name = f"result_{timestamp}.txt"
    file_path = os.path.join(save_dir, file_name)

    # 保存内容を準備
    result_details = {
        "総ターン数": game_state["turn"],
        "最終資金": f"{game_state['funds']} 万円",
        "最終従業員数": f"{game_state['employees']} 人",
        "最終技術力": f"{game_state['tech_level']} 点",
        "最終市場シェア": f"{game_state['market_share']}%",
        "結果": result_message,
        "日時": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
    }

    # テキストファイルに保存
    with open(file_path, "w", encoding="utf-8") as file:
        file.write("ゲーム結果:\n")
        for key, value in result_details.items():
            file.write(f"{key}: {value}\n")

    print(f"結果が保存されました: {file_path}")
