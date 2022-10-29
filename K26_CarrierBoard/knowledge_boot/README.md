# キャリアカード開発に必要な知識

## Image Selector Linux をブートするまでのシーケンス 
* https://qiita.com/ikwzm/items/a9a8d1946fa5899742bd

## カスタムKria-SOM(K26)のブートファームウェア更新手順
* https://github.com/Xilinx/Xilinx_Kria_KV260_Workshop/blob/main/Enable%20Boot%20for%20SD%20card.md
* https://qiita.com/ikwzm/items/4e5e954eabc988bd78d5

## 概略1 Vitis を使う方法
1. Vivodoでハードウエア設計を行い、XSAファイルを用意する。なんでも良い
2. VitisでXSAからプラットフォームを作成する。
3. プラットフォームを用いて、アプリーションプロジェクトを作成する。
4. KV260に書き込む対象のK26を差し込む。シリアルケーブルを接続し、電源を投入する。
5. アプリーションプロジェクトのメニューのProgram Flash Memoryを用いて、K26にboot.binを書き込む。"Success"が表示される。

## 概略2 Update Boot Binary Toolを使う方法
* https://www.hackster.io/whitney-knitter/update-boot-binary-and-install-pynq-on-kria-kv260-03b7e9
1. 最新のブートbinを見つけます。
  * https://xilinx-wiki.atlassian.net/wiki/spaces/A/pages/1641152513/Kria+K26+SOM
2. KV260にK26を差し込み をイーサネット経由でホスト PC に直接接続し、ネットワーク接続を構成する
  * Update Boot Binary Toolは 192.168.0.111 の静的 IP アドレスで構成されている
  * Host PCを以下の通りにセッティングする。
    * IPv4 address: 192.168.0.x (anything from 2 - 255, but not 111)
    * Subnet mask: 255.255.255.0
    * Gateway/router: 192.168.0.1
3. KV260にシリアルケーブルを接続する。    
4. Host PCのネットワーク設定が完了したら、KV260のFWUEN (SW1) ボタンを押したまま 電源を入れる。
  * Kria がリカバリ モードで起動する。
  * USB UART は、Kria がリカバリ モードで起動されたことを確認し、ホスト PC のブラウザ ウィンドウから IP 192.168.0.111 に接続するための指示を出力する。
5. ブートバイナリファイル (2021.1_update2_BOOT.BIN) を QSPI フラッシュ メモリのサイド A にアップロードします。
  * FireFox と Google Chrome のみがサポートされてる。
6. 新ブートバイナリがイメージ A を正常に更新したことを回復ツールが示したら、リセット ボタン (SW2) を押して KV260 の電源を入れ直す  
  * USB UART はフラッシュ メモリが更新されたことを確認表示する。
7. 終了  
  
## KV260 EEPROMの解析
* https://qiita.com/ikwzm/items/a7e1706f56e6b7282c90



