# ilrLuaNode

ilrLuaNode 通过使用 Lua 脚本允许自定义着色器。

Lua 节点将使用语言 Lua 编写的脚本文件作为输入，并对每个片段执行该文件。有关编程语言 Lua 的参考，请访问 [http://www.lua.org](http://www.lua.org)。

可以将 Lua 节点用作输出着色器。这可通过将 Lua 节点连接到 Turtle 渲染全局参数中的输出着色器来实现。然后，可以将“输出着色器”(Output Shader)后端节点连接到 Lua 输入之一。用法示例包括：延缓着色或调整输出图像的级别。请注意，如果 Lua 节点未连接到着色器，则没有灯光或片段信息等隐式数据（输入除外）可用。

**注**

在 Lua 中，数组和向量的索引从 1 开始。

## LUA 属性

#### 脚本文件(Script File)

此字段指定 Lua 脚本的源文件。它可以带有前缀 nn，以便使其与项目相关。例如，nnturtlenscriptsnphong.lua 指定位于项目目录的 turtle 部分中的脚本。

#### 输入 1-5 (Input 1-5)

这些是可以连接到其他着色节点的颜色输入。可以从 Lua 脚本访问它们。

#### 输出 1 (output1)

Lua 脚本的结果。

## 对 Lua 的 Turtle 扩展

数据类型：

- vec3：三个浮点值的向量它可以通过函数 vec3(x,y,z) 构建。

用于检索隐式数据的函数：

- vec3 getPoint()：返回片段的世界空间相交点。

- vec3 getNormal()：返回片段的法线。

- vec3 getTangentU()：返回片段的切线。

- vec3 getTangentV()：返回片段的双切线。

- vec3 getViewDir()：返回世界空间中从片段指向视点的向量。

- vec3 getUV()：返回片段的纹理坐标。使用 vec3 的前两个组件。

- vec3 getdTdX()：返回纹理空间中屏幕空间像素的 X 轴的投影。使用 vec3 的前两个组件。

- vec3 getdTdY()：返回纹理空间中屏幕空间像素的 Y 轴的投影。使用 vec3 的前两个组件。

- float getT()：返回从光线原点到当前片段的距离。

- vec3 getInput(i)：从 Lua 节点返回第 i 个输入。其索引范围为 1 到 5。

照明函数：

- int getLights()：返回场景中的灯光数。

- bool getLightName(i)：返回灯光的名称。

- vec3 getLightDir(i)：返回世界空间中从第 i 个灯光到片段的方向。

- float getLightDist(i)：返回世界空间中从第 i 个灯光到片段的距离。

- vec3 getLightCol(i)：返回第 i 个灯光的颜色。

- vec3 getLightColUnshadowed(i)：返回第 i 个灯光的颜色，而不考虑阴影。

- bool getLightAmb(i)：如果灯光是环境光，则返回 true。

- bool getLightCastShadows(i)：如果灯光投射阴影，则返回 true。

光线跟踪函数：

- vec3 shootRay(vec3 o, vec3 d)：投射一条原点=o 和方向=d（带着色）的光线。返回交集的颜色。

- float shootOccRay(vec3 o, vec3 d, [float tmax])：投射一条原点 = o 和方向 = 无着色的光线。返回到最近交集的距离，如果未找到交集，则返回 -1.0f。如果需要，可以在 tmax 中指定到交集的最大距离。遮挡光线忽略遮光板的透明度。

工具函数：

- float length(vec3)：返回向量的长度。

- float smoothstep(min, max, x)：返回 smoothstep 函数。

- float step(min, max, x)：返回 step 函数。

- float dot3(vec3 x, vec3 y)：返回标量积 x.y。

- vec3 cross3(vec3 x, vec3 y)：返回叉积 x x y。

- float add3(vec3 x, y)：返回 x+y。y 可以是浮点数或 vec3。

- float sub3(vec3 x, y)：返回 x-y。y 可以是浮点数或 vec3。

- float neg3(vec3 x)：返回 -x。x 是 vec3。

- float mul3(vec3 x, y)：返回 x*y。y 可以是浮点数或 vec3。如果 y 是 vec3，则乘法运算是元素智能式乘法运算。

- float div3(vec3 x, float y)：返回 x/y。

- vec3 reflect(vec3 v, vec3 normal)：返回围绕法线反射的 v。

- vec3 refract(vec3 v, vec3 normal, float inIor, float outIor)：返回围绕法线折射的 v。inIor 是光线出射的材质的折射率，outIor 是光线入射的材质的折射率。

- vec3 normalize(vec3 v)：返回归一化 v。

vec3 运算：

- +：别名为 add3。

- -（二进制）：别名为 sub3。

- -（一元)：别名为 neg3。

- *：别名为 mul3。

- /：别名为 div3。

- [i]：返回 vec3 的第 i 个组件。
