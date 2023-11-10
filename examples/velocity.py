#!/usr/bin/env python3
"""
RPZ-Stepper用サンプルコード
モーターを指定速度(回転数)で回転させる
Indoor Corgi, https://www.indoorcorgielec.com
解説ページ: https://www.indoorcorgielec.com/resources/raspberry-pi/rpz-stepper-velocity-mode/
"""

import time
from cgstep import TMC5240

m1 = TMC5240()  # モーター制御クラスのインスタンス

# 必ず行う設定
m1.rampmode = TMC5240.RAMPMODE_VELOCITY_POSITIVE  # 速度指定モードにする.
m1.current_range = 2  # 電流レンジ
m1.vmax = 0  # 回転速度 最初は停止させておくため0にする
m1.amax = 500  # 加速
m1.dmax = 500  # 減速
m1.enable()  # ドライバーの出力をONにしてモーターに電圧印加

m1.vmax = 20000  # 速度vmaxに書き込むとモーターが回転しはじめる
time.sleep(5)

m1.vmax = 70000  # 速度を変更
time.sleep(5)

m1.vmax = 0  # 停止
time.sleep(2)

m1.rampmode = TMC5240.RAMPMODE_VELOCITY_NEGATIVE  # 回転方向を逆にする
m1.vmax = 20000  # 回転
time.sleep(5)

m1.vmax = 0  # 停止
time.sleep(2)

m1.rampmode = TMC5240.RAMPMODE_POSITIONING  # 位置指定モードに戻す
