# “传递贴图”(Transfer Maps)选项

选择“照明/着色 > 传递贴图”(Lighting/Shading > Transfer Maps)可打开“传递贴图”(Transfer Maps)工具。

## 目标网格(Target Meshes)

#### 名称(Name)

列出场景中当前选择的所有对象的名称作为“传递贴图”(Transfer Map)工具中的目标。目标是您要将纹理贴图烘焙到的对象。您可以在该列表中的对象名称上单击鼠标右键以：

- 在场景视图中选择目标对象。

- 从目标网格的列表中移除对象。

- 使用目标对象作为搜索封套。请参见下面的搜索封套 (%) 获得更多详细信息。

  **注**

  如果

  “传递贴图”(Transfer Maps)

  功能未产生预期的结果，请使用 Turtle 插件 (

  Turtle.mll

  ) 来执行贴图烘焙。

  #### 输出 UV 集(Output UV Set)

  对为其创建纹理贴图的目标网格设定 UV 集。UV 集定义映射目标网格的方式。

  **注**

  提示：

  若要获得精确的结果，UV 映射必须为非重叠（即不能将目标网格上的两个不同曲面映射到同一 UV 区域）。

  #### 显示(Display)

  设定在场景视图中显示目标的哪些方面。可以显示目标网格或其封套，或同时显示这两者。

  如果您正在为搜索封套使用自定义几何体，则不需要更改此设置。

  #### 搜索封套(%) (Search Envelope(%))

  搜索封套是用户可编辑的一块几何体，它定义了传递贴图生成操作的搜索体积或阈值。

  该属性设定目标网格的搜索封套的大小 (%)。如果将“搜索封套”(Search Envelope)设定为 10，则封套将比其目标网格大 10%。

  可以编辑搜索封套的顶点以精细调整其形状和覆盖范围。

  ![图：搜索封套是用户可编辑的一块几何体，它定义了传递贴图生成操作的搜索体积或阈值。 该属性设定目标网格的搜索封套的大小 (%)…](https://help.autodesk.com/cloudhelp/2022/CHS/Maya-Rendering/images/GUID-B1DDFFC0-3FB4-44D7-B648-49E2C0FEFF63.png) <!-- baize:img-hook downloaded=false reason="正文 8147 字 ≥300，非承重" -->

  #### 添加选定对象(Add Selected)

  将场景视图中当前选定对象添加到“目标网格”(Target Meshes)列表。

  #### 移除选定对象(Remove Selected)

  将场景视图中当前选定对象从“目标网格”(Target Meshes)列表移除。

  #### 清除全部(Clear All)

  删除“目标网格”(Target Meshes)列表中的所有对象名称。

## 源网格(Source Meshes)

#### 名称(Name)

列出场景中当前选择的所有对象的名称作为“传递贴图”(Transfer Map)工具中的源。源是您要为其创建纹理贴图的具有网格属性的对象。您可以在该列表中的对象名称上单击鼠标右键以：

- 在场景视图中选择源对象。

- 从“源网格”(Source Meshes)列表中移除对象。

  #### 添加选定对象(Add Selected)

  将场景视图中的当前选定对象添加到“源网格”(Source Meshes)列表。

  #### 添加未选定对象(Add Unselected)

  将场景视图中的所有未选定对象添加到“源网格”(Source Meshes)列表。

  #### 移除选定对象(Remove Selected)

  将场景视图中的当前选定对象从“源网格”(Source Meshes)列表中移除。

  #### 清除全部(Clear All)

  删除“源网格”(Source Meshes)列表中列出的所有对象名称。

**注**

Maya 支持从 MPxHwShaderNode 派生的使用硬件着色器的源对象。然后，可以使用

“传递贴图”(Transfer Maps)

功能将

“着色”(Shaded)

输出贴图（照明和着色颜色贴图）从源烘焙到目标网格。

## 输出贴图(Output maps)

从可用图标列表中选择一个贴图类型。此时将显示选定贴图类型部分。您可以根据需要创建任意数量的贴图。

![图：（图旁无可取正文，Maya 手册 img 无 alt）](https://help.autodesk.com/cloudhelp/2022/CHS/Maya-Rendering/images/GUID-A29C5751-F4F6-4FBE-BB9B-41326F3621F2.png) <!-- baize:img-hook downloaded=false reason="正文 8147 字 ≥300，非承重" -->

**注**

在每个部分中，您可以：

- 取消选中贴图类型（例如，“法线贴图”(Normal map)）旁边的框以将其从要生成的贴图列表中移除；

- 单击“移除贴图”(Remove Map)按钮以从贴图列表中移除贴图；

- 选中“使用 Maya 公用设置”(Use Maya common settings)选项可应用这些设置；

- 取消选中“使用 Maya 公用设置”(Use Maya common settings)选项可为每个传递贴图输入自定义设置。

您的设置（例如，已创建并选中的贴图部分）将与 Maya 的每个会话一起保存。

![图：（图旁无可取正文，Maya 手册 img 无 alt）](https://help.autodesk.com/cloudhelp/2022/CHS/Maya-Rendering/images/GUID-83A96C4C-80BC-4E1F-A15A-ED5935636605.png) <!-- baize:img-hook downloaded=false reason="正文 8147 字 ≥300，非承重" -->

### 法线贴图(Normal map)

#### 法线贴图(Normal map)

法线贴图捕捉源网格的曲面法线信息。纹理的大小和位置取决于各个网格的 UV 参数化。

启用时，会生成“法线贴图”(normal map)。输入要保存贴图的文件名和路径。

创建一个法线贴图并应用于曲面可以使一个更低密度的曲面包含更精细的细节，从而提供更高密度曲面的外观。

**注**

- 您可以渲染左手切线空间法线贴图。有关左手切线空间的详细信息，请参见[切线空间(Tangent Space)](https://beehive.autodesk.com/community/service/rest/cloudhelp/resource/cloudhelpchannel/guidcrossbook/jsonp?v=2022&p=MAYAUL&l=CHS&accessmode=live&guid=GUID-169FEA8E-0289-4B12-A181-D7C79FC98BC2)。

#### 文件格式(File format)

为要创建的法线贴图设定文件格式。请参见[文件格式](../../../../可视化和渲染图像/可视化和渲染图像/渲染输出/文件格式.md)。

当从下拉列表中选择文件格式时，Maya 会自动将相应的文件扩展名附加到法线贴图的文件名。例如，如果从下拉列表中选择 gif，.gif 将自动附加到文件名。

同样，如果输入 path/mapname.gif 作为文件名，文件格式选项将自动设定为 gif。

#### 包括材质(Include Materials)

启用时，所有源材质（如凹凸贴图）将包括在法线贴图中。使用该属性可获取修改过的法线（例如应用凹凸贴图后）的视图，即法线在最终渲染中的显示。关闭该选项可查看法线在实际几何体中的显示。

贴图空间(Map Space)

选择下列选项之一：

#### 切线空间(Tangent Space)

切线空间法线是根据每个顶点在本地定义的，并且可以通过变形旋转。将“切线空间”(Tangent Space)用于已设置动画的对象上的纹理。

#### 对象空间(Object Space)

对象空间法线始终指向相同的方向，即使旋转了三角形也是如此。将“对象空间”(Object Space)用于未设置动画的对象上的纹理。

#### 使用 Maya 公用设置(Use Maya common settings)

如果要创建多个相同宽度和高度的贴图，可以通过在“传递贴图”(Transfer Maps)窗口的“Maya 公用输出”区域输入这些设置以重用。

如果取消选中该选项，则窗口的“法线贴图”(Normal Map)区域中将显示“贴图宽度”(Map width)和“贴图高度”(Map height)属性。有关这些属性的详细信息，请参见 [Maya 公用输出](“传递贴图”%28Transfer%20Maps%29选项.md#WS17956D7ADBC6E736427CAAB117AE33EDE2-7FEB)。

**注**

提示：

若要将 Alpha 通道添加到颜色或法线贴图，请参见[用传递贴图工具创建纹理贴图](https://beehive.autodesk.com/community/service/rest/cloudhelp/resource/cloudhelpchannel/guidcrossbook/jsonp?v=2022&p=MAYAUL&l=CHS&accessmode=live&guid=GUID-B011A4BC-1B7A-4EC3-9B73-BCF744886C84)。

### 置换贴图(Displacement map)

#### 置换贴图(Displacement map)

置换贴图可以改变几何体的曲面，以模拟 3D 曲面细节。置换贴图是通过将曲面上两个点之间的高度或垂直距离捕捉到纹理贴图来创建的。置换根据纹理贴图中像素的密度沿着曲面法线发生。

启用时，会生成“置换贴图”(displacement map)。输入要保存贴图的路径和文件名。

置换贴图几何体通常有较高的几何体密度，它会捕获更多细节。这将有助于查看轮廓中的对象。由于其曲面细节的复杂性，渲染置换贴图需花费较长的时间。有关详细信息，请参见[置换贴图](https://beehive.autodesk.com/community/service/rest/cloudhelp/resource/cloudhelpchannel/guidcrossbook/jsonp?v=2022&p=MAYAUL&l=CHS&accessmode=live&guid=GUID-E7A03E4E-8C9A-4B62-8218-28FC063A82AB)。

**注**

“置换贴图”(Displacement map)效果在场景视图中不可见，仅当软件渲染时可见。

#### 文件格式(File format)

为要创建的置换贴图设定文件格式。请参见[文件格式](../../../../可视化和渲染图像/可视化和渲染图像/渲染输出/文件格式.md)。

当从下拉列表中选择文件格式时，Maya 会自动将相应的文件扩展名附加到置换贴图的文件名。例如，如果从下拉列表中选择 gif，.gif 将自动附加到文件名。

同样，如果输入 path/mapname.gif 作为文件名，文件格式选项将自动设定为 gif。

#### 最大值(Maximum Value)

为纹理贴图指定颜色空间的最大值并控制颜色范围比例。使用该属性控制生成贴图的比例。使用 0 以获得最佳比例；将使用最大颜色范围。

#### 使用 Maya 公用设置(Use Maya common settings)

如果要创建多个相同宽度和高度的贴图，您可以在“传递贴图”(Transfer Maps)窗口的“Maya 公用输出”区域输入这些设置以重用。

如果取消选中该选项，则在窗口的“Alpha 贴图”(Alpha Map)区域中将显示“贴图宽度”(Map width)和“贴图高度”(Map height)属性。有关这些属性的详细信息，请参见 [Maya 公用输出](“传递贴图”%28Transfer%20Maps%29选项.md#WS17956D7ADBC6E736427CAAB117AE33EDE2-7FEB)。

### 漫反射颜色贴图(Diffuse color map)

#### 漫反射颜色贴图(Diffuse color map)

漫反射颜色贴图包含一个或多个采样到单一颜色通道的材质。漫反射颜色贴图捕捉目标网格在多个角度反射（或散射）颜色的方式。它有助于创建颜色在曲面上自由扩散的效果。

启用时，将生成“漫反射颜色贴图”(diffuse color map)。输入要保存贴图的路径和文件名。

#### 文件格式(File format)

为要创建的漫反射颜色贴图设定文件格式。请参见[文件格式](../../../../可视化和渲染图像/可视化和渲染图像/渲染输出/文件格式.md)。

当从下拉列表中选择文件格式时，Maya 会自动将相应的文件扩展名附加到漫反射颜色贴图的文件名。例如，如果从下拉列表中选择 gif，.gif 将自动附加到文件名上。

同样，如果输入 path/mapname.gif 作为文件名，文件格式选项将自动设定为 gif。

#### 使用 Maya 公用设置(Use Maya common settings)

如果要创建多个相同宽度和高度的贴图，您可以在“传递贴图”(Transfer Maps)窗口的“Maya 公用输出”区域输入这些设置以重用。

如果取消选中该选项，则窗口的“漫反射颜色贴图”(Diffuse Color Map)区域中将显示“贴图宽度”(Map width)和“贴图高度”(Map height)属性。有关这些属性的详细信息，请参见 [Maya 公用输出](“传递贴图”%28Transfer%20Maps%29选项.md#WS17956D7ADBC6E736427CAAB117AE33EDE2-7FEB)。

**注**

提示：

若要将 Alpha 通道添加到颜色或法线贴图，请参见

用传递贴图工具创建纹理贴图

。

### 照明和着色颜色贴图(Lit and shaded color map)

#### 照明和着色颜色贴图(Lit and shaded color map)

照明和着色颜色贴图包含源对象的所有场景照明信息（包括漫反射照明）。源网格中的照明的采样存储在要应用于目标网格的照明和着色颜色贴图中。

启用时，将生成“照明和着色贴图”(lit and shaded map)。输入要保存贴图的路径和文件名。

照明和着色颜色贴图捕捉目标网格向多角度反射（或散射）光、阴影和颜色的方式。它有助于创建光和颜色在网格上自由扩散的效果。

#### 文件格式(File format)

为要创建的照明和着色颜色贴图设定文件格式。请参见[文件格式](../../../../可视化和渲染图像/可视化和渲染图像/渲染输出/文件格式.md)。

当从下拉列表中选择文件格式时，Maya 会自动将相应的文件扩展名附加到照明和着色颜色贴图的文件名。例如，如果从下拉列表中选择 gif，.gif 将自动附加到文件名。

同样，如果输入 path/mapname.gif 作为文件名，文件格式选项将自动设定为 gif。

#### 包括阴影(Include Shadows)

启用时，深度贴图阴影包含在您创建的纹理贴图中。

#### 使用 Maya 公用设置(Use Maya common settings)

如果要创建多个相同宽度和高度的贴图，您可以在“传递贴图”(Transfer Maps)窗口的“Maya 公用输出”区域输入这些设置以重用。

如果取消选中该选项，则窗口的“照明和着色颜色贴图”(Lit and Shaded Color Map)区域中将显示“贴图宽度”(Map width)和“贴图高度”(Map height)属性。有关这些属性的详细信息，请参见 [Maya 公用输出](“传递贴图”%28Transfer%20Maps%29选项.md#WS17956D7ADBC6E736427CAAB117AE33EDE2-7FEB)。

**注**

提示：

若要将 Alpha 通道添加到颜色或法线贴图，请参见

用传递贴图工具创建纹理贴图

。

#### Alpha 贴图(Alpha map)

Alpha 贴图包含源对象的透明度信息。“传递贴图”(Transfer Map)工具会对源对象上的透明度求值并将其烘焙到目标对象的贴图上。

该贴图在下列情况下很有用：

- 源对象包含透明区域；例如，窗户或玻璃。

- 目标对象的有些部分不存在于源对象上；例如，源对象包含洞和腔。法线贴图包含源对象的轮廓，但不包含曲面中的穿孔或间隙。Alpha 贴图捕捉这些腔和空洞处。

启用时，将生成 Alpha 贴图。输入要保存贴图的路径和文件名。

**注**

提示：

若要将 Alpha 通道添加到颜色或法线贴图，请参见

用传递贴图工具创建纹理贴图

。

#### 文件格式(File format)

为要创建的 Alpha 贴图设定文件格式。请参见[文件格式](../../../../可视化和渲染图像/可视化和渲染图像/渲染输出/文件格式.md)。

当从下拉列表中选择文件格式时，Maya 会自动将相应的文件扩展名附加到漫反射颜色贴图的文件名。例如，如果从下拉列表中选择 gif，.gif 将自动附加到文件名上。

同样，如果输入 path/mapname.gif 作为文件名，文件格式选项将自动设定为 gif。

#### 使用 Maya 公用设置(Use Maya common settings)

如果要创建多个相同宽度和高度的贴图，您可以在“传递贴图”(Transfer Maps)窗口的“Maya 公用输出”区域输入这些设置以重用。

如果取消选中该选项，则窗口的“Alpha 颜色贴图”(Alpha Color Map)区域中将显示“贴图宽度”(Map width)和“贴图高度”(Map height)属性。有关这些属性的详细信息，请参见 [Maya 公用输出](“传递贴图”%28Transfer%20Maps%29选项.md#WS17956D7ADBC6E736427CAAB117AE33EDE2-7FEB)。

## 连接输出贴图(Connect Output Maps)

指定要创建的纹理在目标对象上的显示方式。

#### 将贴图连接至着色器(Connect maps to shader)

禁用时，保留当前网络不变并在磁盘上创建纹理文件。在场景视图中不对网格做任何可见更改。启用时，将贴图连接至:新建着色器(Connect maps to: New shader)和“将贴图连接至:指定的着色器”将贴图连接至:新建着色器(Connect maps to: Assigned shader)选项处于活动状态。

#### 将贴图连接至:新建着色器(Connect maps to: New shader)

创建新的测试着色器并将下列各项连接至新的着色网络：

- 将“法线贴图”(Normal map)连接到新着色器的“凹凸贴图”(Bump Mapping)通道

- 将“置换贴图”(Displacement map)连接到新着色组的“置换材质”(Displacement mat)

- 将“漫反射颜色贴图”(Diffuse color map)连接到“颜色”(Color)通道

- 将“照明和着色颜色贴图”(Lit and shaded color map)连接到“环境色”(Ambient Color)通道

- 将“环境光遮挡贴图”(Ambient occlusion map)连接到“漫反射”(Diffuse)通道

- 将“自定义贴图”(Custom map)连接到“颜色”(Color)通道

#### 将贴图连接至:指定的着色器(Connect maps to: Assigned shader)

通过下列连接将纹理贴图附加到目标对象：

- 将“法线贴图”(Normal map)附加到目标着色器的“凹凸贴图”(Bump Mapping)通道

- 将“置换贴图”(Displacement map)附加到着色组的“置换材质”(Displacement mat)

- 将“漫反射颜色贴图”(Diffuse color map)附加到“颜色”(Color)通道

- 将“照明和着色颜色贴图”(Lit and shaded color map)连接到“环境色”(Ambient Color)通道

- 将“环境光遮挡贴图”(Ambient occlusion map)连接到“漫反射”(Diffuse)通道

- 将“自定义贴图”(Custom map)附加到“颜色”(Color)通道

  **注**

  - 对于每种类型，仅一个贴图可以连接至着色器。如果您为同一类型创建了多个贴图（例如，两个“法线贴图”(Normal maps)），则仅将列表中的最后一个贴图附加到着色器。

  - “漫反射颜色贴图”(Diffuse color map)和“自定义贴图”(Custom map)都将映射到“颜色”(Color)通道。如果您选择同时创建“漫反射颜色贴图”(Diffuse color map)和“自定义贴图”(Custom map)，则仅将列表中的最后一个贴图附加到着色器。

## Maya 公用输出(Maya Common Output)

#### 贴图宽度(Map width)

设定要创建的纹理贴图的宽度（以像素为单位）。滑块捕捉到下列纹理分辨率：16、32、64、128、256、512、1024、2048、4096。默认的贴图宽度是 256。

#### 贴图高度(Map height)

设定要创建的纹理贴图的高度（以像素为单位）。滑块捕捉到下列纹理分辨率：16、32、64、128、256、512、1024、2048、4096。默认的贴图高度为 256。

#### 传入(Transfer in)

选择下列选项之一：

#### 世界空间(World Space)

当对象大小不同时，请使用“世界空间”(World Space)。当传入世界空间时，请确保源对象和目标对象位于场景视图中相同的世界位置（一个位于另一个的上方）。

#### 对象空间(Object Space)

使用“对象空间”(Object Space)查看传递贴图的结果而不必重叠网格。若要确保对象空间传递起作用，请移动对象使之相互叠加（所有网格的枢轴重叠），并冻结对象的所有变换，然后将其分离开来并列放置。

#### UV 空间(UV Space)

当源网格和目标网格比例不同或形状不同时，请使用“UV 空间”(UV Space)。例如，如果要同时创建男性和女性角色，并且需要将曲面属性从一个网格传递到另一个网格。尽管两个网格都有手臂，但手臂还是有很大不同，如果采用基于空间的传递，产生的效果不理想。请确保您为两个网格都定义了 UV 空间映射。

**注**

“对象空间”(Object Space)忽略所有变换（包括组变换）并且单独处理对象。如果有多个源对象（不管是否分组），并且您要传入对象空间，则冻结每个源对象的变换。

#### 采样质量(Sampling Quality)

为贴图指定取自源网格的每像素采样数量，并确定纹理贴图的质量。提高采样质量以获取纹理贴图中的更多细节。但是，在调整采样质量值之前，您必须首先确保源对象是高质量的。例如，如果您正创建环境光遮挡传递贴图，则首先应调整源对象的遮挡光线的数量以确保它提供了高质量的细节，然后再修改“采样质量”(Sampling Quality)属性。

#### 过滤器大小(Filter Size)

控制用于对纹理贴图中的每个像素插值的过滤器大小。小过滤器（如 3）会产生较锐利的纹理贴图，大过滤器（如 7）会产生较平滑/柔和的纹理贴图。

#### 过滤器类型(Filter Type)

控制如何模糊或柔化纹理贴图以消除锯齿或锯齿状边缘。从下列过滤器类型中选择：“高斯”(Gaussian)（稍微柔和）、“三角形”(Triangular)（柔和）或“长方体”(Box)（非常柔和）。

#### 填充纹理接缝(Fill Texture Seams)

计算围绕每个 UV 壳的其他像素以移除围绕 UV 接缝的纹理过滤瑕疵。

#### 忽略镜像面(Ignore Mirrored Faces)

启用时，带有反转 UV 缠绕顺序的面不会用于创建传递贴图。该功能的典型应用是为角色创建镜像法线贴图。请参见[在角色或对象上创建和使用镜像法线贴图](https://beehive.autodesk.com/community/service/rest/cloudhelp/resource/cloudhelpchannel/guidcrossbook/jsonp?v=2022&p=MAYAUL&l=CHS&accessmode=live&guid=GUID-A8BE0CCD-C144-4822-853E-EDA45FE392BD)。

## 高级选项(Advanced Options)

#### 搜索方法(Search Method)

设定正在查找的目标网格相对于搜索封套的位置。

![图：（图旁无可取正文，Maya 手册 img 无 alt）](https://help.autodesk.com/cloudhelp/2022/CHS/Maya-Rendering/images/GUID-6154EE0A-55F5-4B19-BCD0-DADCA9ABC947.png) <!-- baize:img-hook downloaded=false reason="正文 8147 字 ≥300，非承重" -->

#### 与封套最接近(Closest to Envelope)

在封套外部搜索目标网格。

#### 先封套内部再封套外部(Inside Envelope then Outside Envelope)

先后在封套内部和外部搜索目标网格。

#### 仅封套内部(Inside Envelope Only)

仅在封套边界内搜索目标网格。

#### 最大搜索深度(%) (Max Search Depth(%))

设定接受目标网格匹配所需的搜索深度限制或距离目标网格最远的百分比。该选项可以避免查找对象背面的曲面交集作为搜索结果。

如果“最大搜索深度”(Max Search Depth)为 0.0，将设定无限制搜索深度。

**注**

“环境光遮挡贴图”(Ambient occlusion maps)和“自定义贴图”(Custom maps)不支持“最大搜索深度”(Max Search Depth)。

#### 烘焙时删除封套(Delete Envelopes on Bake)

启用后，则在烘焙时删除目标对象的搜索封套。

#### 使用以下对象匹配(Match Using)

选择下列选项之一：

#### 几何体法线(Geometry Normals)

烘焙时将纹理贴图匹配到目标网格的面法线。该匹配方法适用于软边曲面。

#### 曲面法线(Surface Normals)

烘焙时将纹理贴图匹配到目标曲面的顶点法线。该匹配方法适用于硬边曲面。
