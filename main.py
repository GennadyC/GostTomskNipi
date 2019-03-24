from PyQt5 import QtWidgets
from mydesign import Ui_MainWindow
import sys
from PyQt5.QtCore import pyqtSlot

combustion_mode = [[1,1,2,3], [1,2,3,4], [2,3,4,5], [3,4,5,6]]
Classification = ["особо чувствительные вещества ", 
 "чувствительные вещества ",
 "средне чувствительные вещества ",
 "слабо чувствительные вещества "]

Class_zagromo = ["класс 1 - наличие длинных труб, полостей, каверн, заполненных горючей смесью, при сгорании которой возможно ожидать формирование турбулентных струй продуктов сгорания, имеющих размеры не менее трех размеров детонационной ячейки данной смеси",
"класс 2 - сильно загроможденное пространство: наличие полузамкнутых объемов, высокая плотность размещения технологического оборудования, лес, большое количество повторяющихся препятствий",
"класс 3 - средне загроможденное пространство: отдельно стоящие технологические установки, резервуарный парк",
"класс 4 - слабо загроможденное и свободное пространство"]

def class_trebu(number, massa):
	class_treb = ["класс 1 - детонация или горение со скоростью фронта пламени 500 м/с и более",
	"класс 2 - дефлаграция, скорость фронта пламени от 300 до 500 м/с",
	"класс 3 - дефлаграция, скорость фронта пламени от 200 до 300 м/с",
	"класс 4 - дефлаграция, скорость фронта пламени от 150 до 200 м/с",
	"класс 5 - дефлаграция, скорость фронта пламени "+str(43*massa**(1/6)),
	"класс 6 - дефлаграция, скорость фронта пламени "+str(26*massa**(1/6))]
	return class_treb[number]
Classification_number = 1
#row_class = #строка класса
#column_class = #столбец класса

class_zagro ={Class_zagromo[0]: 0,Class_zagromo[1]: 1,Class_zagromo[2]: 2,Class_zagromo[3]: 3}





