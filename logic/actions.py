from logic.game_state import get_game_state

def execute_action(action):
    """指定されたアクションを実行"""
    game_state = get_game_state()

    if action == "資金調達":
        # 資金を増加
        game_state["funds"] += 500
        return "資金調達を実施しました。資金が 500 万円増加しました！"

    elif action == "製品開発":
        # 技術力を増加し、資金を消費
        if game_state["funds"] >= 300:
            game_state["funds"] -= 300
            game_state["tech_level"] += 2
            return "製品開発を進めました。技術力が 2 点増加しました！"
        else:
            return "資金が不足しているため、製品開発を実施できません！"

    elif action == "マーケティング":
        # 市場シェアを増加し、資金を消費
        if game_state["funds"] >= 200:
            game_state["funds"] -= 200
            game_state["market_share"] += 3
            return "マーケティングを展開しました。市場シェアが 3% 増加しました！"
        else:
            return "資金が不足しているため、マーケティングを実施できません！"

    elif action == "採用":
        # 従業員数を増加し、資金を消費
        if game_state["funds"] >= 100:
            game_state["funds"] -= 100
            game_state["employees"] += 5
            return "新しい従業員を採用しました！ 従業員数が 5 人増加しました！"
        else:
            return "資金が不足しているため、採用を実施できません！"

    return "不明なアクションです。"
