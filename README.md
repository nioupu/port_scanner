# TCP多线程端口扫描器

一个基于Python的轻量级多线程端口扫描工具，支持扫描指定IP的端口范围，并导出CSV/HTML格式结果。


## 功能特点
- 多线程扫描（默认10线程），提升扫描效率
- 支持单个端口/端口范围扫描
- 输出开放端口列表
- 可选导出CSV/HTML格式的扫描报告


## 环境依赖
- Python 3.x（无需额外安装第三方库，使用内置模块）


## 使用方法

### 基本命令格式
```bash
python tcp_scanner.py -t <目标IP> -p <端口/端口范围> [-o <输出格式>]
 
 
参数说明
 
参数 作用 示例 
 -t / --target  必填，指定目标主机IP  127.0.0.1 、 8.8.8.8  
 -p / --ports  必填，指定端口（单个/范围）  80 、 1-100  
 -o / --output  可选，指定输出格式（ csv / html ）  csv  
 
示例命令
 
1. 扫描单个端口
 
bash
  
python tcp_scanner.py -t 127.0.0.1 -p 80
 
 
2. 扫描端口范围（1-100）
 
bash
  
python tcp_scanner.py -t 127.0.0.1 -p 1-100
 
 
3. 扫描并导出CSV报告
 
bash
  
python tcp_scanner.py -t 8.8.8.8 -p 80-443 -o csv
 
 
4. 扫描并导出HTML报告
 
bash
  
python tcp_scanner.py -t 192.168.1.1 -p 22-80 -o html
 
 
输出说明
 
- 终端会直接显示开放端口列表
- 若指定了 -o 参数，报告文件会保存在当前目录，文件名格式为： [目标IP]_端口扫描结果.csv （或 .html ）
 
单元测试
 
项目包含单元测试用例，验证核心功能：
 
bash
  
python -m unittest test_tcp_scanner.py -v
 
 
注意事项
 
1. 扫描非授权主机可能违反法律法规，请仅在自己拥有权限的网络环境中使用
2. 部分网络环境可能限制端口扫描行为，建议调整线程数（修改代码中 max_workers 参数）避免被拦截
