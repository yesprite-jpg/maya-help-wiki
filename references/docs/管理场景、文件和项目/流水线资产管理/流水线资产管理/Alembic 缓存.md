# Alembic 缓存

通过 Alembic 缓存导出和导入选项，将 Maya 场景和几何体另存为基于 Alembic 的缓存文件并进行加载。Alembic 文件是具有较强可移植性且与应用程序无关的文件，因此可由多种内容创建应用程序进行共享、处理和播放。

Alembic 文件格式是一种开源格式，专为交换复杂 3D 几何数据而开发。Alembic 文件是具有较强可移植性且与应用程序无关的文件，因此可由多种内容创建应用程序进行共享、处理和播放。

![图：（图旁无可取正文，Maya 手册 img 无 alt）](https://help.autodesk.com/cloudhelp/2022/CHS/Maya-ManagingScenes/images/GUID-60AFF3D2-CC61-4FE8-8B2E-B4594DEE0F94.png) <!-- baize:img-hook downloaded=false reason="正文 821 字 ≥300，非承重" -->

**注**

提示：

若要显示 Maya 正在使用的 Alembic 版本，请在 Maya 的

“脚本编辑器”(Script Editor)

中键入以下 Python 命令：

```text
import alembic.Abc
print alembic.Abc.GetLibraryVersion()
```

在 Maya 中，基于 Alembic 的缓存提供了许多性能改进，包括加快大型场景加载速度、更快速播放复杂角色动画，以及实时播放包含拓扑更改的几何数据。可以将复杂的场景和动画导出为 Alembic 文件，然后将其重新导入到 Maya 中，以提高播放性能并减少内存使用。通过此工作流，可以轻松地将复杂场景数据传递到制作流程的各个区域，如动画与模拟之间的区域或动画与照明之间的区域，而不会因为完全可编辑的场景产生较大的开销。

有两种类型的基于 Alembic 的缓存：Alembic 缓存和 GPU 优化缓存。有关详细信息，请参见[关于 Alembic 缓存](Alembic%20缓存/关于%20Alembic%20缓存.md)和[关于 GPU 缓存](Alembic%20缓存/关于%20GPU%20缓存.md)。这两种缓存文件都与第三方应用程序兼容，并都以 .abc 文件扩展名保存。Alembic 和 GPU 缓存选项位于 [“缓存”(Cache)菜单](https://beehive.autodesk.com/community/service/rest/cloudhelp/resource/cloudhelpchannel/guidcrossbook/jsonp?v=2022&p=MAYAUL&l=CHS&accessmode=live&guid=GUID-9158C004-A9EB-4BF4-9FDB-442EB9851E75)中。

**注**

您可以使用

“文件 > 创建引用”(File > Create Reference)

从 Alembic 文件创建文件引用。

## 相关主题

- [“Alembic 导出”(Alembic Export)选项](https://beehive.autodesk.com/community/service/rest/cloudhelp/resource/cloudhelpchannel/guidcrossbook/jsonp?v=2022&p=MAYAUL&l=CHS&accessmode=live&guid=GUID-854D22F6-7547-465C-8A13-E21A8A6D9714)

- [“Alembic 导入”(Alembic Import)选项](https://beehive.autodesk.com/community/service/rest/cloudhelp/resource/cloudhelpchannel/guidcrossbook/jsonp?v=2022&p=MAYAUL&l=CHS&accessmode=live&guid=GUID-DEA2C5A5-3D04-4081-BBDE-8D9DC788AF02)

- [GPU 缓存导出选项(GPU Cache Export Options)](https://beehive.autodesk.com/community/service/rest/cloudhelp/resource/cloudhelpchannel/guidcrossbook/jsonp?v=2022&p=MAYAUL&l=CHS&accessmode=live&guid=GUID-3E89B28E-6F87-4842-9B2B-5FBEF171810F)

- [“GPU 缓存”(GPU Cache)子菜单](https://beehive.autodesk.com/community/service/rest/cloudhelp/resource/cloudhelpchannel/guidcrossbook/jsonp?v=2022&p=MAYAUL&l=CHS&accessmode=live&guid=GUID-C91C0C17-8A1A-4ADA-85A4-FB3FFE12BE52)
