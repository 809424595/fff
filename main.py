# #_*_conding:utf-8_*_
# #@Time    :2020/2/1815:36
# #@Author  :xiaodong.wu
# #@Email   :2586089125@qq.com

#pytest启动文件
import  pytest

if __name__ == '__main__':
    # pytest.main()         #执行pytest框架下的所有测试用例
    pytest.main(["-m","smoke",  #只执行带有smoke标记的用例（只支持同时执行一种标记的操作）
                 "--reruns","2","--reruns-delay","5",    #失败重运行
                 "--junitxml=Outputs/reports/result.xml",#生成XML格式的测试报告
                 "--html=Outputs/reports/result.html"])    #生成html格式的测试报告




#用例筛选（选择性的执行用例）
    #（1）创建配置文件pytest.ini（文件名固定）
    #（2）在文件中设置标签名称 [pytest]
    #                      makers =
    #                              标记名称
    #                              标记名称
    #（3）打标记 （@pytest.mark.标记名称）
    #           一个用例可以打多个标记


#失败重运行机制
    #安装插件（pip install pytest-rerunfailures）
    #设置重运行参数  pytest --reruns 重试次数
    #             pytest --reruns 2 --reruns-delay 10 (失败可以重运行两次，每次运行的间隔为10秒)

#生成测试报告
