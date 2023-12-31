#!/usr/bin/env python3
"""
RPZ-Stepper用サンプルコード
2つのモーターを制御する
Indoor Corgi, https://www.indoorcorgielec.com
解説ページ: https://www.indoorcorgielec.com/resources/raspberry-pi/rpz-stepper-multiple-motors/
"""

import time
from cgstep import TMC5240

m1 = TMC5240(device=0)  # モーター1 (J3 MOTOR1端子)
m2 = TMC5240(device=1)  # モーター2 (J4 MOTOR2端子)

# 設定はモーターごとに行う必要がある

# モーター1の設定
m1.ifs = 0.5  # モーターの定格に合わせて電流値を設定 (例:0.5A)
m1.vmax_rpm = 60  # 回転速度
m1.amax = 500  # 加速
m1.dmax = 500  # 減速
m1.enable()  # ドライバーの出力をON

# モーター2の設定
m2.ifs = 0.5  # モーターの定格に合わせて電流値を設定 (例:0.5A)
m2.vmax_rpm = 30  # 回転速度
m2.amax = 300  # 加速
m2.dmax = 300  # 減速
m2.enable()  # ドライバーの出力をON

# モーター1を3回転, モーター2を1回転
m1.xtarget = 153600
m2.xtarget = 51200
time.sleep(5)

# モーター1, 2を元の位置に戻す
m1.xtarget = 0
m2.xtarget = 0
