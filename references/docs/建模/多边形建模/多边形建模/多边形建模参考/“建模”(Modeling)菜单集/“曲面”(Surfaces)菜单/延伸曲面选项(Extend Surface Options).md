# 延伸曲面选项(Extend Surface Options)

使用以下选项可设置在选择“曲面 > 延伸”(Surfaces > Extend)时发生的情况。

#### 扩展类型(Extension Type)

“切线”(Tangent)会向延伸后的曲面添加新的等参线。

“外推”(Extrapolate)会按照指定的方向和距离重建曲面，但不会添加新的等参线。

#### 距离(Distance)

设置延伸的长度。

#### 延伸侧面(Extend Side)

指定要延伸的侧面，起点是曲面上 U0 和 V0 的位置。延伸曲面后，“通道盒”(Channel Box)中会提供该选项。选择 extendSurfacen 节点可显示该选项。

#### 延伸方向(Extend Direction)

为要构建的延伸指定 U 和/或 V 方向。延伸曲面后，“通道盒”(Channel Box)中会提供该选项。选择 extendSurfacen 节点可显示该选项。

#### 接合到原始(Join to Original)

仅当“延伸侧面”(Extend Side)和“延伸方向”(Extend Direction)选项未设置为“二者”时才能禁用该选项。Maya 禁止选择“二者”(Both)作为“延伸侧面”(Extend Side)和“方向”(Direction)，从而导致“延伸曲面”(Extend Surfaces)创建未附加的分离曲面。

#### 保持原始(Keep Original)

该选项将导致“延伸曲面”(Extend Surfaces)在构建新曲面的同时保留原始曲面。如果希望丢弃原始曲面，请禁用该选项。

## 相关主题

- [延伸曲面](https://help.autodesk.com/cloudhelp/2022/CHS/Maya-Modeling/files/GUID-0B5F795A-38C7-46EE-94FE-F3C885EA585D.htm)
