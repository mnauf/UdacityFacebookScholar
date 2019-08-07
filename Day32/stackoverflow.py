import torch as th
import syft as sy
hook = sy.TorchHook(th)
from torch import nn, optim
data = th.tensor([[1.,1],[0,1],[1,0],[0,0]],requires_grad = True)
target = th.tensor([[1.],[1],[0],[0]], requires_grad = True)
naufil = sy.VirtualWorker(hook, id="naufil")
faizan = sy.VirtualWorker(hook, id="faizan")
data_naufil = data[0:2].send(naufil)
target_naufil = target[0:2].send(naufil)
data_faizan = data[2:4].send(faizan)
target_faizan = target[2:4].send(faizan)
datasets = [(data_naufil,target_naufil),(data_faizan,target_faizan)]
model = nn.Linear(2,1)
opt = optim.SGD(params = model.parameters(), lr = 0.1)
data1, target1 = datasets[0]
data1.location
target1.location
list(model.parameters())
model = model.send(data1.location)