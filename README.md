# Military Object Detection

This repository contains the implementation of a military object detection system using YOLO (You Only Look Once). The system is designed to detect various military weapons, tanks, and other objects using a custom dataset.

## Features

- Detection of military weapons and tanks
- Utilizes YOLO for object detection
- Custom dataset for training and testing

## Getting Started

### Prerequisites

- Anaconda/Miniconda
- Python 3.8+

### Installation

1. **Clone the repository**

   ```bash
   git clone https://github.com/MianAliKhalid/Military-Object-Detection.git
   cd Military-Object-Detection```



2. **Create conda env**

   ```bash
   conda create --name military-detection python=3.8
   conda activate military-detection```


3. **Download the pre-trained model**

   
   Download the pre-trained YOLO model from [this link](https://drive.google.com/file/d/16OlcFS2Om6256W8u6-h6hM5BpDAXzzSb/view?usp=drive_link) and place it in the `models` directory.


## Usage

### Prepare the Dataset

Ensure your custom dataset is in the correct format and placed in the `data` directory.

### Train the Model

To train the model with your custom dataset, run the following command:

```bash
python train.py --data dataset/data.yaml --cfg models/yolov8.yaml --weights models/pretrained-model.pt --name custom_yolov8
```
