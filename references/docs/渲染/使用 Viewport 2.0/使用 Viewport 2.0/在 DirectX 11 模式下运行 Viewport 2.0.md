# 在 DirectX 11 模式下运行 Viewport 2.0

可以使用 OpenGL、DirectX 11 或“OpenGL 核心配置”(OpenGL Core Profile)模式运行 Viewport 2.0。有两种方法可以将 DirectX 设置为渲染引擎。

方法 1

1. 在“首选项”(Preferences)窗口（“窗口 > 设置/首选项 > 首选项”(Window > Settings/Preferences > Preferences)）中，选择“显示”(Display)类别。将“渲染引擎”(Rendering engine)设置为 DirectX 11。

  **注**

  重要：

  若要使用 DirectX 渲染引擎，您必须使用 64 位的 Windows 和可兼容 DirectX 11 的显卡。

2. 选择“窗口 > 设置/首选项 > 插件管理器”(Window > Settings/Preferences > Plug-in Manager)并加载 dx11Shader.mll 插件。

方法 2

将 MAYA_VP2_DEVICE_OVERRIDE 环境变量设置为 VirtualDeviceDx11 以始终在 DirectX 11 模式下运行 Viewport 2.0。请参见[渲染环境变量](https://beehive.autodesk.com/community/service/rest/cloudhelp/resource/cloudhelpchannel/guidcrossbook/jsonp?v=2022&p=MAYAUL&l=CHS&accessmode=live&guid=GUID-4928A912-DA6C-4734-863B-AB5959DA73C9#GUID-4928A912-DA6C-4734-863B-AB5959DA73C9__GUID-F8BA8FA2-1927-4977-8CDC-4903CAFB16D2)。

此环境变量将覆盖交互式和批处理会话的用户首选项（“窗口 > 设置/首选项 > 首选项 > 显示”(Window > Settings/Preferences > Preferences > Display)）（使用 -hw2 选项）。

**注**

取消设置该环境变量可再次使用用户首选项来选择渲染引擎。

## 相关主题

- [创建 DirectX 着色器](https://beehive.autodesk.com/community/service/rest/cloudhelp/resource/cloudhelpchannel/guidcrossbook/jsonp?v=2022&p=MAYAUL&l=CHS&accessmode=live&guid=GUID-547BDF7D-2FDE-4823-8FA3-A0B3F74EB481)
