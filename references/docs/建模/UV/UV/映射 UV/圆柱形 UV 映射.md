# 圆柱形 UV 映射

圆柱形映射基于圆柱形投影形状为对象创建 UV，该投影形状绕网格折回。该投影最适合完全封闭且在圆柱体中可见的图形，这些图形无需对部分进行投影或中空。

![图：（图旁无可取正文，Maya 手册 img 无 alt）](https://help.autodesk.com/cloudhelp/2022/CHS/Maya-Modeling/images/GUID-DECC5BCC-0C1B-4AAB-9A2C-2FE1DFB5B9BA.png) <!-- baize:img-hook downloaded=false reason="正文 375 字 ≥300，非承重" -->

1. 选择要将 UV 投影到的面。

2. 选择“UV > 圆柱形映射”(UV > Cylindrical Mapping)，或在“UV 编辑器”(UV Editor)的 “UV 工具包”(UV Toolkit)中，转到“创建 > 圆柱形”(Create > Cylindrical)。

3. 使用操纵器更改投影形状的位置和大小。

4. 使用 UV 编辑器以查看和编辑生成的 UV。

  ![图：使用 UV 编辑器以查看和编辑生成的 UV。 注： 投影映射每次仅在单个对象上正常工作。如果需要在单个步骤中将投影应用于…](https://help.autodesk.com/cloudhelp/2022/CHS/Maya-Modeling/images/GUID-60CC0788-CBC4-4B9B-9E39-3DBE1C1E4190.png) <!-- baize:img-hook downloaded=false reason="正文 375 字 ≥300，非承重" -->

  **注**

  投影映射每次仅在单个对象上正常工作。如果需要在单个步骤中将投影应用于多个多边形对象，请将这些对象组合为一个对象，并应用投影，然后将后面部分分离出去。否则，需在每个对象上分别执行投影。

## 相关主题

- [映射 UV](../映射%20UV.md)

- [平面 UV 映射](平面%20UV%20映射.md)

- [自动 UV 映射](自动%20UV%20映射.md)

- [圆柱形映射选项(Cylindrical Mapping options)](../../../多边形建模/多边形建模/多边形建模参考/“建模”%28Modeling%29菜单集/UV%20菜单/圆柱形映射选项%28Cylindrical%20Mapping%20options%29.md)
