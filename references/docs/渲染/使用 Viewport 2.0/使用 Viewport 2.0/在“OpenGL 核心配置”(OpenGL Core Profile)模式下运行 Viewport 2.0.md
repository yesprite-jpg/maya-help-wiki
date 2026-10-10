# 在“OpenGL 核心配置”(OpenGL Core Profile)模式下运行 Viewport 2.0

可以使用 OpenGL、DirectX 11 或“OpenGL 核心配置”(OpenGL Core Profile)模式运行 Viewport 2.0。

可以选择“OpenGL - 核心配置(兼容性)”(OpenGL - Core Profile (Compatibility))或“OpenGL - 核心配置(精确)”(OpenGL - Core Profile (Strict))。

“OpenGL - 核心配置(兼容性)”(OpenGL - Core Profile (Compatibility))仅可用于 Windows 和 Linux 平台，并支持以下版本的所有功能：

- OpenGL 2.1 及更低版本

- OpenGL 3.2 及更高版本

“OpenGL - 核心配置(精确)”(OpenGL - Core Profile (Strict))支持 OpenGL 3.2 及更高版本的功能，是 Mac OS X 平台上的默认渲染引擎。

有关详细信息，请参见[渲染引擎](https://beehive.autodesk.com/community/service/rest/cloudhelp/resource/cloudhelpchannel/guidcrossbook/jsonp?v=2022&p=MAYAUL&l=CHS&accessmode=live&guid=GUID-BF017019-B89A-47F0-8AB5-106C058AB854#GUID-BF017019-B89A-47F0-8AB5-106C058AB854__SECTION_B04F0E5A1332417DA2CD3FE483F186D4)。

若要在核心配置模式下运行 Viewport 2.0，请选择“窗口 > 设置/首选项 > 首选项”(Windows > Settings/Preferences > Preferences)以打开“首选项”(Preferences)窗口，然后从“显示”(Display)类别中选择“OpenGL - 核心配置(兼容性)”(OpenGL - Core Profile (Compatibility))或“OpenGL - 核心配置(精确)”(OpenGL - Core Profile (Strict))作为“渲染引擎”(Rendering engine)。

如果要创建自定义 GLSL 着色器，则还必须加载 glslShader 插件。选择“窗口 > 设置/首选项 > 插件管理器”(Windows > Settings/Preferences > Plug-in Manager)，然后加载 glslShader.mll。

也可以将 MAYA_VP2_DEVICE_OVERRIDE 环境变量设置为在所需模式下始终运行 Viewport 2.0。设置后，此环境变量将覆盖用户首选项。请参见[渲染环境变量](https://beehive.autodesk.com/community/service/rest/cloudhelp/resource/cloudhelpchannel/guidcrossbook/jsonp?v=2022&p=MAYAUL&l=CHS&accessmode=live&guid=GUID-4928A912-DA6C-4734-863B-AB5959DA73C9#GUID-4928A912-DA6C-4734-863B-AB5959DA73C9__GUID-F8BA8FA2-1927-4977-8CDC-4903CAFB16D2)。

## 相关主题

- [创建和可视化 GLSL 着色器](https://beehive.autodesk.com/community/service/rest/cloudhelp/resource/cloudhelpchannel/guidcrossbook/jsonp?v=2022&p=MAYAUL&l=CHS&accessmode=live&guid=GUID-41D74556-0699-4F4E-8382-F9E69FBFC158)

- [GLSL 着色器](https://beehive.autodesk.com/community/service/rest/cloudhelp/resource/cloudhelpchannel/guidcrossbook/jsonp?v=2022&p=MAYAUL&l=CHS&accessmode=live&guid=GUID-BD177012-56E1-43D0-B7A5-F4B1A70EA846)

- [在 DirectX 11 模式下运行 Viewport 2.0](在%20DirectX%2011%20模式下运行%20Viewport%202.0.md)
