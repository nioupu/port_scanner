import unittest
import os
import csv
from tcp_scanner import scan, save_to_csv, save_to_html

class TestTCPScanner(unittest.TestCase):
    # 测试端口扫描函数
    def test_scan_closed_port(self):
        # 测试本地未开放端口
        port, status = scan("127.0.0.1", 9999)
        self.assertEqual(status, "关闭")

    # 测试CSV导出功能
    def test_save_to_csv(self):
        target_host = "test_ip"
        test_results = [(80, "开放"), (443, "关闭")]
        test_filename = "test_scan_result.csv"
        
        # 执行导出
        save_to_csv(target_host, test_results, test_filename)
        
        # 验证文件存在
        self.assertTrue(os.path.exists(test_filename))
        
        # 验证内容正确
        with open(test_filename, "r", encoding="utf-8") as f:
            reader = csv.reader(f)
            header = next(reader)
            self.assertEqual(header, ["目标主机", "端口", "状态"])
            row1 = next(reader)
            self.assertEqual(row1, ["test_ip", "80", "开放"])
        
        # 清理测试文件
        os.remove(test_filename)

    # 测试HTML导出功能（仅验证文件生成）
    def test_save_to_html(self):
        target_host = "test_ip"
        test_results = [(22, "开放")]
        test_filename = "test_scan_result.html"
        
        save_to_html(target_host, test_results, test_filename)
        self.assertTrue(os.path.exists(test_filename))
        
        # 清理测试文件
        os.remove(test_filename)

if __name__ == "__main__":
    unittest.main()
