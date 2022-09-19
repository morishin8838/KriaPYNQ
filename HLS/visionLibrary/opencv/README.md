# OpenCVセットアップ手順

1. ソースを入手する
```
    $git clone https://github.com/Itseez/opencv.git
    $git clone https://github.com/Itseez/opencv_contrib.git
    $cd opencv; 
    $git checkout -b work 3.4.5
    $cd opencv_contrib; 
    $git checkout -b work 3.4.5
```

2. ビルドを行う
```
    $cd opencv
    $mkdir build
    $cd build/
```
3. Makeする
    * インストール先はここにして、LIBだけを使う。
    * /home/User/opencv3.4.5Library

```
    $cmake -DOPENCV_EXTRA_MODULES_PATH=../../opencv_contrib/modules -D CMAKE_BUILD_TYPE=Release -D CMAKE_INSTALL_PREFIX=/home/User/opencv3.4.5Library
    $make -j8 2>&1 |tee make.log
```

4. インストール
```
    $sudo make install
    $sudo ldconfig
```
