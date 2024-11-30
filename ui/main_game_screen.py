import tkinter as tk
from logic.game_state import initialize_game_state, get_game_state, check_game_over, check_victory
from logic.turn_events import trigger_random_event
from logic.actions import execute_action
from tkinter import messagebox
from tkinter import ttk
from ui.result_screen import show_result_screen
from logic.competitor_logic import competitor_turn
from logic.skills import unlock_skill, skills_data
from logic.competitor_logic import load_competitor_data, competitor_turn

# 競合データを初期化
competitors = load_competitor_data()

def show_main_game_screen(selected_industry):
    # ゲーム状態の初期化
    initialize_game_state(selected_industry)
    game_state = get_game_state()

    
    def next_turn():
        competitor_turn(competitors)
        # 競合情報パネル
        competitors_frame = tk.Frame(root, bg="lightyellow", bd=2, relief="groove")
        competitors_frame.place(x=330, y=300, width=550, height=200)

        tk.Label(competitors_frame, text="競合情報", font=("Arial", 14), bg="lightyellow").pack()

        for name, data in competitors.items():
            tk.Label(competitors_frame, text=f"{name}: シェア {data['market_share']}%, 技術力 {data['tech_level']}点", bg="lightyellow").pack()
            
        """次のターン進行の処理"""
        game_state["turn"] += 1

        # ランダムイベントの発生
        event_description, event_type = trigger_random_event()
        log_event(f"ターン {game_state['turn']}: {event_description}", event_type)

        # ステータスを更新
        update_stats()

        # ゲーム終了条件の確認
        game_over_message = check_game_over()
        if game_over_message:
            show_result_screen(game_state, f"ゲームオーバー: {game_over_message}")
            root.destroy()  # ゲーム画面を閉じる
            return

        victory_message = check_victory()
        if victory_message:
            show_result_screen(game_state, f"勝利: {victory_message}")
            root.destroy()  # ゲーム画面を閉じる
            return

    def perform_action(action):
        """アクションを実行し、結果をログに表示"""
        result = execute_action(action)
        event_log.insert(tk.END, result)
        update_stats()

    def update_stats():
        """企業情報とターン数を更新"""
        funds_label.config(text=f"資金: {game_state['funds']} 万円")
        employees_label.config(text=f"従業員数: {game_state['employees']} 人")
        tech_label.config(text=f"技術力: {game_state['tech_level']} 点")
        share_label.config(text=f"市場シェア: {game_state['market_share']}%")

        # ターン数の更新
        turn_label.config(text=f"ターン: {game_state['turn']}")
        
        # ゲージの更新
        funds_bar["value"] = min(100, game_state["funds"] / 20)  # 最大2000万を基準
        tech_bar["value"] = min(100, game_state["tech_level"])   # 最大100点を基準
        share_bar["value"] = min(100, game_state["market_share"])  # 最大100%を基準

    def log_event(event_description, event_type="neutral"):
        """
        イベントをログに表示し、色を付ける。
        - event_description: 表示するテキスト。
        - event_type: イベントの種類 ("positive", "negative", "neutral")。
        """
        colors = {
            "positive": "green",
            "negative": "red",
            "neutral": "black"
        }

        # イベントをログに追加
        event_log.insert(tk.END, event_description)
        event_log.itemconfig(tk.END, fg=colors.get(event_type, "black"))
        event_log.see(tk.END)  # ログの末尾にスクロール



    # メインウィンドウ設定
    root = tk.Tk()
    root.title("メインゲーム画面")
    root.geometry("900x600")

    # ターン数表示
    turn_label = tk.Label(root, text=f"ターン: {game_state['turn']}", font=("Arial", 16), bg="lightgray")
    turn_label.place(x=10, y=10, width=200, height=30)

    # 企業情報パネル
    info_frame = tk.Frame(root, bg="lightblue", bd=2, relief="groove")
    info_frame.place(x=10, y=50, width=300, height=200)

    funds_label = tk.Label(info_frame, text="", bg="lightblue", anchor="w")
    funds_label.pack(fill="x", pady=5)
    funds_bar = ttk.Progressbar(info_frame, orient="horizontal", length=200, mode="determinate", maximum=100)
    funds_bar.pack(pady=5)

    employees_label = tk.Label(info_frame, text="", bg="lightblue", anchor="w")
    employees_label.pack(fill="x", pady=5)

    tech_label = tk.Label(info_frame, text="", bg="lightblue", anchor="w")
    tech_label.pack(fill="x", pady=5)
    tech_bar = ttk.Progressbar(info_frame, orient="horizontal", length=200, mode="determinate", maximum=100)
    tech_bar.pack(pady=5)

    share_label = tk.Label(info_frame, text="", bg="lightblue", anchor="w")
    share_label.pack(fill="x", pady=5)
    share_bar = ttk.Progressbar(info_frame, orient="horizontal", length=200, mode="determinate", maximum=100)
    share_bar.pack(pady=5)

    update_stats()

    def perform_skill_action(skill_name):
        """スキルを取得し、結果をログに表示"""
        result = unlock_skill(skill_name, game_state)
        log_event(result, event_type="positive" if "取得しました" in result else "negative")

    # スキル取得ボタンを動的に生成
    for skill_name, skill_info in skills_data.items():
        button_text = f"{skill_name} (コスト: {skill_info['cost']})"
        tk.Button(root, text=button_text, command=lambda s=skill_name: perform_skill_action(s)).pack()

    # アクションボタンパネル
    actions_frame = tk.Frame(root, bg="lightgreen", bd=2, relief="groove")
    actions_frame.place(x=330, y=50, width=550, height=200)

    actions = ["資金調達", "製品開発", "マーケティング", "採用"]
    for action in actions:
        btn = tk.Button(actions_frame, text=action, width=15, command=lambda a=action: perform_action(a))
        btn.pack(side="left", padx=10, pady=10)

    # イベントログエリア
    event_log_frame = tk.Frame(root, bg="white", bd=2, relief="sunken")
    event_log_frame.place(x=10, y=300, width=870, height=250)

    event_log = tk.Listbox(event_log_frame, bg="white")
    event_log.pack(fill="both", expand=True)

    # 次のターンボタン
    turn_button = tk.Button(root, text="次のターンへ", command=next_turn)
    turn_button.place(x=400, y=550, width=100, height=40)

    tk.Button(root, text="スキル取得", command=lambda: unlock_skill("製品性能向上", game_state)).pack()

    root.mainloop()
