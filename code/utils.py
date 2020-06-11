import numpy as np
import csv
from fractions import Fraction
from scipy.signal import resample_poly
from scipy.stats import rankdata
from partial_corr import partial_corr

def load_fragment_times(d, sound):
    '''load timestamps for sound fragments: speech or nonspeech'''
    with open(d + '/fragments_'+sound+'_100Hz.csv', 'r') as csvfile:
        reader = csv.reader(csvfile)
        data = list(reader)
    return np.array([np.array(''.join(line).split('\t')).astype(np.float) for line in data]).astype(np.int)


def load_noisy_fragment_times(d):
    '''load timestamps for noisy sound fragments'''
    with open(d + '/fragments_speech_100Hz_noisy_mus_overlap.csv', 'r') as csvfile:
        reader = csv.reader(csvfile)
        data = list(reader)
    return np.array([np.array(''.join(line).split('\t')).astype(np.float) for line in data]).astype(np.int)


def resample(x, sr1, sr2, axis=0):
    '''resample signal'''
    a, b = Fraction(sr1, sr2)._numerator, Fraction(sr1, sr2)._denominator
    return resample_poly(x, a, b, axis).astype(np.float32)


def zscore(x, axis=0):
    '''normalize signal'''
    return (x -np.mean(x, axis=axis, keepdims=True))/np.std(x, axis=axis, keepdims=True)


def cross_correlate(x, y, type='pearson'):
    '''run cross-correlation on 1d signals'''
    if type == 'spearman':
        x, y = rankdata(x), rankdata(y)
    x = (x - np.mean(x)) / (np.std(x) * x.shape[0])
    y = (y - np.mean(y)) / np.std(y)
    return np.correlate(x, y, mode='full')


def run_partial_cor(a, b, c, type='pearson'):
    '''run partial correlation'''
    a = (a - np.mean(a)) / np.std(a)
    b = (b - np.mean(b)) / np.std(b)
    c = (c - np.mean(c)) / np.std(c)
    temp = partial_corr(np.vstack([a, b, c]).T, type)
    ab = temp[0, 1]
    ac = temp[0, 2]
    bc = temp[1, 2]
    return ab, ac, bc


def shuffle_fragments(d):
    '''shufle the orders of fragments in the input data for permutation test baseline'''
    d_ = d.reshape(115, -1)
    p_ = np.random.permutation(115)
    return d_[p_].reshape(-1,)

