# GraphVizPlotly(gvplotly)

有向グラフをインタラクティブに可視化する手法があまりいいいのが見当たらなかったので、graphviz, plotlyの組み合わせで自作してみる。

## 要求項目・実装メモ

- ノードの配置はgraphvizで行って、描画自体はplotlyでやる
- エッジは注釈機能を使うが、ノードと被らないようにするのが難しい。
- ノードにマウスオーバーすると、ノードと関連エッジの数値が出る。

### 想定構造
```sh
gvplotly/   
|- __init__.py
|- digviz.py  # 基本はFigure
| |- class Figure()  
| |- 他の同梱物があまり思いつかない...  
|- loader.py  # data loader
| |- def test_dig() -> nx.DiGraph()
| |- def load_pandas()
|- utils.py # utility functions
```

## 類似したもの

- dash-interactive-graphvizは似たような感じかと思って試してはみたが、dashを使わなければならない点や、編集できる機能が必要かどうか微妙なため、保留。それよりは、マウスオーバーした時の反応や関連特徴量の見せ方などの方が大事なので、差別化するようなものにする。

## memo

- networkx -> graphvizとするには、やはりpygraphvizが必要なので、逃げられない。(というか、networkxが内部でpygraphvizを使っているようで、pip installはしておいてあげないといけない。)
- gvplotlyはpackageをパッケージとして
    - digviz.py: directed graph
    - gviz.py: non-directed graph  

    のvisualization toolとしてモジュールを持っておきたい。
- digvizは内部に
    - Figure(class): 図の描画などを担当するメインクラス
    - GAttr(func): Graph attributeの設定
    - NAttr(func): Node attrの設定
    - EAttr(func): Edge attrの設定
    
    など有向グラフを効果的にインテラクティブにするための関数を揃えておく。