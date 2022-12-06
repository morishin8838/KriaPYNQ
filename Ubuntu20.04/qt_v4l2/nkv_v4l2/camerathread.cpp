#include "camerathread.h"
#include <QThread>

extern QLabel *imagelabel;
extern QLabel *fps__label;

CameraThread::CameraThread()
{

}

CameraThread::~CameraThread()
{

}

/** カメラ データ スレッドを取得する */
void CameraThread::dowork()
{
//    v4l.V4l_Init("/dev/video0", V4L2_FPS);                          /** 初期化 */
    v4l.V4l_Init(USE_DEVIDE, V4L2_FPS);                             /** 初期化 */

    while(1){
        if((QThread::currentThread()->isInterruptionRequested()))   {/** このスレッドを中断するシグナル */
            v4l.Close_Camera();                                     /** カメラをオフにする */
            break;
        }
        currentimage = v4l.Get_image();                             /** 画像データのフレームを取得する */
        imagelabel->setPixmap(QPixmap::fromImage(currentimage));    /** ラベルに現在イメージを表示 */
//        fps__label->setText("1");    /** ラベルにFPSを表示 */
    }

}
