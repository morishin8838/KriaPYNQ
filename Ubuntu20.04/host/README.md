# HOSTセットアップ

## QT環境構築
1. rootfs取得 デバイスデータ同期 
* 192.168.1.82は任意アドレス
```
    $mkdr ~/Xilinx/LinuxForKV260
    $cd LinuxForKV260
    $mkdir -p rootfs/{lib,sbin,usr/{include,lib,bin},etc/alternatives}            
    $sudo rsync -e ssh -avz xilinx@192.168.1.82:/lib rootfs/
    $sudo rsync -e ssh -avz xilinx@192.168.1.82:/sbin rootfs/
    $sudo rsync -e ssh -avz xilinx@192.168.1.82:/usr/include rootfs/usr
    $sudo rsync -e ssh -avz --copy-links --exclude build xilinx@192.168.1.82:/usr/lib rootfs/usr
    $sudo rsync -e ssh -avz xilinx@192.168.1.82:/usr/bin rootfs/usr
    $sudo rsync -e ssh -avz xilinx@192.168.1.82:/etc/alternatives rootfs/etc       
    $sudo rsync -e ssh -avz xilinx@192.168.1.82:/usr/include rootfs/usr
```

2. build ソース〜ビルド〜インストール
    * ターゲットマシンと同じバージョンをビルドすること
    * 20.04は、qt5.12.8
```
    $wget https://download.qt.io/archive/qt/5.12/5.12.8/single/qt-everywhere-src-5.12.8.tar.xz
    $sudo chmod 775 qt-everywhere-src-5.12.8.tar.xz
    $xz -dc qt-everywhere-src-5.12.8.tar.xz | tar xfv -
    $cd $HOME/Xilinx/LinuxForKV260/qt-everywhere-src-5.12.8
    $mkdir build
    $cd build
    $ROOT_DIR=$HOME/Xilinx/LinuxForKV260
    $ROOTFS=$ROOT_DIR/rootfs
    $../configure -v -release -opensource -confirm-license -xplatform linux-aarch64-gnu-g++ -device-option CROSS_COMPILE=aarch64-linux-gnu- -no-pch -opengl desktop -no-eglfs -no-openssl -no-qml-debug -nomake tools -nomake examples -nomake tests -prefix /usr/local/qt5.12.8 -extprefix $ROOT_DIR/qt5.12.8 -hostprefix $ROOT_DIR/qt5.12.8-host -sysroot $ROOTFS QMAKE_CFLAGS_ISYSTEM=
../configure -v -release -opensource -confirm-license -xplatform linux-aarch64-gnu-g++ -device-option CROSS_COMPILE=aarch64-linux-gnu- -no-pch -opengl es2 -no-eglfs -no-openssl -no-qml-debug -nomake tools -nomake examples -nomake tests -prefix /usr/local/qt5.12.8 -extprefix $ROOT_DIR/qt5.12.8 -hostprefix $ROOT_DIR/qt5.12.8-host -sysroot $ROOTFS QMAKE_CFLAGS_ISYSTEM=
    $gmake
    $gmake install
```
    
    * 作業領域$ROOT_DIR/qt5.12.11-host にホスト用ツールのディレクトリができる。これを使って、qtcreatorでqt versionを指定する。
    * 作業領域$ROOT_DIR/qt5.12.11に、KV260デバイスと同期させるディレクトリができるが、KV260でapt install qt**を実行してqtインストール済なので、作業不要

3. Qt Creator設定
    * ビルドしたフォルダqt5.12.11-host/bin/qmakeを用いて、KV260用のQtバージョンを作成する。
        
## リモート設定 自マシン上でリモートにあるXサーバーのプログラムを実行する
1. ターゲット側 
    * xhost で KV260 の Ubuntu からの X アプリケーションの実行許可する
    * 全てのホストからの接続を許可
```    
    $xhost +	
    $DISPLAY=:0.0       
    $xhost +192.168.0.24
    
    $nano ~/.bash_profile
    DISPLAY=192.168.0.24:0.0
```
    * KV260 の Ubuntu で X のライブラリをインストールした。
```    
    $sudo apt install xbase-clients xterm x11-apps
    $sudo apt install nautilus geany
```       
    $nautilus &
    で nautilus が起動した。　      

    $geany &
    で geany が起動した。
    
       
    
## クロスコンパイラインストール
* Ubuntu20.04ホストで運用していると、稀に消失。なぜだろう。その時入れなおし。
* $ sudo apt-get install qemu
* $ sudo apt-get install g++-aarch64-linux-gnu
    
