import requests
import json
import time
import copy
import enum

# pip install -i https://mirrors.tencent.com/pypi/simple/ --upgrade tencentcloud-sdk-python
from tencentcloud.common import credential
from tencentcloud.common.profile.client_profile import ClientProfile
from tencentcloud.common.profile.http_profile import HttpProfile
from tencentcloud.common.exception.tencent_cloud_sdk_exception import TencentCloudSDKException
from tencentcloud.hunyuan.v20230901 import hunyuan_client, models


class ChatAPI:
    def __init__(self, api_key, secret_key=None, system_prompt="", temperature=0.9, top_p=0.7, penalty_score=1.14, max_tokens=None):
        self.api_key = api_key
        self.secret_key = secret_key
        self.system_prompt = system_prompt
        self.temperature = temperature
        self.top_p = top_p
        self.penalty_score = penalty_score
        self.max_tokens = max_tokens

        self._process_others()

    def _process_others(self):
        raise NotImplementedError
    
    def _get_payload(self, query):
        raise NotImplementedError


class BaiduChatAPI(ChatAPI):
    def _process_others(self):
        self._access_token_created_time = 0
        self._access_token = self.get_access_token()

        # https://console.bce.baidu.com/qianfan/ais/console/onlineService
        self.model_list = {
            "ernie-speed-8k": "https://aip.baidubce.com/rpc/2.0/ai_custom/v1/wenxinworkshop/chat/ernie_speed?access_token=",
            "ernie-speed-128k": "https://aip.baidubce.com/rpc/2.0/ai_custom/v1/wenxinworkshop/chat/ernie-speed-128k?access_token=",
            "ernie-lite-8k-0922": "https://aip.baidubce.com/rpc/2.0/ai_custom/v1/wenxinworkshop/chat/eb-instant?access_token=",
            "ernie-lite-8k-0308": "https://aip.baidubce.com/rpc/2.0/ai_custom/v1/wenxinworkshop/chat/ernie-lite-8k?access_token=",
            "ernie-tiny-8k":"https://aip.baidubce.com/rpc/2.0/ai_custom/v1/wenxinworkshop/chat/ernie-tiny-8k?access_token=",
            "ernie-speed-AppBuilder": "https://aip.baidubce.com/rpc/2.0/ai_custom/v1/wenxinworkshop/chat/ai_apaas?access_token=",
            # "fuyu-8b": "https://aip.baidubce.com/rpc/2.0/ai_custom/v1/wenxinworkshop/image2text/fuyu_8b?access_token=",  # 多模态模型
            "ernie-character-8K": "https://aip.baidubce.com/rpc/2.0/ai_custom/v1/wenxinworkshop/chat/ernie-char-8k",  # 角色模型
            "yi-34b-chat": "https://aip.baidubce.com/rpc/2.0/ai_custom/v1/wenxinworkshop/chat/yi_34b_chat?access_token="
        }
    

    def _get_payload(self, query, history):
        payload = {
            "temperature": self.temperature,
            "top_p": self.top_p,       
            "penalty_score": self.penalty_score,
            "system": self.system_prompt
        }

        history.append({"role": "user", "content": query})
        payload['messages'] = history
        payload = json.dumps(payload)

        return payload


    def _get_access_token(self):
        """
        使用 AK，SK 生成鉴权签名（Access Token）
        :return: access_token，或是None(如果错误)
        """
        url = "https://aip.baidubce.com/oauth/2.0/token"
        params = {"grant_type": "client_credentials", "client_id": self.api_key, "client_secret": self.secret_key}
        return str(requests.post(url, params=params).json().get("access_token"))

    def get_access_token(self):
        if time.time() - self._access_token_created_time > 29 * 24 * 3600:
            self._access_token = self._get_access_token()
            self._access_token_created_time = time.time()
        return self._access_token


    def chat(self, model, query, history=[]):
        assert model in self.model_list, "model should in " + [x for x in self.model_list]
        payload = self._get_payload(query, history)
        headers = { 
            'Content-Type': 'application/json'
        }

        url = self.model_list[model] + self.get_access_token()
        
        now = time.time()
        response = requests.request("POST", url, headers=headers, data=payload)
        response = response.text
        response = json.loads(response)
        time_used = time.time() - now
        response = response['result']
        history.append({"role": "assistant", "content": response})

        return response, history, time_used


