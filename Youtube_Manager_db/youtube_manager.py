import sqlite3

connection = sqlite3.connect('youtube_manager.db')

cursor = connection.cursor()

cursor.execute('''
    CREATE TABLE IF NOT EXISTS videos(
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        title TEXT NOT NULL,
        duration INTEGER NOT NULL
    )
''')

def list_all_videos():
    cursor.execute('SELECT * FROM videos')
    for row in cursor.fetchall():
        print(row)

def add_video(title, duration):
    cursor.execute('INSERT INTO videos (title, duration) VALUES(?, ?)', (title, duration))
    connection.commit()

def update_video(video_id, title, duration):
    cursor.execute('UPDATE videos SET title = ?, duration = ? WHERE id = ?', (title, duration, video_id))
    connection.commit()

def delete_video(video_id):
    cursor.execute('DELETE FROM videos WHERE id = ?', (video_id,))
    connection.commit()

def main():
    while True:
        print("\n Youtube Manager | Choose an option:")
        print("1. List a Youtube video")
        print("2. Add a Youtube video to favourites")
        print("3. Update a Youtube video")
        print("4. Delete a Youtube video")
        print("5. Exit the Application")
        choice = input("Enter your choice: ")

        if choice == "1":
            list_all_videos()

        elif choice == "2":
            title = input("Enter the title of the video: ")
            duration = input("Enter the duration of the video: ")
            add_video(title, duration)

        elif choice == "3":
            video_id = input("Enter the id of the video you want to update: ")
            title = input("Enter the new title of the video: ")
            duration = input("Enter the new duration of the video: ")
            update_video(video_id, title, duration)

        elif choice == "4":
            video_id = input("Enter the id of the video you want to delete: ")
            delete_video(video_id)

        elif choice == "5":
            break

        else:
            print("Invalid choice")

    connection.close()

if __name__ == "__main__":
    main()