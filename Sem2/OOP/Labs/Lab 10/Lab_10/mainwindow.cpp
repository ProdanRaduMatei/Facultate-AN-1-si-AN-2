#include "mainwindow.h"

MainWindow::MainWindow(QWidget* parent)
    : QMainWindow(parent)
{
    this->setupUI();
    m_allSongs = new QStringList(); // Initialize the m_allSongs QStringList
    m_playlist = new QStringList();
}

MainWindow::~MainWindow()
{
    delete m_leftVLayout;
    delete m_centralWidget;
}

void MainWindow::setupUI()
{
    m_centralWidget = new QWidget();
    m_leftVLayout = new QVBoxLayout();

    // Create a QHBoxLayout for the song section
    QHBoxLayout* songSectionLayout = new QHBoxLayout();

    // Left side: All songs
    QVBoxLayout* allSongsLayout = new QVBoxLayout();
    m_listSongsLabel = new QLabel("All songs:");
    m_listSongs = new QTextEdit();
    m_listSongs->setFixedSize(400, 500);
    allSongsLayout->addWidget(m_listSongsLabel);
    allSongsLayout->addWidget(m_listSongs);

    // Create a QHBoxLayout for the buttons in the Artist, Duration, Link, and Title section
    QHBoxLayout* detailsButtonLayout = new QHBoxLayout();

    // Add Button
    QPushButton* addButton = new QPushButton("Add");
    addButton->setFixedSize(80, 30); // Set a fixed size for the button
    connect(addButton, SIGNAL(clicked()), this, SLOT(addButtonClicked()));
    detailsButtonLayout->addWidget(addButton);

    // Delete Button
    QPushButton* deleteButton = new QPushButton("Delete");
    deleteButton->setFixedSize(80, 30); // Set a fixed size for the button
    connect(deleteButton, SIGNAL(clicked()), this, SLOT(deleteButtonClicked()));
    detailsButtonLayout->addWidget(deleteButton);

    // Update Button
    QPushButton* updateButton = new QPushButton("Update");
    updateButton->setFixedSize(80, 30); // Set a fixed size for the button
    connect(updateButton, SIGNAL(clicked()), this, SLOT(updateButtonClicked()));
    detailsButtonLayout->addWidget(updateButton);

    // Filter Button
    QPushButton* filterButton = new QPushButton("Filter");
    filterButton->setFixedSize(80, 30); // Set a fixed size for the button
    connect(filterButton, SIGNAL(clicked()), this, SLOT(filterButtonClicked()));
    detailsButtonLayout->addWidget(filterButton);

    // Add the song section layout to the main layout
    m_leftVLayout->addLayout(songSectionLayout);

    // Add sections for Title, Artist, Duration, and Link
    QFormLayout* songDetailsLayout = new QFormLayout();
    QLabel* titleLabel = new QLabel("Title:");
    m_titleText = new QLineEdit(); // Update: Make titleText a member variable
    m_titleText->setMaximumWidth(m_titleText->width() * 0.5); // Reduce the width to 50%
    QLabel* artistLabel = new QLabel("Artist:");
    m_artistText = new QLineEdit(); // Update: Make artistText a member variable
    m_artistText->setMaximumWidth(m_artistText->width() * 0.5); // Reduce the width to 50%
    QLabel* durationLabel = new QLabel("Duration:");
    m_durationText = new QLineEdit(); // Update: Make durationText a member variable
    m_durationText->setMaximumWidth(m_durationText->width() * 0.5); // Reduce the width to 50%
    QLabel* linkLabel = new QLabel("Link:");
    m_linkText = new QLineEdit(); // Update: Make linkText a member variable
    m_linkText->setMaximumWidth(m_linkText->width() * 0.5); // Reduce the width to 50%
    songDetailsLayout->addRow(titleLabel, m_titleText);
    songDetailsLayout->addRow(artistLabel, m_artistText);
    songDetailsLayout->addRow(durationLabel, m_durationText);
    songDetailsLayout->addRow(linkLabel, m_linkText);
    m_leftVLayout->addLayout(songDetailsLayout);

    // Add the buttons layout to the Artist, Duration, Link, and Title section
    songDetailsLayout->addRow(detailsButtonLayout);

    // Add the buttons layout to the All songs layout
    songSectionLayout->addLayout(allSongsLayout);

    // Arrow button
    QPushButton* arrowButton = new QPushButton("->");
    arrowButton->setFixedSize(50, 30); // Set a fixed size for the button
    songSectionLayout->addWidget(arrowButton);
    connect(arrowButton, SIGNAL(clicked()), this, SLOT(addToPlaylistButtonClicked()));

    // Right side: Playlist
    QVBoxLayout* playlistLayout = new QVBoxLayout();
    QLabel* playlistLabel = new QLabel("Playlist:");
    m_playlistText = new QTextEdit();
    m_playlistText->setFixedSize(300, 600); // Set custom dimensions for the playlistText
    playlistLayout->addWidget(playlistLabel);
    playlistLayout->addWidget(m_playlistText);

    // Create a QHBoxLayout for the buttons in the Playlist section
    QHBoxLayout* playlistButtonLayout = new QHBoxLayout();
    // Play Button
    QPushButton* playButton = new QPushButton("Play");
    playButton->setFixedSize(80, 30); // Set a fixed size for the button
    playlistButtonLayout->addWidget(playButton);
    connect(playButton, SIGNAL(clicked()), this, SLOT(playButtonClicked()));
    detailsButtonLayout->addWidget(playButton);

    // Next Button
    QPushButton* nextButton = new QPushButton("Next");
    nextButton->setFixedSize(80, 30); // Set a fixed size for the button
    playlistButtonLayout->addWidget(nextButton);
    connect(nextButton, SIGNAL(clicked()), this, SLOT(nextButtonClicked()));
    detailsButtonLayout->addWidget(nextButton);

    // Add the buttons layout to the Playlist layout
    playlistLayout->addLayout(playlistButtonLayout);

    songSectionLayout->addLayout(playlistLayout);

    m_centralWidget->setLayout(m_leftVLayout);
    this->setCentralWidget(m_centralWidget);
}

