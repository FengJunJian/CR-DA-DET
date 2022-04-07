# Copyright (c) Facebook, Inc. and its affiliates. All Rights Reserved.
# from ._utils import _C
#from model import _C
from torchvision.ops import nms as ops_nms
nms = ops_nms

#nms = _C.nms
# nms.__doc__ = """
# This function performs Non-maximum suppresion"""
