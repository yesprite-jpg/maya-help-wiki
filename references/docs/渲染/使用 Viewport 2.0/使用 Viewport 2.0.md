# 使用 Viewport 2.0

Viewport 2.0 是 Maya 中的视口和硬件渲染器，可供您查看场景。

## Viewport 2.0 的优势

Viewport 2.0 提供了旧版视口所不具备的大量性能优势、显示质量优势和功能。如果要过渡到 Viewport 2.0，请参见[关于 Viewport 2.0](使用%20Viewport%202.0/关于%20Viewport%202.0.md)，了解有关这些优势的详细信息。

## 优化 Viewport 2.0

有关如何优化 Viewport 2.0 性能的提示，请参见[优化 Viewport 2.0](使用%20Viewport%202.0/优化%20Viewport%202.0.md)。

## Viewport 2.0 疑难解答

有关常见 Viewport 2.0 问题的解决方案，请参见 [Viewport 2.0 疑难解答](使用%20Viewport%202.0/Viewport%202.0%20疑难解答.md)。

## API 支持

使用 Maya API 创建插件，以在 Viewport 2.0 中绘制、着色和创建各种效果。Maya 开发人员帮助的 *Viewport 2.0 API* 部分提供了有关可用于 Viewport 2.0 的类别和方法的信息，以及有关如何将使用旧版视口 API 的插件更新为使用 Viewport 2.0 API 的信息。

有关如何使用 Maya Viewport 2.0 API 将旧版代码移植到最新 Maya 视口技术的详细信息，请参见《Viewport 2.0 API 移植手册》和 白皮书，网址为 [http://www.autodesk.com/developmaya](http://www.autodesk.com/developmaya)。

## OpenGL、DirectX 11 和 OpenGL 核心配置

在 Viewport 2.0 中可以选择四个渲染引擎：“OpenGL - 旧版”(OpenGL - Legacy)、“DirectX 11”、“OpenGL - 核心配置(兼容性)”(OpenGL - Core Profile (Compatibility))和“OpenGL - 核心配置(精确)”(OpenGL - Core Profile (Strict))。

选择“窗口 > 设置/首选项 > 首选项”(Window > Settings/Preferences > Preferences)以打开“首选项”(Preferences)窗口。选择“显示”(Display)类别，然后在“Viewport 2.0”部分下选择“渲染引擎”(Rendering engine)。

通过选择“DirectX 11”作为渲染引擎，您可以在视口中实时渲染 DX11 硬件着色器。有关详细信息，请参见[在 DirectX 11 模式下运行 Viewport 2.0](使用%20Viewport%202.0/在%20DirectX%2011%20模式下运行%20Viewport%202.0.md)。

通过选择“OpenGL - 核心配置(兼容性)”(OpenGL - Core Profile (Compatibility))或“OpenGL - 核心配置(精确)”(OpenGL - Core Profile (Strict))作为渲染引擎，可以创建支持照明、纹理、阴影和细分的自定义 GLSL（OpenGL 着色语言）着色器。请参见[在核心配置模式下运行 Viewport 2.0](使用%20Viewport%202.0/在“OpenGL%20核心配置”%28OpenGL%20Core%20Profile%29模式下运行%20Viewport%202.0.md)。

有关详细信息，另请参见[渲染引擎](https://beehive.autodesk.com/community/service/rest/cloudhelp/resource/cloudhelpchannel/guidcrossbook/jsonp?v=2022&p=MAYAUL&l=CHS&accessmode=live&guid=GUID-BF017019-B89A-47F0-8AB5-106C058AB854#GUID-BF017019-B89A-47F0-8AB5-106C058AB854__SECTION_B04F0E5A1332417DA2CD3FE483F186D4)（位于 Viewport 2.0 选项中）。

**注**

如果您使用的第三方插件或具有的自定义开发在 Viewport 2.0 中不受支持，则可以使用 MAYA_ENABLE_LEGACY_VIEWPORT 环境变量启用旧版视口。如果启用旧版视口，对于具有平滑 OpenSubdiv 网格的场景，Viewport 2.0 内存使用量会增加。为了保持 Viewport 2.0 性能，应在不使用旧版视口时通过禁用该环境变量将其禁用。请参见

渲染变量

。

## 相关主题

- [Viewport 2.0 选项](https://beehive.autodesk.com/community/service/rest/cloudhelp/resource/cloudhelpchannel/guidcrossbook/jsonp?v=2022&p=MAYAUL&l=CHS&accessmode=live&guid=GUID-9BBB6035-2A02-41BB-AF2D-99D9BEE580F1)
