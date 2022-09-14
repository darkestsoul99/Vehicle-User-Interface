import os
from music_player import *
from mutagen.mp3 import MP3
from PyQt5.QtCore import QUrl
from PyQt5.QtWidgets import QWidget
from PyQt5.QtGui import QPixmap, QIcon
from PyQt5.QtMultimedia import QMediaPlayer, QMediaContent, QMediaPlaylist, \
QMediaMetaData

class MusicPlayerWidget(QWidget):
    def __init__(self, parent=None):
        QWidget.__init__(self)
        self.ui = Ui_music_player()
        self.ui.setupUi(self)
        self.url = QUrl()
        self.player = QMediaPlayer()
        self.playlist = QMediaPlaylist(self.player)
        self.player.setPlaylist(self.playlist)
        self.temp_icon = QIcon()

        # Update various aspects of gui
        self.playlist.currentIndexChanged.connect(self.update)
        self.player.metaDataChanged.connect(self.meta_data)
        self.ui.tracklist.itemClicked.connect(self._itemclick)
        self.player.positionChanged.connect(self.track_position)
        self.player.durationChanged.connect(self.duration)
        self.ui.duration_slider.valueChanged.connect(self.timer)
        self.ui.duration_slider.sliderMoved.connect(self.slider_position)
        self._files()

        # Button Functions
        self.ui.play_button.released.connect(self._state)
        self.ui.previous_button.released.connect(self._prev)
        self.ui.next_button.released.connect(self._next)


    # Volume control
    def _volume(self, val=70):
        self.player.setVolume(val)

    def slider_position(self, sliderPosition):
        self.player.setPosition(sliderPosition)
        print(sliderPosition)

    # Sets position of slider
    def track_position(self, track_pos):
        self.ui.duration_slider.setValue(track_pos)

    # Duration of the track playing
    def duration(self, duration):
        self.ui.duration_slider.setRange(0, duration)

    # Updates duration of track playing
    def timer(self):
        total_milliseconds = self.player.duration()
        total_seconds, total_milliseconds = divmod(total_milliseconds, 1000)
        total_minutes, total_seconds = divmod(total_seconds, 60)
        total_hours, total_minutes = divmod(total_minutes, 60)

        elapsed_milliseconds = self.ui.duration_slider.value()
        elapsed_seconds, elapsed_milliseconds = divmod(elapsed_milliseconds, 1000)
        elapsed_minutes, elapsed_seconds = divmod(elapsed_seconds, 60)
        elapsed_hours, elapsed_minutes = divmod(elapsed_minutes, 60)

        self.ui.duration_label.setText(
            f'Duration: {elapsed_hours:02d}:{elapsed_minutes:02d}:{elapsed_seconds:02d} / {total_hours:02d}:{total_minutes:02d}:{total_seconds:02d}')

    # Shorten text that may be too long
    def _truncate(self, text, length=25):
        if text:
            if len(text) <= length:
                return text
            else:
                return f"{' '.join(text[:length + 1].split(' ')[0:-1])} ...."

    # Get music metadata
    def meta_data(self):
        if self.player.isMetaDataAvailable():
            if self.player.metaData(QMediaMetaData.AlbumArtist):
                self.ui.track_artist.setText(self.player.metaData(QMediaMetaData.AlbumArtist))
            else:
                self.ui.track_artist.setText("Unknown")

            if self.player.metaData(QMediaMetaData.AlbumTitle):
                self.ui.track_album.setText(self._truncate(self.player.metaData(QMediaMetaData.AlbumTitle)))
            else:
                self.ui.track_album.setText("Unknown")

            if self.player.metaData(QMediaMetaData.Title):
                self.ui.track_name.setText(self._truncate(self.player.metaData(QMediaMetaData.Title)))
            else:
                self.ui.track_name.setText("Unknown")

            if self.player.metaData(QMediaMetaData.Year):
                self.ui.track_release.setText(f'{self.player.metaData(QMediaMetaData.Year)}')
            else:
                self.ui.track_release.setText("Unknown")

            if self.player.metaData(QMediaMetaData.Genre):
                genre = self.player.metaData(QMediaMetaData.Genre)
                strippedText = str(genre).replace('[', '').replace(']', '').replace('\'', '').replace('\"', '')
                self.ui.track_genre.setText(strippedText)
            else:
                self.ui.track_genre.setText("Unknown")

            if self.player.metaData(QMediaMetaData.ThumbnailImage):
                pixmap = QPixmap(self.player.metaData(QMediaMetaData.ThumbnailImage))
                pixmap = pixmap.scaled(200, 200)
                self.ui.track_cover_art.setPixmap(pixmap)
            else:
                self.ui.track_cover_art.clear()

    # Method for clicking a track and play
    def _itemclick(self):
        self.playlist.setCurrentIndex(self.ui.tracklist.currentRow())
        self.player.play()
        self.temp_icon.addPixmap(QtGui.QPixmap(":/icons /pause.png"), QIcon.Normal, QIcon.Off)
        self.ui.play_button.setIcon(self.temp_icon)
        self.playlist.setCurrentIndex(self.ui.tracklist.currentRow())
        self.player.play()

    # Method for adding tracks to the playlist and musiclist # PS : COME BACK LATER FOR CURRENT DIRECTORY PROBLEM
    def _files(self):
        directory = f"{os.getcwd()}\\music"
        files = os.listdir(directory)
        for file in files:
            file_name, file_ext = os.path.splitext(file)
            if file_ext == '.mp3':
                self.playlist.addMedia(QMediaContent(self.url.fromLocalFile(f"{directory}\\{file}")))
                try:
                    track = MP3(file)
                    self.ui.tracklist.addItem(str(track['TIT2']))
                except:
                    track = self._truncate(file.rpartition('/')[2].rpartition('.')[0])
                    self.ui.tracklist.addItem(track)
        self.ui.tracklist.setCurrentRow(0)
        self.playlist.setCurrentIndex(0)

    # Methods for the control buttons
    def _prev(self):
        if self.playlist.previousIndex() == -1:
            self.playlist.setCurrentIndex(self.playlist.mediaCount() - 1)
        else:
            self.playlist.previous()

    def _next(self):
        self.playlist.next()
        if self.playlist.currentIndex() == -1:
            self.playlist.setCurrentIndex(0)
            self.player.play()

    def _state(self):
        if self.playlist.mediaCount() > 0:
            if self.player.state() != QMediaPlayer.PlayingState:
                self.temp_icon.addPixmap(QtGui.QPixmap(":/icons /pause.png"), QIcon.Normal, QIcon.Off)
                self.ui.play_button.setIcon(self.temp_icon)
                self.playlist.setCurrentIndex(self.ui.tracklist.currentRow())
                self.player.play()
            else:
                self.temp_icon.addPixmap(QtGui.QPixmap(":/icons /play.png"), QIcon.Normal, QIcon.Off)
                self.ui.play_button.setIcon(self.temp_icon)
                self.player.pause()
        else:
            pass

    # Method for updating the listbox when the playlist updates
    def update(self):
        self.ui.tracklist.setCurrentRow(self.playlist.currentIndex())
        if self.playlist.currentIndex() < 0:
            self.ui.tracklist.setCurrentRow(0)
            self.playlist.setCurrentIndex(0)
