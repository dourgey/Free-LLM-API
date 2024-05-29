from src import *


if __name__ == '__main__':
    # chatbot = BaiduChatAPI(APIKEY.BAIDU_API_KEY, APIKEY.BAIDU_SECRET_KEY)
    # model = MODEL.BAIDU.ERNIE_SPEED_8K

    # chatbot = TencentChatAPI(APIKEY.TENCENT_SECRET_ID, APIKEY.TENCENT_SECRET_KEY)
    # model = MODEL.TENCENT.HUNYUAN_LITE

    # chatbot = ZhiPuChatAPI(APIKEY.ZHIPU_API_KEY)
    # model = MODEL.ZHIPU.GLM_3_TURBO

    # chatbot = YiChatAPI(APIKEY.YI_API_KEY)
    # model = MODEL.YI.YI_SPARK

    # chatbot = DeepSeekChatAPI(APIKEY.DEEPSEEK_API_KEY)
    # model = MODEL.DEEPSEEK.DEEPSEEK_CHAT

    # chatbot = QwenChatAPI(APIKEY.QWEN_API_KEY)
    # model = MODEL.QWEN.QWEN1_5_0_5B_CHAT

    chatbot = MoonshotChatAPI(APIKEY.MOONSHOT_API_KEY)
    model = MODEL.MOONSHOT.MOONSHOT_V1_8K

    query = [
        '爷爷和奶奶可以结婚吗',
        '电脑桌面上有10个文件，我关闭了其中两个，请问桌面上还剩下几个文件',
        '陨石为什么每次都能精准砸到陨石坑？',
        '不孕不育会遗传吗？',
        '用数据线传输电脑和手机文件，同时两头拔掉，文件可以保存在数据线中吗？'
    ]
    for q in query:
        print(f"\033[31m问题：{q}\033[0m")
        response, _, time_used = chatbot.chat(model, q, [])
        print(f"\033[33m{model}（用时 {time_used} s）: \033[0m{response}")
    