#include "mainwindow.h"
#include <QApplication>
#include <QVBoxLayout>
#include <QHBoxLayout>
//#include <QPushButton>
#include<QPushButton>
#include <QListWidget>
#include <QTextEdit>
#include <QShortcut>
#include <QMessageBox>
#include <QStatusBar>
#include <QInputDialog>
#include <algorithm>
#include <random>
#include <iostream>
#include <string>
#include <vector>
#include <fstream>
#include <sstream>
#include <iterator>
#include <stack>

#include <SongAction.h>

MainWindow::MainWindow(QWidget *parent)
    : QMainWindow(parent), m_lastActionIndex(-1) {
    setupUI();
    setupShortcuts();
    m_actionStack = std::vector<SongAction>(); // Declare and initialize m_actionStack
}

void MainWindow::setupUI() {
    QWidget *centralWidget = new QWidget(this);
    setCentralWidget(centralWidget);

    QVBoxLayout *layout = new QVBoxLayout(centralWidget);

    m_songListWidget = new QListWidget(centralWidget);
    layout->addWidget(m_songListWidget);

    m_lyricsTextEdit = new QTextEdit(centralWidget);
    layout->addWidget(m_lyricsTextEdit);

    QHBoxLayout *buttonLayout = new QHBoxLayout();

    m_addSongButton = new QPushButton("Add Song", centralWidget);
    connect(m_addSongButton, &QPushButton::clicked, this, &MainWindow::addSong);
    buttonLayout->addWidget(m_addSongButton);

    m_removeSongButton = new QPushButton("Remove Song", centralWidget);
    connect(m_removeSongButton, &QPushButton::clicked, this, &MainWindow::removeSong);
    buttonLayout->addWidget(m_removeSongButton);

    m_sortByTitleButton = new QPushButton("Sort by Title", centralWidget);
    connect(m_sortByTitleButton, &QPushButton::clicked, this, &MainWindow::sortSongsByTitle);
    buttonLayout->addWidget(m_sortByTitleButton);

    m_sortByArtistButton = new QPushButton("Sort by Artist", centralWidget);
    connect(m_sortByArtistButton, &QPushButton::clicked, this, &MainWindow::sortSongsByArtist);
    buttonLayout->addWidget(m_sortByArtistButton);

    m_viewLyricsButton = new QPushButton("View Lyrics", centralWidget);
    connect(m_viewLyricsButton, &QPushButton::clicked, this, &MainWindow::viewSongLyrics);
    buttonLayout->addWidget(m_viewLyricsButton);

    m_createRandomPlaylistButton = new QPushButton("Create Random Playlist", centralWidget);
    connect(m_createRandomPlaylistButton, &QPushButton::clicked, this, &MainWindow::createRandomPlaylist);
    buttonLayout->addWidget(m_createRandomPlaylistButton);

    m_addToPlaylistButton = new QPushButton("Add to Playlist", centralWidget);
    connect(m_addToPlaylistButton, &QPushButton::clicked, this, &MainWindow::addSongToPlaylist);
    buttonLayout->addWidget(m_addToPlaylistButton);

    m_removeFromPlaylistButton = new QPushButton("Remove from Playlist", centralWidget);
    connect(m_removeFromPlaylistButton, &QPushButton::clicked, this, &MainWindow::removeSongFromPlaylist);
    buttonLayout->addWidget(m_removeFromPlaylistButton);

    layout->addLayout(buttonLayout);

    m_statusBar = new QStatusBar(this);
    setStatusBar(m_statusBar);

    // Playlist List Widget
    m_playlistListWidget = new QListWidget(centralWidget);
    layout->addWidget(m_playlistListWidget);
}


void MainWindow::setupShortcuts() {
    m_undoShortcut = new QShortcut(QKeySequence::Undo, this);
    connect(m_undoShortcut, &QShortcut::activated, this, &MainWindow::undoAction);

    m_redoShortcut = new QShortcut(QKeySequence::Redo, this);
    connect(m_redoShortcut, &QShortcut::activated, this, &MainWindow::redoAction);
}

void MainWindow::addSong() {
    QString title = QInputDialog::getText(this, "Title", "Enter the title of the song");
    QString artist = QInputDialog::getText(this, "Artist", "Enter the name of the artist");

    // Check if the user entered valid inputs
    if (title.isEmpty() || artist.isEmpty()) {
        QMessageBox::critical(this, "Error", "Please enter a valid title and artist name.");
        return;
    }

    // Create a new song item and add it to the list widget
    QListWidgetItem *item = new QListWidgetItem(title + " - " + artist);
    m_songListWidget->addItem(item);

    // Store the action for undo/redo functionality
    SongAction action;
    action.type = ActionType::Add;
    action.title = title;
    action.artist = artist;
    m_actionStack.push_back(action);

    // Update the status bar
    updateStatusBar("Song added: " + title + " - " + artist);
}

