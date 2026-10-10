# 球形 UV 映射

球形映射使用基于球形图形的投影为对象创建 UV，该球形图形绕网格折回。该投影最适合完全封闭且在球体中可见的图形，这些图形无需对部分进行投影或中空。

![图：（图旁无可取正文，Maya 手册 img 无 alt）](https://help.autodesk.com/cloudhelp/2022/CHS/Maya-Modeling/images/GUID-5129DE92-FF04-4A28-BFEA-512EFD7E8953.png) <!-- baize:img-hook downloaded=false reason="正文 375 字 ≥300，非承重" -->

使用球形映射技术创建 UV

1. 选择要将 UV 投影到的面。

2. 选择“UV > 球形映射”(UV > Spherical Mapping)，或在“UV 编辑器”(UV Editor)的“UV 工具包”(UV Toolkit)中，转到“创建 > 球形”(Create > Spherical)。

3. 使用操纵器更改投影形状的位置和大小。

4. 使用 UV 编辑器以查看和编辑生成的 UV。

  ![图：使用 UV 编辑器以查看和编辑生成的 UV。 注： 投影映射每次仅在单个对象上正常工作。如果需要在单个步骤中将投影应用于…](https://help.autodesk.com/cloudhelp/2022/CHS/Maya-Modeling/images/GUID-B03524E9-1BB5-4EB3-A6D6-1D0DB27C6AAC.png) <!-- baize:img-hook downloaded=false reason="正文 375 字 ≥300，非承重" -->

  **注**

  投影映射每次仅在单个对象上正常工作。如果需要在单个步骤中将投影应用于多个多边形对象，请将这些对象组合为一个对象，并应用投影，然后分离后面部分。否则，需在每个对象上分别执行投影。

## 相关主题

- [映射 UV](../映射%20UV.md)

- [球形映射选项(Spherical Mapping options)](../../../多边形建模/多边形建模/多边形建模参考/“建模”%28Modeling%29菜单集/UV%20菜单/球形映射选项%28Spherical%20Mapping%20options%29.md)

- [平面 UV 映射](平面%20UV%20映射.md)

- [自动 UV 映射](自动%20UV%20映射.md)
