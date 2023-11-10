#!/usr/bin/env python3
"""
RPZ-Stepper用サンプルコード
電流設定, 電流測定
Indoor Corgi, https://www.indoorcorgielec.com
解説ページ: https://www.indoorcorgielec.com/resources/raspberry-pi/rpz-stepper-current/
"""

import time
from cgstep import TMC5240

m1 = TMC5240()  # モーター制御クラスのインスタンス

# 電流レンジ
# 2なら3A, 1なら2A, 0なら1A. (ピーク電流なので3Aの場合実効値は2.1A)
# 回転時電流irun, 停止時電流iholdの最大値に影響
m1.current_range = 2

# 電流レンジの微調整
# global_scalerが0だと無効
# global_scalerに1-255を設定すると current_rangeで設定した値 x (global_scaler)/256 を電流レンジにする
m1.global_scaler = 0

m1.irun = 31  # 回転時電流を0-31で指定. 初期値31
m1.ihold = 31  # 停止時電流を0-31で指定. 初期値8
m1.tpowerdown = 10  # 停止後irunを保持する時間 = tpowerdown x 21[ms]. 0-255で指定. 初期値10.

# 必ず行う設定
m1.vmax = 68720  # 回転速度
m1.amax = 500  # 加速
m1.dmax = 500  # 減速
m1.enable()  # ドライバーの出力をONにしてモーターに電圧印加

time.sleep(3)
print('電流(ihold=31): {}A'.format(m1.board_current))  # board_currentで基板の電流合計を取得

m1.ihold = 4  # 停止時電流を変更
time.sleep(3)
print('電流(ihold=4): {}A'.format(m1.board_current))

m1.rampmode = TMC5240.RAMPMODE_VELOCITY_POSITIVE  # 定速で回転
time.sleep(3)
print('電流(irun=31): {}A'.format(m1.board_current))

m1.irun = 16
time.sleep(3)
print('電流(irun=16): {}A'.format(m1.board_current))

# 元の位置に戻す
m1.rampmode = TMC5240.RAMPMODE_POSITIONING
