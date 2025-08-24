import res
import time
from bilibili import video_api
from bilibili import user_api
from PySide6.QtWidgets import QApplication,QLabel
from PySide6.QtUiTools import QUiLoader  
from PySide6.QtCore import QFile,Qt
from PySide6.QtGui import QPixmap,QPainter,QPainterPath,QIcon

loader = QUiLoader()
up = QApplication()

login_ui = QFile("ui/login.ui")
login_window = loader.load(login_ui)
login_ui.close()

def round_pixmap(src_pixmap: QPixmap, radius: int) -> QPixmap:
    """将QPixmap裁剪为圆角矩形"""
    if src_pixmap.isNull():
        return QPixmap()
    
    # 创建透明画布
    result_pixmap = QPixmap(src_pixmap.size())
    result_pixmap.fill(Qt.transparent)
    
    painter = QPainter(result_pixmap)
    painter.setRenderHint(QPainter.Antialiasing)  # 抗锯齿
    
    # 定义圆角路径
    path = QPainterPath()
    path.addRoundedRect(0, 0, src_pixmap.width(), src_pixmap.height(),
                        radius, radius)
    
    # 裁剪并绘制原图
    painter.setClipPath(path)
    painter.drawPixmap(0, 0, src_pixmap)
    
    painter.end()
    return result_pixmap


login_window.background.setPixmap(round_pixmap(QPixmap("pic/image/f1.png"),radius=18))
login_window.setWindowFlags(Qt.WindowType.FramelessWindowHint)
login_window.setAttribute(Qt.WA_TranslucentBackground)


def User_login():
    time.sleep(0.1)
    for num in range(121):
        login_window.background.setPixmap(round_pixmap(QPixmap(f"light/合成 1_00{num:03d}.png"),radius=18))  
        QApplication.processEvents()
        time.sleep(0.015)
    text=login_window.login_uid.text()
    global gain_uid
    gain_uid=text
    login_window.close()
    hub_window_show()
   

def hub_window_show():
    ui_file2=QFile("ui/api.ui")
    loader2 = QUiLoader()
    global window2
    window2 = loader2.load(ui_file2)  
    ui_file2.close()
    window2.setWindowFlags(Qt.WindowType.FramelessWindowHint)
    window2.setAttribute(Qt.WA_TranslucentBackground)
    window2.stackedWidget.setCurrentIndex(1)
    if user_api.code_check(gain_uid)==0:
        window2.User_name.setText(f"{user_api.name(gain_uid)}")
        window2.sub_text.setText(f"{user_api.sub(gain_uid)} Sub")
    elif user_api.code_check(gain_uid)==-400:
        window2.User_name.setText(f"{gain_uid}")
        window2.sub_text.setText("用户不存在")
    
    window2.show()
    window2.backhub.clicked.connect(lambda: window2.stackedWidget.setCurrentIndex(1))
        
    window2.search.clicked.connect(lambda: window2.stackedWidget.setCurrentIndex(0))

    window2.search_video.clicked.connect(search_video_api)

def search_video_api():
    gain_bvid=window2.api_search_bvid.text()
    if video_api.code_check(gain_bvid)==0:
        video_api_dic=video_api.video_stat(gain_bvid)
        window2.view_text_2.setText(f'{video_api_dic.get("view")} View')
        window2.like_text_2.setText(f'{video_api_dic.get("like")} Like')
        window2.coin_text_2.setText(f'{video_api_dic.get("coin")} Coin')
        window2.collect_text_2.setText(f'{video_api_dic.get("favorite")} Collect')
        window2.share_text_2.setText(f'{video_api_dic.get("share")} Share')
        window2.reply_text_2.setText(f'{video_api_dic.get("reply")} Reply')
        window2.danmaku_text_2.setText(f'{video_api_dic.get("danmaku")} Danmaku')
        window2.vt_text_2.setText(f"{video_api.vt(gain_bvid)} Min")
    elif video_api.code_check(gain_bvid)==-400:
        window2.view_text_2.setText("视频不存在")
    QApplication.processEvents()                


    
login_window.login.clicked.connect(User_login)

login_window.show()

up.setWindowIcon(QIcon('up.png'))

up.exec() 
