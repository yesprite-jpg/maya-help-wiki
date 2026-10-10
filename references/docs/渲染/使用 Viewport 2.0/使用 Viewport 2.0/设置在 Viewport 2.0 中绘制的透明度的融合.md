# 设置在 Viewport 2.0 中绘制的透明度的融合

在 Viewport 2.0 中，分别为 RGB 通道和 Alpha 通道指定融合。该行为不同于默认渲染器和高质量渲染器的行为，其中 RGB 和 Alpha 共享一组融合参数。

编写插件时，使用 MHWRender::MBlendStateDesc 融合状态类指定您的融合。

设定源、目标融合和 Alpha 融合，并设定要添加的融合操作。融合因子应设定为 1、1、1、1。

以下示例取自开发人员工具包中提供的 hwPhongShader 节点插件。

[Autodesk Developer Network](https://www.autodesk.com/developmaya) 中提供了开发人员工具包。

```text
MHWRender::MBlendStateDesc blendStateDesc;
for(int i = 0; i < (blendStateDesc.independentBlendEnable ? MHWRender::MBlendState::kMaxTargets : 1); ++i)
{
   blendStateDesc.targetBlends[i].blendEnable = true;
   blendStateDesc.targetBlends[i].sourceBlend = MHWRender::MBlendState::kSourceAlpha;
   blendStateDesc.targetBlends[i].destinationBlend = MHWRender::MBlendState::kInvSourceAlpha;
   blendStateDesc.targetBlends[i].blendOperation = MHWRender::MBlendState::kAdd;
   blendStateDesc.targetBlends[i].alphaSourceBlend = MHWRender::MBlendState::kOne;
   blendStateDesc.targetBlends[i].alphaDestinationBlend = MHWRender::MBlendState::kInvSourceAlpha;
   blendStateDesc.targetBlends[i].alphaBlendOperation = MHWRender::MBlendState::kAdd;
}

blendStateDesc.blendFactor[0] = 1.0f;
blendStateDesc.blendFactor[1] = 1.0f;
blendStateDesc.blendFactor[2] = 1.0f;
blendStateDesc.blendFactor[3] = 1.0f;
```

若要通过内置 cgfx 插件示例设置同一状态，请指定以下过程状态：

```text
BlendFunc = int2( SrcAlpha, OneMinusSrcAlpha);
BlendFuncSeparate = int4( SrcAlpha, OneMinusSrcAlpha, One, OneMinusSrcAlpha);
BlendEquationSeparate = int2( Add, Add );
BlendColor = float4(1.0f,1.0f,1.0f,1.0f);
```

其中：

- BlendColor 对应于 blendFactor

- BlendFuncSeperate 对应于 sourceBlend、destinationBlend、alphaSourceBlend 和 alphaDestinationBlend

- BlendEquationSeparate 对应于 blendOperation 和 alphaBlendOperation

在 MBlendStateDesc 结构中。

用于绘制透明度的默认融合是 { source alpha, 1-source alpha }，如以下示例所示。
