# 使用 Maya 对象合并 Alembic 缓存

导入 Alembic 缓存时，可以使用原始 Maya 对象合并缓存的对象。合并时，Alembic 几何体将替换场景中的原始对象。Alembic 对象的动画数据将保留，并继承场景对象的着色数据。若要进行合并，Alembic 对象必须与源几何体具有相同的名称和对象层次。场景和 Alembic 对象的拓扑不需要匹配。

![图：（图旁无可取正文，Maya 手册 img 无 alt）](https://help.autodesk.com/cloudhelp/2022/CHS/Maya-ManagingScenes/images/GUID-84F67B8F-E625-439A-9D6A-BC6509275729.png) <!-- baize:img-hook downloaded=false reason="正文 340 字 ≥300，非承重" -->

若要从 Maya 几何体中继承着色网络，Alembic 几何体必须具有源对象的 UV 信息。通过在导出 Alembic 缓存时启用[“UV 写入”(UV Write)](https://beehive.autodesk.com/community/service/rest/cloudhelp/resource/cloudhelpchannel/guidcrossbook/jsonp?v=2022&p=MAYAUL&l=CHS&accessmode=live&guid=GUID-854D22F6-7547-465C-8A13-E21A8A6D9714#GUID-854D22F6-7547-465C-8A13-E21A8A6D9714__GUID-10280AF1-89E8-4A63-B718-7E7B8BC9BA22)可以导出 UV 映射。请参见[创建 Alembic 缓存](创建%20Alembic%20缓存文件.md)和[导入 Alembic 缓存文件](导入%20Alembic%20缓存文件.md)。

## 相关主题

- [创建 Alembic 缓存](创建%20Alembic%20缓存文件.md)

- [关于 Alembic 缓存](../关于%20Alembic%20缓存.md)

- [“Alembic 导出”(Alembic Export)选项](https://beehive.autodesk.com/community/service/rest/cloudhelp/resource/cloudhelpchannel/guidcrossbook/jsonp?v=2022&p=MAYAUL&l=CHS&accessmode=live&guid=GUID-854D22F6-7547-465C-8A13-E21A8A6D9714)

- [“Alembic 导入”(Alembic Import)选项](https://beehive.autodesk.com/community/service/rest/cloudhelp/resource/cloudhelpchannel/guidcrossbook/jsonp?v=2022&p=MAYAUL&l=CHS&accessmode=live&guid=GUID-DEA2C5A5-3D04-4081-BBDE-8D9DC788AF02)
