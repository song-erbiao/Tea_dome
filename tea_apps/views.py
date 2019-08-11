from django.shortcuts import render


def Index(request):
    """
    首页
    :param request:
    :return:
    """
    return render(request,'index/index.html')

def Register(request):
    """
    注册
    :param request:
    :return:
    """

    return render(request,'index/registered.htm')

def Login(request):
    """
    登陆
    :param request:
    :return:
    """
    return render(request,'index/login.htm')

def User_info(request):
    """
    用户中心
    :param request:
    :return:
    """
    return render(request,'user/user_info.html')

def Uinfo(request):
    """
    个人信息
    :param request:
    :return:
    """
    return render(request,'user/userinfo.html')