## 安裝 Pillow-SIMD
如果你需要在沒有網路的狀況下 安裝 Pillow-SIMD 在ubuntu 16.04/python 3.52 時, follow below  

Pillow SIMD 的介紹在這裡
https://github.com/uploadcare/pillow-simd  
Pillow SIMD 效能分析 
https://python-pillow.org/pillow-perf/  
### 1. 先在有網路的狀況下 download 這些 package
sudo apt download zlib1g libjbig0 libjpeg8 libjpeg-turbo8 liblzma5 libtiff5 libtiffxx5 libjbig-dev libjpeg8-dev libjpeg-turbo8-dev liblzma-dev zlib1g-dev libtiff5-dev  
pip3 download pillow-simd  

### 你會得到以下安裝文件
並把他copy 到你要安裝的機器上  

zlib1g_1%3a1.2.8.dfsg-2ubuntu4.1_amd64.deb  
libjbig0_2.1-3.1_amd64.deb  
libjpeg8_8c-2ubuntu8_amd64.deb  
libjpeg-turbo8_1.4.2-0ubuntu3.1_amd64.deb  
liblzma5_5.1.1alpha+20120614-2ubuntu2_amd64.deb  
libtiff5_4.0.6-1ubuntu0.4_amd64.deb  
libtiffxx5_4.0.6-1ubuntu0.4_amd64.deb  

libjbig-dev_2.1-3.1_amd64.deb  
zlib1g-dev_1%3a1.2.8.dfsg-2ubuntu4.1_amd64.deb  
libjpeg8-dev_8c-2ubuntu8_amd64.deb  
libjpeg-turbo8-dev_1.4.2-0ubuntu3.1_amd64.deb  
liblzma-dev_5.1.1alpha+20120614-2ubuntu2_amd64.deb  
libtiff5-dev_4.0.6-1ubuntu0.4_amd64.deb  
Pillow-SIMD-5.3.0.post0.tar.gz  

### 2. 在你使用的環境下這樣安裝

sudo dpkg -i zlib1g_1%3a1.2.8.dfsg-2ubuntu4.1_amd64.deb  
sudo dpkg -i libjbig0_2.1-3.1_amd64.deb  
sudo dpkg -i libjpeg8_8c-2ubuntu8_amd64.deb  
sudo dpkg -i libjpeg-turbo8_1.4.2-0ubuntu3.1_amd64.deb  
sudo dpkg -i liblzma5_5.1.1alpha+20120614-2ubuntu2_amd64.deb  
sudo dpkg -i libtiff5_4.0.6-1ubuntu0.4_amd64.deb  
sudo dpkg -i libtiffxx5_4.0.6-1ubuntu0.4_amd64.deb  

sudo dpkg -i libjbig-dev_2.1-3.1_amd64.deb  
sudo dpkg -i zlib1g-dev_1%3a1.2.8.dfsg-2ubuntu4.1_amd64.deb  
sudo dpkg -i libjpeg8-dev_8c-2ubuntu8_amd64.deb  
sudo dpkg -i libjpeg-turbo8-dev_1.4.2-0ubuntu3.1_amd64.deb  
sudo dpkg -i liblzma-dev_5.1.1alpha+20120614-2ubuntu2_amd64.deb  
sudo dpkg -i libtiff5-dev_4.0.6-1ubuntu0.4_amd64.deb  

### 3. install pliiow-simd  

pip3 install Pillow-SIMD-5.3.0.post0.tar.gz  
# DONE
