# amazonSpider_server_build_.py
1 > 环境
    python版本:
        python v3.10.9
    导入包:
        selenium v4.7.2
        getopt
        sys
        time
        os

2 > 说明
    a> 传参说明
        其他说明：
            以命令行的形式传参，默认接受两个参数，如果参数过少或者格式不正确都会报错
        参数格式：
            短格式:  "-g <giftcard> -p <pagesource>" 
            长格式:  "--giftcard=<giftcard> --pagesource=<pagesource>"

        参数说明： 
            -g/--giftcard     传入需要检测的优惠码，例如：ABCDEFG
            -p/--pagesource   传入需要测试的商品的详细链接，例如：https://www.amazon.com/dp/B0BG4BQDPC/ref=twister_B0BG4BK6PQ?_encoding=UTF8&psc=1
    
    b> 其他说明
        1 > 需要在源码中手动输入亚马逊账号信息，包括邮箱信息和登录密码。
        2 > 优惠码的检测结果：有效/无效 以 'true'/'false' 字符串的形式输出到输出流中

3 > 其他说明
    目前还是早期版本，我自己进行少量测试后是基本没有问题的，之后我会进行大规模测试并进行改进。另外程序对于抛出的异常没有进行处理，之后我会添加上去。