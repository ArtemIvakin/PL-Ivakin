#ifndef PASSWORD_H
#define PASSWORD_H

#include <QDialog>
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
#include <unordered_set>
namespace Ui {
class Password;
}

class Password : public QDialog
{
    Q_OBJECT

public:
    explicit Password(QWidget *parent = nullptr);
    ~Password();

private slots:
    void on_pushButton_clicked();

private:
    Ui::Password *ui;
};

#endif // PASSWORD_H
