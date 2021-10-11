Pygame CJCU大冒險 
===
# Introduction
RPG單人小遊戲且有音效，使用WASD來移動、J攻擊、Shift加速，透過急殺前面較簡單的小怪物升級，當到達一定等級後可使用傳送陣，傳送到下一張地圖斬除鬼火BOSS。
# Demo
移動方式: W、A、S、D (shift加速)![](https://i.imgur.com/YUmHiNv.png)

攻擊: J![](https://i.imgur.com/osGKJAI.png)

障礙物判定:圖片為牆壁的地方，會無法繼續往前走。

![](https://i.imgur.com/P4kWN8r.png)

血量等級:擊倒一定數量的怪物可以提升等級，增加血量和攻擊力

![](https://i.imgur.com/5L7yxLx.png)


傳送陣:透過傳送陣前往下一張地圖來打敗魔王，魔王會自動隨機走動，只要碰到就會被扣10滴血

![](https://i.imgur.com/OeYpY6s.png)

遊戲結果:會有成功和失敗的場景和音效跑出來

![](https://i.imgur.com/hwm9Ml6.png)




# Requirement
    pygame
# Package
    CJCU_pygame
        │  game.py 主程式
        │  
        └─source   素材包