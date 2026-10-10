# 将 NURBS 曲面转化为多边形网格

无论 NURBS 曲面是在 Maya 中创建的还是从另一个 3D 应用程序导入的，均可将其转化为多边形网格。此过程也会将修剪曲面转化。

如果 NURBS 曲面应用了纹理，则会将该纹理指定给新的多边形对象。NURBS 到多边形动作可将 NURBS UV 值烘焙到对应的多边形顶点上。

将 NURBS 转化为多边形

1. 选择 NURBS 曲面，然后选择“修改 > 转化 > NURBS 到多边形”(Modify > Convert > NURBS to Polygons)。

  此时将在与 NURBS 曲面相同的位置创建曲面的多边形表示。

  ![图：选择 NURBS 曲面，然后选择“修改 转化 NURBS 到多边形”(Modify Convert NURBS to P…](https://help.autodesk.com/cloudhelp/2022/CHS/Maya-Modeling/images/GUID-21734969-4F76-41C0-896F-1EB786A9148B.png) <!-- baize:img-hook downloaded=false reason="正文 641 字 ≥300，非承重" -->

如果转化 NURBS 曲面时构建历史处于启用状态，则可以编辑 NURBS 曲面，并重新创建多边形曲面以进行匹配。

## 注释

- 如果使用“NURBS 到多边形”功能将 NURBS 曲面转化为多边形对象，并且已修改 NURBS 曲面的历史以生成无效 (Null) NURBS 曲面，则会显示以下警告消息：

  警告: nurbsTesselate1 (Nurbs 镶嵌节点): 输入 NURBS 曲面无效。

  并且将无法成功执行 NURBS 到多边形操作。生成的多边形对象仍将是最后一个可见的有效（被计算的）多边形曲面。

- 在某些情况下，将多个 NURBS 面片转化为单个多边形网格时，可能会注意到网格上奇怪的着色效果。这是由于法线所引起的。若要调整由于法线引起的着色问题，请参见[填充多边形网格中的洞](../../编辑多边形/修改多边形网格/填充多边形网格中的洞.md)。

- NURBS 到多边形转化不会考虑修复纹理扭曲属性（该属性可调整纹理的 UV 参数，以便纹理不依赖于 NURBS 对象的 UV 参数化）。

### 相关主题

- [“NURBS 到多边形”(NURBS to Polygons)选项](https://beehive.autodesk.com/community/service/rest/cloudhelp/resource/cloudhelpchannel/guidcrossbook/jsonp?v=2022&p=MAYAUL&l=CHS&accessmode=live&guid=GUID-DC38BD08-A411-4403-8C59-104337673266)
