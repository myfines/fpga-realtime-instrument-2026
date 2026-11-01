# 浏览器控制与可选中继

`index.html` 是设备本地HTTP控制页面，`relay.html` 是可选HTTP中继的浏览器界面。正式热点直连版本由 `fpga/tools/build.tcl` 构建，手机App可直接连接设备，无须部署公网服务。

`tools/build_web_rom.py` 将本地页面编码为FPGA HTTP响应ROM，并更新AT控制模块中的响应长度常量。运行前先保存现有 `src/esp_http_rom.v` 和 `src/esp_at_control.v`，生成后按正式工程重新构建。

`tools/web_relay.py`、`recording_store.py` 提供可选HTTP中继与短录音数据存储；命令行参数见 `python fpga/tools/web_relay.py --help`。访问令牌与网络配置由部署者自行设置，不随源码提供。原生 TCP 热点直连 App 与浏览器 HTTP 控制属于不同入口。

云端扩展源文件 `src/instrument_cloud_top.v` 使用 `tools/build_cloud_config.py` 生成的配置模块；此扩展不是正式热点工程的构建依赖。需要使用时，按脚本字段提供自己的配置并在本机生成，不要提交包含个人凭据的文件。
