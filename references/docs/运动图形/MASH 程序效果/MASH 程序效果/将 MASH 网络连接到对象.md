# 将 MASH 网络连接到对象

MASH 局部剖视图允许使用 MASH 网络在场景中的对象上驱动可设置动画的属性。如果要直接在对象而非实例上利用“噪波”(Noise)或“弹簧”(Spring)等常见的 MASH 效果，这将非常有用。

将对象连接到“局部剖视图”(Breakout)节点

1. 选择场景中的源对象。

2. 在“属性编辑器”(Attribute Editor)的“MASH_Breakout”选项卡中，在“连接的节点”(Connected Nodes)区域上单击鼠标右键并选择“连接”(Connect)。

  将显示[局部剖视图连接管理器(Breakout Connection Manager)](MASH%20参考/MASH%20窗口和编辑器/局部剖视图连接管理器%28Breakout%20Connection%20Manager%29.md)。

3. 在“局部剖视图连接管理器”(Breakout Connection Manager)的左侧面板中，选择连接的对象。

4. 在右侧面板的“从局部剖视图”(From Breakout)区域中选择一个属性（表示 MASH 网络），然后从“到当前选择”(To Selection)区域中选择一个属性（表示对象）。

  这两个属性已连接，使其中一个属性驱动另一个属性。

在“MASH_Breakout”选项卡的“连接的节点”(Connected Nodes)区域中，通过在现有连接上单击鼠标右键，然后选择“断开连接”(Break Connection)，可以断开这些连接。

## 相关主题

- [MASH 局部剖视图](MASH%20参考/MASH%20节点概述/添加工具/局部剖视图.md)

- [局部剖视图连接管理器(Breakout Connection Manager)](MASH%20参考/MASH%20窗口和编辑器/局部剖视图连接管理器%28Breakout%20Connection%20Manager%29.md)
