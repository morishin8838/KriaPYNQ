# イメージ構築手順 KriaPYNQ For Ubuntu on Xilinx

## ホスト開発環境
* Ubuntu20.04

## ターゲットツールバージョン
* Ubuntu20.04
* PYNQ2.7(KriaPYNQ)

## :warning: Ubuntu自体をupgradeしない前提のSDカードの作成方法です。
* ubuntuをアップグレードを試みると、confrict発生します
* 理由はよくわかりません。
* ホストPC(Ubuntu or Windows等）のシリアルコンソールをKriaに接続し、作業を行ってください。

## 手順
1. Xilinx FOR ubuntu OS作成 SDカード作成
    1. balenaEtcher起動
    2. ダウンロード ubuntu xilinx
        1. https://ubuntu.com/download/xilinx
        2. iot-kria-classic-desktop-2004-x03-20211110-98.img.xzを書き込む        
2. KV260起動
    1. SDカード差し込み
    2. 外部LAN接続
    3. 電源ON
    4. ログイン 初期ユーザ名＆パスワード
        * username: ubuntu
        * password: ubuntu
        * パスワードは必ず聞かれるので変更する。8文字以上で英数字混在
	5. install basic 
		$sudo apt install aptitude   
    6. PYNQ DPUをインストール
```
        $git clone https://github.com/Xilinx/Kria-PYNQ.git
        $cd Kria-PYNQ/
        $nano install.sh     
        # Install DPU-PYNQ
        #yes Y | apt remove --purge vitis-ai-runtime コメントアウトする
        #yes Y | apt remove vitis-ai-runtime #変更する
        $sudo bash install.sh 
```      
            * ModuleNotFoundError: No module named 'vart'は無視して、次の作業に進む   
        
    7. KV260スタータキット
        1. Xilinx Development & Demonstration Environment for Ubuntu 20.04 LTS をインストール
            $sudo snap install xlnx-config --classic            
            $sudo xlnx-config.sysinit            
            * Xilinx environment setup is complete　インストール成功

    8. PYNQ DPUをインストール
        $nano install.sh     
        yes Y | apt install vitis-ai-runtime 
        yes Y | apt install vitis-ai-library #変更して再度インストール
        $sudo bash install.sh     
        Overwrite /root/.jupyter/jupyter_notebook_config.py with default config? [y/N]はyesです

    9.PYNQ 基本動作確認
        1. /etc/vart.confの作成
            なぜか見つからないエラーが発生しますので、手動でファイルを作成します
            $cd /etc
            $sudo nano vart.conf
            firmware: /usr/lib/dpu.xclbin 
            を記載する。            ## クロスコンパイラインストール
* Ubuntu20.04ホストで運用していると、稀に消失。なぜだろう。その時入れなおし。
* $ sudo apt-get install qemu
* $ sudo apt-get install g++-aarch64-linux-gnu
        2 Jupyter起動
            192.168.1.82:9090 これnotebook
            192.168.1.82:9090/lab
    10. 変更
        1 host変更
        $sudo nano /etc/hostname      kria->nkv        
		$sudo timedatectl set-timezone 'Asia/Tokyo'     
        
    11. パスワードポリシ変更
        $sudo apt -y install libpam-pwquality
        $sudo nano /etc/security/pwquality.conf
           a) 11行目：コメント解除して最低文字数を設定 (下例は 4 文字)
            minlen = 4
           b) 34行目：コメント解除して最低文字種類数を設定 (下例は 1種)
            minclass = 1
           c) permit username and common word ex. xilinx 
			dictcheck = 0 
			usercheck = 0
        * セットアップメニューが無くなっている場合、画面をクリックして設定を選択する（メニュー消失は最後に修復する）
    
3. Ubuntu設定変更
    1. 再起動　
        * ubuntuでログオン
    2. ユーザ追加　パスワードはポリシ変更済なので、4文字で問題なし
        * xilinx / xilinx
         自動ログイン、管理者設定
    3. リブートして、xilinxでログインして作業を続ける
        * 壁紙変更等を行う
    4. アップグレード 
```
        $sudo apt update ## クロスコンパイラインストール
* Ubuntu20.04ホストで運用していると、稀に消失。なぜだろう。その時入れなおし。
* $ sudo apt-get install qemu
* $ sudo apt-get install g++-aarch64-linux-gnu
        $sudo apt upgrade
```
        The following packages have unmet dependencies:
        libdrm-xlnx-amdgpu1 : Conflicts: libdrm-amdgpu1
        ★E: Broken packages　★失敗
       
    5. FTPサーバ設定
        $sudo apt -y install vsftpd  
        $sudo nano /etc/vstfpd.conf
        	※以下コメントアウトを削除する（有効化する）## クロスコンパイラインストール