void MainWindow::removeSong() {
    int index = m_songListWidget->currentRow();
    if (index < 0 || index >= m_songListWidget->count()) {
        QMessageBox::critical(this, "Error", "Please select a song to remove.");
        return;
    }

    QListWidgetItem *item = m_songListWidget->takeItem(index);
    QString songTitle = item->text();

    // Store the action for undo/redo functionality
    SongAction action;
    action.type = ActionType::Remove;
    action.title = songTitle;
    m_actionStack.push_back(action);

    // Delete the song item and free the memory
    delete item;

    // Update the status bar
    updateStatusBar("Song removed: " + songTitle);
}

void MainWindow::sortSongsByTitle() {
    // Get the list of songs and sort them by title
    QStringList songs;
    for (int i = 0; i < m_songListWidget->count(); ++i) {
        QListWidgetItem *item = m_songListWidget->item(i);
        songs << item->text();
    }
    songs.sort();

    // Clear the list widget
    m_songListWidget->clear();

    // Add the sorted songs back to the list widget
    m_songListWidget->addItems(songs);

    // Store the action for undo/redo functionality
    SongAction action;
    action.type = ActionType::SortByTitle;
    m_actionStack.push_back(action);

    // Update the status bar
    updateStatusBar("Songs sorted by title");
}

void MainWindow::sortSongsByArtist() {
    // Get the list of songs and sort them by artist
    QStringList songs;
    for (int i = 0; i < m_songListWidget->count(); ++i) {
        QListWidgetItem *item = m_songListWidget->item(i);
        songs << item->text();
    }
    std::sort(songs.begin(), songs.end(), [](const QString& a, const QString& b) {
        QString artistA = a.split(" - ").at(1);
        QString artistB = b.split(" - ").at(1);
        return artistA.compare(artistB, Qt::CaseInsensitive) < 0;
    });

    // Clear the list widget
    m_songListWidget->clear();

    // Add the sorted songs back to the list widget
    m_songListWidget->addItems(songs);

    // Store the action for undo/redo functionality
    SongAction action;
    action.type = ActionType::SortByArtist;
    m_actionStack.push_back(action);

    // Update the status bar
    updateStatusBar("Songs sorted by artist");
}

void MainWindow::viewSongLyrics() {
    int index = m_songListWidget->currentRow();
    if (index < 0 || index >= m_songListWidget->count()) {
        QMessageBox::critical(this, "Error", "Please select a song to view its lyrics.");
        return;
    }

    QString songTitle = m_songListWidget->item(index)->text();

    // Get the lyrics for the selected song
    QString lyrics = getLyrics(songTitle);

    // Display the lyrics in the text edit widget
    m_lyricsTextEdit->setText(lyrics);
}

void MainWindow::createRandomPlaylist() {
    int playlistSize = QInputDialog::getInt(this, "Playlist Size", "Enter the playlist size");
    if (playlistSize <= 0) {
        QMessageBox::critical(this, "Error", "Please enter a valid playlist size.");
        return;
    }

    // Check if there are enough songs to create a playlist
    if (playlistSize > m_songListWidget->count()) {
        QMessageBox::critical(this, "Error", "There are not enough songs to create a playlist of the specified size.");
        return;
    }

    // Shuffle the song list randomly
    QList<QString> songTitles;
    for (int i = 0; i < m_songListWidget->count(); ++i) {
        QListWidgetItem *item = m_songListWidget->item(i);
        songTitles << item->text();
    }
    std::random_device rd;
    std::mt19937 g(rd());
    std::shuffle(songTitles.begin(), songTitles.end(), g);

    // Get the first 'playlistSize' songs from the shuffled list
    QList<QString> playlist;
    for (int i = 0; i < playlistSize; ++i) {
        playlist << songTitles.at(i);
    }

    // Display the playlist in a message box
    QString playlistString = playlist.join("\n");
    QMessageBox::information(this, "Random Playlist", "Here is your random playlist:\n\n" + playlistString);
}

void MainWindow::addSongToPlaylist() {
    int songIndex = m_songListWidget->currentRow();
    if (songIndex < 0 || songIndex >= m_songListWidget->count()) {
        QMessageBox::critical(this, "Error", "Please select a song to add to the playlist.");
        return;
    }

    int playlistIndex = m_playlistListWidget->currentRow();
    if (playlistIndex < 0 || playlistIndex >= m_playlistListWidget->count()) {
        QMessageBox::critical(this, "Error", "Please select a playlist to add the song to.");
        return;
    }

    QString songTitle = m_songListWidget->item(songIndex)->text();
    QListWidgetItem *playlistItem = m_playlistListWidget->item(playlistIndex);

    // Add the song title to the selected playlist
    playlistItem->setText(playlistItem->text() + "\n" + songTitle);

    // Update the status bar
    updateStatusBar("Song added to playlist: " + songTitle);
}

