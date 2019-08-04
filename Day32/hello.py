import syft as sy
import torch as th
hook = sy.TorchHook(th)
naufil = sy.VirtualWorker(hook,id="naufil")
faizan = sy.VirtualWorker(hook,id="faizan")
x = th.tensor([1,2,3,4]).send(naufil).send(faizan)
print("x: ",x) # x:  (Wrapper)>[PointerTensor | me:43428628104 -> faizan:6306965432]
print("naufil._objects: ",naufil._objects) # naufil._objects:  {7757291916: tensor([1, 2, 3, 4])}
print("faizan._objects: ",faizan._objects) # faizan._objects:  {6306965432: (Wrapper)>[PointerTensor | faizan:6306965432 -> naufil:7757291916]}
del x
print("naufil._objects: ",naufil._objects) # naufil._objects:  {}
print("faizan._objects: ",faizan._objects)  # faizan._objects:  {}