# ゲーム状態を保持する辞書
game_state = {
    "turn": 1,
    "funds": 1000,
    "employees": 10,
    "tech_level": 5,
    "market_share": 10,
    "customer_satisfaction": 80,  # 顧客満足度
    "employee_morale": 70         # 従業員士気
}

# 業界ごとの初期設定
industry_data = {
    "テクノロジー": {"funds": 1500, "employees": 20, "tech_level": 10, "market_share": 15},
    "消費財": {"funds": 1000, "employees": 15, "tech_level": 5, "market_share": 10},
    "製造業": {"funds": 1200, "employees": 25, "tech_level": 7, "market_share": 12},
    "エネルギー": {"funds": 2000, "employees": 30, "tech_level": 8, "market_share": 20},
}

def initialize_game_state(industry):
    """選択された業界に基づいてゲーム状態を初期化"""
    global game_state
    game_state = industry_data[industry]
    game_state["turn"] = 1  # ターン数を初期化

def get_game_state():
    """現在のゲーム状態を取得"""
    return game_state

def check_game_over():
    """ゲームオーバー条件を判定"""
    game_state = get_game_state()
    if game_state["funds"] <= 0:
        return "資金が尽きたため、会社は倒産しました。"

    if game_state["turn"] > 16:  # 制限ターン数
        return "制限ターン数を超過しました。会社は市場での競争に敗れました。"

    return None  # ゲーム継続

def check_victory():
    """勝利条件を判定"""
    game_state = get_game_state()
    if game_state["market_share"] >= 50:
        return "市場シェアが50%を超えました！業界トップ企業として認められました！"
    
    return None  # 勝利条件未達成

