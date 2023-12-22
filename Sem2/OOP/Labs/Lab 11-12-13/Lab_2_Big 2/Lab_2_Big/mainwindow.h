#ifndef MAINWINDOW_H
#define MAINWINDOW_H


#include <QMainWindow>
#include <QVector>
#include <QStringList>
#include <stack>

#include "Song.h"
#include "Playlist.h"
#include "Action.h"
#include <SongAction.h>

class QListWidget;
class QPushButton;
class QTextEdit;
class QShortcut;
class QStatusBar;

class MainWindow : public QMainWindow {
    Q_OBJECT

public:
    MainWindow(QWidget *parent = nullptr);

private slots:
    void addSong();
    void removeSong();
    void sortSongsByTitle();
    void sortSongsByArtist();
    void viewSongLyrics();
    void createRandomPlaylist();
    void addSongToPlaylist();
    void removeSongFromPlaylist();
    void undoAction();
    void redoAction();
    QString getLyrics(const QString &songTitle) {
        // TODO: Implement a function to retrieve lyrics for a given song title
        return "Lyrics for " + songTitle;
    }

private:
    void setupUI();
    void setupShortcuts();
    void updateStatusBar(const QString& message);
    std::vector<SongAction> m_actionStack;

    QListWidget *m_songListWidget;
    QTextEdit *m_lyricsTextEdit;
    QPushButton *m_addSongButton;
    QPushButton *m_removeSongButton;
    QPushButton *m_sortByTitleButton;
    QPushButton *m_sortByArtistButton;
    QPushButton *m_viewLyricsButton;
    QPushButton *m_createRandomPlaylistButton;
    QPushButton *m_addToPlaylistButton;
    QPushButton *m_removeFromPlaylistButton;
    QShortcut *m_undoShortcut;
    QShortcut *m_redoShortcut;
    QStatusBar *m_statusBar;
    QListWidget* m_playlistListWidget;

    QVector<Song> m_allSongs;
    Playlist m_playlist;
    QVector<Song> m_playlistSongs;
    int m_lastActionIndex;
};

#endif // MAINWINDOW_H
