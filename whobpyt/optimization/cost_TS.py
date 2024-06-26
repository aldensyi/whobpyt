"""
Authors: Zheng Wang, John Griffiths, Andrew Clappison, Hussain Ather, Kevin Kadak
Neural Mass Model fitting
module for cost calculation
"""

import numpy as np  # for numerical operations
import torch
from ..datatypes import AbstractLoss 
from ..functions.arg_type_check import method_arg_type_check


class CostsTS(AbstractLoss):
    def __init__(self, simKey = None, model = None):
        super(CostsTS, self).__init__(simKey = simKey, model=model)
        self.simKey = simKey

    def main_loss(self, simData: dict, empData: torch.Tensor):
        """
        Calculate the Pearson Correlation between the simFC and empFC.
        From there, compute the probability and negative log-likelihood.
        
        Parameters
        ----------
        simData: dict of tensor with node_size X datapoint
            simulated EEG
        empData: tensor with node_size X datapoint
            empirical EEG
        """
        method_arg_type_check(self.main_loss) # Check that the passed arguments (excluding self) abide by their expected data types
        sim = simData[self.simKey]
        emp = empData

        losses = torch.sqrt(torch.mean((sim - emp) ** 2))  #
        return losses
