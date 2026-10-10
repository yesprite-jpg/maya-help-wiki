# 创建 Alembic 缓存文件

您可以从场景中的多边形或 NURBS 对象创建 Alembic 缓存文件。将对象保存到 Alembic 缓存时，原始几何的对象层次将保留在文件中。

您可以使用“Alembic 导出”(Alembic Export)窗口中的许多[高级选项(Advanced Options)](https://beehive.autodesk.com/community/service/rest/cloudhelp/resource/cloudhelpchannel/guidcrossbook/jsonp?v=2022&p=MAYAUL&l=CHS&accessmode=live&guid=GUID-854D22F6-7547-465C-8A13-E21A8A6D9714#GUID-854D22F6-7547-465C-8A13-E21A8A6D9714__GUID-67B0B167-5EED-419B-82FE-41068054FBFF)来指定要保存到缓存文件中的内容。

创建 Alembic 缓存

1. 执行下列操作之一：

  - 若要将场景中的所有对象保存到缓存文件中，请选择“缓存 > Alembic 缓存 > 将所有内容导出到 Alembic”(Cache > Alembic Cache > Export All to Alembic) > ![图：若要将场景中的所有对象保存到缓存文件中，请选择“缓存 Alembic 缓存 将所有内容导出到 Alembic”(Cach…](https://help.autodesk.com/cloudhelp/2022/CHS/Maya-ManagingScenes/images/GUID-23B160F6-E1FB-4E29-94B2-7323BFE33726.png) <!-- baize:img-hook downloaded=false reason="正文 876 字 ≥300，非承重" -->。

  - 若要保存选定对象，请选择要缓存的对象，然后选择“缓存 > Alembic 缓存 > 将当前选择导出到 Alembic”(Cache > Alembic Cache > Export Selection to Alembic) > ![图：若要保存选定对象，请选择要缓存的对象，然后选择“缓存 Alembic 缓存 将当前选择导出到 Alembic”(Cach…](https://help.autodesk.com/cloudhelp/2022/CHS/Maya-ManagingScenes/images/GUID-23B160F6-E1FB-4E29-94B2-7323BFE33726.png) <!-- baize:img-hook downloaded=false reason="正文 876 字 ≥300，非承重" -->。

2. 在“Alembic 导出”(Alembic Export)窗口中，设定所需的[常规选项(General Options)](https://beehive.autodesk.com/community/service/rest/cloudhelp/resource/cloudhelpchannel/guidcrossbook/jsonp?v=2022&p=MAYAUL&l=CHS&accessmode=live&guid=GUID-854D22F6-7547-465C-8A13-E21A8A6D9714#GUID-854D22F6-7547-465C-8A13-E21A8A6D9714__GUID-BCBD8BBE-F44A-4778-A696-61518BC50194)。

3. （可选）若要将动态或自定义属性添加到缓存，请展开[属性(Attribute)](https://beehive.autodesk.com/community/service/rest/cloudhelp/resource/cloudhelpchannel/guidcrossbook/jsonp?v=2022&p=MAYAUL&l=CHS&accessmode=live&guid=GUID-854D22F6-7547-465C-8A13-E21A8A6D9714#GUID-854D22F6-7547-465C-8A13-E21A8A6D9714__GUID-5918159F-D121-4D87-ACF3-E27BCC8A8967)区域并执行以下操作：

  - 在“属性”(Attribute)字段中键入属性的名称，然后单击“添加”(Add)。

  - 在“通道盒”(Channel Box)中选择属性，然后单击“来自通道盒”(From Channel Box)。

  添加的属性会显示在“属性”(Attribute)下的表中。

4. （可选）在[高级选项(Advanced Options)](https://beehive.autodesk.com/community/service/rest/cloudhelp/resource/cloudhelpchannel/guidcrossbook/jsonp?v=2022&p=MAYAUL&l=CHS&accessmode=live&guid=GUID-854D22F6-7547-465C-8A13-E21A8A6D9714#GUID-854D22F6-7547-465C-8A13-E21A8A6D9714__GUID-67B0B167-5EED-419B-82FE-41068054FBFF)区域中，设定所需的选项。

  **注**

  若要使 Alembic 缓存的几何体继承原始几何体的着色网络，请启用

  UV 写入(UV Write)

  。请参见

  合并 Alembic 缓存与 Maya 对象

  。

5. （可选）在[回调(Callback)](https://beehive.autodesk.com/community/service/rest/cloudhelp/resource/cloudhelpchannel/guidcrossbook/jsonp?v=2022&p=MAYAUL&l=CHS&accessmode=live&guid=GUID-854D22F6-7547-465C-8A13-E21A8A6D9714#GUID-854D22F6-7547-465C-8A13-E21A8A6D9714__GUID-D3F7C4E6-9E3F-4B1E-9E60-D1684252B240)区域中，键入 MEL 或 Python 回调字符串。

6. 单击“导出全部”(Export All)/“导出当前选择”(Export Selection)。

## 相关主题

- [导入 Alembic 缓存文件](导入%20Alembic%20缓存文件.md)

- [合并 Alembic 缓存与 Maya 对象](使用%20Maya%20对象合并%20Alembic%20缓存.md)

- [关于 Alembic 缓存](../关于%20Alembic%20缓存.md)

- [“Alembic 导出”(Alembic Export)选项](https://beehive.autodesk.com/community/service/rest/cloudhelp/resource/cloudhelpchannel/guidcrossbook/jsonp?v=2022&p=MAYAUL&l=CHS&accessmode=live&guid=GUID-854D22F6-7547-465C-8A13-E21A8A6D9714)

- [“Alembic 导入”(Alembic Import)选项](https://beehive.autodesk.com/community/service/rest/cloudhelp/resource/cloudhelpchannel/guidcrossbook/jsonp?v=2022&p=MAYAUL&l=CHS&accessmode=live&guid=GUID-DEA2C5A5-3D04-4081-BBDE-8D9DC788AF02)
