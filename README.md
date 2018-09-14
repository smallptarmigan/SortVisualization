# SortVisualization

Visualizing various sorting algorithms by python3

このプログラムでは様々なソートの可視化を行う

python3を用いてソート時のメモリ空間を棒グラフで表示

pythonのコードではフレームあたりの画像を生成するため、

動画にする際はimagemagickを用いてgifに変換する必要があります

※始めて実行する際はpicという名前のディレクトリを作る必要があります

コマごとの画像の生成(pic/下に画像が生成されます/オプションは下記参照)
```bash
$ python3 -B main.py [sort_option (ex:-in)]
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

| ソート |  | オプション |
|:------------:|:------------:|:------------:|
| 挿入ソート | insertion sort | -in |
| バブルソート | bubble sort | -bu |
| 選択ソート | selection sort | -se |
| マージソート | merge sort | -me |
| クイックソート | quick sort | -qu | 
| 基数ソート | radix sort | -ra |
| シェルソート | shell sort | -sh |

