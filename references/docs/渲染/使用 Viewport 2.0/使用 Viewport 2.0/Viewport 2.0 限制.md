# Viewport 2.0 限制

## 一般功能

Viewport 2.0 支持 Maya 中的所有公用工作流，除了以下限制：

#### 摄影机

- 不能将纹理映射到“零视差颜色”(Zero Parallax Color)属性。

- 目前，对于立体显示模式，不支持多重采样抗锯齿。

#### 选择亮显(Selection Highlighting)

不能对以下项禁用选择亮显：

- 通过“创建 > 体积基本体 > 圆锥体”(Create > Volume Primitive > Cone)创建的圆锥体形状

- 变形器：

  - 晶格变形器的轴

  - 位置和方向标记编号

  - 所有非线性变形器

- 创建 > 测量工具(Create > Measure Tools)

#### 多边形排序

#### 背面消隐(Backface Culling)

“背面消隐”(Backface Culling)不支持以下内容：

- 显示 > 多边形 > 消隐选项 > 保持硬边(Display > Polygons > Culling Options > Keep Hard Edges)

- 形状节点的“网格组件显示”(Mesh Component Display)属性组中的“显示切线”(Display Tangent)属性。

#### 重影

- 自定义关键帧步数(Custom Key Steps)

- 不支持变形几何体的重影

- 淡出重影颜色不受支持。该功能已被否决。

#### Bullet

在“OpenGL - 核心配置(精确)”(OpenGL - Core Profile (Strict))或 DirectX 11 模式下运行 Viewport 2.0 时，不支持 Bullet 对象。使用 Bullet 时，请使用“OpenGL - 核心配置(兼容性)”(OpenGL - Core Profile (Compatibility))或“OpenGL - 旧版”(OpenGL - Legacy)模式。

#### 卡通

卡通着色器不支持渐变纹理

## 着色(Shading)

支持将以下着色器用作烘焙着色器：

- 布朗(Brownian)

- 云(Cloud)

- 凹陷

- 花岗岩

- 皮革

- 水

- 木材

- 3D 程序凹凸贴图

不支持以下着色器：

- 灯光雾(Light Fog)

- 粒子云(Particle Cloud)

- 曲面信息(Surface Info)

- 曲面亮度(Surf. Luminance)

- “渐变着色器”(Ramp Shader)限制：

  - “颜色”(Color)渐变不支持“归一化亮度”(Normalized Brightness) “颜色输入”(Color Input)模式

  - “正向散射”(Forward Scatter)不受支持

- 不支持通过曝光控制转换 .HDR 线性图像以显示颜色空间

- particleSamplerInfo 节点仅支持“精灵”(Sprites)

## 照明

- Viewport 2.0 中的环境光不遵循环境光明暗处理属性

- Viewport 2.0 不支持灯光链接。

- 灯光实例不受支持。

## Viewport 2.0 平台

- 在 Mac OS X 平台上，ATI 9500 X1900 GFX 卡当前不支持 Viewport 2.0。

- 在某些（特别是较旧的）使用 PCI Express 1.0 的 Linux 平台上，存在一个已知的驱动程序问题，该问题可能会强制 Viewport 2.0 回到某个软件路径。这可能会导致性能显著降低。该问题可通过较新的驱动程序修复。

- 在 Linux 平台上不支持远程显示或间接渲染。

### Mac OS X

#### 速度减慢或不稳定

由于 Mac OS X 上的内存管理问题，接近显卡 RAM 限制时，您可能会遇到明显的速度减慢或不稳定。为了能够解决该问题，请设置在为渲染器加载文件纹理时用于视口显示的纹理大小。使用以下步骤：

设置用于视口显示的纹理大小

- 在启动 Maya 之前，将环境变量 MAYA_OGS_ENABLE_MAX_TEXTURE_SIZE_PREF 设置为 1。

也可以将环境变量 MAYA_OGS_CPU_MEMORY_LIMIT 设置为（以 MB 为单位的一个值）预计要用于渲染器的内存量。该值应小于计算机上可用的实际量。

#### 显卡内存较少的 Mac OS X

在 Mac OS X (10.6.x) 上使用 Viewport 2.0 时，使用的图形内存太多时可能会出现不稳定。对于具有较少内存的图形卡，会更经常出现这种情况，因为内存阈值较小。对于 Mac OS X 平台，建议使用 VRAM 为 1GB 或更大的图形卡。

**注**

在 2009 年之前推出的 Apple 计算机系统或硬件上，不能使用 Viewport 2.0。请根据

Maya 认证硬件

建议升级系统。

## 相关主题

- [优化 Viewport 2.0](优化%20Viewport%202.0.md)

- [管理 Viewport 2.0 的 GPU 内存](管理%20Viewport%202.0%20的%20GPU%20内存.md)

- [Viewport 2.0 疑难解答](Viewport%202.0%20疑难解答.md)
