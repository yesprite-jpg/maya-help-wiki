# 关于 Alembic 缓存

您可以在 Maya 中使用 Alembic 缓存以在产品级流水线的各个阶段之间传递资产。Alembic 缓存文件的内容作为 Maya 几何体进行求值，并且可以使用多边形、NURBS 和细分曲面编辑工具进行修改。

当您在 Maya 中导入（“缓存 > Alembic 缓存 > 导入 Alembic”(Cache > Alembic Cache > Import Alembic)）或打开（“缓存 > Alembic 缓存 > 打开 Alembic”(Cache > Alembic Cache > Open Alembic)）Alembic 缓存时，文件中的对象层次保持不变。Alembic 缓存不包括着色信息，而在场景视图中显示默认着色。加载 Alembic 文件后，您可以使用与 Maya 几何体相同的材质和工作流给对象指定着色器。

您可以指定导出和导入选项，以合并 Alembic 文件和源几何体的着色信息。请参见[合并 Alembic 缓存和 Maya 对象](关于%20Alembic%20缓存/使用%20Maya%20对象合并%20Alembic%20缓存.md)。着色 Alembic 对象可以使用 Maya 软件渲染器或 Arnold for Maya 进行渲染。

![图：（图旁无可取正文，Maya 手册 img 无 alt）](https://help.autodesk.com/cloudhelp/2022/CHS/Maya-ManagingScenes/images/GUID-AA9E3D43-C6ED-4C5B-B1BF-90F18C49FE29.png) <!-- baize:img-hook downloaded=false reason="正文 1116 字 ≥300，非承重" -->

## Alembic 导出和导入选项

您可以指定[“Alembic 导出选项”(Alembic Export Options)](https://beehive.autodesk.com/community/service/rest/cloudhelp/resource/cloudhelpchannel/guidcrossbook/jsonp?v=2022&p=MAYAUL&l=CHS&accessmode=live&guid=GUID-854D22F6-7547-465C-8A13-E21A8A6D9714)（“缓存 > Alembic 缓存 > 将所有内容/当前选择导出到 Alembic”(Cache > Alembic Cache > Export All/Export Selection to Alembic) > ![图：您可以指定“Alembic 导出选项”(Alembic Export Options)（“缓存 Alembic 缓存 将…](https://help.autodesk.com/cloudhelp/2022/CHS/Maya-ManagingScenes/images/GUID-23B160F6-E1FB-4E29-94B2-7323BFE33726.png) <!-- baize:img-hook downloaded=false reason="正文 1116 字 ≥300，非承重" -->)，以便：

- 将源几何体的 UV 和折痕信息保存到 Alembic 缓存（请参见 [UV 写入](https://beehive.autodesk.com/community/service/rest/cloudhelp/resource/cloudhelpchannel/guidcrossbook/jsonp?v=2022&p=MAYAUL&l=CHS&accessmode=live&guid=GUID-854D22F6-7547-465C-8A13-E21A8A6D9714#GUID-854D22F6-7547-465C-8A13-E21A8A6D9714__GUID-10280AF1-89E8-4A63-B718-7E7B8BC9BA22)和[写入折痕](https://beehive.autodesk.com/community/service/rest/cloudhelp/resource/cloudhelpchannel/guidcrossbook/jsonp?v=2022&p=MAYAUL&l=CHS&accessmode=live&guid=GUID-854D22F6-7547-465C-8A13-E21A8A6D9714#GUID-854D22F6-7547-465C-8A13-E21A8A6D9714__GUID-7BE70531-5AAD-4587-AB0D-65623D97AC15)）。

- 缓存动态属性和自定义属性（请参见[属性](https://beehive.autodesk.com/community/service/rest/cloudhelp/resource/cloudhelpchannel/guidcrossbook/jsonp?v=2022&p=MAYAUL&l=CHS&accessmode=live&guid=GUID-854D22F6-7547-465C-8A13-E21A8A6D9714#GUID-854D22F6-7547-465C-8A13-E21A8A6D9714__GUID-5918159F-D121-4D87-ACF3-E27BCC8A8967)）。

- 使用 Euler 过滤旋转数据（请参见[过滤器 Euler 旋转(Filter Euler Rotations)](https://beehive.autodesk.com/community/service/rest/cloudhelp/resource/cloudhelpchannel/guidcrossbook/jsonp?v=2022&p=MAYAUL&l=CHS&accessmode=live&guid=GUID-854D22F6-7547-465C-8A13-E21A8A6D9714#GUID-854D22F6-7547-465C-8A13-E21A8A6D9714__GUID-D64B9147-9437-426F-B935-CCE8B38F66E7)）。

请参见[创建 Alembic 缓存](关于%20Alembic%20缓存/创建%20Alembic%20缓存文件.md)。

您可以指定[“Alembic 导入选项”(Alembic Import Options)](https://beehive.autodesk.com/community/service/rest/cloudhelp/resource/cloudhelpchannel/guidcrossbook/jsonp?v=2022&p=MAYAUL&l=CHS&accessmode=live&guid=GUID-DEA2C5A5-3D04-4081-BBDE-8D9DC788AF02)（“缓存 > Alembic 缓存 > 导入 Alembic”(Cache > Alembic Cache > Import Alembic) > ![图：您可以指定“Alembic 导入选项”(Alembic Import Options)（“缓存 Alembic 缓存 导…](https://help.autodesk.com/cloudhelp/2022/CHS/Maya-ManagingScenes/images/GUID-23B160F6-E1FB-4E29-94B2-7323BFE33726.png) <!-- baize:img-hook downloaded=false reason="正文 1116 字 ≥300，非承重" -->），以便：

- 将导入的 Alembic 对象设置为场景中选定对象的父对象。

- 添加或移除与导入几何体匹配的场景几何体。

- 合并缓存动画数据和源对象。

使用“打开”命令时，Alembic 导入选项不可用。请参见[导入 Alembic 缓存文件](关于%20Alembic%20缓存/导入%20Alembic%20缓存文件.md)。

## Alembic 缓存插件

若要将 Maya 对象和场景作为 Alembic 缓存进行保存和加载，请加载 AbcImport.mll 和 AbcExport.mll 插件。若要加载插件，请打开插件管理器(Plug-in Manager)（“窗口 > 设置/首选项 > 插件管理器”(Windows > Settings/Preferences > Plug-in Manager)）。请参见[加载或卸载 Maya 插件](https://beehive.autodesk.com/community/service/rest/cloudhelp/resource/cloudhelpchannel/guidcrossbook/jsonp?v=2022&p=MAYAUL&l=CHS&accessmode=live&guid=GUID-07A89E6C-199C-4719-98A0-11C3A2BCDF21)。

## 相关主题

- [“缓存”(Cache)菜单](https://beehive.autodesk.com/community/service/rest/cloudhelp/resource/cloudhelpchannel/guidcrossbook/jsonp?v=2022&p=MAYAUL&l=CHS&accessmode=live&guid=GUID-9158C004-A9EB-4BF4-9FDB-442EB9851E75#GUID-9158C004-A9EB-4BF4-9FDB-442EB9851E75__GUID-DD40CD48-49AE-42E9-BF00-AD56602DDA75)
