#!/usr/bin/env python3
"""
RPZ-Stepper用サンプルコード
加減速を細かく指定する
Indoor Corgi, https://www.indoorcorgielec.com
解説ページ: https://www.indoorcorgielec.com/resources/raspberry-pi/rpz-stepper-acceleration/
"""

import time
from cgstep import TMC5240

m1 = TMC5240()  # モーター制御クラスのインスタンス

# 加減速を細かく指定する
m1.v1 = 20000  # 1つめの速度域しきい値
m1.a1 = 200  # 速度が0〜v1の範囲の加速
m1.d1 = 200  # 速度が0〜v1の範囲の減速
m1.v2 = 50000  # 2つ目の速度域しきい値. 0を設定して省略できる.
m1.a2 = 1000  # 速度がv1〜v2の範囲の加速
m1.d2 = 1000  # 速度がv1〜v2の範囲の減速
m1.amax = 500  # 速度がv2〜vmaxの範囲の加速
m1.dmax = 500  # 速度がv2〜vmaxの範囲の減速
m1.vmax = 70000  # 回転速度

m1.current_range = 0  # 電流基準値
m1.global_scaler = 128  # 電流倍率
m1.enable()  # ドライバーの出力をONにしてモーターに電圧印加

m1.xtarget = 256000  # 200ステップ/回転のモーターで5回転
time.sleep(5)

m1.xtarget = 0  # 元の位置に戻す
