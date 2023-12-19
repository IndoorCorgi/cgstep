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
m1.current_range = 0  # 電流基準値
m1.global_scaler = 128  # 電流倍率
m1.vmax = 68720  # 回転速度
m1.amax = 500  # 加速
m1.dmax = 500  # 減速
m1.enable()  # ドライバーの出力をON

# モーター2の設定
m2.current_range = 0  # 電流基準値
m2.global_scaler = 128  # 電流倍率
m2.vmax = 34360  # 回転速度
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
