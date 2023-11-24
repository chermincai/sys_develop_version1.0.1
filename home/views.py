# home/views.py
import os
from django.conf import settings
from django.shortcuts import render

def index(request):
    template_path = os.path.join(settings.BASE_DIR,'templates','index.html')
    return render(request, template_path)

def dataset(request):
    template_path = os.path.join(settings.BASE_DIR, 'templates', 'dataset.html')
    return render(request, template_path)


def text_test(request):
    template_path = os.path.join(settings.BASE_DIR, 'templates', 'text-test.html')
    return render(request, template_path)


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

def text_test(request):
    if request.method == 'POST':
        # 获取 POST 请求中的文本内容
        text_input = request.POST.get('TextInput', '')

        # 在这里添加你的文本检测逻辑，获取置信度
        # 这里只是一个示例，你需要根据你的具体需求替换成实际的检测逻辑
        confidence = 0.7  # 这里的值应该根据实际情况获取

        # 分类文本类别和对应颜色
        result_class, result_color = classify_text(confidence)

        # 返回 JSON 格式的结果
        return JsonResponse({'confidence': confidence, 'result_class': result_class, 'result_color': result_color})

    # 如果不是 POST 请求，直接渲染页面
    return render(request, 'index.html')