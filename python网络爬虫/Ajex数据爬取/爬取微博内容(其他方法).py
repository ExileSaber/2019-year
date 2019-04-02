import urllib.error
import urllib.request
import urllib.parse
import urllib
import json
import pandas as pd
import time
import random
import re
from datetime import datetime
from datetime import timedelta
from lxml import etree

class getWeiboContent():
    """
    微博内容爬取：
    mid
    time
    app_source
    content
    url
    others(repost, like, comment)
    is_repost
    rootmid
    rootname
    rootuid
    rooturl
    """
    def __init__(self, uid, begin_date=None, begin_page=1, interval=None, flag=True):
        self.uid = uid  # 微博用户ID
        self.begin_page = begin_page  # 起始页
        self.interval = interval  # 需要爬取的页数，默认为None
        self.begin_date = begin_date  # 爬取的微博的起始发布日期，默认为None
        self.flag = flag

    # 初始化url
    def getBeginURL(self):
        begin_url = 'https://weibo.com/p/aj/v6/mblog/mbloglist?ajwvr=6&domain=100505&is_all=1&id=100505'+str(self.uid)+\
                    '&script_uri=/u/1956890840&domain_op=100505&page='
        return begin_url

    # 设置加载页url，并获取html内容
    def getHTML(self,page_num,extend_part = ''):
        url = self.getBeginURL()+str(page_num)+extend_part
        print(url)
        data = urllib.request.urlopen(url).read().decode('utf-8')
        html = json.loads(data)['data']
        return html

    # 爬取每条微博的内容，输出字典
    def getContent(self,node):
        dic = {}
        dic['mid'] = node.xpath('./@mid')[0]
        print('mid:'+dic['mid'])
        dic['time'] = node.xpath('.//div[@class="WB_from S_txt2"]/a[1]/@title')[0]
        app_source = node.xpath('.//div[@class="WB_from S_txt2"]/a[2]/text()')
        if len(app_source) !=0 :  # 部分微博不显示客户端信息
            dic['app_source'] = app_source[0]
        content = node.xpath('./*/*/div[@class="WB_text W_f14"]')[0].xpath('string(.)')
        dic['content'] = re.compile('\n\s*(.*)').findall(content)[0]
        others = node.xpath('.//ul[@class="WB_row_line WB_row_r4 clearfix S_line2"]//span[@class="line S_line1"]/span/em[2]/text()')
        dic['repost_num'] = others[1]
        dic['comment_num'] = others[2]
        dic['like_num'] = others[3]
        detail_info = node.xpath('./div[@class="WB_feed_handle"]/div/ul/li[2]/a/@action-data')[0]
        dic['url'] = re.compile('&url=(.*?)&').findall(detail_info)[0]
        rootmid = node.xpath('./@omid')
        # 判断是否存在转发微博
        if len(rootmid) != 0:
            dic['is_repost'] = 1
            dic['rootmid'] = rootmid[0]
            weibo_expend = node.xpath('./*/*/div[@class="WB_feed_expand"]')[0]
            rootname = weibo_expend.xpath('./*/*/a[@class="W_fb S_txt1"]/@nick-name')
            # 判断原博是否被删除
            if len(rootname) != 0:
                dic['rootuid'] = re.compile('rootuid=(.*?)&').findall(detail_info)[0]
                dic['rootname'] = re.compile('rootname=(.*?)&').findall(detail_info)[0]
                dic['rooturl'] = re.compile('rooturl=(.*?)&').findall(detail_info)[0]

        return dic

    # 获取微博内容
    def getWeiboInfo(self):
        i = self.begin_page
        # 判断是否划定了爬取页数
        if self.interval is None:
            # 若未划定爬取页数，则设置自动翻页参数hasMore=True
            hasMore = True
            end_page = False
        else:
            # 若划定爬取页数，则爬取页数优先
            end_page = self.begin_page+self.interval
            hasMore = False
        # 初始化一个DataFrame用于存储数据
        weibo_df = pd.DataFrame()
        while (i <= end_page | hasMore) and self.flag:
            for x in range(3):
                if x == 0:  # 初始页面
                    extend_part = ''
                elif x == 1:  # 第一个加载页
                    b = x-1
                    extend_part = '&pre_page=' + str(i) + '&pagebar=' + str(b)
                elif x == 2:  # 第二个加载页
                    b = x-1
                    extend_part = '&pre_page=' + str(i) + '&pagebar=' + str(b)
                html = self.getHTML(i, extend_part)
                page = etree.HTML(html)
                if page is None:
                    break
                else:
                    detail = page.xpath('//div[@class="WB_cardwrap WB_feed_type S_bg2 WB_feed_like "]')
                # 判断用户是否发过微博
                if len(detail) == 0:
                    print('该用户并未发过微博')
                    break
                weibo = {}
                weibo['mid'] = []
                weibo['time'] = []
                weibo['content'] = []
                weibo['app_source'] = []
                weibo['url'] = []
                weibo['repost_num'] = []
                weibo['comment_num'] = []
                weibo['like_num'] = []
                weibo['is_repost'] = []
                weibo['rootmid'] = []
                weibo['rootname'] = []
                weibo['rootuid'] = []
                weibo['rooturl'] = []
                for w in detail:
                    all_info = self.getContent(w)
                    # 判断是否设置了微博的开始日期
                    if self.begin_date is None:
                        pass
                    else:
                        weibo_dt = datetime.strptime(all_info['time'], '%Y-%m-%d %H:%M').date()
                        begin_dt = datetime.strptime(self.begin_date, "%Y-%m-%d").date()
                        # 判断微博发布日期是否在开始日期之后
                        if begin_dt > weibo_dt:
                            # 当微博发布日期在开始日期之后时，停止爬取
                            self.flag = False
                            break
                    weibo['mid'].append(all_info.get('mid', ''))
                    weibo['time'].append(all_info.get('time', ''))
                    weibo['app_source'].append(all_info.get('app_source',''))
                    weibo['content'].append(all_info.get('content', ''))
                    weibo['url'].append(all_info.get('url', ''))
                    weibo['repost_num'].append(all_info.get('repost_num', ''))
                    weibo['comment_num'].append(all_info.get('comment_num', ''))
                    weibo['like_num'].append(all_info.get('like_num', ''))
                    weibo['is_repost'].append(all_info.get('is_repost', 0))
                    weibo['rootmid'].append(all_info.get('rootmid', ''))
                    weibo['rootname'].append(all_info.get('rootname', ''))
                    weibo['rootuid'].append(all_info.get('rootuid', ''))
                    weibo['rooturl'].append(all_info.get('rooturl', ''))
                weibo = pd.DataFrame(weibo)
                weibo['uid'] = self.uid
                weibo_df = weibo_df.append(weibo,ignore_index=True)
            # 提取下一页链接
            if page is None:
                break
            else:
                next_page = page.xpath('//a[@class="page next S_txt1 S_line1"]/@href')
            if len(next_page) == 0:  # 判断是否存在下一页
                self.flag = False
                print('已是最后一页')
            else:
                page_num = re.compile('page=(\d*)').findall(next_page[0])[0]
                i = int(page_num)
            time.sleep(random.randint(5, 10))  # 设置睡眠时间
        return weibo_df

if __name__=='__main__':
    uid = input('请输入uid：')
    begin_date = input('请输入日期，格式为xxxx-xx-xx：')
    begin_page = input('请输入开始页，默认为1：')
    getWeiboContent(uid, begin_date).getWeiboInfo()