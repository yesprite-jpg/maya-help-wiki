# 关于 GPU 缓存

![图：（图旁无可取正文，Maya 手册 img 无 alt）](https://help.autodesk.com/cloudhelp/2022/CHS/Maya-ManagingScenes/images/GUID-2D93A634-9D5D-4477-A677-B6878447FA22.png) <!-- baize:img-hook downloaded=false reason="正文 994 字 ≥300，非承重" -->

GPU 缓存文件从 Alembic 开源文件格式开发而来，通过优化这些文件可提高 Maya 中的播放性能。根据对 GPU 缓存文件进行求值的方式来实现性能提升。GPU 缓存节点直接将缓存的数据路由到系统显卡，以处理、忽略 Maya 依存关系图求值。此数据流可缓解在打开和播放具有庞大数据集的大型场景时出现的性能问题。

在您导入 GPU 缓存文件时，该文件将作为单个 gpuCache 节点显示在“大纲视图”(Outliner)中，并用以下图标表示：![图：在您导入 GPU 缓存文件时，该文件将作为单个 gpuCache 节点显示在“大纲视图”(Outliner)中，并用以下…](https://help.autodesk.com/cloudhelp/2022/CHS/Maya-ManagingScenes/images/GUID-1F60537E-F126-4685-BC17-AF07BDBE9A64.png) <!-- baize:img-hook downloaded=false reason="正文 994 字 ≥300，非承重" -->。在场景中，GPU 缓存几何体显示为虚线线框对象。“属性编辑器”(Attribute Editor)显示一个以对象命名的“变换”(Transform)节点，该节点合并了所有单个源对象“变换”(Transform)节点。以对象命名的形状节点还提供其他属性，如“缓存文件名”(Cache File Name)、“几何体路径”(Geometry Path)和缓存重新加载按钮。对 GPU 缓存文件进行更改（在其首次导入场景之后）时，可以单击 ![图：在您导入 GPU 缓存文件时，该文件将作为单个 gpuCache 节点显示在“大纲视图”(Outliner)中，并用以下…](https://help.autodesk.com/cloudhelp/2022/CHS/Maya-ManagingScenes/images/GUID-8D11FACC-44CC-4ABF-8142-F83A350D3431.png) <!-- baize:img-hook downloaded=false reason="正文 994 字 ≥300，非承重" --> 图标以重新加载更新的缓存文件。无需使用“GPU 缓存 > 导入”(GPU Cache > Import)命令重新导入文件。

不能将 GPU 缓存的对象作为 Maya 几何体进行编辑。

## GPU 缓存功能

使用 GPU 缓存，您可以：

- 使用“捕捉到点”(Snap to points)工具操纵 GPU 缓存的对象。这包括捕捉到其他 GPU 缓存的多边形对象及未缓存的多边形对象的点。请参见[将一个对象捕捉到另一个对象](https://beehive.autodesk.com/community/service/rest/cloudhelp/resource/cloudhelpchannel/guidcrossbook/jsonp?v=2022&p=MAYAUL&l=CHS&accessmode=live&guid=GUID-BABE0532-14F5-4A61-A261-D73E3B84A3FA)。

- 启用 GPU 缓存背景加载，从而使缓存文件在您工作时加载到场景中。请参见 [GPU 缓存首选项(GPU Cache Preferences)](https://beehive.autodesk.com/community/service/rest/cloudhelp/resource/cloudhelpchannel/guidcrossbook/jsonp?v=2022&p=MAYAUL&l=CHS&accessmode=live&guid=GUID-0F340CD7-FDE1-4F64-ADCA-52687835BC90#GUID-0F340CD7-FDE1-4F64-ADCA-52687835BC90__SECTION_F5EFF18768A940139BB174D3D26DC5D4)。

- 从源几何体导出 Lambert 和 Phong 着色信息。请参见[对 GPU 缓存进行着色和渲染](关于%20GPU%20缓存/对%20GPU%20缓存进行着色和渲染.md)。

- 将多个 GPU 缓存节点缓存到单个缓存文件。请参见[递归 GPU 缓存](关于%20GPU%20缓存/递归%20GPU%20缓存.md)。

- 指定首选项，确定用于播放 GPU 缓存文件的系统显卡内存量。请参见 [GPU 缓存首选项(GPU Cache Preferences)](https://beehive.autodesk.com/community/service/rest/cloudhelp/resource/cloudhelpchannel/guidcrossbook/jsonp?v=2022&p=MAYAUL&l=CHS&accessmode=live&guid=GUID-0F340CD7-FDE1-4F64-ADCA-52687835BC90#GUID-0F340CD7-FDE1-4F64-ADCA-52687835BC90__SECTION_F5EFF18768A940139BB174D3D26DC5D4)。

- 重新拓扑具有较高多边形计数的稠密资产。请参见[重新拓扑 GPU 缓存节点](https://beehive.autodesk.com/community/service/rest/cloudhelp/resource/cloudhelpchannel/guidcrossbook/jsonp?v=2022&p=MAYAUL&l=CHS&accessmode=live&guid=GUID-6121F248-5E15-4E42-AFC5-427CBCF540B3)。

## GPU 缓存插件

若要将 Maya 对象和场景另存为 GPU 缓存文件并加载，请加载 gpuCache.mll。若要加载插件，请打开插件管理器(Plug-in Manager)（“窗口 > 设置/首选项 > 插件管理器”(Windows > Settings/Preferences > Plug-in Manager)）。请参见[加载或卸载 Maya 插件](https://beehive.autodesk.com/community/service/rest/cloudhelp/resource/cloudhelpchannel/guidcrossbook/jsonp?v=2022&p=MAYAUL&l=CHS&accessmode=live&guid=GUID-07A89E6C-199C-4719-98A0-11C3A2BCDF21)。
