# K230视觉手势模块

正式预览与识别入口为 `pinch_preview_v2.py`。`gesture_protocol.py` 定义手势协议，`uart_gesture_sender.py` 和 `usb_gesture_sender.py` 封装通信，`uart_gesture_launcher.example.py` 为串口启动示例。USB相关模块及第一版预览源文件一并保留，供开发与接口适配使用。

在 CanMV 环境安装匹配的手部检测与关键点模型，并依照实际接线设置启动脚本中的 UART/FPIOA 引脚。模型路径见识别脚本，模型文件依照其原提供方许可另行获取。K230输出演奏控制信息，主音频合成在FPGA内完成。

电脑上运行 `python -m unittest discover -p "test_*.py"` 可执行离线协议与识别逻辑测试，不需要连接K230。
