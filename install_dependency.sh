#!/bin/bash
sudo apt-get update
sudo apt-get upgrade
sudo apt-get install python3.6
cd ~/Documents
mkdir valkyrie
cd valkyrie
mkdir valkyrie_face_dev_dependencie
sudo apt-get install libboost-all-dev
git clone https://github.com/davisking/dlib.git
cd dlib
mkdir build; cd build; cmake .. -DDLIB_USE_CUDA=0 -DUSE_AVX_INSTRUCTIONS=1; cmake --build .
cd ..
python3 setup.py install --yes USE_AVX_INSTRUCTIONS --no DLIB_USE_CUDA

pip3 install face_recognition