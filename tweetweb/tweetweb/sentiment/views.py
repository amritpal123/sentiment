from django.shortcuts import render,redirect

from .extract import extraction,extractTweets

from .labeling import sentiMent

from .sentipie import sentiFig

from .volumes import volumeChart

from .wordc import makeWordCloud


from .retweetana import reTweetData


from django.contrib.auth.forms import UserCreationForm

from django.contrib.auth import login,logout,authenticate

from .signupform import SignUpForm

from django.contrib import  messages


def home(request):

    return render(request,"sentiment/backuphome.html")

def signup(request):

    if request.method=="POST":

        form=SignUpForm(request.POST)

        if form.is_valid():
            user=form.save()
            '''
            user = form.save()
            user.refresh_from_db()  # load the profile instance created by the signal
            user.profile.birth_date = form.cleaned_data.get('birth_date')
            user.save()
            '''
            login(request,user)
            messages.success(request,"Successfully Sign up")
            return redirect("/sentiment")
        else:
            print('error')

            for msg in form.error_messages:
                messages.error(request,f'{form.error_messages[msg]}')


    form =SignUpForm()
    return render(request,'sentiment/signup.html',context={'form':form})


user=None


def index(request):

    global user

    try:
        username=request.POST.get('username')
        password=request.POST.get('password')

        user = authenticate(username=username, password=password)

    except:
        pass

    if user is not None:
        login(request,user)
        df_dic=extraction()

        print(df_dic)

        topic=list(df_dic.keys())

        for i in range(len(topic)):
            if topic[i][0]=='#':
                topic[i]=topic[i][1:]

        volumes=list(df_dic.values())

        mylist = zip(topic, volumes)

        params = {
                'mylist': mylist,
                'user':user
            }

        img=volumeChart(df_dic)

        return render(request,'sentiment/index.html',params)
    else:
        print('error')

        # for msg in form.error_messages:
        #     messages.error(request,f'{form.error_messages[msg]}')



def logout_request(request):

    global user

    logout(request)
    user=None
    return redirect("/sentiment")

def analize(request,i):
    print(i)

    df=extractTweets(i,100)
    print(len(df))
    df=sentiMent(df)
    img=sentiFig(df)
    img2=makeWordCloud(df)

    reTweetDic=reTweetData(df)

    data={'retweet':reTweetDic}

    return render(request,'sentiment/analize.html',data)

def analizekey(request):

    i=request.GET.get('keyword')
    print(i)
    df=extractTweets(i,100)
    print(len(df))
    df=sentiMent(df)
    img=sentiFig(df)

    img2=makeWordCloud(df)


    reTweetDic=reTweetData(df)

    data={'retweet':reTweetDic}

    return render(request,'sentiment/analize.html',data)


