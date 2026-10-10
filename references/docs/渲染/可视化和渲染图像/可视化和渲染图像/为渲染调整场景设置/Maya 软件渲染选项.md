# Maya 软件渲染选项

## 设置细分选项

虽然细分是按逐个对象进行确定的，但是您可以管理 Maya 处理场景细分设置的方式。

默认情况下，Maya 通过以下方式优化曲面的细分设置：

- 存储（缓存）几何体信息，减少所使用的内存量。

- 相同曲面仅细分一次，节省时间和磁盘空间。

- 重用细分，生成深度贴图。

- 计算为所有置换贴图曲面定义的边界框比例，加快渲染。

有关细分的详细信息，请参见[细分和近似简介](../../../细分和近似/细分和近似/细分和近似简介.md)。

这些优化设置可以在[“渲染设置”窗口](../../../渲染参考/渲染参考/渲染窗口和编辑器/“渲染设置”%28Render%20Settings%29窗口.md)的“内存与性能选项”(Memory and Performance Options)区域中启用或禁用。

## 设置光线跟踪

虽然光线跟踪质量由[“渲染设置”窗口](../../../渲染参考/渲染参考/渲染窗口和编辑器/“渲染设置”%28Render%20Settings%29窗口.md) “光线跟踪质量”(Raytracing Quality)部分中的选项设置（请参见[设置光线跟踪质量](设置光线跟踪质量.md)），但是您可以在[“渲染设置”窗口](../../../渲染参考/渲染参考/渲染窗口和编辑器/“渲染设置”%28Render%20Settings%29窗口.md)的“内存与性能选项”(Memory and Performance Options)区域中设置场景优化选项。

有关光线跟踪的详细信息，请参见[光线跟踪阴影](https://beehive.autodesk.com/community/service/rest/cloudhelp/resource/cloudhelpchannel/guidcrossbook/jsonp?v=2022&p=MAYAUL&l=CHS&accessmode=live&guid=GUID-BC9C9AFE-D90E-4B54-8A2E-22ED1C89A06C#WS17956D7ADBC6E73650E6F747117AE324699-7FEF)。

## 设置多个处理器

可以控制用于交互式渲染的处理器数量。若要使用多个处理器进行渲染，请参见[使用 Maya 软件进行网络渲染](../../../网络渲染/网络渲染/使用%20Render%20命令行实用程序进行网络渲染.md)。
