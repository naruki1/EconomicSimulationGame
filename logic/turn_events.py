import random
from logic.game_state import get_game_state
from tkinter import messagebox

def trigger_random_event():
    """ランダムイベントを発生させる（選択肢付きイベントを含む）"""
    game_state = get_game_state()

    events = [
        {"description": "競合他社が革新的な製品を発表！ 市場シェアが減少しました。", "effect": lambda: update_share(-5), "type": "negative"},
        {"description": "新たな投資家を獲得しました！ 資金が増加しました。", "effect": lambda: update_funds(800), "type": "positive"},
        {"description": "研究開発が成功し、技術力が向上しました！", "effect": lambda: update_tech(3), "type": "positive"},
        {"description": "従業員の士気が向上しました！ 生産力が増加しました。", "effect": lambda: update_employees(10), "type": "positive"},
        {"description": "原材料費の高騰により、資金が減少しました。", "effect": lambda: update_funds(-400), "type": "negative"},
        {"description": "大規模なマーケティングキャンペーンが成功し、市場シェアが増加しました！", "effect": lambda: update_share(7), "type": "positive"},
        {"description": "競合企業から買収提案がありました！", "effect": buyout_event, "type": "neutral"},
    ]

    # ランダムにイベントを選択
    event = random.choice(events)

    # 効果を適用
    if "effect" in event:
        result = event["effect"]()

    # イベント内容を返す
    return event["description"], event["type"]

def update_funds(amount):
    """資金を増減させる"""
    game_state = get_game_state()
    game_state["funds"] = max(0, game_state["funds"] + amount)

def update_employees(amount):
    """従業員数を増減させる"""
    game_state = get_game_state()
    game_state["employees"] = max(0, game_state["employees"] + amount)

def update_tech(amount):
    """技術力を増減させる"""
    game_state = get_game_state()
    game_state["tech_level"] = max(0, game_state["tech_level"] + amount)

def update_share(amount):
    """市場シェアを増減させる"""
    game_state = get_game_state()
    game_state["market_share"] = max(0, min(100, game_state["market_share"] + amount))

def buyout_event():
    """買収提案イベント"""
    def accept():
        update_funds(1000)
        update_share(-10)
        messagebox.showinfo("買収提案", "買収を受け入れました！ 資金が増加しましたが市場シェアが減少しました。")
        return "買収を受け入れ、資金が増加しました。"

    def decline():
        messagebox.showinfo("買収提案", "買収を断りました。現状維持です。")
        return "買収を断り、現状を維持しました。"

    # 選択肢のダイアログを表示
    response = messagebox.askquestion(
        "買収提案",
        "競合企業から買収提案があります。資金を 1000 万円得る代わりに市場シェアが 10% 減少します。\n\n提案を受け入れますか？",
        icon="warning"
    )

    if response == "yes":
        return accept()
    else:
        return decline()