# “几何缓存”(Geometry Cache)子菜单

#### 创建新缓存(Create New Cache)

**注**

几何缓存仅存储对象顶点的 XYZ 位置，不存储对象的

“变换”(Transform)

节点的平移、旋转或缩放。

为当前对象创建新几何缓存。

如果已选定多个对象，那么会为每个选定对象创建几何缓存（“每个几何体一个文件”(One File per Geometry)），或者为所有选定对象创建单个缓存（“每帧一个文件”(One File per Frame)、“一个文件”(One File)）。请参见[创建和编辑几何缓存](https://beehive.autodesk.com/community/service/rest/cloudhelp/resource/cloudhelpchannel/guidcrossbook/jsonp?v=2022&p=MAYAUL&l=CHS&accessmode=live&guid=GUID-F338ECB1-F4C3-4632-9168-EB917C2353DC)。

选择“几何缓存 > 创建新缓存”(Geometry Cache > Create New Cache) > ![图：选择“几何缓存 创建新缓存”(Geometry Cache Create New Cache) ，以设置创建新缓存选项。](https://help.autodesk.com/cloudhelp/2022/CHS/Maya-Basics/images/GUID-23B160F6-E1FB-4E29-94B2-7323BFE33726.png) <!-- baize:img-hook downloaded=false reason="正文 1892 字 ≥300，非承重" -->，以设置[创建新缓存选项](“几何缓存”%28Geometry%20Cache%29子菜单/创建新缓存选项%28Create%20New%20Cache%20Options%29.md)。

#### 导入缓存(Import Cache)

允许浏览本地硬盘驱动器或服务器，找到将附加到当前对象的现有几何缓存文件。如果当前对象已有几何缓存，那么浏览到并选择的缓存文件将替换原始缓存，但不会将其从磁盘中删除。选择的几何缓存文件必须与导入缓存的目标对象具有相同的拓扑。请参见[创建和编辑几何缓存](https://beehive.autodesk.com/community/service/rest/cloudhelp/resource/cloudhelpchannel/guidcrossbook/jsonp?v=2022&p=MAYAUL&l=CHS&accessmode=live&guid=GUID-F338ECB1-F4C3-4632-9168-EB917C2353DC)主题中的“导入几何缓存”。

#### 导出缓存(Export Cache)

允许您导出选定几何体的缓存文件。

选择“几何缓存 > 导出缓存”(Geometry Cache > Export Cache) > ![图：选择“几何缓存 导出缓存”(Geometry Cache Export Cache) ，以设置导出缓存选项。](https://help.autodesk.com/cloudhelp/2022/CHS/Maya-Basics/images/GUID-23B160F6-E1FB-4E29-94B2-7323BFE33726.png) <!-- baize:img-hook downloaded=false reason="正文 1892 字 ≥300，非承重" -->，以设置[导出缓存选项](“几何缓存”%28Geometry%20Cache%29子菜单/“导出缓存”%28Export%20Cache%29选项.md)。

#### 禁用选定对象的所有缓存(Disable All Caches On Selected)

禁用所有当前对象的几何缓存节点和片段。

#### 启用选定对象的所有缓存(Enable All Caches On Selected)

启用所有当前对象的几何缓存节点和片段。

#### 替换缓存(Replace Cache)

用新生成的缓存替换当前对象的几何缓存。请参见[替换几何缓存](https://beehive.autodesk.com/community/service/rest/cloudhelp/resource/cloudhelpchannel/guidcrossbook/jsonp?v=2022&p=MAYAUL&l=CHS&accessmode=live&guid=GUID-4672CB9D-7ADF-4B09-B49E-703991BC16AA)。

**注**

无法替换具有多个附加缓存的对象的几何缓存。

选择“几何缓存 > 替换缓存”(Geometry Cache > Replace Cache) > ![图：选择“几何缓存 替换缓存”(Geometry Cache Replace Cache) ，以设置替换缓存选项。](https://help.autodesk.com/cloudhelp/2022/CHS/Maya-Basics/images/GUID-23B160F6-E1FB-4E29-94B2-7323BFE33726.png) <!-- baize:img-hook downloaded=false reason="正文 1892 字 ≥300，非承重" -->，以设置[替换缓存选项](“几何缓存”%28Geometry%20Cache%29子菜单/替换缓存选项%28Replace%20Cache%20Options%29.md)。

#### 合并缓存(Merge Caches)

合并当前对象已启用的几何缓存，并禁用已合并的缓存节点。默认情况下，该操作不会删除任何几何缓存节点。请参见[合并几何缓存](https://beehive.autodesk.com/community/service/rest/cloudhelp/resource/cloudhelpchannel/guidcrossbook/jsonp?v=2022&p=MAYAUL&l=CHS&accessmode=live&guid=GUID-7A296FB8-3F6C-4EAB-8F93-6A448ED1FD68)和[合并几何缓存片段](https://beehive.autodesk.com/community/service/rest/cloudhelp/resource/cloudhelpchannel/guidcrossbook/jsonp?v=2022&p=MAYAUL&l=CHS&accessmode=live&guid=GUID-8FF11137-F283-4AC9-9447-69FD6071E1F3)。

选择“几何缓存 > 合并缓存”(Geometry Cache > Merge Cache) > ![图：选择“几何缓存 合并缓存”(Geometry Cache Merge Cache) ，以设置合并缓存选项。](https://help.autodesk.com/cloudhelp/2022/CHS/Maya-Basics/images/GUID-23B160F6-E1FB-4E29-94B2-7323BFE33726.png) <!-- baize:img-hook downloaded=false reason="正文 1892 字 ≥300，非承重" -->，以设置[合并缓存选项](“几何缓存”%28Geometry%20Cache%29子菜单/合并缓存选项%28Merge%20Caches%20Options%29.md)。

#### 删除缓存(Delete Cache)

删除当前对象的几何缓存节点和片段。请参见[删除几何缓存](https://beehive.autodesk.com/community/service/rest/cloudhelp/resource/cloudhelpchannel/guidcrossbook/jsonp?v=2022&p=MAYAUL&l=CHS&accessmode=live&guid=GUID-828F34D3-D28B-46D9-BC2E-6B2E7909ADA7)。

选择“几何缓存 > 删除缓存”(Geometry Cache > Delete Cache) > ![图：选择“几何缓存 删除缓存”(Geometry Cache Delete Cache) ，以设置删除缓存选项。](https://help.autodesk.com/cloudhelp/2022/CHS/Maya-Basics/images/GUID-23B160F6-E1FB-4E29-94B2-7323BFE33726.png) <!-- baize:img-hook downloaded=false reason="正文 1892 字 ≥300，非承重" -->，以设置[删除缓存选项](“几何缓存”%28Geometry%20Cache%29子菜单/删除缓存选项%28Delete%20Cache%20Options%29.md)。

#### 附加到缓存

为当前对象生成新的几何缓存，将其附加到对象的已启用几何缓存中。如果附加的缓存在时间上与已启用的缓存重叠，将自动与已启用的缓存融合。但是，如果已启用的缓存和附加的缓存在时间上存在间隙，请对该间隙采用线性插值方式，不将该间隙的缓存数据保存到附加的缓存中。请参见[附加几何缓存](https://beehive.autodesk.com/community/service/rest/cloudhelp/resource/cloudhelpchannel/guidcrossbook/jsonp?v=2022&p=MAYAUL&l=CHS&accessmode=live&guid=GUID-73B28384-BB9F-4112-AA33-1DC311A153CE)。

选择“几何缓存 > 附加到缓存”(Geometry Cache > Append to Cache) > ![图：选择“几何缓存 附加到缓存”(Geometry Cache Append to Cache) ，以设置附加到缓存选项。](https://help.autodesk.com/cloudhelp/2022/CHS/Maya-Basics/images/GUID-23B160F6-E1FB-4E29-94B2-7323BFE33726.png) <!-- baize:img-hook downloaded=false reason="正文 1892 字 ≥300，非承重" -->，以设置[附加到缓存选项](“几何缓存”%28Geometry%20Cache%29子菜单/附加到缓存选项%28Append%20to%20Cache%20Options%29.md)。

#### 替换缓存帧(Replace Cache Frame)

替换在“替换几何缓存帧选项”(Replace Geometry Cache Frames Options)窗口中指定的当前对象的几何缓存帧。请参见[替换几何缓存](https://beehive.autodesk.com/community/service/rest/cloudhelp/resource/cloudhelpchannel/guidcrossbook/jsonp?v=2022&p=MAYAUL&l=CHS&accessmode=live&guid=GUID-4672CB9D-7ADF-4B09-B49E-703991BC16AA)。使用该选项，可以采用战略方式替换几何缓存文件中的单个缓存帧。例如，通过为特定帧中的对象部分重新建模、然后在其几何缓存文件中替换这些帧，可以提高对象的缓存变形。

**注**

对于拥有多个几何缓存节点的对象，不能替换几何缓存帧。

选择“几何缓存 > 替换缓存帧”(Geometry Cache > Replace Cache Frame) > ![图：选择“几何缓存 替换缓存帧”(Geometry Cache Replace Cache Frame) ，以设置替换缓存帧…](https://help.autodesk.com/cloudhelp/2022/CHS/Maya-Basics/images/GUID-23B160F6-E1FB-4E29-94B2-7323BFE33726.png) <!-- baize:img-hook downloaded=false reason="正文 1892 字 ≥300，非承重" -->，以设置[替换缓存帧选项](“几何缓存”%28Geometry%20Cache%29子菜单/“替换缓存帧”%28Replace%20Cache%20Frame%29选项.md)。

#### 删除缓存帧(Delete Cache Frame)

从当前对象的已启用几何缓存中删除单个帧或整个帧范围。例如，可以截断已启用缓存的开始部分或结尾部分。请参见[删除几何缓存帧](https://beehive.autodesk.com/community/service/rest/cloudhelp/resource/cloudhelpchannel/guidcrossbook/jsonp?v=2022&p=MAYAUL&l=CHS&accessmode=live&guid=GUID-828F34D3-D28B-46D9-BC2E-6B2E7909ADA7#GUID-828F34D3-D28B-46D9-BC2E-6B2E7909ADA7__WS1A9193826455F5FF-6D855556117E9F816D2116E)。

选择“几何缓存 > 删除缓存帧”(Geometry Cache > Delete Cache Frame) > ![图：选择“几何缓存 删除缓存帧”(Geometry Cache Delete Cache Frame) ，以设置删除缓存帧选…](https://help.autodesk.com/cloudhelp/2022/CHS/Maya-Basics/images/GUID-23B160F6-E1FB-4E29-94B2-7323BFE33726.png) <!-- baize:img-hook downloaded=false reason="正文 1892 字 ≥300，非承重" -->，以设置[删除缓存帧选项](“几何缓存”%28Geometry%20Cache%29子菜单/“删除缓存帧”%28Delete%20Cache%20Frame%29选项.md)。

#### 删除缓存之前的历史(Delete History Ahead Of Cache)

移除选中对象的所有上游构建历史记录，同时保留对象的几何缓存变形。

#### 绘制缓存权重工具(Paint Cache Weights Tool)

将“绘制缓存权重工具”(Paint Cache Weights Tool)作为当前工具。使用此工具，可以绘制和融合单个对象表面上的多个缓存权重。请参见[绘制几何缓存权重](https://beehive.autodesk.com/community/service/rest/cloudhelp/resource/cloudhelpchannel/guidcrossbook/jsonp?v=2022&p=MAYAUL&l=CHS&accessmode=live&guid=GUID-83339C2D-6BFF-4D13-A8A8-C844BDF72147#GUID-83339C2D-6BFF-4D13-A8A8-C844BDF72147__GUID-F7D15571-3255-4858-A974-FA34BB88E3B3)。

选择“几何缓存 > 绘制缓存权重工具”(Geometry Cache > Paint Cache Weights Tool) > ![图：选择“几何缓存 绘制缓存权重工具”(Geometry Cache Paint Cache Weights Tool) ，…](https://help.autodesk.com/cloudhelp/2022/CHS/Maya-Basics/images/GUID-23B160F6-E1FB-4E29-94B2-7323BFE33726.png) <!-- baize:img-hook downloaded=false reason="正文 1892 字 ≥300，非承重" -->，以设置[绘制缓存权重工具选项](“几何缓存”%28Geometry%20Cache%29子菜单/“绘制缓存权重工具”%28Paint%20Cache%20Weights%20Tool%29选项.md)。

**注**

几何缓存仅存储对象顶点的 XYZ 位置，不存储对象的

“变换”(Transform)

节点的平移、旋转或缩放。
