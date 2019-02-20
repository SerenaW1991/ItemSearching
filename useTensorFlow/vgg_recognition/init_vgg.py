import sys
sys.path.append("/Users/tengwang/Documents/GitHub/ItemSearching/UseTensorFlow/models/research/slim/")


from datasets import dataset_utils
url = "http://download.tensorflow.org/models/vgg_16_2016_08_28.tar.gz"

# Specify where you want to download the model to
checkpoints_dir = "/Users/tengwang/Documents/GitHub/ItemSearching/UseTensorFlow/download_models"

if not tf.gfile.Exists(checkpoints_dir):
    tf.gfile.MakeDirs(checkpoints_dir)

dataset_utils.download_and_uncompress_tarball(url, checkpoints_dir)
