# SortVisualization

Visualizing various sorting algorithms by python3

このプログラムでは様々なソートの可視化を行う

python3を用いてソート時のメモリ空間を棒グラフで表示

pythonのコードではフレームあたりの画像を生成するため、
動画にする際はimagemagickを用いてgifに変換する必要

コマごとの画像の生成
```bash
$ python3 vissort.py
```

gif動画の生成
```bash
$ convert -delay 10 -loop 0 pic/image*.png movie.gif
```

gif動画の圧縮
```bash
$ convert movie.gif -coalesce -scale 70% -deconstruct output.gif
```

以下の動画は挿入ソートの例です。

![result](https://github.com/smallptarmigan/SortVisualization/blob/master/media/sample.gif)

