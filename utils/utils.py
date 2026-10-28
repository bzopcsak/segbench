import torch


def sync(device):
    if device == "cuda":
        torch.cuda.synchronize()
