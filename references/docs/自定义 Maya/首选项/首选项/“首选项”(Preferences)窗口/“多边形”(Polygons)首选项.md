# “多边形”(Polygons)首选项

可以在[首选项(Preferences)窗口](../“首选项”%28Preferences%29窗口.md)的“多边形”(Polygons)类别中设置以下首选项。

若要返回到出厂默认设置，请在此窗口中选择“编辑 > 还原默认设置”(Edit > Restore Default Settings)。请注意，这将重置“首选项”(Preferences)窗口中每个类别的首选项。

## 多边形显示(Polygon Display)

#### 顶点(Vertices)

指定希望顶点显示的方式：

#### 显示(Display)

启用或禁用顶点的显示。

#### 法线(Normals)

启用或禁用显示顶点法线。

#### 背面消隐(Backculling)

使顶点在法线背离摄影机的区域中不可见。

#### 顶点大小(Vertex Size)

可用于调整新多边形的顶点大小。

#### 边(Edges)

指定希望边显示的方式：

#### 标准(Standard)

以相同方式显示所有边（硬或软）。

#### 软/硬(Soft/Hard)

将软边显示为虚线，将硬边显示为线框。

#### 硬边(颜色)(Hard (colors))

将硬边显示为彩色线，将软边显示为线框。请参见[以自定义颜色显示硬边](https://beehive.autodesk.com/community/service/rest/cloudhelp/resource/cloudhelpchannel/guidcrossbook/jsonp?v=2022&p=MAYAUL&l=CHS&accessmode=live&guid=GUID-D23D15E0-8E14-4A4F-892E-2413FA58D85A)。

#### 硬边(Hard)

将硬边显示为彩色线。软边仍可以亮显和选择，但是在网格上不显示。

#### 亮显(Highlight)

指定希望亮显多边形的方式：

#### 边界边(Border edges)

显示较粗的外部边，以使它们在进行某些操作时更为明显。

#### 纹理边界(Texture borders)

显示粗边界，以亮显某个纹理按多边形或按顶点影响的区域。

#### 折痕边(Crease edges)

显示多边形折痕边，亮显（较粗和粗体）或无亮显。可以在“显示 > 多边形 > 自定义多边形显示”(Display > Polygons > Custom Polygon Display)选项对话框（它影响当前选定的对象的位置）中以及在此处启用和禁用该选项。该首选项会影响任何新创建的多边形对象，而不影响现有对象。

#### 边宽度(Edge Width)

指定多边形边的宽度。范围为从 1 到 10。

#### 面(Faces)

指定希望面显示的方式：

#### 中心(Centers)

显示小方形以指示面中心。

#### 法线(Normals)

在每个多边形的中心处显示法线。

#### 三角形(Triangles)

将所有多边形显示为三角形。

#### 非平面(Non-planar)

用染色的颜色来显示非平面的面，以易于识别。非平面的面具有位于面的平面外部的顶点。通过确定和消除非平面的面，可以避免因以后重新定形该曲面而产生异常结果。

#### 显示项目编号(Show item numbers)

指定要显示项目编号的位置：在每个顶点处，在每条边处，在每个面上，或者在每个 UV 处。

#### 法线大小(Normals size)

指定法线的显示大小。范围为从 0.1 到 10。

#### UV 大小(UV Size)

指定 UV 在主面板和“UV 纹理编辑器”(UV Texture Editor)中显示的大小。

#### 颜色(Color)

启用“彩色着色”(Colored Shading)可使用“应用颜色”(Apply Color)操作（“网格显示 > 应用颜色”(Mesh Display > Apply Color)）。有关详细信息，请参见[应用颜色选项(Apply Color Options)](https://beehive.autodesk.com/community/service/rest/cloudhelp/resource/cloudhelpchannel/guidcrossbook/jsonp?v=2022&p=MAYAUL&l=CHS&accessmode=live&guid=GUID-FB177486-E576-4C30-AD7E-94D662FFAF17)。

#### 对材质上色(Color material)

这些菜单选项会覆盖任何现有材质通道，并会使用指定的顶点颜色替换它们。对于“无”之外的所有选项，照明会影响对象的着色。

#### 无(None)

不会使用指定给对象的着色器的任何材质属性。在这种情况下，照明也会被禁用。

#### 环境光(Ambient)

顶点颜色会覆盖指定的着色器的环境光材质通道。

#### 环境光 + 漫反射(Ambient + Diffuse)

顶点颜色会覆盖指定的着色器的环境光和漫反射材质通道。

#### 漫反射(Diffuse)

顶点颜色会覆盖指定的着色器的漫反射材质通道。

#### 镜面反射(Specular)

顶点颜色会覆盖指定的着色器的镜面反射材质通道。

#### 发射(Emission)

顶点颜色会覆盖指定的着色器的发射材质通道。

#### 材质融合(Material blend)

在硬件中渲染材质融合。有关“材质融合”(Material Blend)的工作原理的详细信息，请参见[材质融合设置选项(Material Blend Setting Options)](https://beehive.autodesk.com/community/service/rest/cloudhelp/resource/cloudhelpchannel/guidcrossbook/jsonp?v=2022&p=MAYAUL&l=CHS&accessmode=live&guid=GUID-B62EED3D-CCE7-4A06-B057-856276653459)。“网格显示 > 材质融合设置”(Mesh Display > Material Blend Setting)中也提供了这些选项。

#### 颜色集仅包含 Alpha 时将 Alpha 显示为灰度(Display Alpha as Grey Scale if Color Set Contains Only Alpha)

在场景视图中，将仅包含 Alpha 的颜色集显示为灰度。

#### 背面消隐(Backface culling)

指定背面消隐的显示：

#### 禁用(Off)

不会发生背面消隐。这是默认设置。

#### 启用(On)

曲面在法线背离摄影机的区域中变得不可见。

#### 保持线框(Keep wire)

显示线框轮廓，但会隐藏法线背离摄影机的所有区域。

#### 保持硬边(Keep hard edges)

仅为软边设定背面消隐。有关多边形建模的详细信息，请参见“多边形建模”。

#### 细分方法(Subdivision Method)

设置新多边形对象的默认细分方法。默认值为 OpenSubdiv Catmull-Clark。

**注**

这可以在各个对象的

“平滑网格”(Smooth Mesh)

选项中进行更改。
