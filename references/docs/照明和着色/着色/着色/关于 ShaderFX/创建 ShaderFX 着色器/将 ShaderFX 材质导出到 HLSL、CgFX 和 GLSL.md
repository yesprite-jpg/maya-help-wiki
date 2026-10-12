# 将 ShaderFX 材质导出到 HLSL、CgFX 和 GLSL

您可以将 ShaderFX 材质导出为以下格式：HLSL、GLSL 或 CgFX。

1. 在 ShaderFX 编辑器中选择 *Material* 节点。

2. 在 *ShaderfxShader* 属性编辑器中的“HwShader/着色器配置”(HwShader/Shader Config)下，从下拉列表中选择您想导出的格式。

3. 在“HwShader/文件名”(HwShader/Filename)下，浏览到您希望将着色器文件导出到的目录并输入文件名，然后按 ![图：在“HwShader/文件名”(HwShader/Filename)下，浏览到您希望将着色器文件导出到的目录并输入文件名…](https://help.autodesk.com/cloudhelp/2022/CHS/Maya-LightingShading/images/GUID-6222D533-8226-4499-A976-3C4A762C2345.png) <!-- baize:img-hook downloaded=false reason="正文 319 字 ≥300，非承重" -->。

4. 单击“HwShader/保存到磁盘”(HwShader/Save to Disk)。

着色器文件将保存到您指定的位置。

**注**

生成的着色器文件会设置相应格式以在 Maya 内使用。如果您正在 Maya 外使用文件，则可能需要调整其格式和语义。
