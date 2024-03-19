import json
import os


def load_data():
    if os.path.exists('data.json') and os.path.getsize('data.json') > 0:
        with open('data.json', 'r') as file:
            return json.load(file)
    else:
        return []
    
def save_data_helper(videos):
    with open("youtube.txt", "w") as file:
        json.dump(videos, file)

def list_all_videos(videos):
    print("\n")
    print("*" * 70)
    for index, video in enumerate(videos, start = 1):
        print(f"{index}. {video['title']} ({video['duration']} min)")

def add_video(videos):
    name = input("Enter the title of the video: ")
    duration = input("Enter the duration of the video: ")
    videos.append({"title": name, "duration": duration})
    save_data_helper(videos)

def update_video(videos):
    list_all_videos(videos)
    index = int(input("Enter the index of the video you want to update: "))
    if 1 <= index <= len(videos):
        name = input("Enter the new title of the video: ")
        duration = input("Enter the new duration of the video: ")
        videos[index - 1] = {"title": name, "duration": duration}
        save_data_helper(videos)
    else:
        print("Invalid index")

def delete_video(videos):
    list_all_videos(videos)
    index = int(input("Enter the index of the video you want to delete: "))
    if 1 <= index <= len(videos):
        del videos[index - 1]
        save_data_helper(videos)
    else:
        print("Invalid index")

def main():
    pass

    videos = load_data()

    while True:
        print("\n Youtube Manager | Choose an option:")
        print("1. List a Youtube video")  
        print("2. Add a Youtube video to favourites")
        print("3. Update a Youtube video")
        print("4. Delete a Youtube video")
        print("5. Exit the Application")
        choice = input("Enter your choice: ")
        print(videos)

        match choice:
            case "1":
                list_all_videos(videos)
            case "2":
                add_video(videos)
            case "3":
                update_video(videos)
            case "4":   
                delete_video(videos)
            case "5":
                break
            case _:
                print("Invalid choice. Please try again")

if __name__ == "__main__":
    main()

