import os.path
import time
import pickle

# from threading import Thread
import paramiko
from PyQt5.QtGui import *
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *


class RemoteDialog(QDialog):
    printRequest = pyqtSignal(str)

    def __init__(self, parent=None):
        super().__init__(parent)

        self.printRequest.connect(self.show_text)

        layout = QHBoxLayout()
        layout.setContentsMargins(0, 0, 0, 0)
        input_layout = QVBoxLayout()

        ip_label = QLabel("IP地址: ")
        input_layout.addWidget(ip_label)
        self.host = QLineEdit()
        input_layout.addWidget(self.host)

        post_label = QLabel("端口号: ")
        input_layout.addWidget(post_label)
        self.port = QLineEdit('22')
        input_layout.addWidget(self.port)

        username_label = QLabel('用户名: ')
        self.username = QLineEdit()
        input_layout.addWidget(username_label)
        input_layout.addWidget(self.username)

        self.pwd_label = QLabel("密码: ")
        self.pwd = QLineEdit()
        input_layout.addWidget(self.pwd_label)
        input_layout.addWidget(self.pwd)

        path_label = QLabel("文件路径: ")
        input_layout.addWidget(path_label)
        self.remote_path = QPlainTextEdit()
        input_layout.addWidget(self.remote_path)

        output_layout = QVBoxLayout()
        self.output = QTextBrowser()
        output_layout.addWidget(self.output)

        self.choose = QPushButton("选择下载目录")
        self.choose.clicked.connect(self.choose_dir)
        self.choose.setFocusPolicy(Qt.NoFocus)
        output_layout.addWidget(self.choose)
        self.local_path = QLineEdit()
        output_layout.addWidget(self.local_path)

        self.submit = QPushButton("下载")
        self.submit.clicked.connect(self.click_download)
        self.pgb = QProgressBar()
        self.pgb.setMinimum(0)
        self.pgb.setMaximum(100)
        self.pgb.setStyleSheet(
            "QProgressBar {text-align: center;}")
        output_layout.addWidget(self.submit)
        output_layout.addWidget(self.pgb)

        layout.addLayout(input_layout)
        layout.addLayout(output_layout)
        self.setLayout(layout)
        self.setWindowTitle("打开远程文件")
        self.setContentsMargins(20, 20, 20, 20)

        self.cache_path = 'cache/recent.pkl'
        self.info = {}
        self.get_recent()

    def get_recent(self):
        if not os.path.exists(self.cache_path):
            return
        with open(self.cache_path, 'rb') as f:
            self.info = pickle.load(f)

        self.host.setText(self.info['host'])
        self.port.setText(self.info['port'])
        self.username.setText(self.info['username'])
        self.pwd.setText(self.info['pwd'])
        self.remote_path.setPlainText(self.info['remote_path'])

    def overlap_recent(self):
        new_info = {
            'host': self.host.text(),
            'port': self.port.text(),
            'username': self.username.text(),
            'pwd': self.pwd.text(),
            'remote_path': self.remote_path.toPlainText()
        }
        if new_info != self.info:
            if not os.path.exists(os.path.dirname(self.cache_path)):
                os.makedirs(os.path.dirname(self.cache_path))
            with open(self.cache_path, 'wb') as f:
                pickle.dump(new_info, f)

    def show_text(self, text):
        """将文本内容追加到程序「展示框」"""
        self.output.append(text)

    def click_download(self):
        """处理点击「下载」按钮事件"""
        if self.check_value():
            # t = Thread(target=self.download)
            # t.start()
            self.download()

    def show_process(self, transferred, toBeTransferred):
        bar_len = 100
        filled_len = int(round(bar_len * transferred / float(toBeTransferred)))
        self.pgb.setValue(filled_len)

    def check_value(self):

        if not is_valid_ip(self.host.text()):
            self.printRequest.emit('Error: 输入的IP地址有误！')
            return False

        if not is_valid_port(self.port.text()):
            self.printRequest.emit('Error: 输入的端口号有误！')
            return False

        if self.username.text().isspace() or self.pwd.text().isspace():  # 判断输入的用户名或密码是否为空
            self.printRequest.emit('Error: 用户名或密码不能为空！')
            return False

        if not is_valid_path(self.remote_path.toPlainText()):
            self.printRequest.emit('Error: 输入的文件目录有误！')
            return False

        if not is_valid_path(self.local_path.text()):
            self.printRequest.emit('Error: 下载文件目录有误！')
            return False
        return True

    def choose_dir(self):
        dir_path = QFileDialog.getExistingDirectory(self,
                                                    'Choose Directory',
                                                    './',
                                                    QFileDialog.ShowDirsOnly | QFileDialog.DontResolveSymlinks)
        filename = os.path.basename(self.remote_path.toPlainText())
        self.local_path.setText(os.path.join(dir_path, filename))

    def download(self):

        try:
            self.printRequest.emit('***连接服务器***')
            tran = paramiko.Transport((self.host.text(), int(self.port.text())))  # 获取 Transport 实例

            tran.connect(username=self.username.text(), password=self.pwd.text())  # 连接 SSH 服务端
            self.printRequest.emit('服务器连接成功！')

            sftp = paramiko.SFTPClient.from_transport(tran)  # 创建 SFTP 实例

            self.printRequest.emit('***下载文件***')
            sftp.get(remotepath=self.remote_path.toPlainText(),
                     localpath=self.local_path.text(),
                     callback=self.show_process)  # 下载文件
            self.printRequest.emit(f'文件下载成功！\n{self.local_path.text()}\n完成！')
            time.sleep(1)
            self.accept()  # 下载完成后，关闭窗口

            self.overlap_recent()

        except Exception as e:
            self.printRequest.emit(str(e))

    def pop_up(self):
        """
        弹出窗口
        Returns
        -------
        下载的Docset地址
        """
        self.restore_statue()
        self.host.setFocus(Qt.PopupFocusReason)

        # self.exec_() 显示窗口，阻塞主程序，直到关闭窗口且有返回值
        return self.local_path.text() if self.exec_() else None

    def restore_statue(self):
        self.output.clear()
        self.pgb.reset()

    def closeEvent(self, ev):
        self.restore_statue()


def is_valid_ip(ipaddr):
    addr = ipaddr.strip().split('.')  # 切割IP地址为一个列表

    if len(addr) != 4:  # 切割后列表必须有4个参数
        return False

    for i in range(4):
        try:
            addr[i] = int(addr[i])  # 每个参数必须为数字，否则校验失败
        except:
            return False

        if addr[i] > 255 or addr[i] < 0:  # 每个参数值必须在0-255之间
            return False

    return True


def is_valid_port(port):
    try:
        if int(port) not in range(0, 65536):
            return False
    except:
        return False

    return True


def is_valid_path(path):
    filename = os.path.basename(path)
    if os.path.splitext(filename)[1] != '.ds':
        return False
    return True
