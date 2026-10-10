# cacheFile

（该节点参考几何缓存/nCloth 缓存格式。有关头发、流体和和抖动缓存的详细信息，请参见[创建流体缓存文件](https://beehive.autodesk.com/community/service/rest/cloudhelp/resource/cloudhelpchannel/guidcrossbook/jsonp?v=2022&p=MAYAUL&l=CHS&accessmode=live&guid=GUID-7624468B-2E14-4C20-B90B-16E38E520EA2)和[对抖动动画使用磁盘缓存](https://beehive.autodesk.com/community/service/rest/cloudhelp/resource/cloudhelpchannel/guidcrossbook/jsonp?v=2022&p=MAYAUL&l=CHS&accessmode=live&guid=GUID-3AD3BE2D-B71E-4FEC-8032-B5FBD9721DE0)。)

该节点存储了单个“几何缓存”(geometry cache)的所有设置。该节点属性的更改不会影响它在磁盘中的关联缓存文件。

在依存关系图和“属性编辑器”(Attribute Editor)中，几何缓存表示为 objectShapeNodeName#Cache# 节。例如，“BallShape1Cache1”、“BallShape1Cache2”和“BallShape1Cache3”是三个几何缓存节点的名称，其中包含名为“球”(Ball)的对象的缓存设置。在“Trax 编辑器”(Trax Editor)中，几何缓存表示为缓存片段。更改几何缓存节点的设置时，也会更改其对应几何缓存片段的设置。

## 缓存文件(Cache File)

#### 基础目录(Base Directory)

指定当前几何缓存节点的原始缓存文件在磁盘中的目录。默认情况下，基础目录是：\maya\projects\default\data。

#### 缓存名称(Cache Name)

指定当前几何缓存节点的原始缓存文件在磁盘中的名称。

#### 启用(Enable)

启用时，当前几何缓存节点的变形将由其对象在播放时使用。禁用时，当前几何缓存节点的变形不会由其对象在播放时使用。。

请参见[启用或禁用几何缓存](../../../几何缓存/几何缓存/创建和编辑几何缓存/缓存几何体/启用或禁用几何缓存.md)、[启用或禁用几何缓存片段](../../../几何缓存/几何缓存/创建和编辑几何缓存/使用几何缓存片段/启用或禁用几何缓存片段.md)和[已启用/已禁用的片段](../../../Maya%20中的非线性动画/Maya%20中的非线性动画/Trax%20编辑器/Trax%20中的非线性动画组件/Trax%20中的片段/片段状态.md)。

#### 开始帧(Start Frame)

指定当前几何缓存节点的播放开始时间。可以更改该属性，以修改几何缓存节点开始播放的时间。

#### 缩放(Scale)

展开或缩小当前几何缓存节点的时间范围。如果增大比例，则几何缓存节点的变形播放速度将会减慢。减小比例会有相反的效果。请参见[缩放几何缓存片段](../../../几何缓存/几何缓存/创建和编辑几何缓存/使用几何缓存片段/缩放几何缓存片段.md)。

#### 保持(Hold)

指定帧数以保持当前几何缓存节点的上一帧。请参见[保持几何缓存片段](../../../几何缓存/几何缓存/创建和编辑几何缓存/使用几何缓存片段/保持几何缓存片段.md)。

#### 前方循环/后方循环(Pre Cycle/Post Cycle)

指定位于当前几何缓存节点之前（“前方循环”(Pre Cycle)）和之后（“后方循环”(Post Cycle)）的循环数。

可以使用循环来重复几何缓存中包含的变形。请参见[循环几何缓存片段](../../../几何缓存/几何缓存/创建和编辑几何缓存/使用几何缓存片段/循环几何缓存片段.md)和[循环](../../../曲线图编辑器%28Graph%20Editor%29/曲线图编辑器%28Graph%20Editor%29/“曲线图编辑器”%28Graph%20Editor%29菜单/“曲线图编辑器”%28Graph%20Editor%29%20“曲线”%28Curves%29菜单.md)。

#### 源开始/源结束(Source Start/Source End)

对于当前几何缓存节点包含的原始缓存，指定其帧范围在磁盘中的开始帧编号和结束帧编号。如果当前几何缓存节点已修剪，则“源开始”(Source Start)和“源结束”(Source End)值将与“原始开始”(Original Start)或“原始结束”(Original End)值不匹配。

可以对这些值进行编辑，以便仅使用当前几何缓存节点的一部分。请参见[修剪几何缓存片段](../../../几何缓存/几何缓存/创建和编辑几何缓存/使用几何缓存片段/修剪几何缓存片段.md)。

#### 原始开始/原始结束(Original Start/Original End)

指定当前几何缓存节点的原始缓存文件在磁盘中的开始帧编号和结束帧编号。这些值为只读。

#### 反向(Reverse)

启用时，当前节点的 nCache 将从缓存的上一帧开始反转播放。默认情况下，“反向”已禁用。

#### 往返(Oscillate)

启用时，当前节点的 nCache 将在反转播放和向前播放之间往返其他每个循环，从而创建连续播放循环。默认情况下，“往返”已禁用。

#### 多线程(Multi Thread)

启用时，将在播放期间为多线程设置 cacheFile 节点。默认情况下，“多线程”(Multi Thread)已禁用。

#### 队列大小(帧) (Queue Size(frames))

指示在启用多线程、但并未经过设置以预加载整个缓存的情况下，Maya 尝试预加载并保持在内存中的 cacheFile 节点缓存的帧数。默认情况下，“队列大小”(Queue Size)（帧）”为 20。

#### 显示加载进度(Display Load Progress)

启用时，将显示已满的多线程缓存内存队列所占的百分比。默认情况下，“显示加载进度”(Display Load Progress)已启用。

### 缓存描述(Cache Description)

显示一些包含在当前 cacheFile 节点的 XML 描述文件中的信息。有关“缓存描述”(Cache Description)中所含值的详细信息，请参见[几何缓存 XML 描述文件](../../../几何缓存/几何缓存/几何缓存%20XML%20描述文件.md)。
