# “缓存播放”(Cached Playback)不支持的节点

Maya 依存关系图 (DG) 中的某些节点将禁用“缓存播放”(Cached Playback)过程。此部分仅讨论禁用“播放缓存”(Playback Caching)的已设置动画节点。如果节点未设置动画，“播放缓存”(Playback Caching)将不会受其影响。例如，只要未设置动画的 XGen 节点是静态的，便可以将其与“缓存播放”(Cached Playback)结合使用。（其中“未设置动画”表示节点不是解算图的一部分。）

如果 Maya 在场景中检测到任何不支持的节点，则禁用“播放缓存”(Playback Caching)并进入安全模式。当“缓存播放”(Cached Playback)处于安全模式时，“缓存播放”(Cached Playback)状态行和“缓存播放”(Cached Playback)图标将变为黄色。（有关详细信息，请参见[“缓存播放”(Cached Playback)状态行的状态](../“缓存播放”%28Cached%20Playback%29状态行的状态.md)。）

![图：（图旁无可取正文，Maya 手册 img 无 alt）](https://help.autodesk.com/cloudhelp/2022/CHS/Maya-Animation/images/GUID-E1962425-643E-4910-A1B0-C7A0AFD2573A.png) <!-- baize:img-hook downloaded=false reason="正文 2806 字 ≥300，非承重" -->

在安全模式下时，“缓存播放”(Cached Playback)图标变为黄色

- **textureDeformer** 节点不受支持，因此禁用“缓存播放”(Cached Playback)。

- 仅当“hairSystem.simulationMethod”为 **off** 或 **static** 并且 nucleus 节点设置为**“已禁用”(disabled)**时，才支持 **hairSystem** 节点，而无论“缓存动力学”(Cache Dynamics)选项（在[解算工具包(Evaluation Toolkit)](https://beehive.autodesk.com/community/service/rest/cloudhelp/resource/cloudhelpchannel/guidcrossbook/jsonp?v=2022&p=MAYAUL&l=CHS&accessmode=live&guid=GUID-E22B253D-914B-4056-93F5-755702A6C998)的“缓存”(Caching)部分中）如何。

提供了单独的“动力学”(Dynamics)状态行（不同于“动画”(Animation)状态行），可用于在场景中加载和刷新 nParticle 和 nCloth 动力学以及动画（尚不支持 nHair）。使用[缓存播放首选项(Cached Playback Preferences)](https://beehive.autodesk.com/community/service/rest/cloudhelp/resource/cloudhelpchannel/guidcrossbook/jsonp?v=2022&p=MAYAUL&l=CHS&accessmode=live&guid=GUID-3CB35662-DB1D-4CF3-9135-E09B973635DE)的“缓存”(Caching)部分中的“缓存动力学”(Cache Dynamics)选项，激活“缓存播放”(Cached Playback)动力学支持。

通过使用以下环境变量，您可以覆盖任何其他动力学的限制并将“缓存播放”(Cached Playback)强制用于动力学节点：MAYA_CACHE_IGNORE_UNSAFE_<节点名称>。

对于每个不支持的节点，使用下表中的变量。

**注**

有关使用环境变量的信息，请参见

使用 Maya.env 设置环境变量

。

**注**

有关

“缓存播放”(Cached Playback)

的技术详细信息，请参见

Maya 缓存播放白皮书

。

#### Bifrost

| 禁用的节点/属性 | 支持的值 | 强制启用缓存方式 |
|---|---|---|
| bifrostContainer |  | MAYA_CACHE_IGNORE_UNSAFE_BIFROST |

#### 缓存文件

| 禁用的节点/属性 | 支持的值 | 强制启用缓存方式 |
|---|---|---|
| cacheFile |  | MAYA_CACHE_IGNORE_UNSAFE_CACHE_FILE |

#### 油性铅笔

| 禁用的节点/属性 | 支持的值 | 强制启用缓存方式 |
|---|---|---|
| greasePlane greasePencilSequence |  | MAYA_CACHE_IGNORE_UNSAFE_GREASE_PENCIL |

#### MASH

| 禁用的节点/属性 | 支持的值 | 强制启用缓存方式 |
|---|---|---|
| MASH_Jiggle |  | MAYA_CACHE_IGNORE_UNSAFE_MASH |
| MASH_Trails.trailsMode （有条件的支持：某些属性值禁用缓存） | 接合点 (2) 连接到点 (3) 连接到最近点 (4) 按距离连接 (5) 约束对 (6) |  |
| MASH_Flight | FALSE |  |
| MASH_Spring | FALSE |  |
| MASH_Falloff.falloffEventType （有条件的支持：某些属性值禁用缓存） | FALSE |  |
| MASH_Time.enableVelocity （有条件的支持：某些属性值禁用缓存） | FALSE |  |
| MASH_Time.simulateTime （有条件的支持：某些属性值禁用缓存） | FALSE |  |
| MASH_Orient.orientMode （有条件的支持：某些属性值禁用缓存） | FALSE |  |
| MASH_Color.enableVelocity （有条件的支持：某些属性值禁用缓存） | FALSE |  |

#### 肌肉

| 禁用的节点/属性 | 支持的值 | 强制启用缓存方式 |
|---|---|---|
| cMuscleSystem.enableJiggle （有条件的支持：某些属性值禁用缓存） | FALSE | MAYA_CACHE_IGNORE_UNSAFE_MUSCLE |
| cMuscleSystem.enableSliding （有条件的支持：某些属性值禁用缓存） | FALSE |  |
| cMuscleSystem.enableForce （有条件的支持：某些属性值禁用缓存） | FALSE |  |
| cMuscleSystem.enableRelax （有条件的支持：某些属性值禁用缓存） | FALSE |  |

#### 细分

| 禁用的节点/属性 | 支持的值 | 强制启用缓存方式 |
|---|---|---|
| subdiv.aOutSubdiv （有条件的支持：某些属性值禁用缓存） | *未设置动画 | MAYA_CACHE_IGNORE_UNSAFE_DEFORMING_SUBDIV |

#### 纹理变形器(Texture Deformer)

| 禁用的节点/属性 | 支持的值 | 强制启用缓存方式 |
|---|---|---|
| textureDeformer |  | MAYA_CACHE_IGNORE_UNSAFE_TEXTURE_DEFORMER |

#### Trax

| 禁用的节点/属性 | 支持的值 | 强制启用缓存方式 |
|---|---|---|
| animClip |  | MAYA_CACHE_IGNORE_UNSAFE_TRAX |
| clipGhostData |  |  |
| clipLibrary |  |  |
| clipScheduler |  |  |
| clipToGhostData |  |  |

#### XGen

| 禁用的节点/属性 | 支持的值 | 强制启用缓存方式 |
|---|---|---|
| xgmPalette |  | MAYA_CACHE_IGNORE_UNSAFE_XGEN |
| xgmDescription |  |  |
| xgmPatch |  |  |
| xgmMakeGuide |  |  |
| xgmGuide |  |  |
| xgmGuideManip |  |  |
| xgmGuideSculptManip |  |  |
| xgmPointsManip |  |  |
| xgmConnectivity |  |  |
| xgmPointsViewer |  |  |
| xgmNurbsPatch |  |  |
| xgmSubdPatch |  |  |
| xgmArchiveGuide |  |  |
| xgmCardGuide |  |  |
| createPtexUV |  |  |
| xgmHairMapping |  |  |
| xgmSphereGuide |  |  |
| xgmSplineGuide |  |  |
| xgmSplineBase |  |  |
| xgmModifierBase |  |  |
| xgmModifierCut |  |  |
| xgmModifierCollision |  |  |
| xgmModifierSculpt |  |  |
| xgmModifierNoise |  |  |
| xgmModifierDisplacement |  |  |
| xgmModifierGuide |  |  |
| xgmModifierLinearWire |  |  |
| xgmModifierScale |  |  |
| xgmModifierClump |  |  |
| xgmCurveToSpline |  |  |
| xgmSeExpr |  |  |
| xgmSplineCache |  |  |
| xgmSplineDescription |  |  |
| igBrushManip |  |  |
| igmDescription |  |  |
