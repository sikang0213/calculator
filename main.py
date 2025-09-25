import sys
from PyQt6.QtWidgets import QApplication, QWidget

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
        
        # 윈도우가 화면에 나타날 위치(x, y)와 크기(너비, 높이)를 설정합니다.
        # setGeometry(x_pos, y_pos, width, height)
        self.setGeometry(300, 300, 400, 300)

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
