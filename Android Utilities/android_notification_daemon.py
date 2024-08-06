from plyer import notification


def receive_notification(title, message):
    notification.notify(
        title=title,
        message=message,
        app_icon=None,  # You can set a custom icon if needed
        timeout=10,  # The notification will disappear after 10 seconds
    )


if __name__ == "__main__":
    # Example usage
    receive_notification("Notification Title", "This is a test notification.")

# Install Join on Android:

#     Install the "Join" app on your Android device from the Google Play Store.
#     Follow the setup instructions to link your Android device with your Google account.

# Install plyer on Windows:

#     Install the plyer library on your Windows machine using the following command in your terminal or command prompt:

# add functionality for android to linux
