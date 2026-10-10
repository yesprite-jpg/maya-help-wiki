# 创建 UV

在 Maya 中，可以使用以下 UV 映射技术为多边形曲面网格创建 UV 纹理坐标 (UV)：

- [自动 UV 映射](映射%20UV/自动%20UV%20映射.md)

- [平面 UV 映射](映射%20UV/平面%20UV%20映射.md)

- [圆柱形 UV 映射](映射%20UV/圆柱形%20UV%20映射.md)

- [球形 UV 映射](映射%20UV/球形%20UV%20映射.md)

- [用户定义的 UV 映射](映射%20UV/用户定义的%20UV%20映射.md)

- [最佳平面映射](映射%20UV/最佳平面%20UV%20映射.md)

- 摄影机 UV 映射 - 请参见[平面 UV 映射](映射%20UV/平面%20UV%20映射.md)

每种 UV 映射技术为曲面网格生成 UV 纹理坐标，方法是根据曲面网格固有的投影方法，将 UV 纹理坐标投影到曲面网格上。但是，通过上述 UV 映射技术生成的初始映射通常不会产生纹理所需的最终 UV 排列。因此，通常需要使用 [UV 编辑器](“UV%20编辑器”%28UV%20Editor%29概述.md)对 UV 执行进一步的编辑操作。 最好仅在已完成的模型上映射 UV。

**注**

多边形和细分曲面基本体具有默认的 UV 纹理坐标，可用于纹理映射。但是，如果以任何方式（即缩放、挤出面、插入或删除边）修改默认的基本体，则需要将一组新的 UV 纹理坐标映射到对象，以适合您的纹理映射要求。

## 相关主题

- [映射 UV](映射%20UV.md)

- [查看 UV 并求值](查看%20UV%20并求值.md)

- [UV 编辑器概述](“UV%20编辑器”%28UV%20Editor%29概述.md)

- ![图：Maya 教学频道：展开 UV 网格](https://help.autodesk.com/cloudhelp/2022/CHS/Maya-Modeling/images/GUID-03430D01-DE17-4A95-936F-1C9085FDCF84.png) <!-- baize:img-hook downloaded=false reason="正文 371 字 ≥300，非承重" --> [Maya 教学频道：展开 UV 网格](https://www.youtube.com/playlist?list=PL8hZ6hQCGHMX7JjZTmz5Dke-NFfBvL8Wu)
