# “设置受驱动关键帧”(Set Driven Key)窗口

- （“动画”(Animation)菜单集）“关键帧 > 设置受驱动关键帧 > 设置”(Key > Set Driven Key > Set)

使用“设置受驱动关键帧”(Set Driven Key)窗口，可以链接对象，使一个对象的属性可以驱动或指定另一个对象的属性。请参见[受驱动关键帧](../受驱动关键帧.md)和[使用“受驱动关键帧”来链接属性](../设定关键帧/使用“设置受驱动关键帧”%28Set%20Driven%20Key%29来链接属性.md)。

| 目标 | 操作 |
|---|---|
| 加载链接到所选已加载受驱动对象的驱动者。 | 选择“加载 > 当前驱动者”(Load > Current Driver)。 在“驱动者”列表中将显示当前受驱动对象的驱动者。 |
| 仅加载选定对象的形状节点。 | 启用“选项 > 加载形状”(Options > Load Shapes)，然后单击“加载驱动者”(Load Driver)或“加载受驱动项”(Load Driven)。 |
| 将对象添加到现有“驱动者”(Driver)或“受驱动项”(Driven)列表中。 | 禁用“选项 > 加载时清除”(Options > Clear On Load)，然后单击“加载驱动者”(Load Driver)或“加载受驱动项”(Load Driven)。 |
| 列出选定对象的可设置关键帧或不可设置关键帧的属性。 | 若要列出可设置关键帧的属性，请启用“选项 > 显示不可设置关键帧的属性”(Options > Show Non-Keyable Attributes)。禁用此选项以列出不可设置关键帧的属性。 提示： 使用[通道控制编辑器](https://beehive.autodesk.com/community/service/rest/cloudhelp/resource/cloudhelpchannel/guidcrossbook/jsonp?v=2022&p=MAYAUL&l=CHS&accessmode=live&guid=GUID-5636D755-8FA3-4E72-83AD-A67956727D55)（“窗口 > 常规编辑器 > 通道控制”(Window > General Editors > Channel Control)）来控制属性是可设置关键帧的属性还是不可设置关键帧的属性。 |

## “驱动者”(Driver)列表

选定驱动者对象的名称显示在左列，对象的可设置关键帧属性显示在右列。在右列中选择其中一项属性作为驱动者属性。

## “受驱动”(Driven)项”列表

选定受驱动对象的名称显示在左列，对象的可设置关键帧属性显示在右列。在右列中选择其中一项属性作为“受驱动”(driven)项”属性。

## “加载”(Load)菜单

#### 作为驱动者选择(Selected as Driver)

将当前对象设定为驱动者对象。“作为驱动者选择”(Selected as Driver)的功能等效于单击“设置受驱动关键帧”(Set Driven Key)窗口中的“加载驱动者”(Load Driver)按钮。

#### 作为受驱动项选择(Selected as Driven)

将当前对象设定为受驱动对象。“作为受驱动项选择”(Selected as Driven)的功能等效于单击“设置受驱动关键帧”(Set Driven Key)窗口中的“加载受驱动项”(Load Driven)按钮。

#### 当前驱动者(Current Driver)

从驱动者列表中删除“当前驱动者”(current driver)。

## “选项”(Options)菜单

#### 加载时清除(Clear on Load)

启用时，加载驱动者或受驱动对象会导致删除“驱动者”(Driver)或“受驱动项”(Driven)列表中的当前内容。禁用时，加载驱动者或受驱动对象会导致“驱动者”(Driver)或“受驱动项”(Driven)列表中添加当前对象。

#### 加载形状(Load Shapes)

启用时，“驱动者”(Driver)或“受驱动”(Driven)项”列表的右手列中只会显示加载对象的形状节点属性。禁用时，“驱动者”(Driver)或“受驱动”(Driven)项”列表中只会显示加载对象的变换节点属性。

#### 自动选择(Auto Select)

启用时，如果在“设置受驱动关键帧”(Set Driven Keys)窗口中选定某一对象，则场景视图中会自动选择该对象。禁用时，如果在“设置受驱动关键帧”(Set Driven Keys)窗口中选定某一对象，则场景视图中不会自动选择该对象。

#### 显示不可设置关键帧的属性(Show Non-Keyable Attributes)

启用时，“驱动者”(Driver)或“受驱动”(Driven)项”列表的右手列中只会显示加载对象的可设定关键帧属性。禁用时，“驱动者”(Driver)或“受驱动”(Driven)项”列表的右手列中会显示加载对象的所有可设定关键帧属性和非可设定关键帧属性。请参见[编辑对象的可设定关键帧能力](../设定关键帧/使通道可设置关键帧或不可设置关键帧.md)。

**注**

在 Maya 的早期版本中，

“显示不可设置关键帧的属性”(Show Non-Keyable Attributes)

称为

“列出可设置关键帧的受驱动属性”(List Keyable Driven Attributes)

。该名称已更改，旨在反映此设置过滤仅显示无法设置关键帧的属性。

## “关键帧”(Key)菜单

#### 设定(Set)

用它们的当前值链接所选“驱动者”(Driver)和“受驱动”(Driven)项”对象的属性。其功能等效于单击“设置受驱动关键帧”(Set Driven Key)窗口中的“加载”按钮。

#### “转到上一个”(Go to Previous)和“转到下一个”(Go to Next)

循环查看当前对象受驱动属性的所有关键帧，并查看每一个关键帧处对象的状态。请参见[使用受驱动关键帧来链接属性](../设定关键帧/使用“设置受驱动关键帧”%28Set%20Driven%20Key%29来链接属性.md)，以了解有关查看受驱动对象的信息。

## “选择”(Select)菜单

#### 受驱动项目(Driven Items)

在场景视图的“受驱动”(Driven)项”列表中选择当前对象。例如，如果在“受驱动项”列表中选定了圆锥体 1，则通过选择“菜单”(menu) >“受驱动项目”(Driven Items)选择场景视图中的圆锥体 1。
