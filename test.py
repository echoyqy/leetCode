# -*- coding:utf-8 -*-

import shutil
import os
import pandas as pd
import numpy as np


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


def find_videoName(x):
    return x.split('_')[0]


class Data():
    def __init__(self, srcDir, desDir, txtDir):
        self.srcDir = srcDir
        self.desDir = desDir
        self.txtDir = txtDir

    def del_img(self):
        if not os.path.exists(self.desDir):
            os.makedirs(self.desDir)
        imgs = os.listdir(self.srcDir)
        imgDf = self.get_dataFrame(imgs)
        self.del_mutilImg(imgDf)

    def get_dataFrame(self, imgs):
        imgDf = pd.DataFrame({'imgPath': imgs})
        imgDf['videoName'] = imgDf['imgPath'].map(find_videoName)
        return imgDf

    def del_mutilImg(self, imgDf):
        for name, group in imgDf.groupby("videoName"):
            chosenVideoPaths = self.get_chosenVideoPath(group)
            self.moveImg(chosenVideoPaths)

    def get_chosenVideoPath(self, group):
        group = group.reset_index(drop=True)
        indexs = np.arange(0, len(group), 5)
        return group.loc[indexs]['imgPath'].to_list()

    def moveImg(self, chosenVideoPaths):
        for path in chosenVideoPaths:
            srcPath = os.path.join(self.srcDir, path)
            desPath = os.path.join(self.desDir, path)
            if os.path.exists(srcPath):
                shutil.move(srcPath, desPath)

    def move_video(self):
        if not os.path.exists(self.desDir):
            os.makedirs(self.desDir)
        txtNames = os.listdir(self.txtDir)
        for txt in txtNames:
            print(txt)
            videoName = txt.split('.')[0] + '.mp4'
            srcVideo = os.path.join(self.srcDir, videoName)
            desVideo = os.path.join(self.desDir, videoName)
            if os.path.exists(srcVideo):
                shutil.move(srcVideo, desVideo)


if __name__ == '__main__':
    # data = Data(r'D:\inhand\cv\inhandMotYoloDataset2\images\train', r'D:\inhand\cv\inhandMotYoloDataset2\images\train2')
    # data.del_img()
    data = Data(srcDir=r'D:\inhand\cv\dataInhand\video', desDir=r'D:\inhand\cv\dataInhand\video2', txtDir=r'D:\inhand\cv\dataInhand\txt')
    data.move_video()
    # remove_file(videoDir='D:/inhand/video', txtDir='D:/inhand/txt', saveDir='D:/inhand/video2')
    #
    # skus = ['????????????',
    #         '?????????????????????',

    #         '?????????????????????500ml',
    #         '????????????500ml',
    #         '?????????????????????500ml',
    #         '????????????????????????500ml',
    #         '????????????330ml',
    #         '?????????????????????????????????',
    #         '??????????????????????????????',
    #         '????????????600ml',
    #         '??????????????????500ml',
    #         '????????????????????????????????????',
    #         '??????????????????',
    #         '??????????????????',
    #         '???????????????',
    #         '??????????????????245ml',
    #         '??????????????????500ml',
    #         '?????????AD??????',
    #         '???????????????????????????',
    #         '?????????????????????500ml',
    #         ]
    # srcDir = r'D:\yqy\project\Inhand\??????\goodsVideoUrl'
    # desDir = r'D:\yqy\project\Inhand\??????\test20'
    # for sku in skus:
    #     find_test_file(srcDir, desDir,sku)
