# MaskRCNN-for-Tooth-Dentistry
<div align="center">
    <img src="https://github.com/Bassem-2000/MaskRCNN-for-Tooth-Dentistry/blob/main/Deploy/images/Screenshot%202023-09-09%20042132.png?raw=true">
  </div>
  
## Overview

This project utilizes the Mask R-CNN model for tooth instance segmentation, enabling various applications in the field of dentistry. The model can identify tooth numbers and conditions like implants, root canals, or crowns in dental X-ray images. This README provides an overview of the project, its setup, and potential use cases.

## Table of Contents

- [Setup](#setup)
- [Usage](#usage)
- [Use Cases](#use-cases)
- [Contributing](#contributing)
- [Contact](#Contact)
- [Feedback](#Feedback)

## Setup

### Prerequisites

Before running this project, ensure you have the following installed:

- Docker
- Streamlit
- FastAPI
- Python 3.8

### Installation

1. Clone the project repository:

    ```
   git clone https://github.com/Bassem-2000/MaskRCNN-for-Tooth-Dentistry
    ```

2. Navigate to the project directory:

   ```
   cd MaskRCNN-for-Tooth-Dentistry/Deploy
   ```

3. Download the model from here:

    ```
    https://drive.google.com/file/d/1Ybc0KyJYaYtF5VrlwlvBB8lkZlSZsglx/view?usp=sharing
    ```
    
4. Build the Docker container:

    ```
   docker build -t dentistry-computer-vision .
    ```

5. Run the Docker container:

    ```
   docker run -p 8000:8000 -p 8501:8501 dentistry-computer-vision
    ```



## Usage

### Streamlit Web Interface

1. Access the Streamlit web interface at [http://localhost:8501](http://localhost:8501) to interact with the Dentistry Computer Vision application.

### FastAPI API

The FastAPI API is available at [http://localhost:8000/docs](http://localhost:8000/docs). You can use this API to integrate the computer vision model into your own applications.

## Use Cases

Here are a few use cases for this Dentistry Computer Vision project:

### 1. Dental Treatment Planning

Dentists and orthodontists can use this computer vision model to analyze dental X-rays, identify teeth numbers, and assess conditions such as implants, root canals, or crowns. Automatic classification enhances efficiency and treatment planning accuracy.

### 2. Dental Education and Training

This model serves as a valuable learning tool for dental students. It helps them become familiar with tooth numbering, implants, crowns, and root canals. This educational resource can be integrated into virtual classrooms or educational mobile applications.

### 3. Dental Insurance Claim Processing

Insurance companies can employ this model for automatic dental claim processing. It identifies specific treatments or procedures from dental X-ray images (e.g., root canals or implants), leading to faster and more accurate claim processing.

### 4. Dental Record Management

Clinics and hospitals can streamline dental patient record management by using this model to categorize X-ray images based on tooth number and treatment type. This enhances patient record organization and accessibility.

### 5. Dental Research and Analytics

Dental researchers can benefit from this model for oral health analytics. Analyzing large datasets of dental X-ray images helps identify patterns and trends related to different treatments and tooth conditions, providing valuable insights for oral care and health improvement.


## Contributing

Contributions to this project are welcome! If you have ideas for improvements or bug fixes, please create an issue or submit a pull request.

## Contact

[<img alt="alt_text" width="30px" src="https://cdn2.iconfinder.com/data/icons/social-media-2285/512/1_Whatsapp2_colored_svg-512.png" />](https://wa.me/+201006491306)
&nbsp;&nbsp;
[<img alt="alt_text" width="30px" src="https://cdn2.iconfinder.com/data/icons/social-media-2285/512/1_Linkedin_unofficial_colored_svg-512.png" />](https://www.linkedin.com/in/bassem-ahmed-ahmed/)
&nbsp;&nbsp;
[<img alt="alt_text" width="30px" src="https://cdn4.iconfinder.com/data/icons/social-media-logos-6/512/112-gmail_email_mail-256.png" />](mailto:bassemahmed.am@gmail.com)
&nbsp;&nbsp;
[<img alt="alt_text" width="30px" src="https://cdn2.iconfinder.com/data/icons/social-media-2285/512/1_Facebook2_colored_svg-512.png" />](https://www.facebook.com/bassem.ahmed.7712/)


## Feedback

Can you please provide me with feedback on how I can improve myself and any ideas to improve the model, I am eager to receive any advice that can help me develop my skills.

&nbsp;&nbsp;
**Wish you a nice day :)**


