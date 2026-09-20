"""
ステップ1: 自機の移動と弾の発射
シューティングゲームの一番の土台になるサンプルです。

操作方法:
  左右矢印キー / A・D : 左右移動
  スペースキー         : 弾を発射
  Esc または ウィンドウを閉じる : 終了
"""
import pygame
import sys

import config

# ----- initial settings -----
pygame.init()

