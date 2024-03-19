

while True:
    print("\n Youtube Manager | Choose an option:")
    print("1. List a Youtube video")  
    print("2. Add a Youtube video to favourites")
    print("3. Update a Youtube video")
    print("4. Delete a Youtube video")
    print("5. Exit the Application")
    choice = input("Enter your choice: ")
    match choice:
        case "1":
            list_all_videos(video)
        

