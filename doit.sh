
rootpath=$HOME/VisualSearch
videoCollection=tv2016test
sentSet=setA
modelName=random
overwrite=1

videosetfile=$rootpath/$videoCollection/VideoSets/$videoCollection.txt
if [ ! -f $videosetfile ]; then
    echo "video set file $videosetfile not found. quit"
    exit
fi

python make_submission.py $videoCollection $sentSet $modelName --rootpath $rootpath --overwrite $overwrite

python eval.py $videoCollection $sentSet $modelName --rootpath $rootpath

