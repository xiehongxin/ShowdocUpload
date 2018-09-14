# coding: utf-8
# @author: hongxin
# @date: 18-6-2


"""
参考文档： https://www.showdoc.cc/page/102098
"""


from requests import post


def check_article_suffix(article_path):
    """
    检查文件格式是否为md
    :param article_path:
    :return:
    """
    if article_path.split('.')[1] == 'md':
        return True
    else:
        return None


def get_article_title(article_path):
    path = article_path.split('.')[0]
    title = path.split('/')[-1]
    return title


def get_article_content(article_abs_path):
    with open(article_abs_path, 'r') as read_article:
        article_content = ''.join(read_article.readlines())
        if '---\n' in article_content:
            article_text = article_content.split('---')[2]  # 正文
            article_head = article_content.split('---')[1]  # 题头
            date = article_head.split('\n')[2]
            date = date.replace('date', '__date__')
            all_article_content = date + article_text
        else:
            all_article_content = article_content
        return all_article_content


def generate_article(url, article_data):
    request = post(url=url, data=article_data)
    return request.text


def import_article_to_showdoc(api_url, api_key, api_token, article_dir, article_dir_sub, article_path):
    """
    :param api_url:  上传url
    :param api_key: 上传的key
    :param api_token: 上传的token
    :param article_dir:  showdoc 一级目录
    :param article_dir_sub: showdoc 二级目录
    :param article_path: markdown路径
    :return:
    """
    if (api_url and api_key and api_token and article_dir and article_path) is not None:
        if check_article_suffix(article_path):
            # 一级，二级目录
            cat_name, cat_name_sub = article_dir, article_dir_sub
            # 获取文章标题
            page_title = get_article_title(article_path)
            # 获取文章内容
            page_content = get_article_content(article_path)
            # 文章排序
            s_number = '99'
            # post数据
            post_datas = {'api_key': api_key, 'api_token': api_token, 'cat_name': cat_name,
                          'cat_name_sub': cat_name_sub,
                          'page_title': page_title, 'page_content': str(page_content), 's_number': s_number}
            # post 请求
            try:
                response_text = generate_article(api_url, post_datas)
                response_text = eval(response_text)
                page_id = str(response_text['data']['page_id'])
                print(page_id)
                return True
            except Exception:
                return None
        else:
            print('article suffix is not md')
            return None
    else:
        print('article path is not exist')
        return None

if __name__ == '__main__':
    # 测试
    url = 'https://www.showdoc.cc/server/api/item/updateByApi'
    key = 'xxx'
    token = 'xxxx'
    article = 'Other'
    article_sub = ''
    path = '/run/xxxx/Linux-1-Yum源介绍.md'
    import_article_to_showdoc(url, key, token, article, article_sub, path)




