# 发布属性选项(Publish Attributes Options)

使用这些选项，可设置选择“修改 > 资产 > 发布属性”(Modify > Asset > Publish Attributes)时发生的情况。另请参见[发布或取消发布属性](https://beehive.autodesk.com/community/service/rest/cloudhelp/resource/cloudhelpchannel/guidcrossbook/jsonp?v=2022&p=MAYAUL&l=CHS&accessmode=live&guid=GUID-7BBE4BC1-4B18-47DA-A972-62121764AFBF)。

## 发布(Publish)

指定要发布的节点。

#### 选定通道盒属性(Selected Channel Box attributes)

在“通道盒”(Channel Box)中发布所有当前亮显的属性。

#### 所有可设定关键帧(All Keyable)

为选定节点发布所有可设置关键帧的动画属性。

#### 传入连接(Incoming Connections)

发布所有当前由其他节点的连接来决定值的属性。

#### 选定属性(Selected Attributes)

将选定节点中的所有当前选定属性发布到选定资产中。

## 属性名称(Attribute name)

指定资产中已发布属性的名称。对已发布的属性进行重命名操作不会对原始节点上源属性的名称产生影响，而且重命名的属性仍能保持与这些源属性的连接。

#### 添加一个数字使其唯一(Add a number to make it unique)

如果在资产中已存在同名的已发布属性，则会自动附加一个数字到已发布属性的名称中。

#### 使用节点名称作为前缀(Prefix with node name)

自动将节点名称（后面紧接一个下划线）用作资产中已发布属性的名称前缀。例如，pSphere1_translateX。

#### 使用自定义字符串作为前缀(Prefix with custom string)

自动将“自定义字符串”(Custom string)字段中的文本（后面紧接一个下划线）用作资产中已发布属性的名称前缀。

#### 自定义名称(Custom name)

将已发布的属性重命名为“自定义字符串”(Custom string)字段中的文本。

## 自定义字符串(Custom string)

在将“属性名称”(Attribute name)选项设置为使用自定义字符串或“自定义名称”(Custom name)作为“前缀”(Prefix)时，该选项会使用此字段中的文本。

**注**

无法发布名称为“note”或名称中包含“.”的属性名称，因为二者分别是保留关键字和保留符号。

## 相关主题

- [已发布的属性和节点](https://beehive.autodesk.com/community/service/rest/cloudhelp/resource/cloudhelpchannel/guidcrossbook/jsonp?v=2022&p=MAYAUL&l=CHS&accessmode=live&guid=GUID-93823D5C-2DFE-476C-B624-B77D862AC3EA)
