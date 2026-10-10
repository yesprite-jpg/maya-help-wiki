# 确认 UV 放置

如果希望纹理正确地显示在网格的曲面上，确认 UV 是否正确定位是关键。确认 UV 放置的方法之一就是应用临时纹理贴图，然后可以使用该贴图对模型上可能的扭曲求值。为此专门创建了两个着色器：棋盘格和扭曲。

将临时贴图应用于 UV 壳

1. 选择网格。

2. 打开 UV 编辑器。

3. 单击“棋盘格着色器”(Checker Shader) (![图：单击“棋盘格着色器”(Checker Shader) () 或“扭曲着色器”(Distortion Shader) ()…](https://help.autodesk.com/cloudhelp/2022/CHS/Maya-Modeling/images/GUID-96307EC3-7425-4FA5-BEEB-40BAF69406D6.png) <!-- baize:img-hook downloaded=false reason="正文 301 字 ≥300，非承重" -->) 或“扭曲着色器”(Distortion Shader) (![图：单击“棋盘格着色器”(Checker Shader) () 或“扭曲着色器”(Distortion Shader) ()…](https://help.autodesk.com/cloudhelp/2022/CHS/Maya-Modeling/images/GUID-6EF6E8DD-7A18-428C-BFF5-7091B93B2C74.png) <!-- baize:img-hook downloaded=false reason="正文 301 字 ≥300，非承重" -->) 按钮。

![图：（图旁无可取正文，Maya 手册 img 无 alt）](https://help.autodesk.com/cloudhelp/2022/CHS/Maya-Modeling/images/GUID-D185CCE6-D2B1-4CF5-B93F-77EF87C4B25C.png) <!-- baize:img-hook downloaded=false reason="正文 301 字 ≥300，非承重" -->

棋盘格着色器允许通过查看彩色方块扭曲的位置，对扭曲区域进行求值。

扭曲着色器将特定颜色应用于拉伸或压缩 UV 壳的区域（分别为红色和蓝色）。为了避免扭曲，您将需要移动 UV，直到 UV 壳的大部分为白色。

## 相关主题

- [映射 UV](../映射%20UV.md)

- [平面 UV 映射](平面%20UV%20映射.md)

- [圆柱形 UV 映射](圆柱形%20UV%20映射.md)

- [球形 UV 映射](球形%20UV%20映射.md)
