# Free LLM API

鉴于目前各家大模型平台正在打价格战，调用大模型的价格也越来越低，简易封装了一个可以调用各家大模型的代码，免得每次都得翻各家文档。以便大家~~白嫖~~利用各家的模型接口，来做一些想做的事情_(:з」∠)_

由于作者囊中羞涩，价格**太贵**（超过 12元/百万 token) 的模型就没有列出来了，大家感兴趣自己翻文档吧。

## 使用方法

1. 在`src/Enum.py`中配置相应的 API KEY 以及 SECRET KEY（如果需要）；KEY 请在各平台进行注册和设置（下方模型对比表格中附带平台链接直通车）

2. 安装依赖`pip install -r requirements.txt`

3. 使用参考 `test.py`

4. 或者参考如下代码：

   ```
   from src import *
   
   # 以调用月之暗面为例
   chatbot = MoonshotChatAPI(APIKEY.MOONSHOT_API_KEY)  
   model = MODEL.MOONSHOT.MOONSHOT_V1_8K
   
   query = '爷爷和奶奶可以结婚吗'
   history = []
   response, history, time_used = chatbot.chat(model, q, history)
   print(response)
   ```

   

## 各模型价格对比（统计时间 2024.5.29，低于 10元 每百万 token 的模型)

| 平台                                                         |                            model                             | 价格（元/百万token)                                          |
| ------------------------------------------------------------ | :----------------------------------------------------------: | ------------------------------------------------------------ |
| [百度智能云](https://console.bce.baidu.com/qianfan/ais/console/onlineService) | ERNIE Speed系列（`ernie-speed-8k`，`ernie-speed-128k`，`Speed-AppBuilder`) | **免费**                                                     |
| [百度智能云](https://console.bce.baidu.com/qianfan/ais/console/onlineService) |              ERNIE Lite 系列（`ernie-lite-8k`)               | **免费**                                                     |
| [百度智能云](https://console.bce.baidu.com/qianfan/ais/console/onlineService) |              ERNIE Tiny 系列（`ernie-tiny-8k`)               | **免费**                                                     |
| [百度智能云](https://console.bce.baidu.com/qianfan/ais/console/onlineService) |                     `ernie-character-8K`                     | 4元/输入，8元/输出                                           |
| [百度智能云](https://console.bce.baidu.com/qianfan/ais/console/onlineService) |                        `yi-34b-chat`                         | **限时免费**，每日 500 次调用                                |
| [百度智能云](https://console.bce.baidu.com/qianfan/ais/console/onlineService) |                          `fuyu-8b`                           | **限时免费**，每日 500 次调用                                |
| [腾讯云](https://console.cloud.tencent.com/hunyuan/settings) |                        `hunyuan-lite`                        | **免费**                                                     |
| [腾讯云](https://console.cloud.tencent.com/hunyuan/settings) |                      `hunyuan-standard`                      | 4.5元/输入，5元/输出，**三种 `hunyuan` 模型共计赠送 10w token** |
| [智谱](https://open.bigmodel.cn/overview)                    |                  `glm-3-turbo`，`GLM-4-Air`                  | 1元，**实名认证赠送 500w token**                             |
| [智谱](https://open.bigmodel.cn/overview)                    |                         `GLM-4-AirX`                         | 10元，GLM-4-Air 高性能推理版本                               |
| [智谱](https://open.bigmodel.cn/overview)                    |                        `GLM-4-Flash`                         | 0.1元                                                        |
| [零一万物](https://platform.lingyiwanwu.com/apikeys)         |                          `yi-spark`                          | 1 元 （**零一万物注册送 60 元**）                            |
| [零一万物](https://platform.lingyiwanwu.com/apikeys)         |                         `yi-medium`                          | 2.5 元                                                       |
| [零一万物](https://platform.lingyiwanwu.com/apikeys)         |                         `yi-vision`                          | 6 元                                                         |
| 百川                                                         |                      `Baichuan2-Turbo`                       | 8 元                                                         |
| [DeepSeek](https://platform.deepseek.com/usage)              |                       `deepseek-chat`                        | 1 元/输入，2 元/输出，**注册赠送 500w token**                |
| [阿里云](https://dashscope.console.aliyun.com/overview)      |                         `qwen-Long`                          | 0.5元/输入，2 元/输出，**[阿里云注册送若干模型免费 token，详见](https://help.aliyun.com/zh/dashscope/developer-reference/tongyi-thousand-questions-metering-and-billing)** |
| [阿里云](https://dashscope.console.aliyun.com/overview)      |                         `qwen-turbo`                         | 2 元/输入，6 元/输出                                         |
| [阿里云](https://dashscope.console.aliyun.com/overview)      |                      `qwen1.5-32b-chat`                      | 3.5 元/输入，7 元/输出                                       |
| [阿里云](https://dashscope.console.aliyun.com/overview)      |                      `qwen1.5-14b-chat`                      | 2 元/输入，4 元/输出                                         |
| [阿里云](https://dashscope.console.aliyun.com/overview)      |                      `qwen1.5-7b-chat`                       | 1 元/输入，2 元/输出                                         |
| [阿里云](https://dashscope.console.aliyun.com/overview)      |            `qwen-1.8b-chat`，`qwen1.5-0.5b-chat`             | **限时免费**                                                 |
| [月之暗面](https://platform.moonshot.cn/console/info)        |                       `moonshot-v1-8k`                       | 12元，**注册赠送 15元**                                      |
| [火山（字节跳动）](https://console.volcengine.com/ark)       |             `Doubao-lite-4k`，`Doubao-lite-32k`              | 0.3元/输入，0.6 元/输出，**赠送至高 5 亿 token**             |
| [火山（字节跳动）](https://console.volcengine.com/ark)       |                      `Doubao-lite-128k`                      | 0.8元/输入，1 元/输出，**赠送至高 5 亿 token**               |
| [火山（字节跳动）](https://console.volcengine.com/ark)       |              `Doubao-pro-4k`，`Doubao-pro-32k`               | 0.8元/输入，2 元/输出，**赠送至高 5 亿 token**               |
| [火山（字节跳动）](https://console.volcengine.com/ark)       |                      `Doubao-pro-128k`                       | 5元/输入，9 元/输出，**赠送至高 5 亿 token**                 |
# 备注

* 飞书的模型名称需要手动进行设置 https://console.volcengine.com/ark
  1. 左侧菜单找到 API KEY 管理, 创建 API KEY
  1. 左侧菜单找到开通管理, 对需要的模型进行开通
  1. 左侧菜单找到模型推理, 针对每个需要的模型创建模型推理接入点
  1. 接入点下方以 ep- 开头的字符串即为模型名称
  1. 在开通管理页面中，可以开通 5 亿免费 token

## TODO

* [ ] 限流、调用失败 Exception 处理
* [ ] FunctionCall 模式调用
* [ ] 智谱 Batch 接口
* [ ] 测试百川接口
* [ ] 多模态模型适配
