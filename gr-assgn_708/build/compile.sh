#!/bin/bash
cmake ../ -Wno-dev
make
sudo make install
sudo ldconfig