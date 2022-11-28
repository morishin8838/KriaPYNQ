# pynq libビルド方法

## 手順
1. Kria-PYNQダウンロード、ターゲットボードにコピーする
$git clone https://github.com/Xilinx/Kria-PYNQ
* ターゲットボードにコピーする。/home/xilinx/Kria-PYNQ  （例）ここでは、/home/xilinxがホーム

2. embeddedswをダウンロードし、Kria-PYNQにコピーする
$git clone https://github.com/Xilinx/embeddedsw
*ターゲットボードにコピーする。 /home/xilinx/Kria-PYNQ/pynq/pynq/lib/_pynq/embeddedsw

3. ターゲットボード上でmakeする
$ssh username@ipadress (例) sshでログオン
$cd /home/xilinx/Kria-PYNQ/pynq/pynq/lib/_pynq/_pcam5c
$make

$cd /home/xilinx/Kria-PYNQ/pynq/pynq/lib/_pynq/_displayport
$make

$cd /home/xilinx/Kria-PYNQ/pynq/pynq/lib/_pynq/_xhdmi
$make

4. 終了

