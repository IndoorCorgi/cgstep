#!/usr/bin/env python3
"""
RPZ-Stepper用サンプルコード
4つのモーターを制御する
Indoor Corgi, https://www.indoorcorgielec.com
解説ページ: https://www.indoorcorgielec.com/resources/raspberry-pi/rpz-stepper-multiple-motors/
"""

import time
from cgstep import TMC5240

m1 = TMC5240(board_id=0, device=0)  # モーター1 (BD_ID OFF基板 / J3 MOTOR1端子)
m2 = TMC5240(board_id=0, device=1)  # モーター2 (BD_ID OFF基板 / J4 MOTOR2端子)
m3 = TMC5240(board_id=1, device=0)  # モーター3 (BD_ID ON基板 / J3 MOTOR1端子)
m4 = TMC5240(board_id=1, device=1)  # モーター4 (BD_ID ON基板 / J4 MOTOR2端子)

# 設定はモーターごとに行う必要がある

# モーター1の設定
m1.current_range = 2  # 電流レンジ
m1.vmax = 68720  # 回転速度
m1.amax = 500  # 加速
m1.dmax = 500  # 減速
m1.enable()  # ドライバーの出力をON

# モーター4の設定
m4.current_range = 2  # 電流レンジ
m4.vmax = 34360  # 回転速度
m4.amax = 300  # 加速
m4.dmax = 300  # 減速
m4.enable()  # ドライバーの出力をON

# モーター1を3回転, モーター4を1回転
m1.xtarget = 153600
m4.xtarget = 51200
time.sleep(5)

# モーター1, 4を元の位置に戻す
m1.xtarget = 0
m4.xtarget = 0
