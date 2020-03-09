#_*_conding:utf-8_*_
#@Time    :2020/2/1812:03
#@Author  :xiaodong.wu
#@Email   :2586089125@qq.com
import os

#项目目录
base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

testdatas_dir = os.path.join(base_dir,"TestDatas")

testcases_dir =  os.path.join(base_dir,"TestCases")

htmlreport_dir =  os.path.join(base_dir,"Outputs/reports")

logs_dir =  os.path.join(base_dir,"Outputs/logs")

screenshot_dir = os.path.join(base_dir,"Outputs/screenshots")

libs = os.path.join(base_dir,"Libs")