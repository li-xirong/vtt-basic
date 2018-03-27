from __future__ import print_function

import os
from constant import ROOT_PATH

def readVideoSet(videoCollection, rootpath=ROOT_PATH):
    video_set_file = os.path.join(rootpath, videoCollection, 'VideoSets', videoCollection+'.txt')
    videoSets = map(str.strip, open(video_set_file).readlines())
    assert(len(videoSets) == len(set(videoSets))), 'the video ids are not unique'
    return videoSets

def readSentenceSet(videoCollection, sentenceSet, rootpath=ROOT_PATH):
    sent_set_file = os.path.join(rootpath, videoCollection, 'TextData', videoCollection+'.'+sentenceSet+'.txt')
    sentSets = [x.split()[0] for x in open(sent_set_file).readlines()]
    assert(len(sentSets) == len(set(sentSets))), 'the sentence ids are not unique'
    return sentSets

if __name__ == '__main__':
    rootpath = os.path.join(os.environ['HOME'], 'VisualSearch1')
    
    for videoCollection in 'tv2016train tv2016test'.split():
        for sentSetName in 'setA setB'.split():
            videoSet = readVideoSet(videoCollection, rootpath)
            sentSet = readSentenceSet(videoCollection, sentSetName, rootpath)
            print (videoCollection, sentSetName, len(videoSet), len(sentSet))


