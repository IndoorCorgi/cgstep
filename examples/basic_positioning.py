#!/usr/bin/env python3
"""
RPZ-Stepper用サンプルコード
モーターを指定位置まで回転させる
Indoor Corgi, https://www.indoorcorgielec.com
解説ページ: https://www.indoorcorgielec.com/resources/raspberry-pi/rpz-stepper-basic-positioning/
"""

import time
from cgstep import TMC5240

m1 = TMC5240(steps_per_rev=200)  # モーター制御クラスのインスタンス, steps_per_revは使用モーターの1回転のフルステップ数. 省略すると200

# 必ず行う設定
m1.ifs = 0.5  # モーターの定格に合わせて電流値を設定 (例:0.5A)
m1.vmax_rpm = 60  # 回転速度をrpmで指定. vmax=68720のように直接速度vの値も指定可能. 200ステップ/回転のモーターなら, 68720で約60rpm.
m1.amax = 500  # 加速の速さ 500だと1秒で速度v=47684(200ステップ/回転のモーターで41.6rpm)に達する加速
m1.dmax = 500  # 減速の速さ 500だと1秒で速度v=47684(200ステップ/回転のモーターで41.6rpm)から停止する減速
m1.enable()  # ドライバーの出力をONにしてモーターに電圧印加

# 目標位置をxtargetに書き込むとモーターが回転しはじめる
# 200ステップ/回転のモーターなら, 200x256マイクロステップ=51200で1回転
# +/-2147483647の範囲で指定 マイナスだと反対方向に回転
# この例では3回転
m1.xtarget = 153600

# モーター回転中は, xactualで現在位置, vactualで現在速度,
# position_reachedで目標到達したか確認できる
time.sleep(2)
print('----------')
print('現在の位置:', m1.xactual)
print('現在の速度:', m1.vactual)
print('目標到達したか:', m1.position_reached)

time.sleep(3)
print('----------')
print('現在の位置:', m1.xactual)
print('現在の速度:', m1.vactual)
print('目標到達したか:', m1.position_reached)

m1.xtarget = 0  # 目標座標に0を設定して最初の位置に戻す
time.sleep(5)

m1.moveto(153600)  # moveto関数を使うと, 目標に到達するまで自動で待機する
m1.moveto(0)

m1.disable()  # ドライバーの出力をOFFにしてモーターへの電圧印加停止
