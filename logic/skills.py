import json
import os

# スキルデータをロード
def load_skills_data():
    """JSONファイルからスキルデータを読み込む"""
    file_path = os.path.join("data", "skills.json")
    with open(file_path, "r", encoding="utf-8") as file:
        return json.load(file)

# スキルデータをロード
skills_data = load_skills_data()

def unlock_skill(skill_name, game_state):
    """スキルをアンロック"""
    skill = skills_data.get(skill_name)
    if not skill:
        return f"スキル '{skill_name}' が見つかりません。"

    if game_state["tech_level"] >= skill["cost"]:
        game_state["tech_level"] -= skill["cost"]
        return f"{skill_name} を取得しました: {skill['effect']}"
    else:
        return "技術力が不足しています。"
