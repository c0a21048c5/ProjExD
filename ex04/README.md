# 第4回
## 逃げろこうかとん(ex04/dodge_bomb.py)
### ゲーム概要
- ex04/dodge_bomb.pyを実行すると、1600×900のスクリーンに草原が描画されこうかとんを移動させ飛び回る爆弾から逃げるゲーム
- こうかとんが爆弾と接触するとゲームオーバで終了する
###　操作方法
- 矢印キーまたはWASDキーでこうかとんを上下左右に移動する
### 追加機能
- 矢印キーに加えてWASDキーでこうかとんを移動できるように変更
- 爆弾を複数個に変更
- 被弾した際にメッセージボックスを表示し閉じるように変更
- メッセージボックスに被弾するまでの経過時間を計測し表示するように変更
### ToDo (実装しようと思ったけど時間がなかった)
- 着弾するとこうかとんの画像が切り替わる
- 時間経過に応じて、爆弾の速度と爆弾の個数を増加させる