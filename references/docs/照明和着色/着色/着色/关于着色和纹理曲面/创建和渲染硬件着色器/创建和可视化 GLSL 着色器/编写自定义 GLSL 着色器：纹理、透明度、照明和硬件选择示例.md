# 编写自定义 GLSL 着色器：纹理、透明度、照明和硬件选择示例

GLSL 着色语言规范不包含描述，允许您将各种着色器碎片及其关联的 UI 连接到单个效果文件中，就像可能对 CgFX 或 HLSL 那样。

因此，提供了包裹器文件格式，允许您为各个着色阶段指定 GLSL 碎片：处理灯光和纹理绑定，并确定如何在属性编辑器中显示参数。下面将描述此文件格式 .ogsfx。

若要编写自定义 GLSL 着色器，请将它另存为 .ogsfx 文件。有关如何编写 GLSL 着色器的示例，请参见 Maya 安装的 ..\presets\GLSL\examples 文件夹中的 WaterSimulation.ogsfx 效果文件。

此示例演示以下内容：

  纹理

  透明度

  如何在 Maya 属性编辑器中创建 UI

  如何将 Maya 灯光应用于着色器

- 如何对置换组件执行硬件选择

- 如何绘制置换组件

要可视化此示例，请创建一个立方体，并通过 polyCube 节点属性编辑器将其“细分宽度”(Subdivisions Width)和“细分深度”(Subdvisions Depth)增至 100。对于着色的和带纹理的显示模式，按 6。

