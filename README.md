# 基于FPGA的多维交互实时多音色合成电子乐器

2026年高云选题二作品源码。音频由FPGA根据演奏指令逐声部、逐样本生成；光电、摇杆、视觉手势和手机构成多维演奏交互。

## 作品功能

- 32份独立相位、频率与ADSR声部状态，采用时分流水线完成实时合成。
- 电钢琴、风琴、弦乐与Bass四种音色，支持弯音、力度、颤音及明亮度控制。
- FPGA内部合唱、延迟、混响，可独立启用及组合。
- 八路光电选音、摇杆表情、K230捏合音量与高度控制。
- OLED波形、16带频谱、立体声XY、曲谱指引和声部状态；LED分组曲目提示。
- Android多指键盘、ADSR与效果设置、文本曲谱下载及缓存下发、键位映射、短PCM录音与WAV导出。

## 工程结构

|目录|内容|
|---|---|
|fpga/src|正式音频与交互RTL|
|fpga/constraints|Tang Primer 20K引脚及时钟约束|
|fpga/tools/build.tcl|Gowin EDA热点直连构建入口 E049|
|fpga/sim|RTL仿真测试台|
|android|App 0.16源码、清单、构建及测试|
|k230|视觉手势与串口协议代码|
|fpga/web|浏览器控制页面与可选中继页面|
|fpga/tools|正式构建入口、网页ROM生成与可选HTTP中继工具|
|docs|作品报告与使用说明|

## 构建与使用

FPGA：安装适用于GW2A-LV18PG256C8/I7的Gowin EDA，在Tcl环境执行`source fpga/tools/build.tcl`。脚本按自身路径定位源文件，输出目录为`fpga/build-public`，可用环境变量`FPGA_BUILD_ROOT`指定输出位置。

Android：安装JDK 17及以上、Android SDK Build Tools 36.0.0和脚本指定平台SDK；设置`JAVA_HOME`，执行`powershell -File android/build.ps1 -Sdk <SDK目录> -Jdk <JDK目录>`。脚本运行Java测试并构建APK，为本地构建生成独立调试签名；已有不同签名安装包请在独立测试设备安装。

K230：使用CanMV及配套手部识别模型，按硬件连接设置串口；`uart_gesture_launcher.example.py`为启动配置示例，`pinch_preview_v2.py`执行识别与预览，`uart_gesture_sender.py`封装发送。

设备启用：按住S1与S2，按下并松开摇杆，再松开S1/S2，等待外设初始化。手机连接`FPGA-Instrument`，密码`fpga-demo-2026`，App连接`192.168.4.1:9000`。电脑保持原网络。在线获取曲谱与热点下发分步进行。

## 实现索引

核心声部：`fpga/src/synth32.v`；音色：`wave_source.v`；效果：`fx_engine.v`；I²S：`i2s_tx16.v`；曲谱与指引：`song_player.v`、`led_guide.v`、`oled_ui.v`；App直连扩展：`android/src/cn/myfines/instrument/reference/ReferenceActivity.java`。

主时钟设计值27 MHz，音频帧576周期，设计输出率46,875 Hz。32声部在同一帧内调度，设计吞吐量为1,500,000声部样本每秒。

报告见[作品设计报告](docs/report.md)。资料来源见[NOTICE](NOTICE.md)。

## 源码交付与依赖

本仓库包含正式 E049 / App 0.16 对应的 FPGA RTL、引脚和时钟约束、Android Java 源码及测试、K230 识别与通信源码、网页控制页面、仿真测试台和构建工具。`fpga/legacy` 与 `fpga/sim/legacy` 保留早期模块及配套测试；正式工程以 `fpga/tools/build.tcl` 列出的源文件为准。

Gowin EDA、Android SDK/JDK、CanMV 固件与手部识别模型属于外部运行或构建依赖，按各提供方许可获取。仓库不包含个人签名密钥；Android 构建脚本会为本地构建生成调试密钥。`SOURCE-MANIFEST.json` 提供逐文件 SHA-256，可用于核对下载包内容。

RTL测试：将 Icarus Verilog 的 `iverilog`、`vvp` 加入 PATH，运行 `powershell -File fpga/sim/run_icarus.ps1`。

K230离线测试：在 `k230` 目录执行 `python -m unittest discover -p "test_*.py"`。这些测试在电脑执行，不访问设备。

网页及中继说明见 [浏览器控制源码](fpga/web/README.md)；完整源码压缩包与本仓库同版本文件对应，不包含 Git 历史、编译缓存、个人密钥和本机调试日志。
