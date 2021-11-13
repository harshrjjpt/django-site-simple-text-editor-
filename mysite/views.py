from django.http import HttpResponse
from django.shortcuts import render


def home_page(request):
	return render(request, "index.html")

def about_us(request):
    return render(request, "about_us.html")


def analyze(request):
    #Get the text
    main_text = request.POST.get('text', 'default')

    # Check checkbox values
    remove_punc = request.POST.get('remove_punc', 'off')
    capitalize = request.POST.get('capitalize', 'off')
    newlineremove = request.POST.get('newlineremove', 'off')
    remove_spaces = request.POST.get('remove_spaces', 'off')
    char_count = request.POST.get('char_count', 'off')

    #Check which checkbox is on
    if remove_punc == "on":
        punctuations = '''!()-[]{};:'"\,<>./?@#$%^&*_~'''
        analyzed = ""
        for char in main_text:
            if char not in punctuations:
                analyzed = analyzed + char
        params = {'purpose':'Removed Punctuations', 'analyzed_text': analyzed}
        answer = render(request, 'analyze.html', params)

    elif(capitalize=="on"):
        analyzed = ""
        for char in main_text:
            analyzed = analyzed + char.upper()

        params = {'purpose': 'Changed to Uppercase', 'analyzed_text': analyzed}
        # Analyze the text
        answer = render(request, 'analyze.html', params)

    elif(remove_spaces=="on"):
        analyzed = ""
        space = " "
        for char in main_text:
            if char not in space:
                analyzed = analyzed + char
        params = {'purpose': 'Removed spaces', 'analyzed_text': analyzed}
        # Analyze the text
        answer = render(request, 'analyze.html', params)

    elif (newlineremove == "on"):
        analyzed = ""
        for char in main_text:
            if char != "\n":
                analyzed = analyzed + char

        params = {'purpose': 'Removed NewLines', 'analyzed_text': analyzed}
        # Analyze the text
        answer = render(request, 'analyze.html', params)

    elif (char_count == "on"):
        space = " "
        y = "".join(main_text)
        if y not in space:
            num = len(y)
        
        params = {'purpose': 'Removed NewLines', 'analyzed_text': num}
        # Analyze the text
        answer = render(request, 'analyze.html', params)    

    return answer           
 