void MainWindow::removeSongFromPlaylist() {
    int songIndex = m_songListWidget->currentRow();
    if (songIndex < 0 || songIndex >= m_songListWidget->count()) {
        QMessageBox::critical(this, "Error", "Please select a song to remove from the playlist.");
        return;
    }

    int playlistIndex = m_playlistListWidget->currentRow();
    if (playlistIndex < 0 || playlistIndex >= m_playlistListWidget->count()) {
        QMessageBox::critical(this, "Error", "Please select a playlist to remove the song from.");
        return;
    }

    QString songTitle = m_songListWidget->item(songIndex)->text();
    QListWidgetItem *playlistItem = m_playlistListWidget->item(playlistIndex);

    // Remove the song title from the selected playlist
    QStringList playlist = playlistItem->text().split("\n", Qt::SkipEmptyParts);
    playlist.removeAll(songTitle);
    playlistItem->setText(playlist.join("\n"));

    // Update the status bar
    updateStatusBar("Song removed from playlist: " + songTitle);
}

void MainWindow::undoAction() {
    if (!m_actionStack.empty() && m_lastActionIndex > -1) {
        SongAction lastAction = m_actionStack[m_lastActionIndex];

        if (lastAction.type == ActionType::Add) {
            // Remove the last added song
            m_songListWidget->takeItem(m_songListWidget->count() - 1);

            // Update the status bar
            updateStatusBar("Undone: Song added");
        } else if (lastAction.type == ActionType::Remove) {
            // Add the last removed song back to the list
            m_songListWidget->addItem(lastAction.title);

            // Update the status bar
            updateStatusBar("Undone: Song removed");
        } else if (lastAction.type == ActionType::SortByTitle) {
            // Restore the song list order
            QStringList songs;
            for (int i = 0; i < m_songListWidget->count(); ++i) {
                QListWidgetItem *item = m_songListWidget->item(i);
                songs << item->text();
            }

            // Clear the list widget
            m_songListWidget->clear();

            // Add the songs back to the list widget
            m_songListWidget->addItems(songs);

            // Update the status bar
            updateStatusBar("Undone: Songs sorted by title");
        } else if (lastAction.type == ActionType::SortByArtist) {
            // Restore the song list order
            QStringList songs;
            for (int i = 0; i < m_songListWidget->count(); ++i) {
                QListWidgetItem *item = m_songListWidget->item(i);
                songs << item->text();
            }

            // Clear the list widget
            m_songListWidget->clear();

            // Add the songs back to the list widget
            m_songListWidget->addItems(songs);

            // Update the status bar
            updateStatusBar("Undone: Songs sorted by artist");
        }

        m_actionStack.pop_back();
        m_lastActionIndex--;
    } else {
        QMessageBox::information(this, "Undo", "No more actions to undo.");
    }
}

void MainWindow::redoAction() {
    if (m_lastActionIndex < m_actionStack.size() - 1) {
        m_lastActionIndex++;
        SongAction nextAction = m_actionStack.at(m_lastActionIndex);

        if (nextAction.type == ActionType::Add) {
            // Add the next song back to the list
            m_songListWidget->addItem(nextAction.title);

            // Update the status bar
            updateStatusBar("Redone: Song added");
        } else if (nextAction.type == ActionType::Remove) {
            // Remove the next song from the list
            for (int i = 0; i < m_songListWidget->count(); ++i) {
                QListWidgetItem *item = m_songListWidget->item(i);
                if (item->text() == nextAction.title) {
                    m_songListWidget->takeItem(i);
                    break;
                }
            }

            // Update the status bar
            updateStatusBar("Redone: Song removed");
        } else if (nextAction.type == ActionType::SortByTitle) {
            // Sort the songs by title
            sortSongsByTitle();

            // Update the status bar
            updateStatusBar("Redone: Songs sorted by title");
        } else if (nextAction.type == ActionType::SortByArtist) {
            // Sort the songs by artist
            sortSongsByArtist();

            // Update the status bar
            updateStatusBar("Redone: Songs sorted by artist");
        }
    } else {
        QMessageBox::information(this, "Redo", "No more actions to redo.");
    }
}

void MainWindow::updateStatusBar(const QString &message) {
    m_statusBar->showMessage(message);
}

/*QString MainWindow::getLyrics(const QString &songTitle) {
    // TODO: Implement a function to retrieve lyrics for a given song title
    return "Lyrics for " + songTitle;
}*/
