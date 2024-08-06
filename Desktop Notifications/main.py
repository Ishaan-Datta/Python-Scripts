# desktop notifier w/ tkinter or fast disappearing emojis for reminders periodically
# how did league add that logo onto screen without window, copy it
# stretch reminders, rolling, notifies you and starts next timer after you have confirmed you have finished the task
# posture, water
# desktop reminders icon fades out
# remidners for eat and exercise

# 30 minute looping timer for drying
# test

from PyQt5.QtCore import Qt, QTimer, QCoreApplication
from PyQt5.QtGui import QPixmap, QImageReader
from PyQt5.QtWidgets import QApplication, QLabel, QVBoxLayout, QWidget, QDesktopWidget
import sys


class TransparentWindow(QWidget):
    def __init__(self, image_path, opacity=1.0):
        super().__init__()

        # Set the window attributes for transparency and no title bar
        self.setWindowFlags(
            Qt.Window | Qt.FramelessWindowHint | Qt.WindowStaysOnTopHint
        )
        self.setAttribute(Qt.WA_TranslucentBackground, True)

        # Load the image
        pixmap = QPixmap(image_path)

        # Set up the label for the image
        label = QLabel(self)
        label.setPixmap(pixmap)

        # Set up the layout
        layout = QVBoxLayout(self)
        layout.addWidget(label)

        # Apply the layout
        self.setLayout(layout)

        # Calculate the center coordinates
        screen_geometry = QDesktopWidget().screenGeometry()
        window_width = pixmap.width()
        window_height = pixmap.height()
        x = (screen_geometry.width() - window_width) // 2
        y = (screen_geometry.height() - window_height) // 2

        # Show the window at the center
        self.setGeometry(x, y, window_width, window_height)

        # Set the window opacity
        self.setWindowOpacity(opacity)

        # Show the window
        self.show()

        # Close the window after 2 seconds
        QTimer.singleShot(2000, self.close)


if __name__ == "__main__":
    app = QApplication(sys.argv)

    # Replace with the path to your custom image
    image_path = "C:/Users/ishaa/OneDrive - UBC/Coding/Python/Projects/New/image.png"

    # Specify the opacity value (between 0.0 and 1.0)
    opacity_value = 0.7

    window = TransparentWindow(image_path, opacity_value)

    sys.exit(app.exec_())

# desktop reminders:
# every 10 minutes water break
# hourly chime
# popup reminder should pause 1 second then if there is keyboard/mouse input then disappear
# reminders for vaseline and etc. timed
# mewing
# requires .png files
# interface with gcal for reminders related to those tasks
# gui for confirming task is finished?
# 2 types of reminders: visual or confirmation based before continuing work
