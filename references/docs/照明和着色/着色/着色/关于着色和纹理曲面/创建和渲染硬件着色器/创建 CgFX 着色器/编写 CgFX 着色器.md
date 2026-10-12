# 编写 CgFX 着色器

## 编写“CgFX 着色器”(CgFX shader)

Maya 支持 Cg 版本 3.0.015。

CgFX 示例随 Maya 一起提供。您可以在以下位置找到这些示例：

- (Windows) <驱动器>:\Program Files\Autodesk\<版本>\presets\CgFX\examples

- (Mac OS X) /Applications/Autodesk/<版本>/Maya/Contents/presets

- (Linux) /usr/autodesk/<版本>/presets/CgFX/examples

![图：（图旁无可取正文，Maya 手册 img 无 alt）](https://help.autodesk.com/cloudhelp/2022/CHS/Maya-LightingShading/images/GUID-79F64816-09CA-4ECE-8007-89D9346372B8.png) <!-- baize:img-hook downloaded=false reason="正文 1987 字 ≥300，非承重" -->

## 变化参数填充

可以将多个网格输入填充到单个变化参数注册中。例如，可以将两组 UV 坐标填充到单个 float4 注册中。

下列为示例工作流：

1. 以下顶点着色器输入结构显示了需要在单个变化参数中包含两个 UV 集的填充 float4：

  ```text
struct appdata {     float3    Position: POSITION;     float4    UVs:      TEXCOORD0; };
```

2. 创建第二个结构，描述应填充至该输入中的元素。若要启用 Maya 来查找第二个结构，其名称必须与原始变化参数的名称（在本例中为 UV）匹配。

  在本示例中，该辅助结构通知 Maya 应实时地从两个 float2 输入汇编原始 float4 参数：一个名为 UV1，另一个名为 UV2。着色器本身未使用该结构 - 它仅告知 Maya 如何为该输入汇编数据。

  ```text
struct UVs {     float2 UV1;     float2 UV2; };
```

3. 由于 Maya 知道这是填充输入，它向美工人员提供了基本数据（UV1 和 UV2），而非最终填充结构 (UV) 的界面。现在可以优化及重新组织变化参数注册指定，而无需破坏场景中使用着色器的任何现有着色器绑定。

  有关详细信息，请以 UVPacking.cgfx 为例。

  **注**

  如果对于指定的 Cg 数据类型而言，指定给结构元素的数据太大(例如，(X, Y, Z)坐标的位置变成 float2 值)，则前 n 个值将用于填充值，而将忽略任何后续元素(例如，X 和 Y 将获准进入，而 Z 将被忽略)。

## 其他“CgFX 着色器”(CgFX shader)功能

#### 时间语义(Time semantic)

Maya 支持随时间变化的参数。有关随时间移动的着色器的示例，请参见 MrWiggle.cgfx。

#### 矩阵语义(Matrix semantic)

可以在“CgFX 着色器”(CgFX shader)中指定矩阵。Maya 支持所有矩阵语义关键字。

#### 透明 CgFX 着色器

Maya 支持渲染透明 CgFX 着色器。Maya 检测在第一个过程中是否启用了融合状态。如果启用了融合，Maya 在场景视图中使用“对象透明度排序”(Object Transparency Sorting)或“多边形透明度排序”(Polygon Transparency Sorting)选项来正确渲染透明着色器。

#### Maya 着色器文件

Maya 在以下目录中提供了开发人员可以合并到自己的 CgFX 着色器中的着色器文件：

- (Windows) <*install_dir*>\bin\cg

- (Linux) <*install_dir*>/bin/cg

- (Mac OS X) <*install_dir*>/Maya.app/Contents/bin/cg

其中，<*install_dir*> 是 Maya 安装目录。

选择 Maya_ *.cgh 代码示例；例如，Maya 用于融合分层纹理的代码 maya_blends.cgh：

#### 纹理坐标系的方向

当 CgFx 插件编译 Cgfx 着色器时，它将编译宏 MAYA_TEXCOORD_ORIENTATION 设置为 OpenGL 或 DirectX，以指定用于纹理坐标系的方向。详细信息请参见 [CgFX 着色器的纹理坐标系的方向](CgFX%20着色器的纹理坐标系的方向.md)。

## 自定义 CgFX 着色器

您可以使用 MAYA_CGFX 宏来自定义 CgFX 着色器，从而包括 Maya 特定属性注释，而不破坏与可能也使用相同 CgFX 着色器的其他应用程序的兼容性。

例如，可以使用以下代码来声明 Maya 和其他应用程序的平行光属性，且不会造成任何兼容性问题：

```text
#if defined(MAYA_CGFX) || defined(XSI)
// Declares the « dirlight0 » with attribute annotations for Maya or XSI
float4 dirlight0 : Direction <
     string UIName =  "Distant Light 0 Direction";
     string Object = "DirectionalLight";
     string Space = "World";
> = {-1.0f, -1.0f, 0.3f, 0.0f};
#else
// Declares the « dirlight0 » with attribute annotations for another application:
....
#endif
```

# if (MAYA_CGFX) |VERTBAR defined (XSI) 和 # else 之间的行只有在 Maya/XSI 加载时才会解析。
