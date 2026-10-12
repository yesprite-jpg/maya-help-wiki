# “关节标签设置”(Joint Labelling)菜单

#### 添加关节标签(Add Joint Labels)

使用“添加关节标签”(Add Joint Labels)菜单，可以将标准、一致的标签指定给源的关节和目标骨架。

另请参见[设置骨架关节标签](../../../../使用骨架/使用骨架/重定目标角色动画/使用关节标签/设置骨架关节标签.md)。

#### 切换选定标签(Toggle Selected Labels)

在场景视图中显示或隐藏选定关节的关节标签。

#### 显示所有标签(Show All Labels)

显示场景视图中的所有关节标签。

#### 隐藏所有标签(Hide All Labels)

在场景视图中隐藏所有关节标签。

#### 根据标签重命名关节(Rename Joints From Labels)

将当前关节的名称更改为其关节标签。

例如，如果某个关节名为 joint2，而且其标签为 Shoulder (L)，则该关节的名称将更改为 LeftShoulder。

#### 基于关节名称设置标签(Label Based On Joint Names)

根据当前关节的关节名称更改其标签。例如，如果某个关节的标签为 Shoulder (L)且其关节名称为 Right_Hip，则关节的标签将更改为 Hip (R)。

若要使用该菜单项，需要满足下列条件：

- 关节的名称必须包含所需标签的名称。例如，如果希望关节的标签为 elbow，则关节名称中必须包含单词“elbow”。

- 如果希望关节标签为 left 或 right，则其名称必须包含单词“left”或“right”，或以字母“l”或“r”开始。

  **注**

  “基于关节名称设置标签”(Label Based On Joint Names)

  不会创建有效的全身 IK 关节标签。
