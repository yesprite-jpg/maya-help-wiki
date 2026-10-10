# “Alembic 导入”(Alembic Import)选项

使用这些选项可控制在选择“缓存 > Alembic 缓存 > 导入 Alembic”(Cache > Alembic Cache > Import Alembic)将 Alembic 缓存文件导入场景时发生的情况。另请参见[导入 Alembic 缓存文件](https://beehive.autodesk.com/community/service/rest/cloudhelp/resource/cloudhelpchannel/guidcrossbook/jsonp?v=2022&p=MAYAUL&l=CHS&accessmode=live&guid=GUID-3C1D1B0C-5D75-41DF-8480-CD7A42CCBCBE)。

#### 文件内容

从下列选项中选择：

#### 导入到场景根(Import to scene root)

将 Alembic 文件导入到场景根并保持文件的原始对象层次。

#### 在当前选择下导入(Import under current selection)

导入 Alembic 文件，并允许您指定它在层次中相对于场景中其他对象的位置。请参见下面的“添加”(Add)和“合并”(Merge)导入选项。

#### 添加(Add)

将选定对象设置为导入的基于 Alembic 的对象的父对象。如果选择多个对象，则基于 Alembic 的对象将成为首先选择的对象的子对象。此选项仅在“导入”(Import)处于启用状态时适用。

**注**

在

“添加”(Add)

处于启用状态的情况下，每次导入 Alembic 文件时，只能选择一个场景对象层次。

#### 合并(Merge)

可以将选定对象中的数据与导入的 Alembic 对象的数据合并。要进行合并，场景和 Alembic 对象必须具有相同的名称和对象层次。否则，不会导入任何文件。

合并时，Alembic 对象几何体将替换场景对象。场景和 Alembic 对象的拓扑不需要匹配即可进行合并。Alembic 对象的动画数据将保留，并继承场景对象的着色数据。

#### 从文件中添加非匹配内容(Add non-matching content from file)

指定如果场景中不存在具有相同名称或层次的对象，将创建一个对象，并将其连接到导入的 Alembic 文件。此选项仅适用于“合并”(Merge)。

#### 从场景中移除非匹配内容(Remove non-matching content from the scene)

移除不包含在导入的 Alembic 文件中的场景对象。例如，如果有一个 pSphere1 对象在场景中，但不在导入的 Alembic 文件中，则将移除该 pSphere1。

#### 适配时间范围(Fit Time Range)

更新当前场景的时间滑块范围，以匹配导入的 Alembic 文件的时间滑块范围。

#### 将当前时间设置为开始帧(Set Current Time to Start Frame)

将场景的当前时间设置为导入的 Alembic 文件的开始帧。

#### 调试(Debug)

在“脚本编辑器”(Script Editor)窗口中显示调试信息。

## 相关主题

- [创建 Alembic 缓存](https://beehive.autodesk.com/community/service/rest/cloudhelp/resource/cloudhelpchannel/guidcrossbook/jsonp?v=2022&p=MAYAUL&l=CHS&accessmode=live&guid=GUID-6C9504CD-9107-4DA2-B618-CAA9045906D4)

- [关于 Alembic 缓存](https://beehive.autodesk.com/community/service/rest/cloudhelp/resource/cloudhelpchannel/guidcrossbook/jsonp?v=2022&p=MAYAUL&l=CHS&accessmode=live&guid=GUID-332E42EB-148B-4AFC-8F8C-B912470609C6)
