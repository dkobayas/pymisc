# Directed Acyclic Graph Learning and Analysis(DAGLAs)

DAGの学習+可視化+利用をまとめておきたい。

## ベースとなる学習手法

各々はPyTorchでの実装を試してみたい。
- CausalNex
- DAG-GNN

## 想定構造
```sh
daglas/  
|- __init__.py
|- learner.py # DAG learning
| |- class dag_gnn()  
| |- class dag_notears()   
|- addition.py # insert new edges from new node in learned DAG
|- adaption.py # learn based on learned DAG  
|- prediction.py # predict based on learned DAG
|- loader.py # data loader
| |- def test_sample()  
| |- def load_pandas()
|- utils.py # utility funtions
```

出力はnx.DiGraph()形式にすることで、gvplotlyと連携が取れるようにする。

## 制限の入れ方など、追加機能

制限の入れ方として、各エッジの初期値と誤差を定義して、(初期値からの差分/誤差)に基づいた損失を課すことで、既知の因果構造をベースにした調整、及びエッジの追加ができるようにできないか。  
tabuを設定するときも、初期値を 0 として、誤差が非常に小さいものと定義すれば、同様の実装で可能そうだと考えた。

## 可視化

Plotlyを使ってみる。
- エッジの正負での色分け
- エッジの大きさで強さを表現
- ノードの形、色、など

## 因果構造図の利用

ナレッジグラフ、ベイジアンネットワークなど