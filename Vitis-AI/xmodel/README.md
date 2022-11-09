# vai_c_tensorflow用 jsonファイル生成方法
* Vitis-AIコマンド "vai_c_tensorflow"の引数で指定するjsonファイルを作成する
* 手順
    1. DPU-PYNQのboardsのmakeから、bitstream,hwhを生成する。
    2. hwhを取得し、 dcfファイルを生成させる
        * vitis-aiを起動し、以下のコマンドを実行
        * $ dlet -f ./***.hwh
        * 例：dpu-06-07-2021-19-15.dcfが生成されたとする。

    4. dcfファイル名を記載したjsonファイルを作成する。

        {  
            "target"   : "DPUCZDX8G",   
            "dcf"      : "dpu-06-07-2021-19-15.dcf",  
            "cpu_arch" : "arm64"  
        }

    5.完了