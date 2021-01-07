import torch
import matplotlib.pyplot as plt
import numpy as np
from torchvision import datasets, transforms
import torch.nn.functional as F
import torch.nn as nn
import PIL.ImageOps
from PIL import Image
from torch.autograd import Variable
import logging

logger = logging.getLogger(__name__)

class LeNet(nn.Module):
    def __init__(self):
        super().__init__()
        self.conv1 = nn.Conv2d(3, 32, 3, 1, padding = 1)
        self.conv2 = nn.Conv2d(32, 64, 3, 1, padding = 1)
        self.conv3 = nn.Conv2d(64, 128, 3, 1, padding = 1)
        self.fc1 = nn.Linear(4*4*128, 500)
        self.dropout1 = nn.Dropout(0.4)
        self.fc2 = nn.Linear(500, 10)
    def forward(self, x):
        x = F.relu(self.conv1(x))
        x = F.max_pool2d(x, 2, 2)
        x = F.relu(self.conv2(x))
        x = F.max_pool2d(x, 2, 2)
        x = F.relu(self.conv3(x))
        x = F.max_pool2d(x, 2, 2)
        x = x.view(-1, 4*4*128)
        x = F.relu(self.fc1(x))
        x = self.dropout1(x)
        x = self.fc2(x)
        return x

def image_loader(image_name):
    """load image, returns cuda tensor"""
    loader = transforms.Compose([transforms.Resize((32, 32)), transforms.ToTensor()])
    image = Image.open(image_name)
    # image = loader(image).float()
    # image = Variable(image, requires_grad=True)
    # image = image.unsqueeze(0)  #this is for VGG, may not be needed for ResNet
    return image  #assumes that you're using GPU

def verwerkImage(imageFile):
    """ als input krijgt deze method een image files
    en als output geeft hij een getal (prediction)"""


    transform = transforms.Compose([transforms.ToTensor(),
                                    transforms.Normalize((0.5,), (0.5,))])
    model = LeNet()
    model
    criterion = nn.CrossEntropyLoss()
    optimizer = torch.optim.Adam(model.parameters(), lr=0.0001)
    image = image_loader(imageFile)
    logger.warning('tot hier dan')
    checkpoint = {'model': LeNet(),
                  'state_dict': model.state_dict(),
                  'optimizer': optimizer.state_dict()}
    torch.load('SVHN_mijnCheckpoint.pth')

