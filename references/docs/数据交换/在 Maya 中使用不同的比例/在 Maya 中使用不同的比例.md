# 在 Maya 中使用不同的比例

有时，可能希望更改 Maya 的默认设置，以简化涉及使用不同比例的软件的工作流，或者与其他度量（如英制单位）相对应。

可以更改 Maya 中的默认工作单位（公制单位），但是建议将它们保持不变，因为 Maya 中的一些工具具有固定的类型，例如，Nucleus 和 Bifrost 是硬编码的，因此 1 单位 = 1 米，而不管工作单位如何。相反，不要更改 Maya 的默认工作单位，并调整您的栅格，使之与您所处理的项目的比例保持一致。

**注**

本主题将介绍比例和大小相关内容。不过，您可能还会遇到有关变换上方向轴的问题。请参见

切换文件的上方向轴

，了解有关使用不同的世界轴的信息。

## Unreal 游戏引擎

**更改 Maya 的栅格线以便它们与 Unreal 游戏引擎匹配**

1. 请确保 Maya 工作单位设置为厘米（Maya 默认值），因为 1 Unreal 单位 (uu) 等于 1 厘米 (cm)。（在“设置/首选项”(Settings/Preferences)窗口的[“设置首选项”(Settings preferences)](https://beehive.autodesk.com/community/service/rest/cloudhelp/resource/cloudhelpchannel/guidcrossbook/jsonp?v=2022&p=MAYAUL&l=CHS&accessmode=live&guid=GUID-4D653DC9-57AA-4D8B-987A-5B7A9735CAF0)部分中更改“工作单位”(Working Units)。）

2. 打开[栅格选项(Grid Options)](https://beehive.autodesk.com/community/service/rest/cloudhelp/resource/cloudhelpchannel/guidcrossbook/jsonp?v=2022&p=MAYAUL&l=CHS&accessmode=live&guid=GUID-8BA33EDC-70A9-43E5-83CA-9E87225AB7F7)（“显示”(Display) > “栅格”(Grid) > ![图：打开栅格选项(Grid Options)（“显示”(Display) “栅格”(Grid) ）。](https://help.autodesk.com/cloudhelp/2022/CHS/Maya-DataExchange/images/GUID-23B160F6-E1FB-4E29-94B2-7323BFE33726.png) <!-- baize:img-hook downloaded=false reason="正文 1804 字 ≥300，非承重" -->）。

3. 将“栅格线间距”(Grid Lines Every)设置为 10.000。

**注**

- 每次创建新文件时，都将 Maya 的“工作单位”(Working Units)重置为默认值（厘米）。请参见[新建场景选项(New Scene Options)](https://beehive.autodesk.com/community/service/rest/cloudhelp/resource/cloudhelpchannel/guidcrossbook/jsonp?v=2022&p=MAYAUL&l=CHS&accessmode=live&guid=GUID-8F961875-1D41-4C52-9CD5-B90DE75C546C)。

- 激活“栅格捕捉”(Grid snapping)以避免笨拙的分数度量。请参见[捕捉到栅格、曲线、点、视图平面或几何体中心](https://beehive.autodesk.com/community/service/rest/cloudhelp/resource/cloudhelpchannel/guidcrossbook/jsonp?v=2022&p=MAYAUL&l=CHS&accessmode=live&guid=GUID-E6E866EE-EEE8-4974-A3E7-9AD6ADBB9BCD)。

- 使用“文件”(File) > “发送到 Unreal”(Send to Unreal)选项将场景导出到 Unreal 游戏引擎。请参见[将场景导出到 Unreal 引擎](../将场景导出到%20Unreal%20Engine/将场景导出到%20Unreal%20Engine.md)。

## Unity3D 游戏引擎

Unity3D 和 Maya 都使用公制工作单位，因此无需更改 Maya 的“工作单位”(Working Units)。

但是，导出到 Unity 时，在**[“FBX 导出”(FBX Export)窗口](../Maya%20FBX%20插件/Maya%20FBX%20插件/FBX%20导出/FBX%20导出选项.md)**中也将导出设置设为厘米。这可确保您的场景单位为米，而导出设置为厘米，这样将场景置于 Unity3D 中时，比例因子是 1 而不是 0.01。

- 使用**“文件 > 发送到 Unity”(File > Send to Unity)**选项进行导出。请参见**[将场景导出到 Unity](../将场景导出到%20Unity/将场景导出到%20Unity.md)**。

## 3ds Max 的缩放

3ds Max 有两个单位设置：“系统”(System)和“显示”(Display)。但与 Maya 不同，3ds Max 使用英寸作为其工作单位。如果在 3ds Max 中将显示单位更改为厘米，而将默认系统单位（即英寸）保持不变，那么在与其他软件应用程序交换文件时会产生问题。

在 Maya 和 3ds Max 之间移动数据时，会使用 .fbx 格式，在这种情况下，请更改 3ds Max 系统单位设置以便与 Maya 工作单位匹配。

## 使用英尺和英寸

将栅格更改为英尺和英寸，同时将 Maya 的默认工作单位保持为厘米

1. 选择“显示”(Display) > “栅格”(Grid) > ![图：选择“显示”(Display) “栅格”(Grid) ，以打开栅格选项(Grid Options)。](https://help.autodesk.com/cloudhelp/2022/CHS/Maya-DataExchange/images/GUID-23B160F6-E1FB-4E29-94B2-7323BFE33726.png) <!-- baize:img-hook downloaded=false reason="正文 1804 字 ≥300，非承重" -->，以打开[栅格选项(Grid Options)](https://beehive.autodesk.com/community/service/rest/cloudhelp/resource/cloudhelpchannel/guidcrossbook/jsonp?v=2022&p=MAYAUL&l=CHS&accessmode=live&guid=GUID-8BA33EDC-70A9-43E5-83CA-9E87225AB7F7)。

2. 将**“长度和宽度”(Length and Width)**设置设为 1.0。这表示总体栅格大小。

3. 将**“栅格线间距”(Grid Lines Every)**设置为 30.48。这是因为 1 英尺等于 30.48 厘米。

4. 将**“细分”(Subdivisions)**设置为 12。这会将栅格拆分为 1 英尺方形，每 12 英寸有一个细分。

#### 大型场景

处理大型场景（如城市）时很难以厘米为单位按现实世界的比例展开工作，因为您需要处理特别大的值，这可能会导致精度错误。

在这种情况下，可以将单位设置为米，同时将线性单位设置为厘米。

#### 角色和比例

一般规则是，角色应为 10 个单位高，以避免出现精度问题。

#### 动画和比例

由于 Maya 内部使用 1 单位表示 1 厘米，因此对于动画角色涉及较大距离的场景来说，这通常太小了。为此，请尝试切换为 1 单位 = 1 米。当然，将单位从 1 厘米切换为 1 米会产生精度问题，在横跨较大距离的场景中您的动画会远离原点，但是，如果改为围绕角色和摄影机来设置集的动画，则可以解释这一点。

#### 剪裁平面

如果以厘米为单位按现实世界的比例展开工作，则很可能需要调整剪裁平面。检查正交摄影机的位置，因为它们可能离对象太近。将场景转化为米时，尤其需要这样做。请参见[剪裁平面](https://beehive.autodesk.com/community/service/rest/cloudhelp/resource/cloudhelpchannel/guidcrossbook/jsonp?v=2022&p=MAYAUL&l=CHS&accessmode=live&guid=GUID-D69C23DA-ECFB-4D95-82F5-81118ED41C95)。

## 相关主题

- [计算两点之间的距离](https://beehive.autodesk.com/community/service/rest/cloudhelp/resource/cloudhelpchannel/guidcrossbook/jsonp?v=2022&p=MAYAUL&l=CHS&accessmode=live&guid=GUID-FBCD868D-4BFB-4C1F-8A2F-9DAF64E46A8E)

- [缩放对象和组件](https://beehive.autodesk.com/community/service/rest/cloudhelp/resource/cloudhelpchannel/guidcrossbook/jsonp?v=2022&p=MAYAUL&l=CHS&accessmode=live&guid=GUID-09D0E733-74DF-44E2-937A-C857001E45B2)

- [捕捉到栅格、曲线、点、视图平面或几何体中心](https://beehive.autodesk.com/community/service/rest/cloudhelp/resource/cloudhelpchannel/guidcrossbook/jsonp?v=2022&p=MAYAUL&l=CHS&accessmode=live&guid=GUID-E6E866EE-EEE8-4974-A3E7-9AD6ADBB9BCD)

- [将工作单位从厘米更改为英寸](https://beehive.autodesk.com/community/service/rest/cloudhelp/resource/cloudhelpchannel/guidcrossbook/jsonp?v=2022&p=MAYAUL&l=CHS&accessmode=live&guid=GUID-C5A6B812-9ECF-4A87-A7D3-D434348DCCD5)

- [切换文件的上方向轴](https://beehive.autodesk.com/community/service/rest/cloudhelp/resource/cloudhelpchannel/guidcrossbook/jsonp?v=2022&p=MAYAUL&l=CHS&accessmode=live&guid=GUID-DAB331B4-7623-4810-9740-DB526F85333F)
