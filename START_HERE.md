# 完整工程阅读与运行入口

作品：基于FPGA的多维交互实时多音色合成电子乐器。正式硬件版本 E049，配套 Android App 0.16。

## 一、先看这几个文件

|目的|入口|
|---|---|
|作品功能与目录|[README.md](README.md)|
|设计原理与实现|[作品设计报告PDF](docs/report.pdf)、[文字报告](docs/report.md)|
|硬件接口|[硬件连接表](docs/hardware/connections.md)|
|部署与操作|[部署使用指南](docs/deployment.md)|
|完整工程索引|[PROJECT-INDEX.json](PROJECT-INDEX.json)|
|正式运行文件与版本|[runtime/RELEASE.json](runtime/RELEASE.json)|
|海报|[PDF](docs/poster/poster.pdf)、[可编辑PPT](docs/poster/poster.pptx)|

## 二、直接使用运行文件

1. FPGA：`runtime/fpga/instrument-E049.fs` 为正式烧录文件；目标器件为 GW2A-LV18PG256C8/I7。使用 Gowin Programmer 按板卡SPI Flash配置下载，详见部署指南。`.bin` 为配套二进制文件，常规操作优先使用 `.fs`。
2. Android：安装 `runtime/android/instrument-companion-0.16-e049-instant-effects.apk`。手机连接 `FPGA-Instrument`，密码 `fpga-demo-2026`，App连接 `192.168.4.1:9000`。
3. K230：`runtime/k230/sdcard` 提供启动脚本、UART发送器、捏合识别和厂商识别类参考。使用与板卡匹配的CanMV固件及手部模型，按部署指南放到SD卡对应路径。
4. 开机后按住 S1＋S2，按下并松开摇杆，再松开S1/S2，等待约20秒完成外设初始化。组合操作用于切换外设启用状态，启用后无需反复操作。

## 三、重新构建

- Gowin GUI：打开 `fpga/project/instrument_e049.gprj`，项目内使用相对路径，顶层为 `instrument_ap_top`。正式构建参数入口为 `fpga/tools/build.tcl`。
- Gowin Tcl：在支持Gowin工程命令的Tcl环境执行 `source fpga/tools/build.tcl`。
- Android：JDK 17及以上、Android SDK平台37、Build Tools 36.0.0；执行 `powershell -File android/build.ps1 -Sdk <SDK目录> -Jdk <JDK目录>`。
- K230：执行 `python scripts/build-k230-uart-sender.py` 生成独立UART脚本，源文件位于 `k230`。

外部工具链、固件和模型的具体入口见 [依赖清单](docs/dependencies.md)。这份工程包包含项目源码与正式运行文件，不附带第三方IDE、SDK安装目录。

## 四、查验文件

执行 `python scripts/source_manifest.py`，核对包内文件与 `SOURCE-MANIFEST.json` 的SHA-256。此操作只读文件，不连接或修改设备。

工程文件和运行文件分目录管理：`fpga`、`android`、`k230` 是可修改源码；`runtime` 是本次交付的运行文件。重新构建输出到各自 `build` 目录，不覆盖正式运行文件。
