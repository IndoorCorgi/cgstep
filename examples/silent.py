#!/usr/bin/env python3
"""
RPZ-Stepper用サンプルコード
静音モード
Indoor Corgi, https://www.indoorcorgielec.com
解説ページ: https://www.indoorcorgielec.com/resources/raspberry-pi/rpz-stepper-silent/
"""

import time
from cgstep import TMC5240

m1 = TMC5240()  # モーター制御クラスのインスタンス

# 静音モード有効
m1.en_pwm_mode = 1

# PWM周波数(通常は初期値の0で問題ない)
#  0: 24.4kHz
#  1: 36.6kHz
#  2: 48.8kHz
m1.pwm_freq = 0

# 必ず行う設定
m1.current_range = 0  # 電流基準値
m1.global_scaler = 128  # 電流倍率
m1.vmax = 80000  # 回転速度
m1.amax = 500  # 加速
m1.dmax = 500  # 減速
m1.enable()  # ドライバーの出力をONにしてモーターに電圧印加

m1.xtarget = 153600  # 回転
time.sleep(5)

# オプション機能
# tpwmthrsで速度vが一定以上になったら静音モードを解除できる
# tpwmthrsはtstep単位で指定する. tstep = 16777216 / v
# 200ステップ/回転のモーターで 60rpmのとき, 速度v=68720, tstep=244
m1.tpwmthrs = 244

m1.xtarget = 0  # 元の位置に戻す
time.sleep(5)

m1.tpwmthrs = 0  # 静音モード常に有効に戻す

# オプション機能
# freewheelで停止時の動作を変更可能(停止時電流ihold=0のときに有効)
#  0: 通常の動作. モーター位置を保持する
#  1: フリーホイール. 電流を流さず, モーターが外力で回転する
#  2: パッシブブレーキ. 電流を流さず, モーターが外力で回転するがブレーキがかかる
m1.freewheel = 1
m1.ihold = 0
