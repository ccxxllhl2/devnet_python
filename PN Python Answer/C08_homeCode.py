########################
### YESLAB 网工Python ###
########################

# 最终任务
# TODO: 完成类log_robot的编写
import re
class log_robot():
    def __init__(self,hostname):
        self.hostname= hostname
    def get_info(self):
        print("-"*40)
        with open("data/huaweiFull.log") as if_file:
            self.logdate = if_file.read()
    def get_ver_info(self):
        result = re.findall("version.*", self.logdate)
        print(result)
        ver_info =" ".join(result)
        with open("data/new_log.log", "w") as flie:
            flie.write(ver_info)
    def get_config_info(self):
        result = re.findall("config.*", self.logdate)
        print(result)
        config_info =" ".join(result)
        with open("data/new_log.log", "a") as flie:
            flie.write(config_info)
    def get_cpu_info(self):
        result =re.findall("CPU.*",self.logdate)
        print(result)
        cpu_info =" ".join(result)
        with open("data/new_log.log", "a") as flie:
            flie.write(cpu_info)


    def get_mem_info(self):
        result = re.findall("memory.*", self.logdate)
        print(result)
        mem_info =" ".join(result)
        with open("data/new_log.log", "a") as flie:
            flie.write(mem_info)

switch=log_robot("BD-H3C5110-11")
switch.get_info()
switch.get_ver_info()
switch.get_config_info()
switch.get_cpu_info()
switch.get_mem_info()

