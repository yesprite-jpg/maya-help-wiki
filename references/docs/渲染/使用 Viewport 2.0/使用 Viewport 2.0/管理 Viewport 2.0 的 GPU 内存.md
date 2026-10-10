# 管理 Viewport 2.0 的 GPU 内存

![图：（图旁无可取正文，Maya 手册 img 无 alt）](https://help.autodesk.com/cloudhelp/2022/CHS/Maya-Rendering/images/GUID-4AB6AA8F-094A-422B-981B-D2867DCC6E66.png) <!-- baize:img-hook downloaded=false reason="正文 1443 字 ≥300，非承重" -->

## Viewport 2.0 硬件要求

要运行 Viewport 2.0，您必须拥有正确的图形配置和图形驱动程序版本。有关 Maya 认证显卡和最新驱动程序版本的信息，请参见 Autodesk 知识网络上的 [Maya 认证硬件](https://knowledge.autodesk.com/zh-hans/support/maya/troubleshooting/caas/simplecontent/simplecontent/CHS/content/maya-certified-hardware.html)。

另请参见 [http://www.autodesk.com/hardware-chs](http://www.autodesk.com/hardware-chs)。

## 监视 GPU 内存使用

![图：（图旁无可取正文，Maya 手册 img 无 alt）](https://help.autodesk.com/cloudhelp/2022/CHS/Maya-Rendering/images/GUID-4AB6AA8F-094A-422B-981B-D2867DCC6E66.png) <!-- baize:img-hook downloaded=false reason="正文 1443 字 ≥300，非承重" -->

对于包含大量纹理、几何体或缓存动画的场景，请务必记下显卡上可用的 GPU RAM 量。

如果您的 GPU RAM 使用量非常接近显卡的 GPU RAM 限制，则纹理可能看起来比较模糊或根本不加载，使得场景以着色模式显示，具体取决于您当前的[最大纹理分辨率钳制(Maximum Texture Resolution Clamping)](https://beehive.autodesk.com/community/service/rest/cloudhelp/resource/cloudhelpchannel/guidcrossbook/jsonp?v=2022&p=MAYAUL&l=CHS&accessmode=live&guid=GUID-9BBB6035-2A02-41BB-AF2D-99D9BEE580F1#GUID-9BBB6035-2A02-41BB-AF2D-99D9BEE580F1__SECTION_FE279AE79FA54506909D0358F2A3D88D)设置。有关解决此问题的详细信息，请参见 [Viewport 2.0 疑难解答](Viewport%202.0%20疑难解答.md)。

若要查看卡的 GPU 内存使用情况（以 MB 为单位），请使用命令 ogs -gpu。

若要在脚本编辑器中查看所有已加载纹理及其详细信息的列表，请使用命令 ogs -gpu -dt full。

若要查看卡的 GPU RAM 限制，请参见“Maya 的输出窗口”(Output Window of Maya)。

## 优化 GPU 内存

Viewport 2.0 管理其使用的 GPU 内存。处理包含大量对象或高分辨率纹理的复杂场景时，您可能需要减少内存使用量。以下是一些指导原则：

- 如果场景中包含许多视口效果，例如屏幕空间环境光遮挡、多重采样抗锯齿、运动模糊等，则达到 GPU 内存限制时可能会遇到视觉损坏。若要解决此问题，请禁用某些视口效果；或者在具有更大 GPU 内存的显卡上运行 Maya。

- 对于使用复杂着色器网络（例如复杂的 ShaderFX 网络）或大量使用 DirectX 11 ubershader 的场景；或者涉及到视口效果（如屏幕空间环境光遮挡或景深）的场景，显卡的速度可能会影响性能。

- 启用阴影会影响 GPU 内存使用情况以及性能。成本取决于阴影分辨率和启用阴影的灯光数量。

- GPU 实例化可减少 GPU 内存使用量（如果有大量实例）。

- 对于大型的复杂场景，请考虑使用 GPU 缓存工作流。有关详细信息，请参见[关于 GPU 缓存](https://beehive.autodesk.com/community/service/rest/cloudhelp/resource/cloudhelpchannel/guidcrossbook/jsonp?v=2022&p=MAYAUL&l=CHS&accessmode=live&guid=GUID-C893BE60-6E65-4F36-8005-FD4D1A0E9822)。

- 减小摄影机的远剪裁距离，以便在视口中显示较少的几何体

- 隐藏无需显示的对象

- 卸载引用

- 将对象更改为边界框模式

### 运行多个 Maya 会话

![图：（图旁无可取正文，Maya 手册 img 无 alt）](https://help.autodesk.com/cloudhelp/2022/CHS/Maya-Rendering/images/GUID-4AB6AA8F-094A-422B-981B-D2867DCC6E66.png) <!-- baize:img-hook downloaded=false reason="正文 1443 字 ≥300，非承重" -->

运行多个 Maya 会话；或同时运行 Maya 和其他 3D 程序，需要额外的 GPU 内存。如果 Maya 和其他 3D 应用程序同时运行，它不会自动检测到需要与其他应用程序共享内存，因此可能会无意中超过 GPU 内存限制。

您可以设置 MAYA_OGS_GPU_MEMORY_LIMIT 环境变量，以覆盖 Viewport 2.0 中的内存检测并手动设置较低的内存限制，从而为其他 3D 应用程序保留 GPU 内存。将 MAYA_OGS_GPU_MEMORY_LIMIT 设置为内存限制 (MB)，然后重新启动 Maya。例如，若要将 2GB 卡上的 Viewport 2.0 限制为仅使用 1GB，请将该环境变量设置为 1024。输出窗口确认已手动设置内存限制。

或者，您可以使用命令 ogs -gmt 后跟一个数字来实现相同的效果，而无需重新启动 Maya。例如，若要将 2GB 卡上的 Viewport 2.0 限制为仅使用 1GB，请使用命令 ogs -gmt 1024。然后，您可以使用命令 ogs -q -gmt 仔细检查每个 Maya 会话认为它具有的 GPU 内存量。

这两种方法可以在同时运行 3D 应用程序的实例中提高性能，否则会降低性能，因此应谨慎使用。

## 相关主题

- [优化 Viewport 2.0](优化%20Viewport%202.0.md)

- [Viewport 2.0 限制](Viewport%202.0%20限制.md)

- [Viewport 2.0 疑难解答](Viewport%202.0%20疑难解答.md)
