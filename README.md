# anyshotlearning
ubc engphys capstone project 2021-2022 

## UniT: Unified Knowledge Transfer for Any-shot Object Detection and Segmentation

This repository contains the code for the web demo of the CVPR 2021 paper titled [**"UniT: Unified Knowledge Transfer for Any-shot Object Detection and Segmentation"**](https://arxiv.org/pdf/2006.07502.pdf).

## Requirements
To setup the environment with all the required dependencies, follow the steps detailed in [INSTALL.md](https://github.com/ubc-vision/UniT/blob/main/INSTALL.md). 

## Prepare Dataset
- To obtain the data and curate the splits for PASCAL VOC
```python
python data/prepare_voc.py --DATA-ROOT "Path/to/Save/Location/"

```
**Note**: These splits are the same as the ones released by the authors of [Few-shot Object Detection via Feature Reweighting](https://github.com/bingykang/Fewshot_Detection).


## Prepare Models
Download ImageNet pretrained models from [this Google drive](https://drive.google.com/drive/folders/1plLDI55qKvwPa5OuT_DcGobdnAPqBfq1?usp=sharing), and place them in the `models/` folder in the root directory. 
