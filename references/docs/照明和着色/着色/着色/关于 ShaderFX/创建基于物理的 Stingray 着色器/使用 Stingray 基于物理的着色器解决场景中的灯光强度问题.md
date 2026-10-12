# 使用 Stingray 基于物理的着色器解决场景中的灯光强度问题

Stingray PBS 材质中的灯光强度以灯光停止数进行测量。如果您发现灯光强度太亮，可以禁用“灯光强度(以停止数为单位)”(Light Intensity in Stops)选项。在“Stingray PBS”节点“属性编辑器”(Attribute Editor)中，单击“打开 ShaderFX”(Open ShaderFX)，然后在 ShaderFX 编辑器中选择 Stingray 的“标准基础”(Standard Base)节点，并在“属性编辑器”(Attribute Editor)中禁用“停止中的灯光强度”(Light Intensity in Stops)选项。
