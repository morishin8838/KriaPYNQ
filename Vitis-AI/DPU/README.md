# DPU-IP 組込み手順
* HDMI-IPを組み込んだ場合になります。組み込まない場合、チュートリアル通りで組込み可能です。

## 回路設計 Vivado
1. Xilinx HDMI-IPがあるK26 FPGAカスタム回路設計を行う
2. Clock追加
    * 200MHz,400MHz出力と、それぞれ200M用、400M用のSysReset追加する
    * 私の場合、300/600MHzはどう試行錯誤しても、TimingErrorが発生し、300/600のクロックラインは搭載できませんでした。
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

## ビルド
1. 設定ファイル編集
    1. dpu_conf.vh編集
        * `define B3136
        * `define def_UBANK_IMG_N          4
        * `define def_UBANK_WGT_N          15
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
