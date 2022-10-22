# HDMI-IPを組み込んだDPU-PYNQプラットフォームの組込み手順
* Xilinx HDMI-IPを組み込んだ回路にDPU-PYNQを組み込む場合の手順です。
* HDMI-IPを組み込まない場合、本手順である必要はなさそうです。

## 回路設計 Vivado
1. Xilinx HDMI-IPがあるK26 FPGAカスタム回路設計を行う
2. Clock追加
    * 300MHz,600MHz出力と、それぞれ300M用、600M用のSysReset追加する
    * TimingErrorが発生した場合、connectvityを工夫すると、タイミングエラーが解消します。
3. plartform設定
    * AXI port
        * M_HPM0_FPD:HPM1
        * M_HPM1_FPD:MLPD
        * S_HPC0_FPD:HPC0
        * S_HPC1_FPD:HPC1
        * S_HP0_FPD:HP1
    * Clock
        * pl_clk0:Enabledチェック, is Defaultチェック
        * clk_out1:Enabledチェック、id=2
        * clk_out1:Enabledチェック、id=4     
        
4. bitstream生成
5. xsaファイルをエクスポート生成

## プラットフォーム作成 Vitis
1. vitis起動し、メニューからプラットフォーム選択し、プラットフォームを生成する。
2. エクスポートしたxsaファイルを選択し、linuxを選択し、bootはチェック外す。ワーニングは無視して、終了
3. トンカチボタンでbuildする。
4. exportディレクトリ配下にあるxpfmファイルのパスを確認する。下記、VITIS_PLATFORMのパスに指定する

## ビルド DPU-PYNQ
0. 下準備
    1. ビルド環境をダウンロードする
        * $wget https://github.com/Xilinx/DPU-PYNQ
        * $cd board
    2. 評価ボード(ZCU104,Ultra96,KV260)を使う場合、このままでよい
    3. カスタムボードを使う場合、適当なディレクトリを作成する。
        * 作成したディレクトリにdpu_conf.vh,prj_configを配置する。仕様が似ている評価ボードの設定ファイルをコピーすること
        * dpu_conf.vh,prj_configの編集内容は、設定ファイル編集を参照する。
1. 設定ファイル編集
    1. dpu_conf.vh編集
        * `define B4096
        * `define def_UBANK_IMG_N          5
        * `define def_UBANK_WGT_N          17
        * `define def_UBANK_BIAS           1
    2. prj_config
        * freqHz=200000000:DPUCZDX8G_1.aclk
        * freqHz=400000000:DPUCZDX8G_1.ap_clk_2
        * id=2:DPUCZDX8G_1.aclk
        * id=4:DPUCZDX8G_1.ap_clk_2
        * sp=DPUCZDX8G_1.M_AXI_GP0:HP1
        * sp=DPUCZDX8G_1.M_AXI_HP0:HPC0
        * sp=DPUCZDX8G_1.M_AXI_HP2:HPC1
        * prop=run.impl_1.strategy=Performance_Explore
    
2. ビルド実行  
$VERSION=2021.1   
$source /tools/Xilinx/Vitis/$VERSION/settings64.sh  
$source /opt/xilinx/xrt/$VERSION/setup.sh  
$make clean  
$make BOARD=NKV VITIS_PLATFORM=<path xpfm>/xxxxx.xpfm  

* CPUパワーにもよりますが、ビルドは3時間コースです。

## 注意事項
* B3136でクロック200/400Mhzで設定すると、Timingエラーは解消できますが、推論エンジンを実行するとDPUはクラッシュします。
