# Viewport 2.0 支持的着色器语义

可识别以下语义，并支持将其用于 Viewport 2.0 中的着色器。可使用这些语义创作完整效果，然后使用 MShaderManager 类作为 MShaderInstance 对象来访问。还可将其应用于使用 MFragmentManager 注册的碎片的参数。

**注**

dx11Shader.mll

和

glslShader.mll

插件都是

MPxShaderOverride

。因此，它们必须解析效果才能确定并手动绑定语义。相比之下，碎片系统和

MShaderInstance

都可自动执行所有这些操作；但是，它们也都更具限制性。

世界坐标系可以进一步分为不同的区域设置，每个区域设置具有不同的原点。然后可以在其中任一区域设置中指定节点。这样，建立的节点位置比在世界坐标系中定义的精度更高。

当前节点的区域设置与以前节点的区域设置不同时，将重新应用属于 FrameLocale 组的所有矩阵。在渲染时，摄影机和灯光将变换到当前节点的区域设置空间中，以便对象、摄影机和灯光都在同一局部坐标空间中表示，并可以用单精度浮点值存储和表示。

| **语义** | **用法** | **类型** | **组** |
|---|---|---|---|
| World | 世界变换 | 矩阵 | 项目 FL |
| WorldTranspose | 世界变换，已转置 | 矩阵 | 项目 FL |
| WorldInverse | 世界变换，已反转 | 矩阵 | 项目 FL |
| WorldInverseTranspose | 世界变换，已反转并已转置 | 矩阵 | 项目 FL |
| PreviousWorld | 上一世界变换 | 矩阵 | 项目 |
| NextWorld | 下一世界变换 | 矩阵 | 项目 |
|  |  |  |  |
| View | 视图变换 | 矩阵 | FrameLocale |
| ViewTranspose | 视图变换，已转置 | 矩阵 | FrameLocale |
| ViewInverse | 视图变换，已反转 | 矩阵 | FrameLocale |
| ViewInverseTranspose | 视图变换，已反转并已转置 | 矩阵 | FrameLocale |
|  |  |  |  |
| Projection | 投影变换 | 矩阵 | 帧 |
| ProjectionTranspose | 投影变换，已转置 | 矩阵 | 帧 |
| ProjectionInverse | 投影变换，已反转 | 矩阵 | 帧 |
| ProjectionInverseTranspose | 投影变换，已反转并已转置 | 矩阵 | 帧 |
| ProjectionZSense | 指示投影矩阵在变换时是否翻转点的 Z 分量。如果翻转，则为 -1.0 ，否则为 1.0。 | 浮点 | 帧 |
|  |  |  |  |
| WorldView | 世界视图变换 | 矩阵 | 项目 FL |
| WorldViewTranspose | 世界视图变换，已转置 | 矩阵 | 项目 FL |
| WorldViewInverse | 世界视图变换，已反转 | 矩阵 | 项目 FL |
| WorldViewInverseTranspose | 世界视图变换，已反转并已转置 | 矩阵 | 项目 FL |
| WorldLocaleOrigin | 将偏移应用于区域设置变换矩阵，以获取真实的（全局的）世界变换矩阵。 如果需要双精度以表示大坐标系中的精确位置，则应用此偏移可导致精度不足。 | Float3 | FrameLocale |
|  |  |  |  |
| ViewProjection | 视图投影变换 | 矩阵 | FrameLocale |
| ViewProjectionTranspose | 视图投影变换，已转置 | 矩阵 | FrameLocale |
| ViewProjectionInverse | 视图投影变换，已反转 | 矩阵 | FrameLocale |
| ViewProjectionInverseTranspose | 视图投影变换，已反转并已转置 | 矩阵 | FrameLocale |
| PreviousViewProjection | 上一视图投影变换 | 矩阵 | FrameLocale |
|  |  |  |  |
| WorldViewProjection | 世界视图投影变换 | 矩阵 | 项目 FL |
| WorldViewProjectionTranspose | 世界视图投影变换，已转置 | 矩阵 | 项目 FL |
| WorldViewProjectionInverse | 世界视图投影变换，已反转 | 矩阵 | 项目 FL |
| WorldViewProjectionInverseTranspose | 世界视图投影变换，已反转并已转置 | 矩阵 | 项目 FL |
| 以下是其他语义的 MultiDraw 版本，当 MPxShaderOverride::supportsMultiDraw() 被覆盖以返回 true·时用作渲染 MultiDraw 的替代项。 |  |  |  |
| WorldMD | 世界变换的 MultiDraw 数组 | Matrix[64] | 项目 FL |
| WorldTMD | 世界变换的 MultiDraw 数组，已转置 | Matrix[64] | 项目 FL |
| WorldIMD | 世界变换的 MultiDraw 数组，已反转 | Matrix[64] | 项目 FL |
| WorldITMD | 世界变换的 MultiDraw 数组，已反转并已转置 | Matrix[64] | 项目 FL |
|  |  |  |  |
| WorldViewMD | 世界视图变换的 MultiDraw 数组 | Matrix[64] | 项目 FL |
| WorldViewTMD | 世界视图变换的 MultiDraw 数组，已转置 | Matrix[64] | 项目 FL |
| WorldViewIMD | 世界视图变换的 MultiDraw 数组，已反转 | Matrix[64] | 项目 FL |
| WorldViewITMD | 世界视图变换的 MultiDraw 数组，已反转并已转置 | Matrix[64] | 项目 FL |
|  |  |  |  |
| WorldViewProjMD | 世界视图投影变换的 MultiDraw 数组 | Matrix[64] | 项目 FL |
| WorldViewProjTMD | 世界视图投影变换的 MultiDraw 数组，已转置 | Matrix[64] | 项目 FL |
| WorldViewProjIMD | 世界视图投影变换的 MultiDraw 数组，已反转 | Matrix[64] | 项目 FL |
| WorldViewProjITMD | 世界视图投影变换的 MultiDraw 数组，已反转并已转置 | Matrix[64] | 项目 FL |
|  |  |  |  |
| ViewDirection | 视图（摄影机）的世界空间方向 | Float3 | FrameLocale |
| ViewPosition | 视图（摄影机）的世界空间位置 | Float3 | FrameLocale |
| LocalViewer | 表示要使用局部视图方向还是要使用非局部视图方向 | 布尔 | 帧 |
|  |  |  |  |
| IsOrthoGraphic | 表示投影矩阵是否为正交 | 布尔 | 帧 |
|  |  |  |  |
| ViewportPixelSize | 当前视口的尺寸（以像素为单位），即宽度和高度 | Float2 | 帧 |
|  |  |  |  |
| ClippingPlanes | 活动剪裁平面的系数，每平面一个 float4 | Float4 数组 | 剪裁 |
| ClippingPlaneCount | 活动剪裁平面的数量 | 整数 | 剪裁 |
| NearClipPlane | 摄影机的近剪裁平面 | 浮点 | 帧 |
|  |  |  |  |
| 时间 AnimationTime Sas.Time.Now | 时间（秒） 注： 仅适用于使用 MPxShaderOverride 创建的着色替代。MPxShaderOverride 必须支持将 MUniformParameter 自动绑定到着色器一致参数。 即，MPxShaderOverride 必须为每个一致参数创建 MUniformParameter，根据关联语义检索每个 MUniformParameter 值，并将此值绑定到着色器一致参数。 此操作由 dx11Shader 和 glslShader 插件自动完成。 此外，仅当已从 glslShader 插件加载效果文件时，“时间”(Time)和“帧”(Frame)才可用。 | 浮点 | 帧 |
| 帧 FrameNumber | 在帧单位中框显 注： 仅适用于使用 MPxShaderOverride 创建的着色替代。MPxShaderOverride 必须支持将 MUniformParameter 自动绑定到着色器一致参数。 即，MPxShaderOverride 必须为每个一致参数创建 MUniformParameter，根据关联语义检索每个 MUniformParameter 值，并将此值绑定到着色器一致参数。 此操作由 dx11Shader 和 glslShader 插件自动完成。 | 整数 | 帧 |
|  |  |  |  |
| AlphaTestFunction | Alpha 测试比较函数 1 = 从不 2 = 小于 3 = 等于 4 = 小于或等于 5 = 大于 6 = 不等于 7 = 大于或等于 8 = 始终 | 整数 | Alpha 测试 |
| AlphaTestReference | Alpha 测试引用值，范围为 (0.0, 1.0) | 浮点 | Alpha 测试 |
|  |  |  |  |
| RelativeViewportDimensions | 指定相对视口尺寸 | Float2 | 帧 |
|  |  |  |  |
| MayaReceivesShadowOn | 表示对象是否接收阴影 | 布尔 | 项目 |
|  |  |  |  |
| EnableXRayComp | 表示是否已启用 X 射线组件模式 | 布尔 | 帧 |
|  |  |  |  |
| MayaViewportModes | 视口模式 0 = 不包含边界框 1 = 包含边界框 | 整数 | 帧 |
|  |  |  |  |
| FogEnabled | 表示是否已启用硬件雾 | 布尔 | 帧 |
| FogMode | 硬件雾衰减模式 0 = 线性 1 = 指数 2 = 指数平方 | 整数 | 帧 |
| FogStart | 视图空间中的硬件雾开始 z 距离 | 浮点 | 帧 |
| FogEnd | 视图空间中的硬件雾结束 z 距离 | 浮点 | 帧 |
| FogDensity | 硬件雾密度 | 浮点 | 帧 |
| FogColor | 硬件雾颜色 | Float4 | 帧 |

**注**

FL

指示语义还与帧区域设置相关。
