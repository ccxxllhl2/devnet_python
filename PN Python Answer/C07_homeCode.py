########################
### YESLAB 网工Python ###
########################
import unitTest
from funSystem import funWebex

api = "webex/v1/rooms"
room_names = ["网络开发小组01", "网络开发小组02", "运维小组01", "运维小组02", "临时会议组"]
# 此脚本需要完成以下任务：
# 你需要在这个脚本中编写一个函数，利用funWebex中的功能，建立5个Webex房间
# 建立房间需要的api和房间名称已经在上面给出了
# -------------------作业区域开始------------------------
# TODO: 编写函数一次性建立5个Webex房间


def create_rooms():
    for room in room_names:
        funWebex.post_room(api, room)

create_rooms()


# -------------------作业区域结束------------------------


if __name__ == "__main__":
    unitTest.check_webex_rooms(funWebex.rooms)
    unitTest.output_error()
