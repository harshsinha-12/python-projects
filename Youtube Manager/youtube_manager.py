import json

def load_data():
    try:
        with open("youtube.txt", "r") as file:
            return json.load(file)
    except FileNotFoundError:
        return []
    
def save_data_helper(videos):
    with open("youtube.txt", "w") as file:
        json.dump(videos, file)

def list_all_videos(videos):
    for index, video in enumerate(videos, start = 1):
        print(f"{index}. {video['title']} ({video['duration']} min)")

def add_video(videos):
    name = input("Enter the title of the video: ")
    duration = input("Enter the duration of the video: ")
    videos.append({"title": name, "duration": duration})
    save_data_helper(videos)

def update_video(videos):
    pass

def delete_video(videos):
    pass

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

