import cPickle

def unpickle(file):
    f = open(file, 'rb')
    dict = cPickle.load(f)
    f.close()
    return dict