* Ubuntu20.04ホストで運用していると、稀に消失。なぜだろう。その時入れなおし。
* $ sudo apt-get install qemu
* $ sudo apt-get install g++-aarch64-linux-gnu
		    ・write_enable=YES
		    ・ascii_upload_enable=YES
		    ・ascii_download_enable=YES
		    ・ftpd_banner=Welcome to blah FTP service.
		$ sudo systemctl enable vsftpd
		$ sudo systemctl restart vsftpd
		
    6. SSH設定　★PermitRootLogin yesにしないと、rootでログインできない
	    $sudo apt -y install aptitude 
		$sudo aptitude install ssh
		$sudo nano /etc/ssh/sshd_config
		PermitRootLoginの行を PermitRootLogin yes に書き換える
		$sudo /etc/init.d/ssh restart●●●●●●●●
		
    7. rsync パスワード無し設定（デバイス側で設定ファイルを作成する）
        $sudo nano /etc/rsyncd.conf
        　	[APP_DIR]
        　   comment=user data
        　   path=/opt
        　   read only=false
        　   uid=root
        　   gid=root
        　   hosts allow=192.168.2.99/24
        　   hosts deny=*
        　   list = true
        再起動する
        $sudo systemctl start rsync

    8.Ubuntuのrootパスワード設定
        Ubuntuはインストール直後はrootパスワードが設定されていないので、自身で設定し利用出来るようにする必要があります。
        $ sudo passwd root
        Enter new UNIX password:○○○○○○ ← 設定をしたいrootパスワード
        Retype new UNIX password:○○○○○○ ← 設定をしたいrootパスワードを再度入力
        passwd: password updated successfully        
        
    9. 基本ソフトインストール
        6-1 QT
            $sudo apt install -y build-essential mesa-common-dev
            $sudo apt install -y libglu1-mesa-dev mesa-common-dev freeglut3 libglfw3 freeglut3-dev libglew1.5-dev at-spi2-core libopencv-dev python3-opencv
            $sudo apt install -y qtbase5-dev qttools5-dev-tools qt5-default qtdeclarative5-dev qtbase5-private-dev qtdeclarative5-private-dev 
            $sudo apt install -y libqt5opengl5-dev qml-module-qtquick-controls qml-module-qtquick2 qml-module-qt-labs-folderlistmodel qml-module-qtquick-extras
            $sudo apt install -y qml-module-qt-labs-platform qml-module-qtquick-controls2 qml qml-module-qtmultimedia qtquickcontrols2-5-dev
            $sudo apt install -y libqt5quickcontrols2-5 qtcreator qtcreator-doc libqt5serialport5-dev qtconnectivity5-dev qtmultimedia5-dev qtquickcontrols2-5-dev
            $sudo apt install -y libqt5multimedia5-plugins qtwayland5
            
       
    10. 日本語化
        設定が消えるのでいろいろと難しい（これができない：左ペインで [Region & Languege] を選択し、右ペインで言語を日本語に変更）
	    $sudo apt -y install language-pack-ja-base language-pack-ja ibus-kkc		
        アクティビティからLanguegeを選択し、ひとまず、設定   
	    さらに [Input Source] には [日本語 (Kana Kanji)] を指定ができないので、ひとまずいかのコマンドで日本語化は出来る。
	    gsettings set org.gnome.desktop.input-sources sources "[('xkb', 'jp+OADG109A'), ('ibus', 'mozc-jp')]"
	    
    11. ネットワーク設定
	    以前 ZCU104では、/etc/network/interfacesに設定を記述していましたが、これが変更
        IPアドレスの変更が/etc/network/interfacesをいじる方式からNetplanへ変更になっている
        /etc/netplan/99_config.yaml を作成し設定を上書きするのが正式
        /etc/netplan/99_config.yaml を作成しIPアドレスを設定します。
	    
	    IPアドレスを固定するための設定ファイルを作成する
	    $sudo nano /etc/netplan/99_config.yaml
        network:
          version: 2
          renderer: networkd
          ethernets:
            eth0:
              dhcp4: false
              dhcp6: false
              addresses: [192.168.2.99/24]
              gateway4: 192.168.2.1
              nameservers:
                addresses: [192.168.2.1]

        netplan applyを実行して反映します。再起動不要です。
        $sudo netplan apply            
	    設定を適用する。IPアドレスを設定した後に、再度IPアドレスを確認してみます。
        $ifconfig

