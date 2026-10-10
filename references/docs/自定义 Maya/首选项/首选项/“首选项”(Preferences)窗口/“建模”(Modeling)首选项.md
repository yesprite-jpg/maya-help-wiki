# “建模”(Modeling)首选项

可以在[首选项(Preferences)窗口](../“首选项”%28Preferences%29窗口.md)的“建模”(Modeling)类别中设置以下首选项。

若要返回到出厂默认设置，请在此窗口中选择“编辑 > 还原默认设置”(Edit > Restore Default Settings)。请注意，这将重置“首选项”(Preferences)窗口中每个类别的首选项。

## 输出几何体类型(Output Geometry Type)

#### 将几何体输出为(Output geometry as)

通过这些设置，可以确定通过建模操作（例如旋转、放样、挤出、圆角融合等等）创建的几何体类型。此处的设置将影响所有适用的建模操作。否则，请选择“混合”(Mixed)，以便单独使用各建模操作的设置。

## NURBS 交互(NURBS Interaction)

#### 交互模式(Interaction mode)

确定是否需使用类似操作或工具的特定 NURBS 建模命令。通过操作，可以对选定的对象采用离散函数。通过工具，可以操纵对象，直到完成操作。当您能够熟练地运用 Maya 的 NURBS 建模功能时，您可能希望将操作更改为工具。

若要全局更改适用的建模工具，请选择“全部为工具”(Everything is a Tool)或“全部为操作”(Everything is an Action)。若要分别设置每个命令，请选择“混合”。

## 多边形(Polygons)

#### 转化组件选择(Convert component selection)

如果某项操作只作用于组件，则启用“转化组件选择”(Convert component selection)，以使 Maya 自动将对象选择转化为适当的组件选择模式。

例如，如果选择一个多边形对象并尝试挤出面，则 Maya 将自动选择对象上的所有面，然后继续。

#### 创建单面网格(Create meshes single sided)

启用此选项后，新的多边形网格（例如，通过多边形基本体工具或多边形操作创建的网络）将自动关闭“渲染统计信息 > 双面”(Render Stats > Double Sided)属性。

#### 智能命令设置(Smart command settings)

根据所执行操作的种类修改多边形设置：

可选择下列选项：

- 设置显示属性以显示与操作相关的多边形组件（例如，显示法线或边界边）。

- 将选择遮罩设定为适合操作的对象/组件。

- 设置选择约束，使操作具有含义。

#### 自动顶点颜色显示(Automatic vertex color display)

如果启用该选项，Maya 会自动修改以下设置来使顶点颜色可见：

- 视口着色模式设置为“对所有项目进行平滑着色处理”(Smooth Shade All)。

- 活动对象的“网格组件显示 > 显示颜色”(Mesh Component Display > Display Colors)属性处于启用状态。

“自动顶点颜色显示”(Automatic vertex color display)在默认情况下处于启用状态。

#### 保持面的连接性(Keep faces together)

