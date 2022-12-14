# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'music_player.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_music_player(object):
    def setupUi(self, music_player):
        music_player.setObjectName("music_player")
        music_player.resize(1006, 658)
        self.verticalLayout = QtWidgets.QVBoxLayout(music_player)
        self.verticalLayout.setObjectName("verticalLayout")
        self.upper_frame = QtWidgets.QFrame(music_player)
        self.upper_frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.upper_frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.upper_frame.setObjectName("upper_frame")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.upper_frame)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.track_info_frame = QtWidgets.QFrame(self.upper_frame)
        self.track_info_frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.track_info_frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.track_info_frame.setObjectName("track_info_frame")
        self.gridLayout = QtWidgets.QGridLayout(self.track_info_frame)
        self.gridLayout.setObjectName("gridLayout")
        self.artist_label = QtWidgets.QLabel(self.track_info_frame)
        self.artist_label.setObjectName("artist_label")
        self.gridLayout.addWidget(self.artist_label, 0, 0, 1, 1)
        self.track_artist = QtWidgets.QLabel(self.track_info_frame)
        self.track_artist.setText("")
        self.track_artist.setObjectName("track_artist")
        self.gridLayout.addWidget(self.track_artist, 0, 1, 1, 1)
        self.track_album = QtWidgets.QLabel(self.track_info_frame)
        self.track_album.setText("")
        self.track_album.setObjectName("track_album")
        self.gridLayout.addWidget(self.track_album, 1, 1, 1, 1)
        self.name_label = QtWidgets.QLabel(self.track_info_frame)
        self.name_label.setObjectName("name_label")
        self.gridLayout.addWidget(self.name_label, 2, 0, 1, 1)
        self.release_label = QtWidgets.QLabel(self.track_info_frame)
        self.release_label.setObjectName("release_label")
        self.gridLayout.addWidget(self.release_label, 3, 0, 1, 1)
        self.track_name = QtWidgets.QLabel(self.track_info_frame)
        self.track_name.setText("")
        self.track_name.setObjectName("track_name")
        self.gridLayout.addWidget(self.track_name, 2, 1, 1, 1)
        self.track_release = QtWidgets.QLabel(self.track_info_frame)
        self.track_release.setText("")
        self.track_release.setObjectName("track_release")
        self.gridLayout.addWidget(self.track_release, 3, 1, 1, 1)
        self.album_label = QtWidgets.QLabel(self.track_info_frame)
        self.album_label.setObjectName("album_label")
        self.gridLayout.addWidget(self.album_label, 1, 0, 1, 1)
        self.genre_label = QtWidgets.QLabel(self.track_info_frame)
        self.genre_label.setObjectName("genre_label")
        self.gridLayout.addWidget(self.genre_label, 4, 0, 1, 1)
        self.track_genre = QtWidgets.QLabel(self.track_info_frame)
        self.track_genre.setText("")
        self.track_genre.setObjectName("track_genre")
        self.gridLayout.addWidget(self.track_genre, 4, 1, 1, 1)
        self.horizontalLayout.addWidget(self.track_info_frame)
        self.tracklist = QtWidgets.QListWidget(self.upper_frame)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.tracklist.sizePolicy().hasHeightForWidth())
        self.tracklist.setSizePolicy(sizePolicy)
        self.tracklist.setObjectName("tracklist")
        self.horizontalLayout.addWidget(self.tracklist)
        self.verticalLayout.addWidget(self.upper_frame)
        self.bottom_frame = QtWidgets.QFrame(music_player)
        self.bottom_frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.bottom_frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.bottom_frame.setObjectName("bottom_frame")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.bottom_frame)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.track_cover_frame = QtWidgets.QFrame(self.bottom_frame)
        self.track_cover_frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.track_cover_frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.track_cover_frame.setObjectName("track_cover_frame")
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout(self.track_cover_frame)
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.track_cover_art = QtWidgets.QLabel(self.track_cover_frame)
        self.track_cover_art.setText("")
        self.track_cover_art.setObjectName("track_cover_art")
        self.horizontalLayout_4.addWidget(self.track_cover_art)
        self.horizontalLayout_2.addWidget(self.track_cover_frame, 0, QtCore.Qt.AlignHCenter|QtCore.Qt.AlignVCenter)
        self.player_frame = QtWidgets.QFrame(self.bottom_frame)
        self.player_frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.player_frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.player_frame.setObjectName("player_frame")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.player_frame)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.player_buttons_frame = QtWidgets.QFrame(self.player_frame)
        self.player_buttons_frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.player_buttons_frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.player_buttons_frame.setObjectName("player_buttons_frame")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout(self.player_buttons_frame)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.previous_button = QtWidgets.QPushButton(self.player_buttons_frame)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.previous_button.sizePolicy().hasHeightForWidth())
        self.previous_button.setSizePolicy(sizePolicy)
        self.previous_button.setStyleSheet("border: none; ")
        self.previous_button.setText("")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/icons /back.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.previous_button.setIcon(icon)
        self.previous_button.setIconSize(QtCore.QSize(40, 40))
        self.previous_button.setFlat(False)
        self.previous_button.setObjectName("previous_button")
        self.horizontalLayout_3.addWidget(self.previous_button)
        self.play_button = QtWidgets.QPushButton(self.player_buttons_frame)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.play_button.sizePolicy().hasHeightForWidth())
        self.play_button.setSizePolicy(sizePolicy)
        self.play_button.setStyleSheet("border: none; \n"
"")
        self.play_button.setText("")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(":/icons /play.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.play_button.setIcon(icon1)
        self.play_button.setIconSize(QtCore.QSize(40, 40))
        self.play_button.setFlat(False)
        self.play_button.setObjectName("play_button")
        self.horizontalLayout_3.addWidget(self.play_button)
        self.next_button = QtWidgets.QPushButton(self.player_buttons_frame)
        self.next_button.setEnabled(True)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.next_button.sizePolicy().hasHeightForWidth())
        self.next_button.setSizePolicy(sizePolicy)
        self.next_button.setStyleSheet("border: none; ")
        self.next_button.setText("")
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap(":/icons /next.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.next_button.setIcon(icon2)
        self.next_button.setIconSize(QtCore.QSize(40, 40))
        self.next_button.setFlat(False)
        self.next_button.setObjectName("next_button")
        self.horizontalLayout_3.addWidget(self.next_button)
        self.verticalLayout_3.addWidget(self.player_buttons_frame)
        self.duration_frame = QtWidgets.QFrame(self.player_frame)
        self.duration_frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.duration_frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.duration_frame.setObjectName("duration_frame")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.duration_frame)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.duration_slider = QtWidgets.QSlider(self.duration_frame)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.duration_slider.sizePolicy().hasHeightForWidth())
        self.duration_slider.setSizePolicy(sizePolicy)
        self.duration_slider.setOrientation(QtCore.Qt.Horizontal)
        self.duration_slider.setObjectName("duration_slider")
        self.verticalLayout_2.addWidget(self.duration_slider)
        self.duration_label = QtWidgets.QLabel(self.duration_frame)
        self.duration_label.setObjectName("duration_label")
        self.verticalLayout_2.addWidget(self.duration_label, 0, QtCore.Qt.AlignHCenter|QtCore.Qt.AlignVCenter)
        self.verticalLayout_3.addWidget(self.duration_frame)
        self.horizontalLayout_2.addWidget(self.player_frame)
        self.verticalLayout.addWidget(self.bottom_frame)

        self.retranslateUi(music_player)
        QtCore.QMetaObject.connectSlotsByName(music_player)

    def retranslateUi(self, music_player):
        _translate = QtCore.QCoreApplication.translate
        music_player.setWindowTitle(_translate("music_player", "Form"))
        self.artist_label.setText(_translate("music_player", "Artist : "))
        self.name_label.setText(_translate("music_player", "Track : "))
        self.release_label.setText(_translate("music_player", "Release : "))
        self.album_label.setText(_translate("music_player", "Album : "))
        self.genre_label.setText(_translate("music_player", "Genre : "))
        self.tracklist.setSortingEnabled(True)
        self.duration_label.setText(_translate("music_player", "Duration : 00:00:00 "))
import player_resources_rc
