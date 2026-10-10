# Waiter

此节点是 MASH 网络的主干，可用于创建影响网络的其他节点。

## Waiter 节点

### 计数

#### 计数(Count)

显示 MASH 网络中的点数。

#### 批渲染倍增(Batch Render Multiplier)

发送到批渲染时，此值会乘以点数。有助于减少渲染时的大量计算（即：将场景中的点数减半并将该值设置为 2）。

### 添加节点

单击任意图标可将相应节点添加到 MASH 网络。

### 高级

#### RenderMan 归档(RIB) (RenderMan Archives (RIBs))

用于指定任何 RIB 文件的位置，以便在 RenderMan 中更好地渲染实例。有关详细信息，请参见[使用 RenderMan 渲染 MASH](../../使用%20RenderMan%20渲染%20MASH.md)。

### 预设

您可以从此处创建并访问自己保存的 MASH 网络。

#### 预设位置(Preset Location)

用于保存预设的文件夹。

#### 创建预设(Create Preset)

用于创建并命名预设。

#### 显示 Visor (Show Visor)

在 Visor 中打开 MASH“预设”(Presets)选项卡。

### 缓存

用于创建缓存并将其应用于 MASH 网络。缓存是每个通道的单个文件 (.mcx)，其名称基于 Waiter 的名称。创建缓存后，可以在该通道中禁用 MASH 节点，因为 Waiter 将改为依赖于缓存。

#### 打开缓存创建器(Open the Cache Creator)

打开[缓存创建器(Cache Creator)](../MASH%20窗口和编辑器/缓存创建器.md)窗口。

#### 启用/禁用缓存(Enable/Disable Cache)

用于对各个通道启用和禁用缓存。
