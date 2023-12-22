#ifndef MAINWINDOW_H
#define MAINWINDOW_H

#include <QMainWindow>
#include <QVBoxLayout>
#include <QLabel>
#include <QTextEdit>
#include <QLineEdit>
#include <QFormLayout>
#include <QMainWindow>
#include <QWidget>
#include <QVBoxLayout>
#include <QLabel>
#include <QTextEdit>
#include <QFormLayout>
#include <QLineEdit>
#include <QPushButton>


class MainWindow : public QMainWindow

{
    Q_OBJECT

public:
    MainWindow(QWidget* parent = nullptr);
    ~MainWindow();
private:
    void setupUI();

    QWidget* m_centralWidget;
    QVBoxLayout* m_leftVLayout;
    QFormLayout* m_leftFormLayout;

    // form layout
    QLabel* m_titleLable;
    QLineEdit* m_titleText;

    QLabel* m_artistLable;
    QLineEdit* m_artistText;

    QLabel* m_durationLable;
    QLineEdit* m_durationText;

    QLabel* m_linkLable;
    QLineEdit* m_linkText;

    QLabel* m_listSongsLabel;
    QTextEdit* m_listSongs;

    QPushButton* m_addButton;
    QPushButton* m_deleteButton;
    QPushButton* m_updateButton;
    QPushButton* m_filterButton;

private slots:
    // New slots for button clicks
    void addButtonClicked();
    void deleteButtonClicked();
    void updateButtonClicked();
    void filterButtonClicked();
};

#endif // MAINWINDOW_H
