# 创建和可视化 GLSL 着色器

若要创建并可视化 GLSL 着色器，必须在“OpenGL 核心配置”(OpenGL Core Profile)模式下运行 Viewport 2.0，并加载 glslShader 插件。请参见[在核心配置模式下运行 Viewport 2.0](https://beehive.autodesk.com/community/service/rest/cloudhelp/resource/cloudhelpchannel/guidcrossbook/jsonp?v=2022&p=MAYAUL&l=CHS&accessmode=live&guid=GUID-43B99310-5D5B-4C86-B716-0BF44A3CFB4C)。执行这些步骤后，在 Hypershade 的“创建”(Create)选项卡中以及“创建渲染节点”(Create Render Node)窗口和“指定新材质”(Assign New Material)窗口中将显示 GLSL 着色器。

创建自定义 GLSL 着色器

1. 右键单击对象，然后选择“指定新材质”(Assign New Material)。

2. 从“指定新材质”(Assign New Material)窗口中选择“GLSL 着色器”(GLSL Shader)。

3. 在 GLSLShader 属性编辑器中，导航到 .ogsfx 文件。

  示例 .ogsfx 文件可在 Maya 安装目录的 ..\presets\GLSL\examples 文件夹中找到。开发人员工具包示例 *brickShader*（C++ 和 Python 版本）也已更新为支持 GLSL，因此可在视口中以“OpenGL 核心配置”(OpenGL Core Profile)模式运行。

  [Autodesk Developer Network](https://www.autodesk.com/developmaya) 中提供了开发人员工具包。

  **注**

    如果在场景中加载效果文件后使用外部文本编辑器编辑了效果文件，则必须通过单击 ![图：如果在场景中加载效果文件后使用外部文本编辑器编辑了效果文件，则必须通过单击 图标重新加载文件，这样着色器才能识别您所做的…](https://help.autodesk.com/cloudhelp/2022/CHS/Maya-LightingShading/images/GUID-49424667-4F99-4E3A-875F-2F3F1B79EF37.png) <!-- baize:img-hook downloaded=false reason="正文 958 字 ≥300，非承重" --> 图标重新加载文件，这样着色器才能识别您所做的最新更改。

    加载 .ogsfx 文件时，如果 GLSL 着色器中的任何参数与您先前已加载的 .ogsfx 文件中的参数名称和类型匹配，则这些参数将使用现有场景值，而不是新文件中的默认值。

    例如，如果您有两个效果文件，其中 effect1.ogsfx 的 gAmbient 参数默认值为“绿色”(green)，effect2.ogsfx 的 gAmbient 参数默认值为“红色”(red)，您先加载第一个 effect1，然后再加载 effct2，加载 effect2 后，gAmbient 参数值仍为“绿色”(green)。此外，如果您加载 effect1，稍后将 gAmbient 颜色更改为“蓝色”(blue)并加载 effect2，则由于系统保留当前值，因此 gAmbient 仍为“蓝色”(blue)

    这允许您从简单的效果切换至更复杂的效果，而不影响环境光和其他共享参数的当前场景值。