void MainWindow::addButtonClicked()
{
    QString title = m_titleText->text();
    QString artist = m_artistText->text();
    QString duration = m_durationText->text();
    QString link = m_linkText->text();

    // Append the song information to the "All songs" list
    QString songInfo = QString("%1 - %2 (%3)\n%4\n").arg(title, artist, duration, link);
    m_allSongs->append(songInfo);

    // Update the "All songs" QTextEdit object
    m_listSongs->setText(m_allSongs->join("\n"));

    // Clear the input fields after adding
    m_titleText->clear();
    m_artistText->clear();
    m_durationText->clear();
    m_linkText->clear();
}

void MainWindow::deleteButtonClicked()
{
    // Retrieve the title from the input field
    QString title = m_titleText->text();

    // Remove the song from the "All songs" list
    for (int i = 0; i < m_allSongs->size(); ++i) {
        if (m_allSongs->at(i).contains(title)) {
            m_allSongs->removeAt(i);
            break;
        }
    }

    // Update the "All songs" QTextEdit object
    m_listSongs->setText(m_allSongs->join("\n"));

    // Clear the input field after deleting
    m_titleText->clear();
}


void MainWindow::updateButtonClicked()
{
    QMessageBox::information(this, "Not implemented", "Update functionality is not implemented yet.");

    // Clear the input fields after updating
    m_titleText->clear();
    m_artistText->clear();
    m_durationText->clear();
    m_linkText->clear();
}


void MainWindow::filterButtonClicked()
{
    QMessageBox::information(this, "Not implemented", "Filter functionality is not implemented yet.");

    // Clear the input fields after filtering
    m_titleText->clear();
}

void MainWindow::nextButtonClicked()
{
    QMessageBox::information(this, "Not implemented", "Next functionality is not implemented yet.");
}

void MainWindow::playButtonClicked()
{
    QMessageBox::information(this, "Not implemented", "Play functionality is not implemented yet.");
}


void MainWindow::addToPlaylistButtonClicked()
{
    // Get the selected song from the "All songs" list
    QString selectedSong = m_listSongs->textCursor().selectedText();

    // Append the selected song to the playlist
    m_playlist->append(selectedSong);

    // Update the "Playlist" QTextEdit object
    m_playlistText->setText(m_playlist->join("\n"));
}



