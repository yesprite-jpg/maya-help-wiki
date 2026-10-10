# “传递属性值”(Transfer Attribute Values)选项

使用这些选项可设置在选择“编辑 > 传递属性值”(Edit > Transfer Attribute Values)时会发生的状况。另请参见[传递属性值](../../../../变换对象/变换对象/匹配对象属性值.md)。

#### 属性(Attributes)

如果“来自通道盒”(From channel box)处于启用状态，则只会传递当前在“通道盒”(Channel Box)中亮显的属性。

#### 值(Values)

如果此选项处于启用状态，则属性值将从源对象复制到目标对象。如果此选项禁用，则这些值会被引用。

### 输入连接(In connections)

如果启用此选项，则通过“与源共享”(Share with source)或“从源传递”(Transfer from source)可以将从其他外部节点来的传入连接从源资产传递到目标对象。

#### 与源共享(Share with source)

Maya 会创建从外部节点到目标对象的新传入连接。因此，更改外部节点会影响源对象和目标对象二者。

#### 从源传递(Transfer from source)

Maya 删除到源资产的传入连接并创建到目标对象的新连接。因此，更改外部节点仅影响目标对象。

#### 输出连接(Out connections)

如果启用此选项，则所有到其他节点的引出连接从源对象移动到目标对象。

#### 关系(Relationships)

如果启用“传递父/子关系”(Transfer parent/child relationships)，且源和目标对象是具有相同已发布父或子定位点名称的资产，则父/子关系从源资产传递到目标资产。

#### 重命名(Rename)

如果“重命名目标资产”(Rename target asset)处于启用状态，则目标资产将以源资产的名称重命名。源资产将以 -Orig 为后缀重命名。

当您希望将场景中的目标资产完全替换为源资产时，“关系”(Relationships)和“重命名”(Rename)选项非常有用。

## 相关主题

- [在资产之间传递属性值](https://beehive.autodesk.com/community/service/rest/cloudhelp/resource/cloudhelpchannel/guidcrossbook/jsonp?v=2022&p=MAYAUL&l=CHS&accessmode=live&guid=GUID-DA9C2857-EF01-4BCF-84D5-057281FE52B5)
