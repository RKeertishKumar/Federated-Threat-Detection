# Federated-Threat-Detection
The project aims to expedite the training of deep learning models for log analysis and monitoring, critical for cybersecurity and threat detection.

# Abstract:
This project proposes a comprehensive solution to expedite the training of deep learning models for log analysis and monitoring, crucial for cybersecurity and threat detection. Leveraging parallel processing techniques, log and monitoring data stored in vector databases are efficiently processed, providing invaluable insights into potential security breaches. However, traditional training methods can be time-consuming, hindering timely threat response. To address this, federated learning is introduced to facilitate distributed model training, allowing for collaborative learning across multiple nodes without compromising data privacy. In cases where infrastructure limitations hinder federated learning implementation, an AI adaptive GPU switch mechanism is employed to optimize computational resources. This trade-off between federated learning and GPU optimization ensures rapid model updates, enabling real-time threat prevention by keeping the system continuously responsive to emerging threats worldwide.

# Introduction
The cybersecurity landscape has evolved a lot over the past few years. We have had great strides of improvement but the other side has well. It has come to a point where AI is used to create highly sophisticated malware. We can’t stay as we are and hope to secure our systems with the attacks that are going to occur.

[2019–2023 in Review: Projecting DDoS Threats With ARIMA and ETS Forecasting Techniques | IEEE Journals & Magazine | IEEE Xplore](https://ieeexplore.ieee.org/document/10439150)

The above paper takes a review on the global DDos attacks and has put forth a forecast of attacks that will occur in 2024-2026 and these attacks are predicted to cause substantial economic damages. The community is aware of the unstable situation we are in and we need to up our AI powered security measures to stand what is coming.

# Architecture Design
![image](https://github.com/RKeertishKumar/Federated-Threat-Detection/assets/141417594/b09ab256-2256-447d-b123-926e687a488b)

# Developer logs

Setup the virtual environment:

```bash
pip install virtualenv

python -m venv myenv
```

### To activate virtual environment

```bash
myenv\Scripts\activate
```
You would now have a (myenv) before the directory mentioned in your terminal pointing out that the environment is virtual.

## Install FastAPI and Uvicorn

Uvicorn is used for ASGI server implementation.

```bash
pip install fastapi uvicorn
```

To run site in developement mode. Reload is used to update site after the code is changed.

```bash
uvicorn main:app --reload
```

Open link at:
```link
http://127.0.0.1:8000/api/data
```
Had setup react app, go to frontend/threat-detector folder and run
```bash
npm start
```
The data from fastapi will now be directed to react to display.

### To start InfluxDB server

```bash
cd -Path 'C:\Program Files\InfluxData\influxdb'
```

```bash
./influxd
```
### To setup Material UI

```bash
 npm install @mui/material @emotion/react @emotion/styled
```

### Setting up federated learning framework

installed flwr

### Dataset info

Took the dataset from

https://www.unb.ca/cic/datasets/ddos-2019.html

### Splitting dataset into 3 parts

For example, if you have 1000 samples in your dataset, you might split it as follows:

700 samples for training (70%)
150 samples for validation (15%)
150 samples for testing (15%)

### Running the deep learning model
![image](https://github.com/RKeertishKumar/Federated-Threat-Detection/assets/141417594/7741cdcb-f3db-454a-87d4-6e0129765544)

The accuracy is 77 percent with time taken to train the model being 38 seconds.