class mywindow(QtWidgets.QMainWindow):
	def __init__(self):
		super(mywindow, self).__init__()
		self.ui = Ui_MainWindow()
		self.ui.setupUi(self)

		self.ui.comboBox.addItem("Метан <CH₄> - Methane")
		self.ui.comboBox.addItem("Метиловый спирт <CH₃OH> - Methanol")
		self.ui.comboBox.addItem("Пентан <C₅H₁₂> - Pentan")
		self.ui.comboBox.addItem("Пропан <C₃H₈> - Propan")
		self.ui.comboBox.addItem("Пропилен <C₃H₆> - Propylene")
		self.ui.comboBox.addItem("Сероводород <H₂S> - Hydrogen sulphide")
		self.ui.comboBox.addItem("Бутадиен <C₄H₆> - Butadiene")
		self.ui.comboBox.addItem("Бутан <C₄H₁₀> - Butane")
		self.ui.comboBox.addItem("Винилхлорид <C₂H₃Cl> - Vinylchloride")
		self.ui.comboBox.activated[str].connect(self.onActivated)
		self.ui.comboBox_2.addItem(Class_zagromo[0])
		self.ui.comboBox_2.addItem(Class_zagromo[1])
		self.ui.comboBox_2.addItem(Class_zagromo[2])
		self.ui.comboBox_2.addItem(Class_zagromo[3])
		self.ui.pushButton.clicked.connect(self.on_click)

	def E(Cg, Cct):
		if Cg <= Cct:
			return self.ui.lineEdit_12.text()
		else:

	@pyqtSlot()
	def on_click(self):
		text = str(self.ui.comboBox_2.currentText())
		massa = 0
		try:
			massa = int(self.ui.lineEdit.text())
			self.ui.label_4.setStyleSheet('color: black')
		except Exception:
			self.ui.label_4.setStyleSheet('color: red')
		#print(combustion_mode[Classification_number][class_zagro[text]])
		self.ui.lineEdit_13.setText(class_trebu(combustion_mode[Classification_number][class_zagro[text]] + 1,massa))

	def onActivated(self, text):
		if text=="Метан <CH₄> - Methane":
			Classification_number = 3
			self.ui.lineEdit_32.setText(Classification[Classification_number])
			self.ui.lineEdit_33.setText("(размер детонационной ячейки больше 40 см)")
			self.ui.lineEdit_12.setText("50160")
			self.ui.lineEdit_6.setText("0,656")
			self.ui.lineEdit_34.setText("ГГ")
			self.ui.lineEdit_12.setText(str(44*1.44))
		elif text=="Метиловый спирт <CH₃OH> - Methanol":
			Classification_number = 2
			self.ui.lineEdit_32.setText(Classification[Classification_number])
			self.ui.lineEdit_33.setText("(размер детонационной ячейки лежит в пределах от 10 до 40 см)")
			self.ui.lineEdit_12.setText("23839")
			self.ui.lineEdit_6.setText("792")
			self.ui.lineEdit_34.setText("ЛВЖ")
			self.ui.lineEdit_12.setText(str(44*0.45))

		elif text=="Пентан <C₅H₁₂> - Pentan":
			Classification_number = 3
			self.ui.lineEdit_32.setText(Classification[Classification_number])
			self.ui.lineEdit_33.setText("(размер детонационной ячейки больше 40 см)")
			self.ui.lineEdit_12.setText("45462")
			self.ui.lineEdit_6.setText("626")
			self.ui.lineEdit_34.setText("ГГ")
			self.ui.lineEdit_12.setText(str(44))

		elif text=="Пропан <C₃H₈> - Propan":
			Classification_number = 1
			self.ui.lineEdit_32.setText(Classification[Classification_number])
			self.ui.lineEdit_33.setText("(размер детонационной ячейки лежит в пределах от 2 до 10 см)")
			self.ui.lineEdit_12.setText("46300")
			self.ui.lineEdit_6.setText("493")
			self.ui.lineEdit_34.setText("ГГ")
			self.ui.lineEdit_12.setText(str(44*1))

		elif text=="Пропилен <C₃H₆> - Propylene":
			Classification_number = 1
			self.ui.lineEdit_32.setText(Classification[Classification_number])
			self.ui.lineEdit_33.setText("(размер детонационной ячейки лежит в пределах от 2 до 10 см)")
			self.ui.lineEdit_12.setText("45694")
			self.ui.lineEdit_6.setText("1,81")
			self.ui.lineEdit_34.setText("ГГ")
			self.ui.lineEdit_12.setText(str(44*1))

		elif text=="Сероводород <H₂S> - Hydrogen sulphide":
			Classification_number = 2
			self.ui.lineEdit_32.setText(Classification[Classification_number])
			self.ui.lineEdit_33.setText("(размер детонационной ячейки лежит в пределах от 10 до 40 см)")
			self.ui.lineEdit_12.setText("16989")
			self.ui.lineEdit_6.setText("1,36")
			self.ui.lineEdit_34.setText("ГГ"),
			self.ui.lineEdit_12.setText(str(44*0.34))

		elif text=="Бутадиен <C₄H₆> - Butadiene":
			Classification_number = 1
			self.ui.lineEdit_32.setText(Classification[Classification_number])
			self.ui.lineEdit_33.setText("(размер детонационной ячейки лежит в пределах от 2 до 10 см)")
			self.ui.lineEdit_12.setText("44574")
			self.ui.lineEdit_6.setText("615")
			self.ui.lineEdit_34.setText("ЛВЖ")
			self.ui.lineEdit_12.setText(str(44*1))

		elif text=="Бутан <C₄H₁₀> - Butane":
			Classification_number = 1
			self.ui.lineEdit_32.setText(Classification[Classification_number])
			self.ui.lineEdit_33.setText("(размер детонационной ячейки лежит в пределах от 2 до 10 см)")
			self.ui.lineEdit_12.setText("45800")
			self.ui.lineEdit_6.setText("2,48")
			self.ui.lineEdit_34.setText("ГГ")
			self.ui.lineEdit_12.setText(str(44*1))

		elif text=="Винилхлорид <C₂H₃Cl> - Vinylchloride":
			Classification_number = 3
			self.ui.lineEdit_32.setText(Classification[Classification_number])
			self.ui.lineEdit_33.setText("(размер детонационной ячейки лежит в пределах от 10 до 40 см)")
			self.ui.lineEdit_12.setText("18307")
			self.ui.lineEdit_6.setText("911")
			self.ui.lineEdit_34.setText("ГГ")
			self.ui.lineEdit_12.setText(str(44*0.42))




app = QtWidgets.QApplication([])
application = mywindow()
application.show()

sys.exit(app.exec())