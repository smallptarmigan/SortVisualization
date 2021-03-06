# Sort Visualization 15type

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

|| ソート |  | 計算量 | オプション |
|:------------:|:------------:|:------------:|:------------:|:------------:|
| 1 | 挿入ソート | insertion sort | <img src="https://latex.codecogs.com/png.latex?O(n^2)" /> | -in |
| 2 | バブルソート | bubble sort | <img src="https://latex.codecogs.com/png.latex?O(n^2)" /> | -bu |
| 3 | 選択ソート | selection sort | <img src="https://latex.codecogs.com/png.latex?O(n^2)" /> | -se |
| 4 | マージソート | merge sort | <img src="https://latex.codecogs.com/png.latex?O(n&space;\log&space;n)" /> | -me |
| 5 | クイックソート | quick sort | <img src="https://latex.codecogs.com/png.latex?O(n&space;\log&space;n)" /> | -qu | 
| 6 | LSD 基数ソート | LSD radix sort | <img src="https://latex.codecogs.com/png.latex?O(nk)" /> | -lsd |
| 7 | MSD 基数ソート | MSD radix sort | <img src="https://latex.codecogs.com/png.latex?O(nk)" /> | -msd |
| 8 | シェルソート | shell sort | <img src="https://latex.codecogs.com/png.latex?O(n&space;\log&space;n)" /> | -sh |
| 9 | シェイカーソート | shaker sort | <img src="https://latex.codecogs.com/png.latex?O(n^2)" /> | -sk |
| 10 | ヒープソート | heap sort | <img src="https://latex.codecogs.com/png.latex?O(n&space;\log&space;n)" /> | -he |
| 11 | コムソート | comb sort | <img src="https://latex.codecogs.com/png.latex?O(n^2)" /> | -cm |
| 12 | 奇偶転置ソート | oddeven sort | <img src="https://latex.codecogs.com/png.latex?O(n^2)" /> | -oe |
| 13 | ノームソート | gnome sort | <img src="https://latex.codecogs.com/png.latex?O(n^2)" /> | -gn |
| 14 | グラビティソート | gravity sort | <img src="https://latex.codecogs.com/png.latex?O(n)" /> | -gr |
| 15 | ストゥージソート | stooge sort | <img src="https://latex.codecogs.com/gif.latex?O(n^{log&space;3&space;/&space;log&space;1.5}&space;)" /> | -st |


