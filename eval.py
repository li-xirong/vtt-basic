import os, sys
import numpy as np
import logging

from constant import ROOT_PATH

logger = logging.getLogger(__file__)
logging.basicConfig(
        format="[%(asctime)s - %(filename)s:line %(lineno)s] %(message)s",
        datefmt='%d %b %H:%M:%S')
logger.setLevel(logging.INFO)

def compute_mir(vid_score_file):
    matched_rank = []

    for line in open(vid_score_file):
        elems = line.strip().split()
        video_id = elems[0]
        del elems[0]

        sent_ids = elems[::2]
        rank = len(sent_ids)+1
        for i in range(len(sent_ids)):
            if sent_ids[i].split('#')[0] == video_id:
                rank = i+1
                break
        assert(rank <= len(sent_ids)), video_id + " does not have a correct sentence"
        matched_rank.append((video_id, rank))

    mir = np.mean([1.0/x[1] for x in matched_rank])
    return mir, matched_rank


def process(options, testCollection, sentSet, runName):
    rootpath = options.rootpath
    scorefile = os.path.join(rootpath, testCollection, 'SimilarityIndex', testCollection, sentSet, runName, 'vid.scores.txt')
    if not os.path.exists(scorefile):
        logger.info("%s not exists", scorefile)
        return -1
    logger.info('compute mean inverted rank for %s', scorefile)
    mir, matched_rank = compute_mir(scorefile)
    logger.info('MIR: %.3f', mir)
    resfile = scorefile + '.rank'
    open(resfile, 'w').write('\n'.join(['%s %g' % (x[0],x[1]) for x in matched_rank]))
    logger.info('rank saved to %s', resfile)
    return 0

def main(argv=None):
    if argv is None:
        argv = sys.argv[1:]

    from optparse import OptionParser
    parser = OptionParser(usage="""Usage: %prog [options] videoCollection sentSet runName""")
    parser.add_option("--rootpath", default=ROOT_PATH, type="string", help="root path (default: %s)"%ROOT_PATH)

    (options, args) = parser.parse_args(argv)
    if len(args) < 3:
        parser.print_help()
        return 1

    return process(options, args[0], args[1], args[2])

if __name__ == '__main__':
    sys.exit(main())

