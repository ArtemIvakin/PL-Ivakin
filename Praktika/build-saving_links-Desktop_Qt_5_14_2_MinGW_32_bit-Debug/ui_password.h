/********************************************************************************
** Form generated from reading UI file 'password.ui'
**
** Created by: Qt User Interface Compiler version 5.14.2
**
** WARNING! All changes made in this file will be lost when recompiling UI file!
********************************************************************************/

#ifndef UI_PASSWORD_H
#define UI_PASSWORD_H

#include <QtCore/QVariant>
#include <QtWidgets/QApplication>
#include <QtWidgets/QDialog>
#include <QtWidgets/QLabel>
#include <QtWidgets/QLineEdit>
#include <QtWidgets/QPushButton>
#include <QtWidgets/QVBoxLayout>

QT_BEGIN_NAMESPACE

class Ui_Password
{
public:
    QVBoxLayout *verticalLayout_2;
    QVBoxLayout *verticalLayout;
    QLabel *label_3;
    QLineEdit *lineLink;
    QLabel *label_2;
    QLineEdit *linePassword;
    QLabel *label;
    QLineEdit *lineKey;
    QPushButton *pushButton;

    void setupUi(QDialog *Password)
    {
        if (Password->objectName().isEmpty())
            Password->setObjectName(QString::fromUtf8("Password"));
        Password->resize(257, 233);
        verticalLayout_2 = new QVBoxLayout(Password);
        verticalLayout_2->setObjectName(QString::fromUtf8("verticalLayout_2"));
        verticalLayout = new QVBoxLayout();
        verticalLayout->setObjectName(QString::fromUtf8("verticalLayout"));
        label_3 = new QLabel(Password);
        label_3->setObjectName(QString::fromUtf8("label_3"));

        verticalLayout->addWidget(label_3);

        lineLink = new QLineEdit(Password);
        lineLink->setObjectName(QString::fromUtf8("lineLink"));

        verticalLayout->addWidget(lineLink);

        label_2 = new QLabel(Password);
        label_2->setObjectName(QString::fromUtf8("label_2"));
        label_2->setWordWrap(true);

        verticalLayout->addWidget(label_2);

        linePassword = new QLineEdit(Password);
        linePassword->setObjectName(QString::fromUtf8("linePassword"));

        verticalLayout->addWidget(linePassword);

        label = new QLabel(Password);
        label->setObjectName(QString::fromUtf8("label"));
        label->setMouseTracking(true);
        label->setLayoutDirection(Qt::LeftToRight);
        label->setAutoFillBackground(true);
        label->setTextFormat(Qt::AutoText);
        label->setWordWrap(true);

        verticalLayout->addWidget(label);

        lineKey = new QLineEdit(Password);
        lineKey->setObjectName(QString::fromUtf8("lineKey"));

        verticalLayout->addWidget(lineKey);

        pushButton = new QPushButton(Password);
        pushButton->setObjectName(QString::fromUtf8("pushButton"));
        pushButton->setCursor(QCursor(Qt::PointingHandCursor));
        pushButton->setMouseTracking(true);

        verticalLayout->addWidget(pushButton);


        verticalLayout_2->addLayout(verticalLayout);


        retranslateUi(Password);

        QMetaObject::connectSlotsByName(Password);
    } // setupUi

    void retranslateUi(QDialog *Password)
    {
        Password->setWindowTitle(QCoreApplication::translate("Password", "Dialog", nullptr));
        label_3->setText(QCoreApplication::translate("Password", "\320\222\320\262\320\265\320\264\320\270\321\202\320\265 \321\201\321\201\321\213\320\273\320\272\321\203 \321\201\320\260\320\271\321\202\320\260:", nullptr));
        label_2->setText(QCoreApplication::translate("Password", "\320\222\320\262\320\265\320\264\320\270\321\202\320\265 \320\277\320\260\321\200\320\276\320\273\321\214 \320\264\320\273\321\217 \321\201\320\260\320\271\321\202\320\260 (\320\265\321\201\320\273\320\270 \320\277\320\260\321\200\320\276\320\273\321\217 \320\275\320\265\321\202 \320\262\320\262\320\265\320\264\320\270\321\202\320\265 \" - \"):", nullptr));
        label->setText(QCoreApplication::translate("Password", "\320\222\320\262\320\265\320\264\320\270\321\202\320\265 \320\275\320\260\320\267\320\262\320\260\320\275\320\270\320\265 \321\201\320\260\320\271\321\202\320\260 \320\270\320\273\320\270 \320\272\320\273\321\216\321\207 \320\277\320\276 \320\272\320\276\321\202\320\276\321\200\320\276\320\274\321\203 \320\265\320\263\320\276 \320\274\320\276\320\266\320\275\320\276 \320\261\321\203\320\264\320\265\321\202 \320\275\320\260\320\271\321\202\320\270 \320\277\320\276\320\267\320\266\320\265:", nullptr));
        pushButton->setText(QCoreApplication::translate("Password", "\320\241\320\276\321\205\321\200\320\260\320\275\320\270\321\202\321\214 ", nullptr));
    } // retranslateUi

};

namespace Ui {
    class Password: public Ui_Password {};
} // namespace Ui

QT_END_NAMESPACE

#endif // UI_PASSWORD_H
