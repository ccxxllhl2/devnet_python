class VPN_MONITOR:
    count = 0
    def __init__(self):
        VPN_MONITOR.count += 1
        self._score = 0
        self.anno()

    @staticmethod
    def anno():
        print("目前已有{}个VPN链路建立了监控机制！".format(VPN_MONITOR.count))

    @classmethod
    def reset_count(cls):
        cls.count = 0
        cls.anno()

    @property
    def score(self):
        return self._score

    @score.setter
    def score(self, value):
        if not isinstance(value, int):
            print("分数必须是整数！")
        elif value < 0 or value > 100:
            print("分数必须在0-100之间")
        else:
            self._score = value

monitor1 = VPN_MONITOR()
monitor2 = VPN_MONITOR()
monitor3 = VPN_MONITOR()
VPN_MONITOR.reset_count()
monitor1.score = "哈哈哈"
monitor2.score = 1000
monitor3.score = 55
print(monitor1.score)
print(monitor2.score)
print(monitor3.score)