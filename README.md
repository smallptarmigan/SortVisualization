# SortVisualization

Visualizing various sorting algorithms by python3

このプログラムでは様々なソートの可視化を行う

python3を用いてソート時のメモリ空間を棒グラフで表示

pythonのコードではフレームあたりの画像を生成するため、

動画にする際はimagemagickを用いてgifに変換する必要があります

※始めて実行する際はpicという名前のディレクトリを作る必要があります

#### コマごとの画像の生成(pic/下に画像が生成されます/オプションは下記参照)
```bash
$ python3 -B main.py [sort_option (ex:-in)]
```

#### gif動画の生成(delayによって速さを変えられます)
```bash
$ convert -delay 3 -loop 0 pic/image*.png movie.gif
```

#### gif動画の圧縮
```bash
$ convert movie.gif -coalesce -scale 70% -deconstruct output.gif
```

以下の動画は選択ソートの例です。

![result](https://github.com/smallptarmigan/SortVisualization/blob/master/gif/sample.gif)

#### 現在実行可能なソート

| ソート |  | 計算量 | オプション |
|:------------:|:------------:|:------------:|:------------:|
| 挿入ソート | insertion sort | <img src="https://latex.codecogs.com/png.latex?O(n^2)" /> | -in |
| バブルソート | bubble sort | <img src="https://latex.codecogs.com/png.latex?O(n^2)" /> | -bu |
| 選択ソート | selection sort | <img src="https://latex.codecogs.com/png.latex?O(n^2)" /> | -se |
| マージソート | merge sort | <img src="https://latex.codecogs.com/png.latex?O(n&space;\log&space;n)" /> | -me |
| クイックソート | quick sort | <img src="https://latex.codecogs.com/png.latex?O(n&space;\log&space;n)" /> | -qu | 
| 基数ソート | radix sort | <img src="https://latex.codecogs.com/png.latex?O(nk)" /> | -ra |
| シェルソート | shell sort | <img src="https://latex.codecogs.com/png.latex?O(n&space;\log&space;n)" /> | -sh |
| シェイカーソート | shaker sort | <img src="https://latex.codecogs.com/png.latex?O(n^2)" /> | -sk |
| ヒープソート | heap sort | <img src="https://latex.codecogs.com/png.latex?O(n&space;\log&space;n)" /> | -he |
| コムソート | comb sort | <img src="https://latex.codecogs.com/png.latex?O(n^2)" /> | -cm |
| 奇偶転置ソート | oddeven sort | <img src="https://latex.codecogs.com/png.latex?O(n^2)" /> | -oe |
| ノームソート | gnome sort | <img src="https://latex.codecogs.com/png.latex?O(n^2)" /> | -gn |
| ストゥージソート | stooge sort | <img src="https://latex.codecogs.com/gif.latex?O(n^{log&space;3&space;/&space;log&space;1.5}&space;)" /> | -st |


