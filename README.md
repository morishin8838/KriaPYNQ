# KriaPYNQ For Ubuntu

## ファイル構成
```
├ HLS/ 
│├ jupyter/
│├ vivado/
│└ VisionLibrary/
│ 　└ OpenCV/
│
├ Ubuntu20.04/
│├ KV260/
││　└ custom/
││
│└ KR260/
│ 　└ custom/
├ Vitis-AI/
│├ DPU/
│└ Tensorflow/

```

## クロスコンパイラインストール
* Ubuntu20.04ホストで運用していると、稀に消失。なぜだろう。その時入れなおし。
* $ sudo apt-get install qemu
* $ sudo apt-get install g++-aarch64-linux-gnu


