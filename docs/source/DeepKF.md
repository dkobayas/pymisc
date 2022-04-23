# Deep Kalman Filter(DeepKF)

DKFを実装し、利用しやすい形のAPIに落とし込みたい。
以下のGitHubでは、PyroとPyTorchを使って実装しているようなので、真似て実装してみる。[GitHub(Pyro+Pytorch)][GitHub(Pyro+Pytorch)]
Pyro, Pytorchの扱いに慣れるという意味も込めている。

## 想定構造
```sh
deepkf/  
|- __init__.py
|- deepkf.py  
| |- class model()  
|- loader.py  
| |- def test_sample()
| |- def load_pandas()
|- utils.py
```

## reference

- [paper](https://arxiv.org/abs/1511.05121)
- [slides(jp)](https://deeplearning.jp/wp-content/uploads/2017/07/DL_hacks_20151225.pdf) 
- [GitHub(Pyro+Pytorch)][GitHub(Pyro+Pytorch)]

[GitHub(Pyro+Pytorch)]: https://github.com/DanieleGammelli/DeepKalmanFilter