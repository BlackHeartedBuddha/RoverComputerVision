# RoverComputerVision

## Plan
1. Implement local video capture + model + render
2. Pass capture to a client on which the model is running + render
3. Send capture to cloud server + model that provides streams to respective clients

2.a Transmission protocols (udp, tcp, webrtc for video)
2.b Extra RnD (mqtt, amqp, rabbitmq, zmq)

## Design Document
[Design Document Link](https://docs.google.com/document/d/1fqYJn_2ZgH6EykcJWoc6cJIglp_C8Jcb49K0rCoC3ag/edit?tab=t.8s3b34p6bz0b)

## Setup
```bash
python -m venv venv

# Windows
./venv/Scripts/activate

# Linux
source venv/bin/activate

# For CPU usecase
pip install -r requirements.txt

# For gpu 
pip uninstall torch torchvision torchaudio -y

# Check driver version
nvidia-smi

# Driver installation 
pip install torch torchvision torchaudio --index-url https://download.pytorch.org/whl/cu121

# Running demo
python .\sandbox\template.py


```
## Objectives
- [ ] Test Yolo
- [ ] Investigate Cloud Server Architecture Feasibility
- [ ] Train own model
