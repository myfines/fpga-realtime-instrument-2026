# E049硬件连接表

信号以Dock实际球位丝印和 `fpga/constraints/instrument_e027_ext.cst` 为准；从正面、背面观看排针时左右会镜像。模块连接使用3.3V逻辑，接线时断电，所有信号模块共地。

|模块|模块信号|Dock / 对端|
|---|---|---|
|PCM5102A|DATA / BCK / LRCK|P6 / R8 / P8|
|PCM5102A|GND|公共GND|
|PCM5102A|供电 / 输出|模块USB供电；3.5mm输出接有源音箱|
|ADS1015|SCL / SDA|T6 / T7|
|ADS1015|VDD / GND / ADDR|3V3 / GND / GND，I²C地址0x48|
|摇杆|VRX / VRY|ADS1015 A0 / A1|
|摇杆|SW|T8|
|摇杆|VCC / GND|3V3 / GND|
|八路光键模块|SCL / SDA|T9 / P9，I²C地址0x12|
|八路光键模块|供电 / GND|本作品沿用现有3V3接法 / GND|
|OLED|SCL / SDA|T11 / P11|
|OLED|VCC / GND|3V3 / GND|
|ESP-01S|TX / RX|T12（FPGA接收）/ R11（FPGA发送）|
|ESP-01S|VCC / GND|3V3电源 / GND|
|K230|IO9 / UART1 TX|M14（FPGA接收）|
|K230|GND|公共GND|
|K230|IO10 / UART1 RX|不外接，当前为单向发送|

PCM5102A使用USB供电时，其额外3.3V电源排针不与其他电源并接。ESP的EN/RST启动条件按模块实际电路连接。外部5V电源不要直接接FPGA GPIO；模块替换时按其额定供电和I/O电平核对。

## PMOD1定位

背面视角、接口在下、PMOD排针在上时：

|行 / 从左向右|1|2|3|4|5|6|
|---|---|---|---|---|---|---|
|靠板边外排|P11|R11|M15|L13|GND|3V3|
|靠板中心内排|T12|T11|M14|M13|GND|3V3|

K230所接M14是内排第三个信号孔，不是外排M15。优先按球位丝印识别，不按杜邦线颜色识别。

## 板载控制

时钟H11，27MHz；S0～S3分别为T10 / T3 / T2 / D7。板载LED为L16 / L14 / N14 / N16。OLED承担波形、频谱、XY及精确键位指引，LED提供分组提示。
