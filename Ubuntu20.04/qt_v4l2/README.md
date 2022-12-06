# QtからV4L2 を使用して UVCカメラ映像を高速に描画します

## 説明
* 使用法: Ubuntu の下の Qt プロジェクトに V4L2.h および V4L2.cpp ファイルを追加し、V4L2 オブジェクトを定義します。
* bool V4L2::V4l_Init(char* camera_path, unsigned int frame) 関数を呼び出して、カメラを初期化します
* QImage V4L2::Get_image() 関数を呼び出して、カメラから画像を取得します
* bool Close_Camera(void) 関数を呼び出してカメラを閉じます
* V4L2.hのマクロ定義で、出力画像のピクセルを変更可能