将 GLSL 着色器指定给立方体，并导航到 WaterSimulation.ogsfx 效果文件。详细信息请参见[创建和可视化 GLSL 着色器](https://help.autodesk.com/cloudhelp/2022/CHS/Maya-LightingShading/files/GUID-41D74556-0699-4F4E-8382-F9E69FBFC158.htm)。

示例着色器将创建可能对场景中的一个 Maya 灯光起反应的动画波浪。它将连接到高度和法线贴图，且可以显示透明度。

有关此着色器示例中使用的语义和注释的详细信息，请参见 [Viewport 2.0 中的 glslShader 和 dx11Shader 插件支持的语义和注释在](https://help.autodesk.com/cloudhelp/2022/CHS/Maya-LightingShading/files/GUID-13229A83-B6A0-4280-840C-F9C6F40BB13D.htm)和以及 [Viewport 2.0 支持的着色器语义](https://beehive.autodesk.com/community/service/rest/cloudhelp/resource/cloudhelpchannel/guidcrossbook/jsonp?v=2022&p=MAYAUL&l=CHS&accessmode=live&guid=GUID-0939A615-81AC-455C-9B23-9ECEC5835F93)。

## 指定纹理文件

若要定义文件纹理，请按照以下示例执行操作：

```text
uniform texture2D gHeightMap  <
    //Specify the texture file to be loaded by default
    string ResourceName = "SeaHeightMap.jpg";

    //Specify the type of texture
    string ResourceType = "2D";
    //Name of field in Attribute Editor
    string UIName = "Sea Height Map";

    int mipmaplevels = 0;
>;
uniform sampler2D gHeightMapSamp = sampler_state
{
    texture = <gHeightMap>;
};
```

采样在 gHeightMapSamp 上执行，并且文件纹理加载到 gHeightMap 中。sampler_state 允许将外部纹理关联到采样器。

ResourceName 注释使您可以在加载着色器时，自动连接和加载指定的纹理文件。例如，在本例中，SeaHeightMap.jpg 文件已连接。否则，用户必须创建文件节点并将其连接到该属性。

在这种情况下，SeaHeightMap.jpg 文件与 WaterSimulation.ogsfx 文件位于同一目录中。如果纹理文件位于其他目录中，则必须指定其完整路径。

## 在 Maya 属性编辑器中创建属性

统一参数及其变量名称将自动显示在 Maya 属性编辑器中。若要为统一参数提供用户友好的名称，请使用 UIName 注释。

例如：

```text
uniform texture2D gHeightMap  <
...
...
  string UIName = "Sea Height Map";
...
>;
```

“海洋高度贴图”(Sea Height Map)显示为 GLSLShader 节点属性编辑器中的一个属性，而不是显示为 gHeightMap。

如果不希望某个统一参数显示在属性编辑器中，请使用以下注释：

```text
string UIWidget = "None";
```

## 添加技术

一种可以包含一个或多个过程的技术，其中每个过程定义渲染对象的特定方式。如果具有多个顶点着色器和/或多个几何体着色器和/或像素着色器，则可以指定要用于每种技术/通道的着色器。

在此示例中，technique Main 包含一个通道，指定应该使用 PS_Wave 像素着色器。在 GLSLShader 节点属性编辑器中选择 Main 作为技术时，将在视口中渲染波浪。

同样，technique NormalView 包含一个通道，指定应该使用 PS_Normal 像素着色器。在属性编辑器中选择 NormalView 时，将在视口中显示波浪的法线贴图。

该技术 NormalView_Selection 包括 7 个过程，并且将不同的顶点、几何体和像素着色器用于每个过程。此技术示范硬件选择。有关详细信息，请参见下面的[选择和绘制置换组件](编写自定义%20GLSL%20着色器：纹理、透明度、照明和硬件选择示例.md#GUID-F81B34C5-30B8-4784-8351-F252006C42D8__SECTION_CF1B47E32DF2456BAC7B85A7C38E9383)。

## 显示透明度

在指定技术时使用透明度技术注释，以便对象可以显示透明度。

在 GLSLShader 属性编辑器中选择 Main 技术时，以下项允许对象显示为透明。

```text
technique Main
<
//tell Maya to support transparency for this technique
string Transparency = "Transparent";
>
```

## 将场景中的灯光指定给着色器

示例效果文件的 Light 0 Group 部分演示如何将场景中的一个灯光指定给 GLSL 着色器，以及灯光参数应该如何影响着色器。

若要在着色器计算中包括多个灯光，请在效果着色器中创建其他的 Light 1、Light 2（依此类推）部分。您还将需要为灯光如何彼此交互制定计划。

有三种方法可以用于向着色器添加灯光。可以执行下列操作：

- 通过从“属性编辑器”(Attribute Editor)的“灯光绑定”(Light Binding)部分中的选择“自动绑定”(Automatic Bind)选项，将场景中的任何灯光自动绑定到着色器

- 通过从“灯光绑定”(Light Binding)区域进行选择，手动选择场景中的特定灯光并将其绑定到着色器

- 通过 GLSLShader 的“属性编辑器”(Attribute Editor)调整灯光设置。必须选择“使用着色器设置”(Use Shader Settings)选项，并且首先选择“启用灯光 0”(Enable Light 0)，然后才能使设置生效。

如果您选择前两个选项之一，则在绑定灯光后无法在 GLSLShader 的“属性编辑器”(Attribute Editor)中更改灯光参数。相反，您必须从*灯光的* 属性编辑器进行更改。

若要查看场景灯光的效果，请在 Maya 视口面板菜单中选择“照明 > 使用所有灯光”(Lighting > Use All Lights)。

**注**

在此示例中，照明仅在 PS_Wave 像素着色器中定义，其仅在

“主”(Main)

技术中使用。因此，如果选择

“主”(Main)

作为技术，则只能在

“Viewport 2.0”

中查看照明效果。

## 禁用合并

将技术注释 handlesConsolidatedGeometry 设置为 false，可在要应用 GLSL 着色器的几何体上禁用“合并世界”(Consolidate World)功能。

```text
string handlesConsolidatedGeometry = "false";
```

如果通过技术绘制其计算涉及对象的对象空间坐标（例如，使用世界变换矩阵）的置换，则此注释非常有用。由于“合并世界”(Consolidate World)会将多个对象的顶点移到一个新的共享对象空间中，因此可能会导致插件着色器渲染错误。在这种情况下，您可能需要禁用“合并世界”(Consolidate World)。

## 选择和绘制置换组件

NormalView_Selection 技术演示了如何在置换位置对置换组件执行硬件选择，以及渲染非材质项目（如线框和所选边/顶点）。

硬件选择允许选择细分的几何体。此外，线框和组件在视口中绘图时使用同一轮廓作为着色材质。此技术有 7 个不同的过程。

![图：（图旁无可取正文，Maya 手册 img 无 alt）](https://help.autodesk.com/cloudhelp/2022/CHS/Maya-LightingShading/images/GUID-770B0370-FACD-4202-8D05-FF75BDEE2711.png) <!-- baize:img-hook downloaded=false reason="正文 4420 字 ≥300，非承重" -->

在定义技术之前，#include 指令用于加载四个着色器，如下所示。#include 指令允许在不同的应用程序之间共享相同的 GLSL 片段，并保持单独的着色器代码文件，而不必将它们合并到一个 .ogsfx 文件中。

GS_FatLine.ogsfh：这是可将线转化为矩形的几何体着色器，因此允许渲染线进行较大的绘制（例如，红色预先选择亮显的边绘制得比休眠边大）。

GS_FatPoint.ogsfh：这是可将一个点转化为四边形的几何体着色器，因此允许渲染点进行较大的绘制（例如，顶点将渲染为方形，而不是单个像素）。

PS_SolidColor.ogsfh：这是一个像素着色器，使用纯色进行绘制。

PS_HWSelection.ogsfh：这是一个在硬件选择过程中渲染组件的像素着色器，其中每个组件都使用不同的纯色进行渲染，并且该纯色使用对象或组件 ID 进行计算。

前 4 个过程用于在视口中绘制；因此使用了 PS_Normal 和 PS_SolidColor 像素着色器。

- Pass pNormal：渲染纹理材质

  Pass pNonMaterialItems：渲染组件，如线框和顶点。组件将使用纯色进行渲染，如蓝色用于休眠对象的边，而浅绿色用于活动对象的边。

  Pass pNonMaterialItemsFatLine：使用 GS_FatLine 几何体着色器渲染线。

  Pass pNonMaterialItemsFatPoint：使用 GS_Point 几何体着色器渲染点。

最后 3 个过程用于在硬件选择期间渲染组件，因此使用 PS_HWSelection 像素着色器。未使用 PS_SolidColor 像素着色器，因为这些过程不用于在视口中进行绘制。

基本体 ID（如顶点 ID）用于生成一种颜色来标识拾取的对象。屏幕外缓冲区用于存储这些计算的颜色，以便 Maya 知道鼠标拾取的内容。

  Pass pNonMaterialItemsSelection：用于选择组件，如线框和顶点。

  Pass pNonMaterialItemsSelectionFatLine：用于选择粗的线

  Pass pNonMaterialItemsSelectionFatPoint：用于选择粗的点。

### 技术和过程注释

overridesNonMaterialItems 技术注释指定此技术可用于渲染非材质项目，例如线框以及边或顶点等组件。

```text
string overridesNonMaterialItems = "true";
```

过程注释用于告知插件将哪些过程用于哪些渲染项目。

例如：

```text
pass pNonMaterialItemsFatLine
<
// This pass will be used to render non material items as fat lines
string drawContext = "nonMaterialItemsPass";
string primitiveFilter = "fatLine";
>
```

因此，如果渲染项目属于非材质项目，而基本体类型属于粗线，则使用 pNonMaterialItemsFatLine 过程。

有关这些过程注释的信息，请参见[支持的过程注释](https://help.autodesk.com/cloudhelp/2022/CHS/Maya-LightingShading/files/GUID-13229A83-B6A0-4280-840C-F9C6F40BB13D.htm#GUID-13229A83-B6A0-4280-840C-F9C6F40BB13D__SECTION_A918E2F899F4430F806D16FEEFCE82B2)。

有关 OverrideNonMaterialItems 的详细信息，请参见 *Maya 开发人员帮助*中的 MRenderItem::RenderItemType。
