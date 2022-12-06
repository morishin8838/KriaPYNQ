#-------------------------------------------------
# 大元のリポジトリはこちらです。
# https://github.com/jianfenggithub/V4L2_example
#-------------------------------------------------

QT += core gui
QT += widgets

TARGET = nkv_v4l2
TEMPLATE = app

SOURCES += main.cpp\
        widget.cpp \
    v4l2.cpp \
    camerathread.cpp

HEADERS  += widget.h \
    v4l2.h \
    camerathread.h

FORMS    += widget.ui
