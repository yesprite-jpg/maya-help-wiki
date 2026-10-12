# 与其他应用程序共享 DirectX 11 着色器代码

## 使用 _MAYA_ 宏

如果您与其他应用程序共享 HLSL 文件，但需要包括 Maya 特定的代码，可以将 HLSL 代码包含在 _MAYA_ 宏中，类似于以下示例：

```text
#ifdef _MAYA_
    float2 UV = float2(U, 1.0-V);
#endif
```
