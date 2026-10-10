# “删除缓存帧”(Delete Cache Frame)选项

使用这些选项可设置在选择“缓存 > 几何缓存 > 删除缓存帧”(Cache > Geometry Cache > Delete Cache Frame)时发生的情况。另请参见[删除几何缓存](https://beehive.autodesk.com/community/service/rest/cloudhelp/resource/cloudhelpchannel/guidcrossbook/jsonp?v=2022&p=MAYAUL&l=CHS&accessmode=live&guid=GUID-828F34D3-D28B-46D9-BC2E-6B2E7909ADA7)中的“删除几何缓存帧”。

#### 当前时间(Current Time)

指定要从当前对象的已启用几何缓存中删除的当前缓存帧。

#### 开始/结束(Start/End)

指定从当前对象的已启用几何缓存中删除“开始删除帧”(Start Delete Frame)到“结束删除帧”(End Delete Frame)的缓存帧的范围。

#### 开始删除帧/结束删除帧(Start Delete Frame/End Delete frame)

这些字段使您可以为要删除的帧的范围指定开始和结束时间。

#### 已移除帧的默认重命名(Default renaming of removed frames)

指定已删除的帧在磁盘上另存为新的单独几何缓存文件以及使用前缀 backup 重命名。例如，如果从 Ball1 几何缓存中删除帧 20，那么帧 20 在磁盘上另存为 backup_Ball1.mc，并且为已删除的缓存帧生成新 .xml 描述文件。

#### 已移除帧的自定义重命名(Custom renaming of removed frames)

指定已删除的帧在磁盘上保存为新的单独几何缓存文件，文件名称使用已移除帧的自定义重命名字段中指定的自定义名称。例如，如果指定的自定义名称为 deleted20Ball1 并从 Ball1 几何缓存中删除帧 20，那么帧 20 在磁盘上另存为 deleted20Ball1.mc，并且为已删除的缓存帧生成新 .xml 描述文件。

#### 删除备份文件(Delete backup files)

启用时，要删除的缓存帧也将从磁盘上的其几何缓存文件中删除。删除是永久性的，无法通过“编辑 > 撤消”(Edit > Undo)或 Ctrl+Z 撤消。
