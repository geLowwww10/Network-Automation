from webexteamssdk import WebexTeamsAPI

def list_rooms(webex_token):
    api = WebexTeamsAPI(access_token=webex_token)
    rooms = api.rooms.list()
    for room in rooms:
        print(f"Room ID: {room.id}, Room Name: {room.title}")

# Replace 'YOUR_ACCESS_TOKEN' with your actual WebEx Teams access token
webex_token = 'NDZkMTRjYWUtOTJiMy00MTNkLWFlOGYtNzY0OTYyZmZlYjVlMzVjMmM5ZWYtY2Ez_P0A1_1ad92174-dfe2-4740-b008-57218895946c'
list_rooms(webex_token)