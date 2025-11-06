# 多线程端口扫描器

基于Python的多线程端口扫描工具，支持快速扫描目标IP开放端口，输出CSV/HTML报告。

## 依赖
Python 3.6及以上

## 使用方法
1. 克隆仓库
```bash
git clone https://github.com/nioupu/port_scanner.git
cd port_scanner
 
 
2. 扫描示例（扫描192.168.1.1的1-100端口，输出CSV）
 
bash
  
python3 port_scanner.py -t 192.168.1.1 -p 1-100 -o result.csv
 
 
命令行参数
 
-  -t ：目标IP
-  -p ：端口范围（如1-100）
-  -o ：输出文件（.csv或.html后缀）
