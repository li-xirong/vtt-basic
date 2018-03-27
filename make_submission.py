from __future__ import print_function

import os, sys
import logging
from constant import ROOT_PATH
from models import get_model
from utils import readVideoSet, readSentenceSet

logger = logging.getLogger(__file__)
logging.basicConfig(
        format="[%(asctime)s - %(filename)s:line %(lineno)s] %(message)s",
        datefmt='%d %b %H:%M:%S')
logger.setLevel(logging.INFO)

class MakeSubmission:
    def __init__(self, videoCollection, sentenceSet, modelName, rootpath=ROOT_PATH):
        self.rootpath = rootpath
        self.videoCollection = videoCollection
        self.sentenceSet = sentenceSet
        self.modelName = modelName
        self.scorer =  get_model(modelName)(videoCollection, sentenceSet)

    def get_res_file(self):
        resfile = os.path.join(self.rootpath, self.videoCollection, 'SimilarityIndex', self.videoCollection, self.sentenceSet, self.modelName, 'vid.scores.txt')
        return resfile
 
    def process(self, overwrite=0):
        resfile = self.get_res_file()
        if os.path.exists(resfile):
            if overwrite:
                logger.info('%s exists. overwrite', resfile)
            else:
                logger.info('%s exists. do nothing', resfile)
                return 0
        
        video_ids = readVideoSet(self.videoCollection, self.rootpath)
        sent_ids = readSentenceSet(self.videoCollection, self.sentenceSet, self.rootpath)
        logger.info('%d videos, %d sentences', len(video_ids), len(sent_ids))

        if not os.path.exists(os.path.split(resfile)[0]):
            os.makedirs(os.path.split(resfile)[0])

        fw = open(resfile, 'w')
        for video_id in video_ids:
            results = [(sent_id, self.scorer.score(video_id, sent_id)) for sent_id in sent_ids]
            results.sort(key=lambda v:v[1], reverse=True)
            fw.write('%s %s\n' % (video_id, ' '.join(['%s %g' % (x[0],x[1]) for x in results])))
        fw.close()
        return len(video_ids)

def main(argv=None):
    if argv is None:
        argv = sys.argv[1:]

    from optparse import OptionParser
    parser = OptionParser(usage="""Usage: %prog [options] videoCollection sentSet modelName""")
    parser.add_option("--overwrite", default=0, type="int", help="overwrite existing file (default=0)")
    parser.add_option("--rootpath", default=ROOT_PATH, type="string", help="rootpath (default: %s)" % ROOT_PATH)

    (options, args) = parser.parse_args(argv)
    if len(args) < 3:
        parser.print_help()
        return 1
   
    submit = MakeSubmission(args[0], args[1], args[2], rootpath=options.rootpath)
    submit.process(options.overwrite)

if __name__ == '__main__':
    main()

