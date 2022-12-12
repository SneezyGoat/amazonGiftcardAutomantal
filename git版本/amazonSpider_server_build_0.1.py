from selenium import webdriver
import getopt
import sys
import time
import os

def mkdir(path):
	# 去除首位空格
    path=path.strip()
    # 去除尾部 \ 符号
    path=path.rstrip("\\")
    # 判断路径是否存在
    isExists=os.path.exists(path)

    if not isExists:
        # 创建目录操作函数
        os.makedirs(path)
        return True
    else:
        return False

def init():
	opts,args=getopt.getopt(sys.argv[1:],'-g:-p:',['giftcard=','pagesource='])
	giftcard=''
	pagesource=''
	for opt,value in opts:
		if opt in ('-g','--giftcard'):
			giftcard=value
		if opt in ('-p','--pagesource'):
			pagesource=value
	print(opts)
	print(giftcard + pagesource)
	spider=amazonSpider(giftcard,pagesource)
	return spider

class amazonSpider(object):
	def __init__(self,giftcard,pagesource):
		self.keyWord=['success','成功']
		#手动输入亚马逊账号信息，否则无法成功测试优惠码
		self.account={'email':'','password':''}
		self.browserInfo={'browser_path':'','log_path':''}
		self.loginPage='https://www.amazon.com/gp/css/order-history?ref_=nav_orders_first'
		self.giftcard=giftcard
		self.pagesource=pagesource

	#设置浏览器参数,默认chrome浏览器
	def set_options(self):
		options=webdriver.ChromeOptions()
		options.add_argument('--headless')                                                 #开启无头浏览器
	#   options.add_argument('user-agent=""')                                              #设置UA
		options.add_argument('--disable-gpu')                                              #禁用GPU
		options.add_argument('blink-settings=imagesEnabled=false')                         #开启无图模式
		options.add_argument('--disable-javascript')                                       #禁用JS
		options.add_experimental_option('excludeSwitches',['enable-logging'])              #隐藏所有报错
	#	options.add_argument('--ignore-certificate-errors')                                #隐藏证书错误提示
	#	options.add_argument('--ignore-ssl-errors')                                        #隐藏SSL错误提示
		return options

	#用于防止页面加载时间过长，设置加载超时后停止后续加载
	def get(self,browser,url):
		browser.set_page_load_timeout(10)
		try:
			browser.get(url)
		except Exception:
			browser.execute_script("window.stop()")
		browser.set_page_load_timeout(1000)

	#登录账号
	def login(self,browser):
		browser.get(self.loginPage)
		browser.find_element("name","email").send_keys(self.account['email'])
		browser.find_element("class name","a-button-input").click()
		browser.find_element("name","password").send_keys(self.account['password'])
		browser.find_element("id","signInSubmit").click()

	def has_keyWord(self,text):
		#将礼品码的激活信息放入到输出流中
		#print(text)
		for keyword in self.keyWord:
			if text.find(keyword)>=0:
				return True

	#测试礼品码
	def test_giftcard(self,browser,giftcard):
		browser.find_element("name","ppw-claimCode").send_keys(giftcard)
		browser.find_element("name","ppw-claimCodeApplyPressed").click()
		time.sleep(5)
		alertInfo=browser.find_elements("xpath","//p")[1].text
		if self.has_keyWord(alertInfo):
			#激活码有效
			print('true')
		else:
			#激活码无效
			print('false')

	def run(self):
		options=self.set_options()
		driver=webdriver.Chrome(options=options)
		self.login(driver)
		driver.get('https://www.baidu.com/')
		self.get(driver,self.pagesource)
		#driver.get(self.goodsPage)
		driver.find_element("name","submit.buy-now").click()
		self.test_giftcard(driver,self.giftcard):
		driver.quit()

if __name__=='__main__':
	print('hello, program starting')
	try:
		spider=init()
		spider.run()
	except Exception as e:
		print(e)
	#else:
	#	input('输入任意内容退出：')