# 导入 Alembic 缓存文件

您可以将 Alembic 缓存作为单独的对象层次导入 Maya 场景中，也可以将缓存的对象添加到场景的现有对象层次中。将 Alembic 对象添加到现有对象层次时，可选择将所选几何体设置为 Alembic 对象的子对象，或者将 Alembic 对象与原始 Maya 几何体进行合并。请参见[合并 Alembic 与 Maya 几何体](使用%20Maya%20对象合并%20Alembic%20缓存.md)。

将 Alembic 缓存作为单独的对象层次导入

1. 在“动画”(Animation)菜单集中，选择“缓存 > 导入 Alembic”(Cache > Import Alembic) > ![图：在“动画”(Animation)菜单集中，选择“缓存 导入 Alembic”(Cache Import Alembic)…](https://help.autodesk.com/cloudhelp/2022/CHS/Maya-ManagingScenes/images/GUID-23B160F6-E1FB-4E29-94B2-7323BFE33726.png) <!-- baize:img-hook downloaded=false reason="正文 1267 字 ≥300，非承重" -->。

  有关信息，请参见[“Alembic 导入”(Alembic Import)选项](https://beehive.autodesk.com/community/service/rest/cloudhelp/resource/cloudhelpchannel/guidcrossbook/jsonp?v=2022&p=MAYAUL&l=CHS&accessmode=live&guid=GUID-DEA2C5A5-3D04-4081-BBDE-8D9DC788AF02)。

2. 在“Alembic 导入”(Alembic Import)窗口中，选择“缓存 > Alembic 缓存 > 导入 Alembic”(Cache > Alembic Cache > Import Alembic)。

3. 单击“导入”(Import)。

  Alembic 对象将作为单独的层次导入到场景的根。

将 Alembic 导入现有对象层次

1. 在“大纲视图”(Outliner)或场景视图中，选择要设为父对象或要与 Alembic 对象合并的对象层次。

2. 选择“缓存 > 导入 Alembic”(Cache > Import Alembic) > ![图：选择“缓存 导入 Alembic”(Cache Import Alembic) 。](https://help.autodesk.com/cloudhelp/2022/CHS/Maya-ManagingScenes/images/GUID-23B160F6-E1FB-4E29-94B2-7323BFE33726.png) <!-- baize:img-hook downloaded=false reason="正文 1267 字 ≥300，非承重" -->。

3. 在“Alembic 导入”(Alembic Import)窗口中，选择[“在当前选择下导入”(Import under current selection)](https://beehive.autodesk.com/community/service/rest/cloudhelp/resource/cloudhelpchannel/guidcrossbook/jsonp?v=2022&p=MAYAUL&l=CHS&accessmode=live&guid=GUID-DEA2C5A5-3D04-4081-BBDE-8D9DC788AF02#GUID-DEA2C5A5-3D04-4081-BBDE-8D9DC788AF02__GUID-3576B09F-0071-45A2-A474-2D73D91E7EB9)。

4. 在“在当前选择下导入”(Import under current selection)下，执行以下操作之一：

  - 选择[添加(Add)](https://beehive.autodesk.com/community/service/rest/cloudhelp/resource/cloudhelpchannel/guidcrossbook/jsonp?v=2022&p=MAYAUL&l=CHS&accessmode=live&guid=GUID-DEA2C5A5-3D04-4081-BBDE-8D9DC788AF02#GUID-DEA2C5A5-3D04-4081-BBDE-8D9DC788AF02__GUID-FCB17371-0FDE-4B95-B0EB-F0567F066A4C)将所导入的 Alembic 对象设置为选定对象层次的子对象。

    导入时，Alembic 对象会显示在选定场景对象下方的层次中。

  - 选择[合并(Merge)](https://beehive.autodesk.com/community/service/rest/cloudhelp/resource/cloudhelpchannel/guidcrossbook/jsonp?v=2022&p=MAYAUL&l=CHS&accessmode=live&guid=GUID-DEA2C5A5-3D04-4081-BBDE-8D9DC788AF02#GUID-DEA2C5A5-3D04-4081-BBDE-8D9DC788AF02__GUID-062FCD60-7420-4161-8770-F29F2AA4B4A5)将 Alembic 对象与选定几何体进行合并。

    导入时，Alembic 对象与原始几何体将合并为一个对象层次。要进行合并，Alembic 对象与选定 Maya 几何体必须具有相同的名称和对象层次。请参见[合并 Alembic 与 Maya 几何体](使用%20Maya%20对象合并%20Alembic%20缓存.md)。

5. 如果选择了“合并”(Merge)，可选择[从文件中添加非匹配内容(Add non-matching content from file)](https://beehive.autodesk.com/community/service/rest/cloudhelp/resource/cloudhelpchannel/guidcrossbook/jsonp?v=2022&p=MAYAUL&l=CHS&accessmode=live&guid=GUID-DEA2C5A5-3D04-4081-BBDE-8D9DC788AF02#GUID-DEA2C5A5-3D04-4081-BBDE-8D9DC788AF02__GUID-A5D5BC07-E4E7-4E3E-B20E-569E95E7DAA4)或[从场景中移除非匹配内容(Remove non-matching content from the scene)](https://beehive.autodesk.com/community/service/rest/cloudhelp/resource/cloudhelpchannel/guidcrossbook/jsonp?v=2022&p=MAYAUL&l=CHS&accessmode=live&guid=GUID-DEA2C5A5-3D04-4081-BBDE-8D9DC788AF02#GUID-DEA2C5A5-3D04-4081-BBDE-8D9DC788AF02__GUID-494F8679-8DE3-4612-BAC2-79F0483E59F7)。

6. 单击“导入”(Import)。

  **注**

  如果未着色显示合并的对象，请确保 Alembic 缓存文件包含源对象的 UV 信息。请参见

  UV 写入

  。

**注**

重要：

如果导出的 Alembic 缓存不使用默认的 Maya 场景单位“厘米”，随后将其导入到使用该单位的场景，Alembic 几何体的变换值将不正确。

若要更正这些值，请选择已导入的缓存，然后在“节点编辑器”(Node Editor)中选择“unitConversion”节点，并将其“转化因子”(Conversion Factor)属性值设置为 1。

## 相关主题

- [创建 Alembic 缓存](创建%20Alembic%20缓存文件.md)

- [合并 Alembic 缓存与 Maya 对象](使用%20Maya%20对象合并%20Alembic%20缓存.md)

- [关于 Alembic 缓存](../关于%20Alembic%20缓存.md)

- [“Alembic 导入”(Alembic Import)选项](https://beehive.autodesk.com/community/service/rest/cloudhelp/resource/cloudhelpchannel/guidcrossbook/jsonp?v=2022&p=MAYAUL&l=CHS&accessmode=live&guid=GUID-DEA2C5A5-3D04-4081-BBDE-8D9DC788AF02)

- [“Alembic 导出”(Alembic Export)选项](https://beehive.autodesk.com/community/service/rest/cloudhelp/resource/cloudhelpchannel/guidcrossbook/jsonp?v=2022&p=MAYAUL&l=CHS&accessmode=live&guid=GUID-854D22F6-7547-465C-8A13-E21A8A6D9714)
