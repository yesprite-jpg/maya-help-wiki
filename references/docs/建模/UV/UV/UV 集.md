# UV 集

可以使用 UV 集为曲面网格创建 UV 纹理坐标的多个排列。如果对象需要为不同的纹理（称为“多重纹理”）使用多个 UV 布局，则 UV 集十分有用。

例如，如果创建砖墙，并且需要在顶部分层喷洒绘制，则通过使用分层纹理，可以为砖和绘制分别使用不同的纹理。如果砖纹理重复，但绘制纹理不重复，则每个纹理需使用不同的 UV 布局（UV 集）。

如果计划在场景中将曲面预照明（也称为“灯光烘焙”），则需使用 UV 集将多边形网格的渲染外观中的着色和照明颜色直接存储在该网格的逐顶点信息中。。

![图：（图旁无可取正文，Maya 手册 img 无 alt）](https://help.autodesk.com/cloudhelp/2022/CHS/Maya-Modeling/images/GUID-240372D2-D07F-42B3-836D-4736EB4223B9.png) <!-- baize:img-hook downloaded=false reason="正文 622 字 ≥300，非承重" -->

设置多重纹理的主要步骤如下所示：

- 将多个纹理指定给对象的材质。

  这些纹理可以指定给不同的材质属性，例如，“颜色”(Color)和“白炽度”(Incandescence)，也可以使用“分层纹理”(Layered Texture)节点指定给单个属性。

- 创建含有不同布局的 UV 集。

- 使用“关系编辑器”(Relationship Editor)将每个 UV 集链接到给定的纹理。

## 示例

以下示例显示用来纹理砖墙的 UV 集。在两个示例中，UV 集包括：

- unitizedUV — 用于重复的砖纹理。

- planarUV — 用于非重复的纹理。

### 颜色和透明度的 UV 集

在该示例中，UV 集将连接到材质的不同属性（“颜色”(Color)和“透明度”(Transparency)）中的纹理。

![图：（图旁无可取正文，Maya 手册 img 无 alt）](https://help.autodesk.com/cloudhelp/2022/CHS/Maya-Modeling/images/GUID-5CC19C9B-6535-46D3-843A-C0410705B422.png) <!-- baize:img-hook downloaded=false reason="正文 622 字 ≥300，非承重" -->

### 分层纹理的 UV 集

在该示例中，UV 集已连接到分层纹理。

![图：（图旁无可取正文，Maya 手册 img 无 alt）](https://help.autodesk.com/cloudhelp/2022/CHS/Maya-Modeling/images/GUID-B1C1C471-B3D9-4267-BF2E-83F803909FAC.png) <!-- baize:img-hook downloaded=false reason="正文 622 字 ≥300，非承重" -->

### 相关主题

- [创建 UV 集](UV%20集/创建%20UV%20集.md)

- [在 UV 集之间切换](UV%20集/在%20UV%20集之间切换.md)

- [复制、重命名或删除 UV 集](UV%20集/复制、重命名或删除%20UV%20集.md)

- [将纹理指定给 UV 集](UV%20集/将纹理指定给%20UV%20集.md)

- [将 UV 从一个 UV 集复制到另一个 UV 集](UV%20集/将%20UV%20从一个%20UV%20集复制到另一个%20UV%20集.md)
