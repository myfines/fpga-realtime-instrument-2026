# 外部依赖与获取入口

|依赖|用途 / 对应版本|获取入口|
|---|---|---|
|Gowin EDA与Programmer|正式文件由V1.9.11.03 Education生成；GW2A-18C / GW2A-LV18PG256C8/I7|https://www.gowinsemi.com.cn/|
|Tang Primer 20K文档|板卡接口和下载流程|https://github.com/sipeed/TangPrimer-20K-example|
|JDK|17及以上，Android源码构建|https://adoptium.net/|
|Android SDK|平台37、Build Tools 36.0.0，按构建脚本配置|https://developer.android.com/tools|
|Icarus Verilog|RTL离线仿真，交付检查使用13.0|https://github.com/steveicarus/iverilog|
|Python|电脑端脚本与测试使用Python 3|https://www.python.org/|
|CanMV固件与运行库|需与亚博K230模块、摄像头及屏幕匹配|https://www.yahboom.net/study/K230/|
|手部检测与关键点模型|`hand_det.kmodel`、`handkp_det.kmodel`|https://www.yahboom.net/study/K230/15032/|
|CanMV AI示例文档|手部关键点双模型与依赖说明|https://www.kendryte.com/k230_canmv/en/v1.2/example/ai/AI_Demo_User_Manual.html|

Gowin EDA、Android SDK、CanMV固件及模型采用各原提供方的许可；本包不重打包第三方IDE、SDK或固件安装目录。K230模型放到 `/sdcard/kmodel`，项目Python入口见部署指南。原厂已有匹配模型与库时沿用现有环境。

`runtime/k230/sdcard/k230_hand_keypoint_official.py` 是本项目保存的厂商示例类参考，权利归原提供方；`pinch_preview_v2.py` 在该类之上实现本项目的识别筛选与控制逻辑。外部模型文件由原厂资源取得，未附带于本包。
