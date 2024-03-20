import json
from pymongo import MongoClient
from bson import ObjectId

with open('/Users/harsh/VS Code Codes/Python Projects/Youtube_manager_mongo/secrets.json') as f:
    secrets = json.load(f)

mongo_connection = secrets['mongo_connection']

client: MongoClient = MongoClient(mongo_connection, tlsAllowInvalidCertificates=True)

db = client["ytmanager"]

video_collection = db["videos"]

print(video_collection)

def add_video(name, duration):
    video_collection.insert_one({"name": name, "duration": duration})

def list_videos():
    for video in video_collection.find():
        print(f"ID: {video['_id']}, Name: {video['name']}, Duration: {video['duration']}")

def update_video(id, name, duration):
    video_collection.update_one({"_id": ObjectId(id)}, {"$set": {"name": name, "duration": duration}})

def delete_video(id):
    video_collection.delete_one({"_id": ObjectId(id)})


def main():
    while True:
        print("1. List all videos")
        print("2. Add a new video")
        print("3. Update a video")
        print("4. Delete a video")
        print("5. Exit")
        choice = input("Enter your choice: ")
        if choice == "1":
            list_videos()

        elif choice == "2":
            name = input("Enter the name of the video: ")
            duration = input("Enter the duration of the video: ")
            add_video(name, duration)

        elif choice == "3":
            id = input("Enter the id of the video: ")
            name = input("Enter the new name of the video: ")
            duration = input("Enter the new duration of the video: ")
            update_video(id, name, duration)

        elif choice == "4":
            id = input("Enter the id of the video: ")
            delete_video(id)

        elif choice == "5":
            break
        else:
            print("Invalid choice")

if __name__ == "__main__":
    main()
