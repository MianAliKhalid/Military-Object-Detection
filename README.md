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
   cd Military-Object-Detection
   ```



2. **Create conda env**

   ```bash
   conda create --name military-detection python=3.8
   conda activate military-detection
   ```


3. **Download the pre-trained model**

   
   Download the pre-trained YOLO model from [this link](https://drive.google.com/file/d/16OlcFS2Om6256W8u6-h6hM5BpDAXzzSb/view?usp=drive_link) and place it in the `models` directory.


4. **Run the Application**

Once you have set up your environment and the pretrained model is in place, you can start the application by running `app.py`:

```bash
python app.py
```

## Dataset

To access and download the custom dataset used for training our military object detection model, please follow the link below:

- **YOLO Military Dataset**: [Download Here](https://universe.roboflow.com/uce03211-gmail-com/yolo-military)

Please ensure you comply with any usage restrictions and licensing agreements specified by the dataset provider.

## Usage

### Prepare the Dataset

Ensure your custom dataset is in the correct format and placed in the `data` directory.

### Train the Model

To train the model with your custom dataset, run the following command:

```bash
python train.py --data dataset/data.yaml --cfg models/yolov8.yaml --weights models/pretrained-model.pt --name custom_yolov8
```

## Acknowledgments

This project would not have been possible without the contributions and support from various individuals and organizations. We would like to extend our gratitude to the following:

- **[YOLOv8 Team](https://github.com/ultralytics/yolov8)**: For their open-source object detection model which has been crucial in developing our military object detection capabilities.
- **Project Contributors**: Thanks to all the developers and data scientists who have contributed their time and expertise to enhance the functionalities of this project.
- **Data Providers**: Special thanks to the organizations and partners who provided access to invaluable datasets that have made this project feasible.
- **Community Members**: Thank you to the wider open-source community for their ongoing support, feedback, and suggestions that help improve this project.
- **Financial Supporters**: We are also grateful for the financial support from various grants and funding sources that have enabled us to advance our research and development efforts.

Your contributions are sincerely appreciated and have played a vital role in advancing this project.

