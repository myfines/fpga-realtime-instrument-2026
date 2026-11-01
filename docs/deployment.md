# 部署与使用指南

## 1. 硬件与版本

Tang Primer 20K＋Dock，FPGA器件 GW2A-LV18PG256C8/I7；PCM5102A音频DAC、ADS1015与双轴摇杆、八路光键、OLED、ESP-01S、K230视觉模块。接线见 [connections.md](hardware/connections.md)。

正式交付：FPGA E049；Android `0.16-e049-instant-effects`，包名 `cn.myfines.instrument`。逐项哈希见 `runtime/RELEASE.json`。

## 2. FPGA下载

1. 使用USB连接Dock的下载接口，打开Gowin Programmer并扫描设备，核对器件型号。
2. 如需临时运行，按板卡文档选择SRAM下载方式，加载 `runtime/fpga/instrument-E049.fs`。SRAM内容断电失效。
3. 如需断电后自动启动，按Tang Primer 20K官方文档配置板载SPI Flash，选择相应擦除、编程与校验流程，加载同一 `.fs`。完成后重新上电。
4. 下载工具里的器件、Flash类型和操作模式应与实物板一致；本工程不将 `.bin` 直接当作带Flash布局的固件镜像。

板卡文档与示例：https://github.com/sipeed/TangPrimer-20K-example 。Gowin GUI项目入口 `fpga/project/instrument_e049.gprj`；重编译输出与本次交付文件分开存放。

## 3. Android安装与连接

安装 `runtime/android/instrument-companion-0.16-e049-instant-effects.apk`。它保留原自绘演奏UI；构建源码位于 `android/src`。最低Android 8.0（API 26）。已有相同签名安装包可覆盖安装；如自行重建，构建脚本会使用本地调试密钥，签名不同的安装包应在测试设备安装。

手机Wi-Fi连接 `FPGA-Instrument`，密码 `fpga-demo-2026`，无互联网提示时保持连接。在App输入 `192.168.4.1`、端口 `9000` 并连接。电脑保持原网络，不需要加入ESP热点。

界面支持多指演奏、音色/音区/音量、ADSR、颤音、合唱/延迟/混响组合、OLED显示切换、曲谱、映射和短录音。效果选项可在离线状态保存；设备发声需要连接FPGA。

在线曲谱分两步：手机在有互联网的网络下载文本并缓存，再连接设备热点下发；ESP热点本身不提供互联网。

## 4. K230 SD卡目录

先使用与实物板匹配的CanMV固件和厂商库，将 `runtime/k230/sdcard` 内文件按同名放到SD卡根目录：

```text
/sdcard/main.py
/sdcard/uart_gesture_sender_standalone.py
/sdcard/pinch_preview_v2.py
/sdcard/k230_hand_keypoint_official.py
/sdcard/kmodel/hand_det.kmodel
/sdcard/kmodel/handkp_det.kmodel
```

前四个Python文件随工程提供；后两个模型由板卡原配资源或厂商下载页取得。厂商参考代码所需 `libs.PipeLine`、`libs.AIBase`、`libs.AI2D`、`media`、`nncase_runtime`、`ulab`、`aicube` 来自匹配的CanMV环境。不要将不同板卡固件或模型随意混用。

UART1为115200、8N1；K230 IO9输出到FPGA M14，GND共地；IO10用于UART接收引脚复用但不外接信号。启动脚本校验捏合识别文件的SHA-256，部署时保留该文件的原始字节，不要让编辑器转换换行。

工程提供的 `k230_hand_keypoint_official.py` 来源于本项目已保存的厂商类参考文件；捏合程序只加载其类定义，不运行厂商示例的独立主循环。模型和CanMV库仍按厂商许可获取。

## 5. 演奏操作

- 外设启用：按住S1＋S2，按下并松开摇杆，再松开S1/S2，等待约20秒。再次执行会关闭外设。
- 八路光键选音与组合演奏；松键进入对应声部释放过程。
- 摇杆短按切换四音色；弯音轴改变音高，另一轴在新音触发时提供力度。
- 视觉手势控制音量上限与明亮度；先保持发声再做手势，手势本身不触发音符。
- S0短按循环效果组合，长按约1秒切换32声部测试；S1短按切音区。
- S3短按启停曲谱，长按约1秒切换锁存。锁存、曲谱和32声部模式按需退出。
- App可分别设置ADSR与效果组合，切换OLED波形、16带频谱、XY、曲谱指引和声部状态。

## 6. 源码测试入口

RTL：安装Icarus Verilog，将 `iverilog` 与 `vvp` 放入PATH后执行 `powershell -File fpga/sim/run_icarus.ps1`。K230：在 `k230` 目录执行 `python -m unittest discover -p "test_*.py"`。网页工具：在 `fpga/tools` 目录执行 `python -m unittest test_cloud_config test_relay test_recording_store`。

测试日志和编译缓存由本机生成，不作为运行依赖。作品功能、原理和源文件索引见设计报告。
