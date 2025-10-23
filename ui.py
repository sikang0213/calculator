# ui.py
from PyQt6.QtWidgets import (
    QWidget,
    QLineEdit,
    QPushButton,
    QLabel,
    QVBoxLayout,
    QHBoxLayout,
)
from PyQt6.QtCore import Qt

class Ui_Calculator(object):
    """
    계산기 애플리케이션의 UI를 정의하는 클래스.
    위젯 생성 및 레이아웃 설정을 담당합니다.
    """
    def setupUi(self, main_window: QWidget):
        # 메인 윈도우 객체에 이름 설정
        main_window.setObjectName("main_window")
        
        # 위젯 생성
        self.num1_edit = QLineEdit()
        self.num1_edit.setPlaceholderText("첫 번째 숫자")
        self.num1_edit.setAlignment(Qt.AlignmentFlag.AlignRight)

        self.num2_edit = QLineEdit()
        self.num2_edit.setPlaceholderText("두 번째 숫자")
        self.num2_edit.setAlignment(Qt.AlignmentFlag.AlignRight)

        self.add_button = QPushButton("add")

        self.result_label = QLabel("결과: ")
        self.result_label.setAlignment(Qt.AlignmentFlag.AlignCenter)

        # 레이아웃 설정
        input_layout = QHBoxLayout()
        input_layout.addWidget(self.num1_edit)
        input_layout.addWidget(QLabel("+"))
        input_layout.addWidget(self.num2_edit)

        main_layout = QVBoxLayout()
        main_layout.addLayout(input_layout)
        main_layout.addWidget(self.add_button)
        main_layout.addWidget(self.result_label)

        # 메인 윈도우에 레이아웃 적용
        main_window.setLayout(main_layout)

        # 윈도우 기본 설정
        main_window.setWindowTitle('간단한 덧셈 계산기 (UI 분리)')
        main_window.setGeometry(300, 300, 300, 150)
