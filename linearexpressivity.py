import torch
from torch.special import expit as sigmoid
from torch.nn.functional import one_hot

x = torch.Tensor()
y = torch.Tensor()
feature_num = 0


def loss_fn(params):
    one_d = sigmoid(x * params)
    x_t = torch.t(x)
    diag = torch.diag(one_d)
    basis = one_hot(torch.Tensor(feature_num))
    return basis*torch.inverse(x*x_t*diag)*(x_t*diag*y)



