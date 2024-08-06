# insta/tiktok automation w/ pyautogui and bot delay (watch video)
# database for insta and tikotk to find removed/banned users and inactive users from post history
# downloads naming
# instaloader module
# Check accounts date followed, date of saved posts, ratio of saved posts to determine who to stop following


import instaloader
import os
import tkinter as tk
from tkinter import filedialog
import zipfile


def download_instagram_posts(username, output_folder):
    # Create an instance of Instaloader
    loader = instaloader.Instaloader()

    # Download all posts from the specified Instagram profile
    loader.download_profile(username, profile_pic_only=False)

    # Get the directory where the posts are saved
    profile_dir = os.path.join(os.getcwd(), username)

    # Create a ZIP file to export the downloaded posts
    zip_filename = os.path.join(output_folder, f"{username}_posts.zip")
    with zipfile.ZipFile(zip_filename, "w") as zipf:
        # Iterate over the downloaded posts directory and add each file to the ZIP
        for foldername, _, filenames in os.walk(profile_dir):
            for filename in filenames:
                filepath = os.path.join(foldername, filename)
                zipf.write(filepath, os.path.basename(filepath))

    print(f"All posts downloaded and exported as {zip_filename}")


def select_output_folder():
    # Use tkinter's filedialog to select the output folder
    root = tk.Tk()
    root.withdraw()
    output_folder = filedialog.askdirectory()
    return output_folder


def create_gui():
    # Create a simple GUI window
    window = tk.Tk()
    window.title("Instagram Post Downloader")

    # Function to handle button click and start downloading posts
    def download_posts():
        username = username_entry.get()
        output_folder = select_output_folder()

        if username and output_folder:
            download_instagram_posts(username, output_folder)
            window.destroy()
        else:
            tk.messagebox.showerror(
                "Error", "Please enter a username and select an output folder."
            )

    # Label and entry for Instagram username
    username_label = tk.Label(window, text="Instagram Username/URL:")
    username_label.pack()
    username_entry = tk.Entry(window)
    username_entry.pack()

    # Button to select output folder and start downloading
    download_button = tk.Button(window, text="Download", command=download_posts)
    download_button.pack()

    window.mainloop()


# Call the function to create the GUI
create_gui()
