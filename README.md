# SortVisualization

Visualizing various sorting algorithms by python3

このプログラムでは様々なソートの可視化を行う

python3を用いてソート時のメモリ空間を棒グラフで表示

pythonのコードではフレームあたりの画像を生成するため、

動画にする際はimagemagickを用いてgifに変換する必要

コマごとの画像の生成(pic/下に画像が生成されます)
```bash
$ python3 -B main.py
```

gif動画の生成(delayによって速さを変えられます)
```bash
$ convert -delay 3 -loop 0 pic/image*.png movie.gif
```

gif動画の圧縮
```bash
$ convert movie.gif -coalesce -scale 70% -deconstruct output.gif
```

以下の動画は選択ソートの例です。

![result](https://github.com/smallptarmigan/SortVisualization/blob/master/gif/sample.gif)

現在実行可能なソート

・挿入ソート

・バブルソート

・選択ソート

・マージソート

・クイックソート

