#!/usr/bin/env python3
"""
RPZ-Stepper用サンプルコード
モーターを指定速度(回転数)で回転させる
Indoor Corgi, https://www.indoorcorgielec.com
解説ページ: https://www.indoorcorgielec.com/resources/raspberry-pi/rpz-stepper-velocity-mode/
"""

import time
from cgstep import TMC5240

m1 = TMC5240(steps_per_rev=200)  # モーター制御クラスのインスタンス

# 必ず行う設定
m1.rampmode = TMC5240.RAMPMODE_VELOCITY_POSITIVE  # 速度指定モードにする.
m1.ifs = 0.5  # モーターの定格に合わせて電流値を設定 (例:0.5A)
m1.vmax = 0  # 回転速度 最初は停止させておくため0にする
m1.amax = 500  # 加速, 減速
m1.enable()  # ドライバーの出力をONにしてモーターに電圧印加

m1.vmax_rpm = 20  # 速度を設定するとモーターが回転しはじめる

# velocity_reachedが0: 指定速度に未到達
# velocity_reachedが1: 指定速度に到達
while 0 == m1.velocity_reached:  # 指定速度に到達するまで待機
  time.sleep(1)
time.sleep(3)

m1.vmax_rpm = 60  # 速度を変更
time.sleep(5)

m1.vmax = 0  # 停止
while 0 == m1.velocity_reached:  # 指定速度に到達するまで待機
  time.sleep(1)

m1.rampmode = TMC5240.RAMPMODE_VELOCITY_NEGATIVE  # 回転方向を逆にする
m1.vmax_rpm = 30  # 回転
time.sleep(5)

m1.vmax = 0  # 停止
while 0 == m1.velocity_reached:  # 指定速度に到達するまで待機
  time.sleep(1)

m1.rampmode = TMC5240.RAMPMODE_POSITIONING  # 位置指定モードに戻す
m1.xactual = 0  # 速度指定モードで回転中も現在位置xactualは変動するので, 必要に応じて0に戻す
