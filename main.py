from collections import namedtuple
import time
from models import RNNencdec
from helpers import Dataloader


def main():

    train_start = time.time()
    print("TRAINING")
    Params = namedtuple('Params', ['batch_size', 'embed_size', 'rnn_size', 'alpha', 'phase', 'num_epoch'])

    data = Dataloader('data/hansard/dev.fr', 'data/hansard/dev.en', 'data/hansard/word2idx.fr', 'data/hansard/word2idx.en')
    mparams = Params(20, 30, 64, 1e-3, 'TRAIN', 1)
    print(mparams)
    RNNencdec(data, mparams)

    train_end = time.time() - train_start
    print("--- %s seconds ---" % (train_end))

    print("DEV")
    data.read_data('data/hansard/dev.fr', 'data/hansard/dev.en')
    mparams = Params(20, 30, 64, 1e-3, 'DEV', 1)
    RNNencdec(data, mparams)

    print("--- %s seconds ---" % (time.time() - train_end))

if __name__ == "__main__":
    main()