指定是保留每个面的边还是仅保留沿着所选边界边的那些面。请参见[保持面的连接性(Keep Faces Together)](https://beehive.autodesk.com/community/service/rest/cloudhelp/resource/cloudhelpchannel/guidcrossbook/jsonp?v=2022&p=MAYAUL&l=CHS&accessmode=live&guid=GUID-2D20D2B8-4B0D-465C-A244-67A9BC608663)。

#### 顶点法线方法(Vertex Normal Method)

用于为多边形网格设置默认的顶点法线方法。

#### 未加权(Unweighted)

该方法从每个连接的面获取法线，并将其加到一起。这是 Maya 2013 之前版本的默认方法。如果需要匹配来自较旧 Maya 版本的文件，请选择此首选项。

#### 加权角度(Angle Weighted)

此方法将计算多边形角点的角度，并将其用作权重。

#### 加权区域(Area Weighted)

此方法将使用每个相邻面的曲面面积作为权重。因此，小多边形对结果的影响很小，大多边形对结果的影响很大。

#### 加权角度和区域(Angle and Area Weighted)

此方法将“加权角度”(Angle Weighted)和“加权区域”(Area Weighted)求值方法组合在一起。这是默认方法。

#### 细分方法(Subdivision Method)

在平滑网格预览模式下，为所有现有对象和新对象设定全局细分方法。请参见[平滑网格预览概述](https://help.autodesk.com/cloudhelp/2022/CHS/Maya-Customizing/files/GUID-4863E5AE-0EA0-4596-B1AE-10C19603838E.htm)。

#### Maya Catmull-Clark

使用 Maya 的 Catmull-Clark 算法实施平滑网格的面。

有关详细信息，请参见 [Maya Catmull-Clark 控件](https://help.autodesk.com/cloudhelp/2022/CHS/Maya-Customizing/files/GUID-FF35F773-1FC0-4EBA-A64C-6199375F489A.htm#GUID-FF35F773-1FC0-4EBA-A64C-6199375F489A__WS73099CC142F48755-7B21313411809411AE9-705C)。

**注**

在 Maya 2014 和早期版本中，

“Maya Catmull-Clark”

是默认的细分方法。

#### OpenSubdiv Catmull-Clark

（默认）将统一的细化方案应用于网格的面，同时以相同的量细分整个网格。请参见 [OpenSubdiv 概述](https://beehive.autodesk.com/community/service/rest/cloudhelp/resource/cloudhelpchannel/guidcrossbook/jsonp?v=2022&p=MAYAUL&l=CHS&accessmode=live&guid=GUID-909B2D5F-D031-4372-B2D7-7D8BCCBE3183)。

有关“OpenSubdiv Catmull-Clark”选项的详细信息，请参见 [OpenSubdiv 控件](https://help.autodesk.com/cloudhelp/2022/CHS/Maya-Customizing/files/GUID-FF35F773-1FC0-4EBA-A64C-6199375F489A.htm#GUID-FF35F773-1FC0-4EBA-A64C-6199375F489A__SECTION_AEC2592F09DA47ACBB9901F1310E01E9)。

#### OpenSubdiv Catmull-Clark 自适应(OpenSubdiv Catmull-Clark Adaptive)

将渐进式细化方案应用于网格的不规则部分，例如非寻常点和半尖锐折痕，仅细分需要细节的区域。

自适应细分完全在 GPU 上评估，从而可以提高性能，并为您提供 WYSIWYG 体验。例如，动画师现在可以使用视觉丰富的网格取代简单的多边形近似和视觉反馈，如置换，消除创意过程中的猜测工作。

**注**

仅 OpenGL 4 和·DirectX11 兼容显卡支持“OpenSubdiv Catmull-Clark 自适应”(OpenSubdiv Catmull-Clark Adaptive)

。

## 多边形切线空间

可用于控制 Maya 为场景中的所有网络设置切线空间的方式。有关“多边形切线空间”(Polygon Tangent Space)的详细信息，请参见“[切线空间](https://beehive.autodesk.com/community/service/rest/cloudhelp/resource/cloudhelpchannel/guidcrossbook/jsonp?v=2022&p=MAYAUL&l=CHS&accessmode=live&guid=GUID-169FEA8E-0289-4B12-A181-D7C79FC98BC2)”。

## 四边形绘制

列出用于“四边形绘制”(Quad Draw)工具的热键映射。有关默认映射的列表，请参见[“四边形绘制”(Quad Draw)热键](https://beehive.autodesk.com/community/service/rest/cloudhelp/resource/cloudhelpchannel/guidcrossbook/jsonp?v=2022&p=MAYAUL&l=CHS&accessmode=live&guid=GUID-ED28E6BC-6141-491C-8C1B-2AE6FC813284)。

#### 预设(Presets)

#### 默认(Default)

Maya 将使用默认的“四边形绘制”(Quad Draw)热键映射。

**注**

选择此选项可以将映射重置为默认设置。

#### 自定义(Custom)

Maya 将使用一组自定义的“四边形绘制”(Quad Draw)热键映射。

## 3D 绘制

#### 重命名纹理(Rename Textures)

启用时，Maya 会在设置的 Maya 项目的 sourceimages 文件夹中创建新的子目录。该子目录采用当前 Maya 场景文件的名称。Maya 将现有的文件纹理复制到新的子目录，这些纹理将变为工作的 3D 绘制纹理。必须先保存场景，才能保存纹理。文件节点的路径将重新设置到活动 3D 绘制纹理，而原始纹理保持不变，且在场景中不再使用。

禁用时，在保存 3D 绘制时会更新原始文件节点纹理。
