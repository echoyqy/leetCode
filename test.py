# -*- coding:utf-8 -*-

import shutil
import os


def find_test_file(srcDir, desDir, name):
    srcPath = os.path.join(srcDir, name + '.csv')
    desPath = os.path.join(desDir, name + '.csv')
    if os.path.exists(srcPath):
        shutil.copyfile(srcPath, desPath)
    else:
        print(srcPath, 'not exists')


def remove_file(videoDir, txtDir, saveDir):
    if not os.path.exists(saveDir):
        os.makedirs(saveDir)
    txts = os.listdir(txtDir)
    for txt in txts:
        videoName = txt.split('.')[0]
        srcVideo = os.path.join(videoDir, videoName + '.mp4')
        desVideo = os.path.join(saveDir, videoName + '.mp4')
        if os.path.exists(srcVideo):
            shutil.copyfile(srcVideo, desVideo)


if __name__ == '__main__':
    remove_file(videoDir='D:/inhand/video', txtDir='D:/inhand/txt', saveDir='D:/inhand/video2')

    skus = ['农夫山泉',
            '百事可乐（罐）',
            '达利园青梅绿茶500ml',
            '百事可乐500ml',
            '统一阿萨姆奶茶500ml',
            '农夫山泉茶派组图500ml',
            '可口可乐330ml',
            '三得利利趣拿铁咖啡饮料',
            '康师傅水蜜桃（罐装）',
            '脉动青柠600ml',
            '康师傅冰红茶500ml',
            '元气森林白桃无糖苏打气泡',
            '康师傅喝开水',
            '美汁源果粒橙',
            '粤丰荔枝果',
            '旺仔牛奶罐装245ml',
            '可口可乐瓶装500ml',
            '娃哈哈AD钙奶',
            '红牛维生素功能饮料',
            '康师傅茉莉蜜茶500ml',
            ]
    # srcDir = r'D:\yqy\project\Inhand\数据\goodsVideoUrl'
    # desDir = r'D:\yqy\project\Inhand\数据\test20'
    # for sku in skus:
    #     find_test_file(srcDir, desDir,sku)