class TencentChatAPI(ChatAPI):
    def _process_others(self):
        self.cred = credential.Credential(self.api_key, self.secret_key)

        # 开通参考 https://console.cloud.tencent.com/hunyuan
        # 模型列表参考 https://cloud.tencent.com/document/product/1729/97731
        self.model_list = [
            "hunyuan-lite",
            "hunyuan-standard",
            "hunyuan-standard-256K",
            "hunyuan-pro"
        ]

    def _get_payload(self, model, query, history):
        payload = {
            "Model": model,
            "Temperature": self.temperature,
            "TopP": self.top_p,       
            "penalty_score": self.penalty_score,
            "system": self.system_prompt
        }

        history.append({"Role": "user","Content": query})
        if self.system_prompt:
            history.insert(0, {"Role": "system", "Content": self.system_prompt})
        payload['Messages'] = history
        payload = json.dumps(payload)

        return payload


    def chat(self, model, query, history=[]):
        assert model in self.model_list, "model should in " + [x for x in self.model_list]
        httpProfile = HttpProfile()
        httpProfile.endpoint = "hunyuan.tencentcloudapi.com"


        now = time.time()
        # 实例化一个client选项，可选的，没有特殊需求可以跳过
        clientProfile = ClientProfile()
        clientProfile.httpProfile = httpProfile
        # 实例化要请求产品的client对象,clientProfile是可选的
        client = hunyuan_client.HunyuanClient(self.cred, "", clientProfile)

        req = models.ChatCompletionsRequest()
        req.from_json_string(self._get_payload(model, query, history))
        resp = client.ChatCompletions(req)

        response = resp.Choices[0].Message.Content

        history.append({"Role": "assistant", "Content": response})

        time_used = time.time() - now

        return response, history, time_used


class OpenAIStyleChatAPI(ChatAPI):
    def _process_others(self):
        raise NotImplementedError

    def _get_payload(self, model, query, history):
        payload = {
            "model": model,
            "temperature": self.temperature,
            "top_p": self.top_p,
            "max_tokens": self.max_tokens
        }
        if self.system_prompt:
            history.insert(0, {"role": "system", "content": self.system_prompt})
        history.append({"role": "user", "content": query})
        payload['messages'] = history
        payload = json.dumps(payload)

        return payload

    def chat(self, model, query, history=None):
        assert model in self.model_list, "model should in " + [x for x in self.model_list]
        if not history:
            history = []
        payload = self._get_payload(model, query, history)
        headers = { 
            'Content-Type': 'application/json',
            'Authorization': 'Bearer ' + self.api_key
        }

        now = time.time()
        response = requests.request("POST", self.url, headers=headers, data=payload)
        status = response.status_code
        response = response.text
        response = json.loads(response)
        if status != 200:
            print(response)

        response = response['choices'][0]['message']['content']
        history.append({"role": "assistant", "content": response})

        time_used = time.time() - now

        return response, history, time_used


class ZhiPuChatAPI(OpenAIStyleChatAPI):
    def _process_others(self):
        self.url = "https://open.bigmodel.cn/api/paas/v4/chat/completions"
        
        # https://open.bigmodel.cn/dev/api#
        self.model_list = [
            'glm-3-turbo',
            'glm-4'
        ]
        


class YiChatAPI(OpenAIStyleChatAPI):
    def _process_others(self):
        self.url = "https://api.lingyiwanwu.com/v1/chat/completions"

        # 模型列表参考 https://platform.lingyiwanwu.com/docs#%E5%B9%B3%E5%8F%B0%E4%BC%98%E5%8A%BF
        self.model_list = [
            "yi-spark",
            "yi-large",
            "yi-large-turbo",
            "yi-large-rag",
            "yi-medium",
            "yi-medium-200k",
            # "yi-vision"
        ]


class DeepSeekChatAPI(OpenAIStyleChatAPI):
    def _process_others(self):
        self.url = "https://api.deepseek.com/chat/completions"

        self.model_list = [
            "deepseek-chat"  # 即 deepseek-v2
        ]


class QwenChatAPI(OpenAIStyleChatAPI):
    def _process_others(self):
        self.url = "https://dashscope.aliyuncs.com/compatible-mode/v1/chat/completions"

        # https://help.aliyun.com/zh/dashscope/developer-reference/tongyi-qianwen-7b-14b-72b-metering-and-billing?spm=a2c4g.11186623.0.0.13b6158bklccp4

        self.model_list = [
            "qwen1.5-0.5b-chat",
            "qwen-1.8b-chat",
            "qwen1.5-7b-chat",
            "qwen1.5-14b-chat",
            "qwen1.5-32b-chat",
            "qwen1.5-72b-chat",
            "qwen1.5-110b-chat",
            "qwen-long",
            "qwen-turbo",
            "qwen-plus",
            "qwen-max"
        ]


class MoonshotChatAPI(OpenAIStyleChatAPI):
    def _process_others(self):
        self.url = "https://api.moonshot.cn/v1/chat/completions"

        # https://platform.moonshot.cn/docs/pricing#%E4%BA%A7%E5%93%81%E5%AE%9A%E4%BB%B7
        self.model_list = [
            "moonshot-v1-8k",
            "moonshot-v1-32k",
            "moonshot-v1-128k"
        ]


class BaichuanChatAPI(OpenAIStyleChatAPI):
    def _process_others(self):
        self.url = "https://api.baichuan-ai.com/v1/chat/completions"

        self.model_list = [
            "Baichuan4",
            "Baichuan3-Turbo",
            "Baichuan3-Turbo-128k",
            "Baichuan2-Turbo",
            "Baichuan2-Turbo-192k"
        ]



