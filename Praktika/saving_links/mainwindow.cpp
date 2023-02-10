#include "mainwindow.h"
#include "ui_mainwindow.h"
#include "password.h"


MainWindow::MainWindow(QWidget *parent)
    : QMainWindow(parent)
    , ui(new Ui::MainWindow)
{
   ui->setupUi(this);


}

MainWindow::~MainWindow()
{
    delete ui;
}

//функция кнопки: переход на окно для ввода ссылки и пароля.
void MainWindow::on_test_clicked()
{

    Password window;
    window.setModal(true);
    window.exec();

}
//функция кнопки: поиск ссылки по ключу.
void MainWindow::on_pushButton_clicked()
{
    int k,t;
    QString B, line, key, Pass, Link;
    bool a;
    k=0;
    t=0;

    //присваивание текта из поля для ввода
    //в переменные.
    B=ui->lineEdit_2->text();
    B.append("\n");
    QFile file("database.txt");

    //цикл для нахождения введённого ключа(названия).
    if (file.open(QIODevice::ReadOnly | QIODevice::Text)) {
        while(!file.atEnd()){
            k=0;
            key="";
            QByteArray Fline =file.readLine();
            line=QString::fromUtf8(Fline);
            //цикл для нахождения ключа в строке.
            for  (int i= 0; i < line.size(); i++){
               if (line[i]== " ")
               {
                   k++;
                   if (k == 2){
                       t= i+1;
                       break;
                   }
               }
            }
            //цикл для сравнивания ключа в строке с ключом
            //введённым пользователем и последующим выводом
            //в отдельное окно найденной ссылки и пароля.
            for (int i = t; i < line.size(); i++)
                key.append(line[i]);
            if (B == key){
                k=0;
                for  (int j= 0; j < line.size(); j++){
                    if (line[j]== " "){
                        k++;
                        j++;
                    }
                    if (k < 1)
                        Link.append(line[j]);
                    if (k == 1)
                        Pass.append(line[j]);
                }
                //вывод найденной ссылки и пароля
                //в отдельное окно с вопросом на открытие ссылки
                //в браузере.
                QClipboard *pClipboard = QApplication::clipboard();
                pClipboard->setText(Pass);
                QMessageBox::StandardButton reply = QMessageBox::question(this,"Ссылка с ключём '" + B + "' найдена",
                                                                           "Ссылка: " + Link +"\n"+"Пароль: "+Pass+ " скопирован в буфер обмена\n"+
                                                                          "Перейти по ссылке?", QMessageBox::Yes | QMessageBox::No);
                if(reply== QMessageBox::Yes){
                    QDesktopServices::openUrl(QUrl(Link));
                }
                a=true;
                break;
            }
            else
                a=false;
            if (a == true){
             break;
            }
        }
        //вывод ошибки если введённый ключ не был найден
        if (a==false)
            QMessageBox::critical(this,"Ошибка!", "Ссылка не найдена!");
     }
    file.close();
    ui->lineEdit_2->clear();
}

void MainWindow::on_pushButton_2_clicked()
{

}
