# DPU-IP 組込み手順

## 回路設計
1. 通常のFPGA回路設計を行う
2. Clock追加
    * 300M,600M
    * 300M用、600M用のSysReset追加
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
5. xsaファイル生成

## プラットフォーム作成
1. vitis起動し、メニューからプラットフォーム選択
2. xsaファイルを選択し、linuxを選択し、bootはチェック外す。ワーニングは無視して、終了
3. トンカチボタンでbuildする。

## ビルド
1. 設定ファイル編集
    1. dpu_conf.vh編集
        * `define B3136
        * `define def_UBANK_IMG_N          4
        * `define def_UBANK_WGT_N          15
        * `define def_UBANK_BIAS           1
    2. prj_config
        * freqHz=300000000:DPUCZDX8G_1.aclk
        * freqHz=600000000:DPUCZDX8G_1.ap_clk_2
        * id=2:DPUCZDX8G_1.aclk
        * id=4:DPUCZDX8G_1.ap_clk_2
        * sp=DPUCZDX8G_1.M_AXI_GP0:HP1
        * sp=DPUCZDX8G_1.M_AXI_HP0:HPC0
        * sp=DPUCZDX8G_1.M_AXI_HP2:HPC1
        * prop=run.impl_1.strategy=Performance_Explore
    
2. ビルド実行
| $VERSION=2021.1
| $source /tools/Xilinx/Vitis/$VERSION/settings64.sh
| $source /opt/xilinx/xrt/$VERSION/setup.sh
| $make BOARD=NKV VITIS_PLATFORM=<path xpfm>/xxxxx.xpfm

