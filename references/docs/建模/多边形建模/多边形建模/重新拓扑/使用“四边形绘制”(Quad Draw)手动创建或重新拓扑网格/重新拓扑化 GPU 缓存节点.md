# 重新拓扑化 GPU 缓存节点

您可以使用 Maya 的“流水线缓存”(Pipeline Cache)选项来重新拓扑化具有较高多边形计数的密集资产。GPU 缓存文件将把模型的原始节点层次合并为单个节点，不仅提高 Maya 的性能和内存使用情况，同时也使资产与“激活”(Make Live)和“四边形绘制”(Quad Draw)兼容。您可以通过以下方法创建 GPU 缓存：将模型导出为 Alembic 文件并将该文件作为 GPU 缓存节点重新导入 Maya 中。

重新拓扑化 GPU 缓存节点

1. 在 Maya 主菜单栏中，选择“流水线缓存 > GPU 缓存 > 导出全部 >(Pipeline Cache > GPU Cache > Export All >) ![图：在 Maya 主菜单栏中，选择“流水线缓存 GPU 缓存 导出全部 (Pipeline Cache GPU Cache …](https://help.autodesk.com/cloudhelp/2022/CHS/Maya-Modeling/images/GUID-23B160F6-E1FB-4E29-94B2-7323BFE33726.png) <!-- baize:img-hook downloaded=false reason="正文 721 字 ≥300，非承重" -->。

2. 在显示的“GPU 缓存导出选项”(GPU Cache Export Options)窗口中，设置以下选项：

  - 缓存时间范围(Cache Time Range)：当前帧(Current Frame)

  - 优化层次(Optimize Hierarchy)：启用

  **注**

  提示：

  如果资产中包含多个对象，请指定大于最高分辨率对象中顶点总数的

  “优化阈值”(Optimization Threshold)

  值。例如，如果最高分辨率对象包含 22000000 个顶点，请将

  “优化阈值”(Optimization Threshold)

  设置为 22000001。

  GPU 缓存文件将导出为 Alembic 文件，并保存在当前 Maya 项目的 cache\alembic 文件夹中。

3. 将 Alembic 文件导入为 GPU 缓存节点。请参见[导入 GPU 缓存节点](https://beehive.autodesk.com/community/service/rest/cloudhelp/resource/cloudhelpchannel/guidcrossbook/jsonp?v=2022&p=MAYAUL&l=CHS&accessmode=live&guid=GUID-907BB76E-1A01-4A29-B2FA-659B7CDA7BC4#GUID-907BB76E-1A01-4A29-B2FA-659B7CDA7BC4__OL_3B56302063A7433A84FB9B58C800C19B)。

  该文件将在 Maya 中加载为单个节点。

4. 使 GPU 缓存节点成为引用网格。请参见[设置四边形绘制的引用网格](使用四边形绘制重新拓扑网格/设置四边形绘制的引用网格.md)。

5. 开始重新拓扑化网格。请参见[使用四边形绘制重新拓扑网格](使用四边形绘制重新拓扑网格.md#GUID-03933C1F-1BA7-4E7E-AAB5-31FB0E6A77B2__OL_9F5FD0AC65FF486AB2A6E7D7E50B2997)。

## 相关主题

- [创建或导入 GPU 缓存](https://beehive.autodesk.com/community/service/rest/cloudhelp/resource/cloudhelpchannel/guidcrossbook/jsonp?v=2022&p=MAYAUL&l=CHS&accessmode=live&guid=GUID-907BB76E-1A01-4A29-B2FA-659B7CDA7BC4)

- [关于 GPU 缓存](https://beehive.autodesk.com/community/service/rest/cloudhelp/resource/cloudhelpchannel/guidcrossbook/jsonp?v=2022&p=MAYAUL&l=CHS&accessmode=live&guid=GUID-C893BE60-6E65-4F36-8005-FD4D1A0E9822)

- [使用四边形绘制重新拓扑网格](使用四边形绘制重新拓扑网格.md)
