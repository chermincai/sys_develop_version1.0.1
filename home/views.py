# home/views.py
import os
from django.conf import settings
from django.http import JsonResponse
from django.shortcuts import render
import torch
from transformers import AutoTokenizer, AutoModel

# 载入模型和分词器
tokenizer = AutoTokenizer.from_pretrained("THUDM/chatglm3-6b", trust_remote_code=True)
model = AutoModel.from_pretrained("THUDM/chatglm3-6b", trust_remote_code=True).quantize(4).cuda()
model = model.eval()

def index(request):
    template_path = os.path.join(settings.BASE_DIR, 'templates', 'index.html')
    return render(request, template_path)

def dataset(request):
    template_path = os.path.join(settings.BASE_DIR, 'templates', 'dataset.html')
    return render(request, template_path)


def tool_box(request):
    template_path = os.path.join(settings.BASE_DIR, 'templates', 'tool-box.html')
    return render(request, template_path)

def text_test(request):
    template_path = os.path.join(settings.BASE_DIR, 'templates', 'text-test.html')
    if request.method == 'POST':
        user_input = request.POST.get('user_input', '')
        model_input = "我将输入一些内容，你来判别它们是否是不良的，如果是，请分析它的类别同时给出判断的置信度，以百分数的形式展示，不要重复需判断文本的内容，。你对输入文本的分类将在涉政敏感类，暴力恐怖类，宗教迷信类，色情类，仇恨谩骂类，诈骗类，赌博类，涉毒类，不良广告类，自残自杀类，校园霸凌类，负面社会民生类这十二类里产生。你只需要说出文本类别和置信度，其他无关文本不用说出。需判断的文本的内容是：" + user_input

        # 检查用户是否想要退出
        if user_input.lower() == 'exit':
            return JsonResponse({'response': '退出文本检测。'})



        # 文本检测逻辑
        response, history = model.chat(tokenizer, model_input, history=[])

        # 更新历史记录
        history.append(user_input)

        return render(request, template_path, {'model_output': response})

    return render(request,template_path)



def img_test(request):
    template_path = os.path.join(settings.BASE_DIR, 'templates', 'img-test.html')
    return render(request, template_path)
def short_video_test(request):
    template_path = os.path.join(settings.BASE_DIR, 'templates', 'short_video-test(3).html')
    return render(request, template_path)
def long_video_test(request):
    template_path = os.path.join(settings.BASE_DIR, 'templates', 'long_video-test(1).html')
    return render(request, template_path)

def classify_text(confidence):
    if confidence > 0.85:
        return "涉政敏感类", "red"
    elif confidence > 0.65:
        return "涉政敏感类", "orange"
    elif confidence > 0.55:
        return "涉政敏感类", "lightorange"
    else:
        return "正常", "black"

# def text_test(request):
#     if request.method == 'POST':
#         # 获取 POST 请求中的文本内容
#         text_input = request.POST.get('TextInput', '')
#
#         # 在这里添加你的文本检测逻辑，获取置信度
#         # 这里只是一个示例，你需要根据你的具体需求替换成实际的检测逻辑
#         confidence = 0.7  # 这里的值应该根据实际情况获取
#
#         # 分类文本类别和对应颜色
#         result_class, result_color = classify_text(confidence)
#
#         # 返回 JSON 格式的结果
#         return JsonResponse({'confidence': confidence, 'result_class': result_class, 'result_color': result_color})
#
#     # 如果不是 POST 请求，直接渲染页面
#     return render(request, 'index.html')