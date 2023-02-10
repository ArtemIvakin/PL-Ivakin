#ifndef MAINWINDOW_H
#define MAINWINDOW_H

#include <QMainWindow>
#include <QFile>
#include <fstream>
#include <QString>
#include <QFile>
#include <fstream>
#include <QString>
#include <QMessageBox>
#include <QCoreApplication>
#include <QFile> // Подключаем класс QFile
#include <QTextStream> // Подключаем класс QTextStream
#include <QWidget>
#include <QLabel>
#include <QLineEdit>
#include <QGridLayout>
#include <QDesktopServices>
#include <QUrl>
#include <QDebug>
#include <unordered_set>
#include <QClipboard>

QT_BEGIN_NAMESPACE
namespace Ui { class MainWindow; }
QT_END_NAMESPACE

class MainWindow : public QMainWindow
{
    Q_OBJECT

public:
    MainWindow(QWidget *parent = nullptr);
    ~MainWindow();

private slots:
    void on_pushButton_clicked();

    void on_test_clicked();

    void on_lineEdit_inputRejected();

    void on_pushButton_2_clicked();

private:
    Ui::MainWindow *ui;
};
#endif // MAINWINDOW_H
