import sys
from PyQt6.QtWidgets import QApplication, QWidget, QPushButton, QVBoxLayout, QMessageBox

class Calculator(QWidget):
    """
    아무것도 없는 기본 창을 표시하는 클래스
    """
    def __init__(self):
        """
        생성자: 부모 클래스의 생성자를 호출하고 UI 초기화 메서드를 실행합니다.
        """
        super().__init__()
        self.init_ui()

    def init_ui(self):
        """
        기본 창의 속성을 설정합니다.
        - 윈도우 제목
        - 윈도우 위치 및 크기
        """
        # 윈도우의 제목을 '계산기'로 설정합니다.
        self.setWindowTitle('계산기')
        
        # 메인 레이아웃 생성 (수직으로 위젯 배치)
        main_layout = QVBoxLayout()

        # 'Message' 버튼 생성
        self.message_button = QPushButton('Message')
        
        # 버튼 클릭 시 show_message_box 메서드 연결
        self.message_button.clicked.connect(self.show_message_box)
        
        # 레이아웃에 버튼 추가
        main_layout.addWidget(self.message_button)
        
        # 윈도우의 메인 레이아웃으로 설정
        self.setLayout(main_layout)

        # 윈도우 크기 및 위치 설정 (레이아웃이 설정된 후 크기 조정)
        self.setGeometry(300, 300, 200, 100) # 버튼 하나에 적당한 크기로 조정

    def show_message_box(self):
        """
        메시지 박스를 표시하는 슬롯 메서드
        """
        QMessageBox.information(self, 'Message', 'Button Clicked')

# 이 스크립트가 직접 실행될 때만 아래 코드를 실행합니다.
if __name__ == '__main__':
    # 모든 PyQt 애플리케이션은 QApplication 객체를 생성해야 합니다.
    app = QApplication(sys.argv)

    # 우리가 만든 Calculator 클래스의 인스턴스를 생성합니다.
    calculator_window = Calculator()

    # 윈도우를 화면에 보여줍니다.
    calculator_window.show()

    # 애플리케이션의 이벤트 루프를 시작합니다.
    # 창이 닫힐 때까지 프로그램이 종료되지 않도록 합니다.
    sys.exit(app.exec())
