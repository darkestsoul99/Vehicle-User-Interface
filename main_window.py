from vehicle_interface import Ui_MainWindow
from music_player_widget import *
from phone_bookWidget import *
from radio_widget import *
from PyQt5.QtWidgets import QMainWindow, QSlider, QHBoxLayout
from PyQt5.QtCore import QTimer, QTime, QUrl
from PyQt5.QtWebEngineWidgets import QWebEngineView

class MainWindow(QMainWindow):
    def __init__(self, parent=None):
        QMainWindow.__init__(self)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.show()
        self.ui.main_widget.setCurrentWidget(self.ui.apps_widget)

        # Set various aspects of UI
        self.StyleSheet()
        self.buttonFunctions()
        self.musicPlayer()
        self.Radio()
        self.Camera()
        self.Map()
        self.Gauge()
        self.setTime()
        self.phoneBook()

    def StyleSheet(self):
        # open qss file
        File = open("SpyBot\SpyBot.qss", 'r')

        with File:
            qss = File.read()
            self.setStyleSheet(qss)

    def phoneBook(self):
        self.phoneWidget = PhoneBookWidget()
        self.ui.phone_box.addWidget(self.phoneWidget)

    def Camera(self):
        pass

    def musicPlayer(self):
        self.musicWidget = MusicPlayerWidget()
        self.ui.music_box.addWidget(self.musicWidget)

    def Radio(self):
        self.radioWidget = RadioWidget()
        self.ui.radio_box.addWidget(self.radioWidget)

    def Map(self):
        Web = QWebEngineView()
        Web.load(QUrl("https://www.google.com/maps"))
        Web.show()
        self.ui.maps_layout.addWidget(Web)

    def Gauge(self):
        # rpm gauge
        self.ui.rpm_gauge.setGaugeTheme(20)
        self.ui.rpm_gauge.units = "Km/h"
        self.ui.rpm_gauge.minValue = 0
        self.ui.rpm_gauge.maxValue = 300
        self.ui.rpm_gauge.scalaCount = 10
        self.ui.rpm_gauge.updateValue(self.ui.rpm_gauge.minValue)
        self.ui.rpm_gauge.setEnableBarGraph(False)
        self.ui.rpm_gauge.setMouseTracking(False)
        # speed gauge
        self.ui.speed_gauge.setGaugeTheme(20)
        self.ui.speed_gauge.units = "x1000"
        self.ui.speed_gauge.minValue = 0
        self.ui.speed_gauge.maxValue = 8
        self.ui.speed_gauge.scalaCount = 5
        self.ui.speed_gauge.updateValue(self.ui.speed_gauge.minValue)
        self.ui.speed_gauge.setEnableBarGraph(False)
        self.ui.speed_gauge.setMouseTracking(False)

    def setTime(self):
        timer = QTimer(self)
        timer.timeout.connect(self.displayTime)
        timer.start(1000)

    def displayTime(self):
        currentTime = QTime.currentTime()
        displayText = currentTime.toString('hh:mm:ss')
        self.ui.hour_label.setText(displayText)

    def buttonFunctions(self):
        self.ui.map_button.clicked.connect(lambda: self.mapsButton())
        self.ui.gauge_button.clicked.connect(lambda: self.gaugeButton())
        self.ui.music_button.clicked.connect(lambda: self.musicButton())
        self.ui.phone_button.clicked.connect(lambda: self.phoneButton())
        self.ui.radio_button.clicked.connect(lambda: self.radioButton())
        self.ui.rear_camera.clicked.connect(lambda: self.rearCameraButton())
        self.ui.menu_button.clicked.connect(lambda: self.menuButton())
        self.ui.volume_button.clicked.connect(lambda: self.volumeButton())

    def volumeButton(self):
        pass

    def mapsButton(self):
        self.ui.main_widget.setCurrentWidget(self.ui.map_widget)

    def gaugeButton(self):
        self.ui.main_widget.setCurrentWidget(self.ui.hmi_widget)

    def musicButton(self):
        self.ui.main_widget.setCurrentWidget(self.ui.music_widget)

    def phoneButton(self):
        self.ui.main_widget.setCurrentWidget(self.ui.phone_widget)

    def radioButton(self):
        self.ui.main_widget.setCurrentWidget(self.ui.radio_widget)

    def rearCameraButton(self):
        self.ui.main_widget.setCurrentWidget(self.ui.camera_widget)

    def menuButton(self):
        if (self.ui.main_widget.currentWidget() != self.ui.apps_widget):
            self.ui.main_widget.setCurrentWidget(self.ui.apps_widget)
