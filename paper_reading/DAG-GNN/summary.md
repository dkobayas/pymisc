# DAG-GNN: DAG Structure Learning with Graph Neural Networks

Author: Yue Yu, Jie Chen, Tian Gao, Mo Yu  
Submitted on 22 Apr 2019  
Cite : [arXiv:1904.10098](https://arxiv.org/pdf/1904.10098.pdf),
Code : [GitHub](https://github.com/fishmoon1234/DAG-GNN)
***

![category](https://img.shields.io/badge/category-paper-00a0a0.svg?longCache=true)
![topic](https://img.shields.io/badge/topic-causal_analysis-a000a0.svg?longCache=true)
![progress](https://progress-bar.dev/7/?title=progress)


## 概要

- 信頼性の高いDAGの学習はチャレンジングな課題である(ノード増加に伴って探索空間が爆発的に増えるため)
- 最近は非循環の条件を微分可能な最小化問題に落とし込むというブレイクスルーがあった
- ただ、彼らは線形の構造方程式(SEM)を仮定して、最小二乗法での損失関数を使っており、よく理解されている反面、制限の多い手法を使っていた。
- DLが複雑な非線形マッピングに対して幅広く応用されてきていることを受けて、DLを利用した構造的な制約を加えたDAGの学習方法を提案する。
- これはGNNを利用したVariational AutoEncoder(VAE)を使った手法になっており、DAG-GNNと名付けている。
- さらにより用途を拡張するために、ベクトル値と同様に、離散値を自然に扱えるようにした。
- 合成データを使ったデモでは、非線形を仮定して作られたサンプルに対しては、より正確な構造学習ができることを示した。
- 離散値を用いたデータでは、大域的最適化と遜色のない結果を示すことを確認した。

## 導入

ベイジアンネットワーク(BN)は機械学習分野で広く利用されてきた。
BNは有向非循環グラフ(DAG)の形式をとり、因果効果の中心的な役割を果たしている。
構造学習の課題はNP困難であり、組み合わせの爆発的増加が挙げられる。

スコアベースの手法は、不明な係数行列(A)に対するスコア関数を最適化するもので、グラフが非循環になるという制約が課されるものになる。
最適化の実質的な課題は、複雑な探索領域である。
そのため、実質的には、さらに構造上の仮定が必要になる。

近年、非循環の制約と等価な連続的な関数が導入された。


## 背景と関連研究
## ニューラルネットでのDAG学習

## 実験

## 結論
