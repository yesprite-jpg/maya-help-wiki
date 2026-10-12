# 解决 Stingray 基于物理的着色器网络问题

在 Stingray PBS 节点的 ShaderFX 编辑器中，如果执行非法运算（如将 float2 与 float3 相乘），则在单击“渲染样例”(Render Swatch) ![图：在 Stingray PBS 节点的 ShaderFX 编辑器中，如果执行非法运算（如将 float2 与 float3…](https://help.autodesk.com/cloudhelp/2022/CHS/Maya-LightingShading/images/GUID-997874AC-2919-414E-BEDE-BF9C19791FB6.png) <!-- baize:img-hook downloaded=false reason="正文 321 字 ≥300，非承重" --> 图标时，将遇到错误“此时此节点不支持样例渲染”(Swatch Rendering not supported for this node at this time)。换句话说，您的样例未编译。

选择“设置 > 显示样例编译错误”(Settings > Show Swatch Compile Errors)，然后单击“渲染样例”(Render Swatch)图标，并检查在 ShaderFX 编辑器窗口中显示的错误。

![图：（图旁无可取正文，Maya 手册 img 无 alt）](https://help.autodesk.com/cloudhelp/2022/CHS/Maya-LightingShading/images/GUID-AED1C6B9-2128-4C55-8B7C-D8E98D93B14C.png) <!-- baize:img-hook downloaded=false reason="正文 321 字 ≥300，非承重" -->

## 相关主题

- [创建 Stingray 基于物理的着色器](../创建基于物理的%20Stingray%20着色器.md)

- [使用 ShaderFX 编辑器构建 Stingray 基于物理的着色器](使用%20ShaderFX%20编辑器构建基于物理的%20Stingray%20着色器.md)
