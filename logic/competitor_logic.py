import random
import json
import os

def load_competitor_data():
    """競合データをJSONファイルからロード"""
    file_path = os.path.join("data", "competitors.json")
    with open(file_path, "r", encoding="utf-8") as file:
        return json.load(file)


def competitor_turn(competitors):
    """競合企業のターン進行"""
    for name, data in competitors.items():
        # 市場シェアと技術力のランダムな変動
        data["market_share"] = max(0, data["market_share"] + random.randint(-1, 2))
        data["tech_level"] = max(0, data["tech_level"] + random.randint(0, 1))
