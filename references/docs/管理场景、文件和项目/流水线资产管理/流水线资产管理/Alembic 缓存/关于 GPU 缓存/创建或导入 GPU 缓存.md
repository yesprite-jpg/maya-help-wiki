# 创建或导入 GPU 缓存

您可以从场景中的多边形或 NURBS 对象创建基于 Alembic 的 GPU 缓存文件。可以将所有场景对象保存到单个缓存，或为每个选定对象创建缓存文件。

**注**

原始几何体中的 Lambert 和 Phong 材质也可以保存到 GPU 缓存文件中。请参见

对 GPU 缓存进行着色和渲染

。

创建 GPU 缓存

1. 执行下列操作之一：

  - 若要将场景中的所有对象保存到一个 GPU 缓存文件中，请选择“缓存 > GPU 缓存 > 导出全部”(Cache > GPU Cache > Export All) > ![图：若要将场景中的所有对象保存到一个 GPU 缓存文件中，请选择“缓存 GPU 缓存 导出全部”(Cache GPU Cac…](https://help.autodesk.com/cloudhelp/2022/CHS/Maya-ManagingScenes/images/GUID-23B160F6-E1FB-4E29-94B2-7323BFE33726.png) <!-- baize:img-hook downloaded=false reason="正文 1195 字 ≥300，非承重" -->。

  - 若要将场景中的每个对象层次保存到单独 GPU 缓存文件中，请选择要缓存的对象，然后选择“缓存 > GPU 缓存 > 导出当前选择”(Cache > GPU Cache > Export Selection) > ![图：若要将场景中的每个对象层次保存到单独 GPU 缓存文件中，请选择要缓存的对象，然后选择“缓存 GPU 缓存 导出当前选择…](https://help.autodesk.com/cloudhelp/2022/CHS/Maya-ManagingScenes/images/GUID-23B160F6-E1FB-4E29-94B2-7323BFE33726.png) <!-- baize:img-hook downloaded=false reason="正文 1195 字 ≥300，非承重" -->。

2. 在“GPU 缓存导出选项”(GPU Cache Export Options)窗口中，选择[缓存时间范围(Cache time range)](https://beehive.autodesk.com/community/service/rest/cloudhelp/resource/cloudhelpchannel/guidcrossbook/jsonp?v=2022&p=MAYAUL&l=CHS&accessmode=live&guid=GUID-3E89B28E-6F87-4842-9B2B-5FBEF171810F#GUID-3E89B28E-6F87-4842-9B2B-5FBEF171810F__GUID-42ABD3E9-A22B-45F9-BAD9-BE8AE85CA117)选项以指定要缓存的帧。

3. 如果选择将选定对象保存到单独缓存中，请指定[文件名前缀(File name prefix)](https://beehive.autodesk.com/community/service/rest/cloudhelp/resource/cloudhelpchannel/guidcrossbook/jsonp?v=2022&p=MAYAUL&l=CHS&accessmode=live&guid=GUID-3E89B28E-6F87-4842-9B2B-5FBEF171810F#GUID-3E89B28E-6F87-4842-9B2B-5FBEF171810F__GUID-D5C1FA1C-D672-4879-B593-2D2AA498B8F9)。

  默认情况下，Maya 会将场景文件名称添加到缓存文件名称的开头。

4. （可选）更改默认的[优化层次](https://beehive.autodesk.com/community/service/rest/cloudhelp/resource/cloudhelpchannel/guidcrossbook/jsonp?v=2022&p=MAYAUL&l=CHS&accessmode=live&guid=GUID-3E89B28E-6F87-4842-9B2B-5FBEF171810F#GUID-3E89B28E-6F87-4842-9B2B-5FBEF171810F__GUID-81714509-DB91-435D-8A20-D570048A856C) [优化阈值](https://beehive.autodesk.com/community/service/rest/cloudhelp/resource/cloudhelpchannel/guidcrossbook/jsonp?v=2022&p=MAYAUL&l=CHS&accessmode=live&guid=GUID-3E89B28E-6F87-4842-9B2B-5FBEF171810F#GUID-3E89B28E-6F87-4842-9B2B-5FBEF171810F__GUID-002B5EB5-9FF0-4298-85F2-4DE9180671CD)设置。

  这些选项可优化 GPU 缓存以提高播放性能。[GPU 缓存首选项(GPU Cache Preferences)](https://beehive.autodesk.com/community/service/rest/cloudhelp/resource/cloudhelpchannel/guidcrossbook/jsonp?v=2022&p=MAYAUL&l=CHS&accessmode=live&guid=GUID-0F340CD7-FDE1-4F64-ADCA-52687835BC90)提供其他优化选项。

5. （可选）在 Viewport 2.0 中播放已设置动画的对象时，若要将其与运动模糊一起显示，请启用[优化运动模糊的动画(Optimize Animations for Motion Blur)](https://beehive.autodesk.com/community/service/rest/cloudhelp/resource/cloudhelpchannel/guidcrossbook/jsonp?v=2022&p=MAYAUL&l=CHS&accessmode=live&guid=GUID-3E89B28E-6F87-4842-9B2B-5FBEF171810F#GUID-3E89B28E-6F87-4842-9B2B-5FBEF171810F__GUID-CD135BE6-9A42-4B71-93AD-8386DF18CFE3)。

6. （可选）若要将原始几何体中的 Lambert 或 Phong 材质保存到缓存文件，请确保启用[写入材质(Write Materials)](https://beehive.autodesk.com/community/service/rest/cloudhelp/resource/cloudhelpchannel/guidcrossbook/jsonp?v=2022&p=MAYAUL&l=CHS&accessmode=live&guid=GUID-3E89B28E-6F87-4842-9B2B-5FBEF171810F#GUID-3E89B28E-6F87-4842-9B2B-5FBEF171810F__GUID-4A7ACC61-2303-4AA1-BF7A-5DDA199711BB)。

在 Viewport 2.0 中播放缓存文件时材质进行渲染。默认情况下，“写入材质”(Write Materials)处于启用状态。

7. 单击“导出”(Export)。

导入 GPU 缓存

1. 选择“缓存 > GPU 缓存 > 导入”(Cache > GPU Cache > Import) >![图：选择“缓存 GPU 缓存 导入”(Cache GPU Cache Import) 。 也可以选择“缓存 Alembic …](https://help.autodesk.com/cloudhelp/2022/CHS/Maya-ManagingScenes/images/GUID-23B160F6-E1FB-4E29-94B2-7323BFE33726.png) <!-- baize:img-hook downloaded=false reason="正文 1195 字 ≥300，非承重" -->。

  也可以选择“缓存 > Alembic 缓存 > 导入 Alembic”(Cache > Alembic Cache > Import Alembic) > ![图：也可以选择“缓存 Alembic 缓存 导入 Alembic”(Cache Alembic Cache Import A…](https://help.autodesk.com/cloudhelp/2022/CHS/Maya-ManagingScenes/images/GUID-23B160F6-E1FB-4E29-94B2-7323BFE33726.png) <!-- baize:img-hook downloaded=false reason="正文 1195 字 ≥300，非承重" --> 来导入 GPU 缓存文件。

2. 在“Alembic 导入选项”(Alembic Import Options)窗口中，选择以下选项：

  - 适配时间范围

  - 将当前时间设置为开始帧

3. 单击“导入”(Import)。

**注**

重要：

若要在使用 Windows 远程桌面连接时导入 GPU 缓存文件，您必须执行以下操作：

1. 从主机计算机启动 Maya。

2. 将“Viewport 2.0”设置为工作区的默认渲染器。

  请勿从远程计算机设置默认渲染器。

3. 从远程计算机访问 Maya 以导入 GPU 缓存文件。

如果不遵循这些步骤，则可能会导致在导入 GPU 缓存文件时 Maya 停止工作。

## 相关主题

- [关于 GPU 缓存](../关于%20GPU%20缓存.md)

- [对 GPU 缓存进行着色和渲染](对%20GPU%20缓存进行着色和渲染.md)

- [递归 GPU 缓存](递归%20GPU%20缓存.md)

- [“Alembic 导入”(Alembic Import)选项](https://beehive.autodesk.com/community/service/rest/cloudhelp/resource/cloudhelpchannel/guidcrossbook/jsonp?v=2022&p=MAYAUL&l=CHS&accessmode=live&guid=GUID-DEA2C5A5-3D04-4081-BBDE-8D9DC788AF02)

- [使用 MEL 命令保存和加载流水线缓存](../使用%20MEL%20命令保存和加载流水线缓存.md)
