#include "mainwindow.h"


MainWindow::MainWindow(QWidget* parent)
    : QMainWindow(parent)
{
    this->setupUI();
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
    allSongsLayout->addWidget(m_listSongsLabel);
    allSongsLayout->addWidget(m_listSongs);

    // Create a QHBoxLayout for the buttons in the All songs section
    QHBoxLayout* allSongsButtonLayout = new QHBoxLayout();
    // Add Button
    m_addButton = new QPushButton("Add");
    m_addButton->setFixedSize(80, 30); // Set a fixed size for the button
    connect(m_addButton, SIGNAL(clicked()), this, SLOT(addButtonClicked()));
    allSongsButtonLayout->addWidget(m_addButton);

    // Delete Button
    m_deleteButton = new QPushButton("Delete");
    m_deleteButton->setFixedSize(80, 30); // Set a fixed size for the button
    connect(m_deleteButton, SIGNAL(clicked()), this, SLOT(deleteButtonClicked()));
    allSongsButtonLayout->addWidget(m_deleteButton);

    // Update Button
    m_updateButton = new QPushButton("Update");
    m_updateButton->setFixedSize(80, 30); // Set a fixed size for the button
    connect(m_updateButton, SIGNAL(clicked()), this, SLOT(updateButtonClicked()));
    allSongsButtonLayout->addWidget(m_updateButton);

    // Filter Button
    m_filterButton = new QPushButton("Filter");
    m_filterButton->setFixedSize(80, 30); // Set a fixed size for the button
    connect(m_filterButton, SIGNAL(clicked()), this, SLOT(filterButtonClicked()));
    allSongsButtonLayout->addWidget(m_filterButton);

    // Add the buttons layout to the All songs layout
    allSongsLayout->addLayout(allSongsButtonLayout);

    songSectionLayout->addLayout(allSongsLayout);

    // Arrow button
    QPushButton* arrowButton = new QPushButton("->");
    arrowButton->setFixedSize(40, 30); // Set a fixed size for the button
    songSectionLayout->addWidget(arrowButton);

    // Right side: Playlist
    QVBoxLayout* playlistLayout = new QVBoxLayout();
    QLabel* playlistLabel = new QLabel("Playlist:");
    QTextEdit* playlistText = new QTextEdit();
    playlistLayout->addWidget(playlistLabel);
    playlistLayout->addWidget(playlistText);

    // Create a QHBoxLayout for the buttons in the Playlist section
    QHBoxLayout* playlistButtonLayout = new QHBoxLayout();
    // Play Button
    QPushButton* playButton = new QPushButton("Play");
    playButton->setFixedSize(80, 30); // Set a fixed size for the button
    playlistButtonLayout->addWidget(playButton);

    // Next Button
    QPushButton* nextButton = new QPushButton("Next");
    nextButton->setFixedSize(80, 30); // Set a fixed size for the button
    playlistButtonLayout->addWidget(nextButton);

    // Add the buttons layout to the Playlist layout
    playlistLayout->addLayout(playlistButtonLayout);

    songSectionLayout->addLayout(playlistLayout);

    // Add the song section layout to the main layout
    m_leftVLayout->addLayout(songSectionLayout);

    // Add sections for Title, Artist, Duration, and Link
    QFormLayout* songDetailsLayout = new QFormLayout();
    QLabel* titleLabel = new QLabel("Title:");
    QLineEdit* titleText = new QLineEdit();
    titleText->setMaximumWidth(titleText->width() * 0.5); // Reduce the width to 50%
    QLabel* artistLabel = new QLabel("Artist:");
    QLineEdit* artistText = new QLineEdit();
    artistText->setMaximumWidth(artistText->width() * 0.5); // Reduce the width to 50%
    QLabel* durationLabel = new QLabel("Duration:");
    QLineEdit* durationText = new QLineEdit();
    durationText->setMaximumWidth(durationText->width() * 0.5); // Reduce the width to 50%
    QLabel* linkLabel = new QLabel("Link:");
    QLineEdit* linkText = new QLineEdit();
    linkText->setMaximumWidth(linkText->width() * 0.5); // Reduce the width to 50%
    songDetailsLayout->addRow(titleLabel, titleText);
    songDetailsLayout->addRow(artistLabel, artistText);
    songDetailsLayout->addRow(durationLabel, durationText);
    songDetailsLayout->addRow(linkLabel, linkText);
    m_leftVLayout->addLayout(songDetailsLayout);

    m_centralWidget->setLayout(m_leftVLayout);
    this->setCentralWidget(m_centralWidget);
}


void MainWindow::addButtonClicked()
{
    QString title = m_titleText->text();
    QString artist = m_artistText->text();
    QString duration = m_durationText->text();
    QString link = m_linkText->text();

    // Perform the add operation using the entered data
    // For example, you could add the song to a list or update a database

    // Clear the input fields after adding
    m_titleText->clear();
    m_artistText->clear();
    m_durationText->clear();
    m_linkText->clear();
}

void MainWindow::deleteButtonClicked()
{
    QString title = m_titleText->text();

    // Perform the delete operation using the entered title
    // For example, you could remove the song from a list or delete it from a database

    // Clear the input fields after deleting
    m_titleText->clear();
}

void MainWindow::updateButtonClicked()
{
    QString title = m_titleText->text();
    QString artist = m_artistText->text();
    QString duration = m_durationText->text();
    QString link = m_linkText->text();

    // Perform the update operation using the entered data and title
    // For example, you could update the song in a list or modify it in a database

    // Clear the input fields after updating
    m_titleText->clear();
    m_artistText->clear();
    m_durationText->clear();
    m_linkText->clear();
}

void MainWindow::filterButtonClicked()
{
    QString filter = m_titleText->text();

    // Perform the filter operation using the entered filter
    // For example, you could filter the songs in a list or query a database

    // Clear the input fields after filtering
    m_titleText->clear();
}



