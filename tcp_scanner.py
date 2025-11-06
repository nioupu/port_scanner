import socket
import csv
import argparse
from concurrent.futures import ThreadPoolExecutor


def scan(host, port):
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.settimeout(3)
    try:
        s.connect((host, port))
        return port, "开放"
    except Exception:
        return port, "关闭"
    finally:
        s.close()


def save_to_csv(target_host, results, filename=None):
    filename = filename or f"{target_host}_端口扫描结果.csv"
    with open(filename, 'w', newline="", encoding="utf-8") as f:
        writer = csv.writer(f)
        writer.writerow(["目标主机", "端口", "状态"])
        for port, status in results:
            writer.writerow([target_host, port, status])
    print(f"\n【csv导出完成】结果已保存到：{filename}")


def save_to_html(target_host, results, filename=None):
    filename = filename or f"{target_host}_端口扫描结果.html"
    html_content = f"""
    <!DOCTYPE html>
    <html lang="zh-CN">
    <head>
        <meta charset="utf-8">
        <title>{target_host}_端口扫描结果</title>
        <style>table {{border-collapse: collapse;}}th,td{{border:1px solid #000;padding:8px;}}</style>
    </head>
    <body>
        <h1>{target_host}_端口扫描结果</h1>
        <table>
            <tr>
                <th>目标主机</th>
                <th>端口</th>
                <th>状态</th>
            </tr>
{''.join([f'<tr><td>{target_host}</td><td>{port}</td><td>{status}</td></tr>' for port, status in results])}
        </table>
    </body>
    </html>
    """
    with open(filename, 'w',  encoding="utf-8") as f:
        f.write(html_content)
    print(f"\n【HTML导出完成】结果已保存到：{filename}")


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description="多线程端口扫描器（支持CSV/HTML输出）")
    parser.add_argument("-t", "--target", required=True, help="目标主机IP（如 127.0.0.1 ）")
    parser.add_argument("-p", "--ports", required=True, help="端口范围（如1-100 或 80）")
    parser.add_argument("-o", "--output", choices=["csv", "html"], help="输出格式(可选：csv/html)")
    args = parser.parse_args()
    port_input = args.ports
    target_host = args.target
    if "-" in port_input:
        start_port, end_port = map(int, port_input.split("-"))
        print(f"正在扫描 {target_host} 的端口 {start_port}-{end_port}...\n")
    else:
        start_port = end_port = int(port_input)
        print(f"正在扫描 {target_host} 的端口 {start_port}...\n")
    port_to_scan = range(start_port, end_port + 1)
    with ThreadPoolExecutor(max_workers=10) as executor:
        results = executor.map(scan, [target_host] * len(port_to_scan), port_to_scan)
    results = list(results)
    print("\n扫描完成。")
    open_ports = [port for port, status in results if status == "开放"]
    if open_ports:
        print("开放端口：")
        for p in open_ports:
            print(p)
    else:
        print("未发现开放端口。")
    if args.output == "csv":
        save_to_csv(target_host, results)
    elif args.output == "html":
        save_to_html(target_host, results)
