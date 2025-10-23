# main.py
import sys
from PyQt6.QtWidgets import QApplication, QWidget

# ui.py에서 정의한 Ui_Calculator 클래스를 가져옵니다.
from ui import Ui_Calculator

class CalculatorApp(QWidget):
    """
    UI 클래스를 사용하여 화면을 만들고, 시그널과 슬롯을 연결하여
    애플리케이션의 실제 동작을 담당하는 메인 클래스.
    """
    def __init__(self):
        super().__init__()
        
        # UI 클래스의 인스턴스 생성
        self.ui = Ui_Calculator()
        # self(CalculatorApp 위젯)를 기반으로 UI를 설정
        self.ui.setupUi(self)

        # 시그널과 슬롯 연결 (이벤트 핸들링)
        self.ui.add_button.clicked.connect(self.calculate_sum)
        self.ui.num1_edit.returnPressed.connect(self.calculate_sum)
        self.ui.num2_edit.returnPressed.connect(self.calculate_sum)
        
        # 윈도우를 화면에 보여줍니다.
        self.show()

    def calculate_sum(self):
        """두 입력 필드의 숫자를 더하고 결과를 레이블에 표시합니다."""
        try:
            # UI 객체를 통해 위젯에 접근하여 텍스트를 가져옵니다.
            num1_text = self.ui.num1_edit.text()
            num2_text = self.ui.num2_edit.text()

            num1 = float(num1_text or 0)
            num2 = float(num2_text or 0)
            
            result = num1 + num2
            
            # 정수이면 소수점 없이 표시
            if result.is_integer():
                self.ui.result_label.setText(f"결과: {int(result)}")
            else:
                self.ui.result_label.setText(f"결과: {result}")

        except ValueError:
            # 변환 중 오류가 발생하면 메시지 표시
            self.ui.result_label.setText("결과: 유효한 숫자를 입력하세요.")

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = CalculatorApp()
    sys.exit(app.exec())
