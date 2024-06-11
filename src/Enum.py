from enum import Enum

class APIKEY:
    """
    对应平台的 API_KEY （百度和腾讯需要对应的 SECRET_KEY）设置
    请移步到各平台进行申请，获取 API_KEY 和 SECRET_KEY
    【请管理好，避免泄露】
    """

    # 百度 KEY 获取文档 https://cloud.baidu.com/doc/Reference/s/9jwvz2egb
    BAIDU_API_KEY = None
    BAIDU_SECRET_KEY = None

    TENCENT_SECRET_ID = None
    TENCENT_SECRET_KEY = None

    ZHIPU_API_KEY = None

    YI_API_KEY = None

    DEEPSEEK_API_KEY = None

    QWEN_API_KEY = None

    MOONSHOT_API_KEY = None

    LARK_API_KEY = None



class MODEL:
    class BAIDU:
        ERNIE_SPEED_8K = "ernie-speed-8k"
        ERNIE_SPEED_128K = "ernie-speed-128k"
        ERNIE_LITE_8K_0922 = "ernie-lite-8k-0922"
        ERNIE_LITE_8K_0308 = "ernie-lite-8k-0308"
        ERNIE_TINY_8K = "ernie-tiny-8k"
        ERNIE_SPEED_APPBUILDER = "ernie-speed-AppBuilder"
        FUYU_8B = "fuyu-8b"
        YI_34B_CHAT = "yi-34b-chat"
        ERNIE_CHARACTER_8K = "ernie-character-8K"
    
    class TENCENT:
        HUNYUAN_LITE = "hunyuan-lite"
        HUNYUAN_STANDARD = "hunyuan-standard"
        HUNYUAN_STANDARD_256K = "hunyuan-standard-256K"
        HUNYUAN_PRO = "hunyuan-pro"
    
    class ZHIPU:
        GLM_3_TURBO = "glm-3-turbo"
        GLM_4 = "glm-4"
    
    class YI:
        YI_SPARK = "yi-spark"
        YI_LARGE = "yi-large"
        YI_LARGE_TURBO = "yi-large-turbo"
        YI_LARGE_RAG = "yi-large-rag"
        YI_MEDIUM = "yi-medium"
        YI_MEDIUM_200K = "yi-medium-200k"
        YI_VISION = "yi-vision"
    
    class DEEPSEEK:
        DEEPSEEK_CHAT = "deepseek-chat"
    
    class QWEN:
        QWEN1_5_0_5B_CHAT = "qwen1.5-0.5b-chat"
        QWEN_1_8B_CHAT = "qwen-1.8b-chat"
        QWEN1_5_14B_CHAT = "qwen1.5-14b-chat"
        QWEN1_5_32B_CHAT = "qwen1.5-32b-chat"
        QWEN1_5_72B_CHAT = "qwen1.5-72b-chat"
        QWEN1_5_110B_CHAT = "qwen1.5-110b-chat"
        QWEN_LONG = "qwen-long"
        QWEN_TURBO = "qwen-turbo"
        QWEN_PLUS = "qwen-plus"
        QWEN_MAX = "qwen-max"
    
    class MOONSHOT:
        MOONSHOT_V1_8K = "moonshot-v1-8k"
        MOONSHOT_V1_32K = "moonshot-v1-32k"
        MOONSHOT_V1_128K = "moonshot-v1-128k"
    
    class BAICHUAN:
        BAICHUAN4 = "Baichuan4"
        BAICHUAN3_TURBO = "Baichuan3-Turbo"
        BAICHUAN3_TURBO_128K = "Baichuan3-Turbo-128k"
        BAICHUAN2_TURBO = "Baichuan2-Turbo"
        BAICHUAN2_TURBO_192K = "Baichuan2-Turbo-192k"