import os
from io import BytesIO
from django.conf import settings
from django.shortcuts import render
from django.http import JsonResponse
import opennsfw2 as n2

# Create your views here.

def porn_detection(request):
    template_path = os.path.join(settings.BASE_DIR, 'tool_box/templates', 'porn_detection.html')
    if request.method == 'POST' and request.FILES.get('image'):
        # 获取上传的图像文件
        image = request.FILES['image']

        # 预测图像的分数
        image_data = image.read()  # 读取图像文件的二进制数据
        image_stream = BytesIO(image_data)  # 使用 BytesIO 创建二进制流对象
        nsfw_probability = n2.predict_image(image_stream)
        # 把分数保留小数点后四位数
        nsfw_probability = round(nsfw_probability, 4)

        # 根据分数，判断图像的分类
        if nsfw_probability > 0.9:
            category = '此图片为色情内容'
        elif nsfw_probability > 0.4:
            category = '此图片疑似色情内容'
        else:
            category = '此图片非色情内容'

        # 返回 JSON 响应
        return JsonResponse({
            'confidence': nsfw_probability,
            'category': category
        })
    return render(request,template_path)
