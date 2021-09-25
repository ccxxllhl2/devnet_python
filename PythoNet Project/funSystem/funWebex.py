api_room = "webex/v1/rooms"
rooms = {}
room_id = 1001


def post_room(api, room_name):
    global room_id
    if api == api_room:
        print("恭喜您已经建立Webex房间！")
        rooms[str(room_id)] = room_name
        room_id += 1


def get_rooms():
    for room in rooms:
        print("{} : {}".format(room, rooms[room]))