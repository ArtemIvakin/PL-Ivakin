#include "password.h"
#include "ui_password.h"

Password::Password(QWidget *parent) :
    QDialog(parent),
    ui(new Ui::Password)
{
    ui->setupUi(this);
}

Password::~Password()
{
    delete ui;
}

//функция для записи информации в файл
//в неё передается 3 параматр, которые беруться из строк для ввода
//link-ссылка, Pass-пароль, Key-ключ(название).
void saveFile(QString link, QString Pass, QString Key, QString filename)
{
    QFile file(filename);

    if (file.open(QIODevice::Append | QIODevice::Text)) {
        QTextStream stream(&file);
        stream << link<< " " << Pass << " " << Key << endl;
    }
    file.close();
}

//функция кнопки: сохранение ссылок и паролей.
void Password::on_pushButton_clicked()
{
    bool A=true;
    QString Pass, Key, Link, Flink, Fkey;

    //присваивание текта из поля для ввода
    //вы переменные
    Link=ui->lineLink->text();
    Pass=ui->linePassword->text();
    Key=ui->lineKey->text();

    QFile file("database.txt");

    if (file.open(QIODevice::ReadOnly | QIODevice::Text)) {
        while(!file.atEnd()){
           int k=0;
           Flink="";
           Fkey="";
            QByteArray Fline =file.readLine();
           QString line=QString::fromUtf8(Fline);

           //цикл для проверки вводимых данных на уникальность
           //при нахождении одинаковой ссылки или ключа
           //выдаст ошибку.
    for  (int j= 0; j < line.size()-1; j++){
        if (line[j]== " "){
            k++;
            j++;
        }
        if (k < 1)
            Flink.append(line[j]);
        if (k == 2)
            Fkey.append(line[j]);
    }
        if (Flink==Link){
            QMessageBox::critical(this,"Ошибка!", "Ссылка уже существует!");
            A=false;break;}
        if (Fkey==Key){
            QMessageBox::critical(this,"Ошибка!", "Данный ключ уже используется!");
            A=false;break;}

     }
    }
    file.close();

    //цикл для проверки вводимых данных на содержание пробелов
    // при их наличии выдает ошибку.
    for  (int i= 0; i < Link.size(); i++){
        if (Link[i]==" "){
            QMessageBox::critical(this,"Ошибка!", "Ссылка не может содержать пробел!");
            A=false;
        }
    }
    for  (int i= 0; i < Pass.size(); i++){
        if (Pass[i]==" "){
            QMessageBox::critical(this,"Ошибка!", "Пароль не может содержать пробел!");
            A=false;
        }
    }
    for  (int i= 0; i < Key.size(); i++){
        if (Key[i]==" "){
            QMessageBox::critical(this,"Ошибка!", "Ключ не может содержать пробел!");
            A=false;
        }
    }

    //проверка полей для ввода на наличие информации
    //и запись её в файл.
    if (A!=false){
    if ((Pass.size() == 0) || (Key.size() == 0) || (Link.size() == 0)){
        QMessageBox::critical(this,"Ошибка!", "Эти поля не могут быть пустыми");
    }
    else{

        saveFile(Link, Pass, Key ,"database.txt");
        QMessageBox::about(this,"Успешно!", "Ссылка, пароль и ключ сохранены");
        close();

    }
    }
}
