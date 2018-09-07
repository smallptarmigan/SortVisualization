# SortVisualization

Visualization by python3 of various sorting algorithms

このプログラムでは様々なソートの可視化を行う

python3を用いてソート時のメモリ空間を棒グラフで表示

pythonのコードではフレームあたりの画像を生成するため、
動画にする際はimagemagickを用いてgifに変換する必要

コマごとの画像の生成
```bash
$ python3 vissort.py
```
出力画像はpicというディレクトリ下に出されるためない場合は
作ってから実行するとエラーが解消されるかもしれません

gif動画の生成
```bash
$ convert -delay 10 -loop 0 pic/image*.png movie.gif
```

![result](https://github.com/smallptarmigan/SortVisualization/blob/master/media/sample.gif)

