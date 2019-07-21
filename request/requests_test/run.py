'''
生成测试报告：
首先创建文件夹reports和testcase
下载BSTestRunner
创建run.py模块
'''

import unittest
from BSTestRunner import BSTestRunner
import time

#指定测试用例和测试报告的路径
test_dir='./test_case'
report_dir='./reports'

#加载测试用例
discover=unittest.defaultTestLoader.discover(test_dir,pattern='test_weather.py')

#定义报告的文件格式
now=time.strftime('%Y-%m-%d %H_%M_%S')
report_name=report_dir+'/'+now+'test_report.html'

#运行用例并生成测试报告
with open(report_name,'wb') as f:
    runner=BSTestRunner(stream=f,title='Weather API Test Report',description='China city weather report')
    runner.run(discover)