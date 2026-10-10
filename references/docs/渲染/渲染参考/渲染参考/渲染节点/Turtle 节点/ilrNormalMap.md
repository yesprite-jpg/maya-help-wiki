# ilrNormalMap

ilrNormalMapNode 是一个工具节点，用于将文件纹理法线贴图重映射到摄影机空间。将其插入到表面着色器的凹凸贴图 (normalCamera) 属性。

**注**

ilrNormalMap 节点应该直接映射到 normalCamera 属性。您不应在二者之间使用 Bump2D 节点。

## 法线贴图属性

#### 坐标系(Coordinate System)

用于创建法线贴图的坐标系。

#### 使用面切线(Use Face Tangent)

逐面使用固定切线空间，而非对顶点切线空间进行插值。

#### 输入(Input)

输入文件。将包含文件纹理法线贴图的文件节点映射到此属性。
