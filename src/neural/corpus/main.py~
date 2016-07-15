import cPickle
training_data = cPickle.load(open('traindata.p','rb'))
testing_data = cPickle.load(open('numpytestdata.p','rb'))

import neuralnet
net = neuralnet.Network([8, 5, 3])

net.SGD(training_data, 30, 10, 3.0, testing_data)
