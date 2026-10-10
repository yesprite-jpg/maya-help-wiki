# GPU 缓存首选项(GPU Cache Preferences)

可以在[首选项(Preferences)窗口](../“首选项”%28Preferences%29窗口.md)的“GPU 缓存”(GPU Cache)类别中设置以下首选项。

若要返回到出厂默认设置，请在此窗口中选择“编辑 > 还原默认设置”(Edit > Restore Default Settings)。请注意，这将重置“首选项”(Preferences)窗口中每个类别的首选项。

通过“GPU 缓存”(GPU Cache)首选项可以设置控制 gpuCache 插件的行为和性能的系统显卡参数。

有关 GPU 缓存的信息，请参见[关于 GPU 缓存](https://beehive.autodesk.com/community/service/rest/cloudhelp/resource/cloudhelpchannel/guidcrossbook/jsonp?v=2022&p=MAYAUL&l=CHS&accessmode=live&guid=GUID-C893BE60-6E65-4F36-8005-FD4D1A0E9822)。

## 硬件信息(Hardware Information)

显示有关系统安装的显卡的只读信息。

#### 制造商(Manufacture)

显卡制造商。

#### 型号(Model)

显卡型号。

#### 驱动号(Driver Number)

显示系统安装的显卡驱动程序的版本。

#### GPU 内存(MB)(GPU Memory in MB)

系统所占用的显卡内存量。

## 全部设置为自动(Set All to Automatic)

启用“全部设置为自动”(Set All to Automatic)选项，会将所有 GPU 缓存首选项的“自动”(Automatic)选项设置为开启。关闭“全部设置为自动”(Set All to Automatic)不会禁用“自动”(Automatic)选项。

“自动”(Automatic)选项的默认值取决于系统的硬件和操作系统配置。当首选项的“自动”(Automatic)选项处于禁用状态时，可以输入值或者选择可用选项。

## VRAM 管理(VRAM Management)

#### 所有缓存缓冲区的最大 VRAM(Maximum VRAM for All Cache Buffers)

指定分配给 gpuCache 插件和 GPU 缓存操作的顶点缓冲区对象的最大总大小。

#### GPU 缓存缓冲区的最大值(Maximum Number of GPU Cache Buffers)

指定分配给 GPU 缓存的顶点缓冲区对象的最大数量。

#### 每个形状进行 GPU 缓存的最小顶点数(Minimum Vertices Per Shape for GPU Caching)

指定形状必须包含（否则无法使用顶点缓冲区对象）的顶点的最小数量。顶点数量少于指定值的形状使用系统内存。

#### 低 VRAM 操作(Low VRAM Operation)

指定因显卡内存不足而无法保留每帧的顶点缓冲区对象时，用于绘制几何体的内存源。

**注**

重要：

如果系统上 GPU 缓存的执行速度很慢，则说明 Maya 可能未检测显卡上可用的 VRAM 量。如果是这种情况，您可以手动设置“所有缓存缓冲区的最大 VRAM”(Maximum VRAM for All Cache Buffers)。请参考下表来设置 VBO 缓存的大小。

| VRAM (Mb) | 适用于 GPU 缓存 (Mb) | 适用于其他进程 (Mb) |
|---|---|---|
| 0 | 0 | 0 |
| 128 | 0 | 128 |
| 512 | 256 | 256 |
| 1024 | 640 | 384 |
| 2048 | 1356 | 512 |
| 3072 | 2560 | 512 |

## 基于 OpenGL 的选择选项(OpenGL-Based Selection Options)

#### OpenGL 选择模式(OpenGL Selection Mode)

指定执行 OpenGL 拾取以进行选择时，用于绘制几何体的是顶点数组还是显卡内存。

#### 直到基于光栅的选择的线框阈值(Wireframe Threshold Until Raster-Based Selection)

指定阈值，该值决定用于线框选择的是 OpenGL 拾取还是基于光栅的拾取。如果缓存中的“每个缓存节点的顶点数”(vertices per cache node)的数量超过设置值，则使用基于光栅的拾取。

#### 直到基于光栅的选择的曲面阈值(Surface Threshold Until Raster-Based Selection)

指定阈值，该值决定用于曲面选择的是 OpenGL 拾取还是基于光栅的拾取。如果缓存中的“每个缓存节点的顶点数”(vertices per cache node)的数量超过设置值，则使用基于光栅的拾取。

## 高级显示设置(Advanced Display Settings)

#### 禁用顶点数组(Disable Vertex Arrays)

指定使用顶点数组还是 OpenGL 基本体。

#### 双面照明(Two Sided Lighting)

指定显卡使用的是 OpenGL 双面照明还是 Maya 双面照明模拟。

#### UV 坐标(UV Coordinates)

指定是否将 UV 坐标写入 GPU 缓存文件，或是否从 GPU 缓存文件中读取 UV 坐标。

#### 后台读取(Background Reading)

启用将 GPU 缓存文件后台加载到显卡内存中。缓存加载时，GPU 缓存中的对象会显示在场景视图中。

您可以在加载 gpuCache 节点时删除、复制和重命名它。“后台读取”(Background Reading)适用于所有 GPU 缓存文件，其中包括场景集合缓存表示。

#### 后台读取刷新间隔(Background Reading Refresh Interval)

指定 GPU 缓存文件在后台加载时场景视图绘制的刷新频率。
