QT       += core gui
QT       += widgets
QT       += multimedia
QT += core gui multimedia



greaterThan(QT_MAJOR_VERSION, 4): QT += widgets

CONFIG += c++17

# You can make your code fail to compile if it uses deprecated APIs.
# In order to do so, uncomment the following line.
#DEFINES += QT_DISABLE_DEPRECATED_BEFORE=0x060000    # disables all the APIs deprecated before Qt 6.0.0

SOURCES += \
    Action.cpp \
    FileRepository.cpp \
    FileRepositoryTest.cpp \
    Playlist.cpp \
    Repository.cpp \
    RepositoryTest.cpp \
    Song.cpp \
    SongCollection.cpp \
    SongController.cpp \
    SongControllerTest.cpp \
    SongException.cpp \
    Test.cpp \
    main.cpp \
    mainwindow.cpp


HEADERS += \
    Action.h \
    FileRepository.h \
    FileRepositoryTest.h \
    Playlist.h \
    Repository.h \
    RepositoryTest.h \
    Song.h \
    SongAction.h \
    SongCollection.h \
    SongControllerTest.h \
    SongException.h \
    Tests.h \
    mainwindow.h
    SongAction.h

FORMS += \
    mainwindow.ui

# Default rules for deployment.
qnx: target.path = /tmp/$${TARGET}/bin
else: unix:!android: target.path = /opt/$${TARGET}/bin
!isEmpty(target.path): INSTALLS += target
