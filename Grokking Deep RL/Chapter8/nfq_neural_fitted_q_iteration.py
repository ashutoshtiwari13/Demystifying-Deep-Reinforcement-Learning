# -*- coding: utf-8 -*-

#Google colab
#ashutoshtiwari13

#Pytorch Implementation
import torch
import torch.nn as nn
import torch.nn.functional as nn
import torch.optim as optim

#Libs
import os
import numpy as np
from collections import namedtuple, deque
from IPython.display import display 
import matplotlib
import matplotlib.pyplot as plt
import matplotlib.pylab as pylab
# %matplotlib inline
from itertools import cycle, count

from gym import wrappers

class NFQ(nn.Module):
  def __init__(self,input_dim, output_dim, hidden_dims =(32,32),activation_fc = F.relu):
    super(NCQ, self).__init__()
    self.activation_fc =activation_fc

    self.input_layer = nn.Linear(input_dim)
