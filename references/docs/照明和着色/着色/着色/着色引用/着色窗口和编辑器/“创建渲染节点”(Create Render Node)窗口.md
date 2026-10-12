# “创建渲染节点”(Create Render Node)窗口

“创建渲染节点”(Create Render Node)窗口提供对材质、纹理、灯光以及可在“Hypershade”中创建和自定义的工具节点的访问。表示节点的图标将显示在每个选项卡下方。

若要打开“创建渲染节点”(Create Render Node)窗口，从“Hypershade”中选择“创建 > 创建渲染节点”(Create > Create Render Node)。

**注**

“创建渲染节点”(Create Render Node)

窗口的功能与

Hypershade

中的

“创建”(Create)

选项卡以及

“创建节点”(Create Node)

窗口（

“窗口 > 创建节点”(Window > Create Node)

）的功能相同。

## 选项菜单

#### 包括带材质的着色组(Include Shading Group with Materials)

启用此选项后，创建材质节点时自动创建着色组。有关“着色组”(Shading Group)的详细信息，请参见[关于着色网络](../../关于着色和纹理曲面/将颜色和着色应用于对象/关于着色网络.md)。

若要在“Hypershade”中显示着色组图标，请单击[图表 > 输入和输出连接(Graph > Input and Output Connections)](Hypershade%20窗口/“Hypershade”菜单/Hypershade%20图形菜单.md#GUID-5B06BA8F-3585-437B-97AD-7C978359BEB9__GUID-F3FD0088-4986-4CAD-A3C7-794887622F3D)按钮。

#### 包括带纹理的放置(Include Placement with Textures)

启用该选项时，Maya 会在您创建纹理渲染节点时自动创建一个纹理放置节点。默认设置为启用。

## 搜索渲染节点

输入要创建的渲染节点关键字。当输入关键字时，“创建”(Create)选项卡的右侧面板会实时更新，并且仅显示名称与输入内容匹配的渲染节点。

![图：（图旁无可取正文，Maya 手册 img 无 alt）](https://help.autodesk.com/cloudhelp/2022/CHS/Maya-LightingShading/images/GUID-E85BADAD-A8F7-406B-9F34-4540624E4B0C.png) <!-- baize:img-hook downloaded=false reason="正文 1899 字 ≥300，非承重" -->

也可以使用搜索区域清除选择。选择一个或多个分区时，右侧面板中仅显示选定区域中的节点。若要清除选择，请在搜索区域按 Enter 键。

## 收藏夹

可以创建“收藏夹”(Favorites)列表，以便轻松访问最常用的着色器。

若要将着色器添加到“收藏夹”(Favorites)列表，请使用鼠标中键将着色器拖动到“收藏夹”(Favorites)。或者，可以在着色器上单击鼠标右键，然后选择“添加到收藏夹”(Add to favorites)。“创建渲染节点”(Create Render Node)窗口将收藏按类别进行排序，以便您轻松地找到着色器。

有关收藏夹的详细信息，请参见[创建和使用收藏夹](../../关于着色和纹理曲面/使用%20Hypershade%20的外观开发/使用%20Hypershade%20构建和创建材质/创建和使用收藏夹.md)。

**注**

通过

“Hypershade”

窗口和

“指定新材质”(Assign New Material)

窗口，也可以创建

“收藏夹”(Favorites)

列表。在

“创建渲染节点”(Create Render Node)

窗口中创建的任何

“收藏夹”(Favorites)

列表，也可以显示在另外两个窗口中，反之亦然。

## Maya

#### 表面(Surface)

描述表面的物理外观。有关详细信息，请参见[关于表面材质](https://help.autodesk.com/cloudhelp/2022/CHS/Maya-LightingShading/files/GUID-634CAFBE-AC48-4B73-89CA-82D64FA1BC70.htm)。

#### 体积(Volumetric)

描述占用一卷空间的现象的物理外观（例如，雾或粒子）。有关详细信息，请参见[关于体积材质](https://help.autodesk.com/cloudhelp/2022/CHS/Maya-LightingShading/files/GUID-6FF09EBA-CD7C-45B7-8B49-305D748EE7B4.htm)。

#### 位移(Displacement)

更改几何体的表面。在轮廓中查看时，可以看到表面的置换。有关详细信息，请参见[关于置换材质](https://help.autodesk.com/cloudhelp/2022/CHS/Maya-LightingShading/files/GUID-204712F3-344B-4A41-9399-51B2BD19A3F7.htm)。

#### 2D 纹理(2D Textures)

2D 图案使用图像文件（文件纹理）或计算机图形程序来模拟各种类型的表面材质。请参见 [2D 和 3D 纹理](../../关于着色和纹理曲面/纹理/2D%20和%203D%20纹理.md)。

#### 3D 纹理(3D Textures)

3D 图案使用计算机图形程序来模拟实体材质（例如，木材或大理石）。将 3D 纹理映射到曲面时，曲面看起来像从材质中雕刻而出。请参见 [2D 和 3D 纹理](../../关于着色和纹理曲面/纹理/2D%20和%203D%20纹理.md)。

#### 环境纹理(Env Textures)

使用一系列图像文件（“环境球”(Env Ball)、“环境立方体”(Env Cube)和“环境球体”(Env Sphere)）或计算机图形程序（“环境铬”(Env Chrome)和“环境天空”(Env Sky)）模拟 3D 空间。请参见[环境纹理](../../关于着色和纹理曲面/纹理/2D%20和%203D%20纹理.md#WS17956D7ADBC6E736-51D3585C117AE33DCFA-7FE5)。

#### 其他纹理(Other Textures)

“分层纹理”(Layered Texture)提供了到达层属性的便捷方式。可以创建一种由场景中已存在的两种或多种纹理组成的纹理，并可以控制这两种材质的合成方式。请参见[分层纹理](../../关于着色和纹理曲面/纹理/2D%20和%203D%20纹理.md#WS17956D7ADBC6E736-51D3585C117AE33DCFA-7FE4)。

#### 灯光(Lights)

曲面由从这些光源直接发射而出的光线照亮。使用灯光相关联的属性和特性，可模拟出不同类型的真实光源以及特殊效果。

有关光源及其属性的详细信息，请参见[直接光源](../../../../照明/照明/照明基础知识/直接光源.md)。

#### 工具(Utilities)

在增强和融合不同属性和纹理的工具中选择，或进行颜色修正和增强纹理颜色。请参见[工具节点](https://help.autodesk.com/cloudhelp/2022/CHS/Maya-LightingShading/files/GUID-DA9707D2-8A0D-4911-A010-8274C57D3FD3.htm)。

#### 图像平面(Image Planes)

控制的图像平面的外观和放置。可将纹理或图像文件指定给图像平面以创建场景背景。

有关详细信息，请参见[创建、编辑或定位图像平面](https://help.autodesk.com/cloudhelp/2022/CHS/Maya-LightingShading/files/GUID-F72F8E1B-EFFE-400E-BD92-5441BE9CD28F.htm)。

#### 辉光(Glow)

当灯光直接照入摄影机时，就会产生辉光、光晕或镜头光斑等光学效果。光学效果可添加到任何灯光。

有关详细信息，请参见[辉光、光晕和镜头光斑](../../../../照明/照明/调整照明/辉光、光晕和镜头光斑.md)。
