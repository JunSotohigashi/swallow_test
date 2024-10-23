import torch

n = torch.cuda.device_count()
print(f"{n} CUDA device(s) available")
for i in range(n):
    print(torch.cuda.get_device_name(i))
