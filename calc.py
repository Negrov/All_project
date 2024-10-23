import sys
import io
from unittest import result

from PyQt6 import uic
from PyQt6.QtWidgets import QMainWindow, QApplication

template = '''<?xml version="1.0" encoding="UTF-8"?>
<ui version="4.0">
 <class>MainWindow</class>
 <widget class="QMainWindow" name="MainWindow">
  <property name="geometry">
   <rect>
    <x>0</x>
    <y>0</y>
    <width>489</width>
    <height>495</height>
   </rect>
  </property>
  <property name="windowTitle">
   <string>MainWindow</string>
  </property>
  <widget class="QWidget" name="centralwidget">
   <widget class="QWidget" name="verticalLayoutWidget">
    <property name="geometry">
     <rect>
      <x>10</x>
      <y>30</y>
      <width>151</width>
      <height>261</height>
     </rect>
    </property>
    <layout class="QVBoxLayout" name="color">
     <item>
      <widget class="QPushButton" name="R">
       <property name="text">
        <string>R</string>
       </property>
      </widget>
     </item>
     <item>
      <widget class="QPushButton" name="G">
       <property name="text">
        <string>G</string>
       </property>
      </widget>
     </item>
     <item>
      <widget class="QPushButton" name="B">
       <property name="text">
        <string>B</string>
       </property>
      </widget>
     </item>
     <item>
      <widget class="QPushButton" name="pushButton_4">
       <property name="text">
        <string>ALL</string>
       </property>
      </widget>
     </item>
    </layout>
   </widget>
   <widget class="QWidget" name="horizontalLayoutWidget">
    <property name="geometry">
     <rect>
      <x>10</x>
      <y>360</y>
      <width>461</width>
      <height>71</height>
     </rect>
    </property>
    <layout class="QHBoxLayout" name="horizontalLayout">
     <item>
      <widget class="QPushButton" name="left_step">
       <property name="text">
        <string>left</string>
       </property>
      </widget>
     </item>
     <item>
      <widget class="QPushButton" name="right_step">
       <property name="text">
        <string>right</string>
       </property>
      </widget>
     </item>
    </layout>
   </widget>
  </widget>
  <widget class="QMenuBar" name="menubar">
   <property name="geometry">
    <rect>
     <x>0</x>
     <y>0</y>
     <width>489</width>
     <height>26</height>
    </rect>
   </property>
  </widget>
  <widget class="QStatusBar" name="statusbar"/>
 </widget>
 <resources/>
 <connections/>
</ui>
'''


class MyPillow(QMainWindow):
    def __init__(self):
        super().__init__()
        f = io.StringIO(template)
        uic.loadUi(f, self)
        self.__init_UI__()

    def __init_UI__(self):
        self.curr_image = QImage(self)



if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MyPillow()
    ex.show()
    sys.exit(app.exec())
