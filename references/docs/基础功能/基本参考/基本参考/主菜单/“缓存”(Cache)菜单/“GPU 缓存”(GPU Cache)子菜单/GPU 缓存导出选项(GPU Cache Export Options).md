# GPU 缓存导出选项(GPU Cache Export Options)

#### 缓存时间范围(Cache time range)

#### 当前帧(Current frame)

仅缓存当前的“时间滑块”(Time Slider)帧。

#### 渲染设置(Render settings)

指定当前“渲染设置”(Render settings)确定“缓存时间范围”(Cache time range)。

#### 时间滑块(Time Slider)

指定“时间滑块”(Time Slider)中的当前播放范围确定“缓存时间范围”(Cache time range)。

#### 开始/结束(Start/End)

指定在指定的“开始”(Start)和“结束”(End)时间之间（包括“开始”(Start)和“结束”(End)时间）的帧范围确定“缓存时间范围”(Cache time range)。

#### 步长(Step)

指定文件创建过程中的采样频率。默认情况下，对象变形的采样将每帧进行一次，并保存到 Alembic 文件。

例如，如果值为 2，表示对于“缓存时间范围”(Cache Time Rang)每隔一帧缓存当前对象的变换。

#### 每 # 次解算保存一次(Save every # evaluation(s))

指定在创建缓存期间保存哪些采样。例如，值 2 指定仅将“每 # 个帧解算一次”(Evaluate every # frame(s))选项指定的每隔一个采样保存到您的 Alembic 文件中。

#### 保存多个文件(Save Multiple Files)

启用后，Maya 会为每个选定对象创建一个缓存文件。当您在场景中选择多个对象时，系统会显示该选项。

请参见“基本文件名”(Base File Name)和“冲突选项”(Clash Options)，了解文件命名约定。

#### 基本文件名(Base File Name)

输入缓存文件的基础名称。Maya 使用此名称保存每个缓存文件，并根据您选择的“冲突选项”(Clash Options)添加后缀。

#### 冲突选项(Clash Options)

选择“递增文件名”(Increment Filenames)可添加递增的编号。选择“节点名称后缀”(Node Name Suffix)可向文件基础名称添加节点名称。

例如，文件名显示为“基础文件名_数字增量”或“基础文件名_节点名称”。

#### 优化层次(Optimize Hierarchy)

启用时，选定层次中的节点和对象会进行合并以使在播放期间缓存文件的性能最大化。

#### 优化阈值(Optimization Threshold)

（仅在“优化层次”(Optimize Hierarchy)处于启用状态时才可用。）指定在单个绘制基本体中包含的最大顶点数。默认值 40000 可能适用于大多数支持 Maya 的图形卡。当设置为默认值时，优化后，在 GPU 缓存文件中的每个对象所拥有的顶点数将不会超过 40000 个。可以将该值设置为更大的值，具体取决于系统图形卡上的可用内存。

#### 优化运动模糊的动画(Optimize Animations for Motion Blur)

如果启用，在 Viewport 2.0 渲染模式下播放缓存时，具有已设置动画的变换节点的对象显示有运动模糊。请参见 [Viewport 2.0 选项](../../../面板菜单/面板菜单：渲染器/Viewport%202.0%20选项.md)。

Maya 首先确定 GPU 缓存是否包含动画数据。如果 GPU 缓存是静态的，且不包含动画数据，Maya 将不会为运动模糊优化 GPU 缓存。

**注**

运动模糊不支持

缓存播放(Cached Playback)

。

#### 写入材质(Write Materials)

如果启用，Maya 会将 Lambert 和 Phong 材质从源几何体导出到 GPU 缓存文件中。在 Viewport 2.0 中播放 GPU 缓存的文件时，将显示这些材质。

GPU 缓存的对象支持由 Viewport 2.0 渲染模式提供的所有高质量照明和着色效果。请参见 [Viewport 2.0 选项](../../../面板菜单/面板菜单：渲染器/Viewport%202.0%20选项.md)。

**注**

在场景视图的

“高质量渲染”(High Quality Rendering)

或

“默认质量渲染”(Default Quality Rendering)

模式下播放 GPU 缓存的文件时，将不会显示

Lambert

和

Phong

材质。

#### 细分(Tessellation)

#### 使用平滑细分(Use Smoothing Tessellation)

导出几何体，并且应用当前“平滑网格预览”(Smooth Mesh Preview)设置。

请参见[平滑多边形](https://beehive.autodesk.com/community/service/rest/cloudhelp/resource/cloudhelpchannel/guidcrossbook/jsonp?v=2022&p=MAYAUL&l=CHS&accessmode=live&guid=GUID-8A5D0FF0-9BA1-435F-A4CA-53183311B819)。

#### 使用基本细分(Use Base Tessellation)

使用基本细分导出几何体，并且不应用任何平滑。

#### File Format

#### HDF5 - Maya 2014 Extension 1 和旧版(HDF5 - Maya 2014 Extension 1 and Legacy)

创建与 HDF5 数据模型保持一致的 Alembic 缓存文件。此选项提供与先前版本 Alembic 的向后兼容性。

#### Ogawa - Maya 2014 Extension 1

创建 Ogawa Alembic 文件。相对旧版 Alembic 文件而言，采用 Ogawa 格式创建的文件大小更小、性能更优。

**注**

只有 Extension for Maya 2014 和更高版本的 Maya 才能读取 Ogawa Alembic 文件。

## 相关主题

- [创建或导入 GPU 缓存](https://beehive.autodesk.com/community/service/rest/cloudhelp/resource/cloudhelpchannel/guidcrossbook/jsonp?v=2022&p=MAYAUL&l=CHS&accessmode=live&guid=GUID-907BB76E-1A01-4A29-B2FA-659B7CDA7BC4)

- [关于 GPU 缓存](https://beehive.autodesk.com/community/service/rest/cloudhelp/resource/cloudhelpchannel/guidcrossbook/jsonp?v=2022&p=MAYAUL&l=CHS&accessmode=live&guid=GUID-C893BE60-6E65-4F36-8005-FD4D1A0E9822)
