import chainer

if chainer.cuda.available:
    print("CUDA is available.")
    print("Devices:", chainer.cuda.Device.count())
else:
    print("CUDA is not available.")
