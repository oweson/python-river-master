import requests

url = 'https://www.lagou.com/jobs/positionAjax.json?px=default&city=%E6%B7%B1%E5%9C%B3&district=%E5%8D%97%E5%B1%B1%E5%8C%BA&needAddtionalResult=false&isSchoolJob=1'

HEADERS = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/65.0.3325.181 Safari/537.36',
    'Referer': 'https://www.lagou.com/jobs/list_Python?px=default&gx=&isSchoolJob=1&city=%E6%B7%B1%E5%9C%B3&district=%E5%8D%97%E5%B1%B1%E5%8C%BA'
}

form_data = {'first': 'true',
             'pn': '1',
             'kd': 'python'}


def getJobs():
    res = requests.post(url=url, headers=HEADERS, data=form_data)
    result = res.json()
    jobs = result['content']['positionResult']['result']
    return jobs


for job in getJobs():
    # 这里演示，提取出公司地址+名称+公司优势+工资待遇
    print(job['district'] + ':' + job['companyFullName'] + ':' + job['positionAdvantage'] + ':' + job['salary'])
