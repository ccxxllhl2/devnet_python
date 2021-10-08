# 类的定义
class VPN_MONITOR:
    def __init__(self, area):
        self.area = area
        print("【{}】的VPN监视器已建立！".format(self.area))
        self.site2site_m()
        self.ipsec_m()
        self.DM_m()

    def site2site_m(self):
        print("正在监控【{}】的 siteTOsite VPN".format(self.area))

    def ipsec_m(self):
        print("正在监控【{}】的 ipsec VPN".format(self.area))

    def DM_m(self):
        print("正在监控【{}】的 DM-VPN".format(self.area))

# 类的使用
vpn_m_1 = VPN_MONITOR("西安-北京")
vpn_m_2 = VPN_MONITOR("上海-广州")
vpn_m_3 = VPN_MONITOR("南京-深圳")