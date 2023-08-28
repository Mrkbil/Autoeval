import ast
import numbers
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.models import User
from django.shortcuts import render, redirect
from django.http import HttpResponse
import os
from django.shortcuts import render
from .functions.metadata import *
from .functions import zipextract
from .functions import file
from .functions import manual_check
from .functions import execute
from .functions import plagiarism
from .functions import automatic_eval
from .functions import check
from .functions import analysis
from .Controller import plagiarismX
from .Controller import manualevalX
from .Controller import analysisX
from .Controller import fileX
from .Controller import exeX
from .Controller import plagfileX
from .Controller import formatX
from .Controller import EditorX

def login_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('homepage')
        else:
            error_message = "Invalid username or password."
            return render(request, 'login.html', {'error_message': error_message})
    return render(request, 'login.html')

def register_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        email = request.POST['email']
        password1 = request.POST['password1']
        password2 = request.POST['password2']

        if password1 != password2:
            error_message = "Passwords do not match."
            return render(request, 'register.html', {'error_message': error_message})

        try:
            User.objects.get(username=username)
            error_message = "Username already exists."
            return render(request, 'register.html', {'error_message': error_message})
        except User.DoesNotExist:
            user = User.objects.create_user(username=username, password=password1, email=email, first_name=first_name, last_name=last_name)
            login(request, user)
            return redirect('index')

    return render(request, 'register.html')

def logout_view(request):
    logout(request)
    return redirect('login')

def index(request):
    return render(request, 'index.html')

@login_required()
def homepage_view(request):
    if request.user.is_authenticated:
        first_name = request.user.first_name
        last_name = request.user.last_name
    else:
        redirect('login')

    name=f", {first_name} {last_name}"

    return render(request, 'homepage.html', { 'username': name})


def automatic_eval_view(request):
    return render(request,'automatic.html')


@login_required()
def manual_evaluation_view(request):
    if request.method == 'POST':
        code_file = request.FILES.get('codeFile',None)
        code = request.POST.get('code',None)
        evaluation_function = request.POST.get('evaluationFunction',None)
        test_cases_file = request.FILES.get('testCasesFile',None)
        if code_file:
            manualevalX.save_uploaded_file(code_file,'code.py')
        else:
            if code:
                manualevalX.save_string_as_py_file(code)
            else:
                manualevalX.save_string_as_py_file("None")

        if evaluation_function:
            manualevalX.save_string_as_py_file(evaluation_function,'evaluation.py')

        if test_cases_file:
            manualevalX.save_uploaded_file(test_cases_file,'TestCase.txt')

        if evaluation_function:
            result= manualevalX.evaulate_func()
        else:
            result=[]
            cases,inp,out=manualevalX.read_test_cases()
            for i in range(cases):
                res=manualevalX.run_python_code(input_text=inp[i],expected_output=out[i])
                result.append(res)
        format_res=manualevalX.format_test_cases(result)
        context = {'formatted_test_cases': format_res}
        return render(request, 'Evaluation.html', context)
    return render(request,'Evaluation.html')


@login_required()
def plagiarism_view(request):
    if request.method == 'POST':
        code = request.POST.get('code', None)
        code_file = request.FILES.get('codeFile', None)
        code_zip = request.FILES.get('codeZip', None)
        code_file_path = request.POST.get('codeFilePath', None)

        if code_zip:
            plagiarismX.unzip_uploaded_zip(code_zip)
        if code_file:
            plagiarismX.save_uploaded_file(code_file)
        else:
            if code:
                plagiarismX.save_string_as_py_file(code)
            else:
                plagiarismX.save_string_as_py_file("None")

        try:
            c1 = plagiarismX.read_file()
            print(c1)
            if code_file_path:
                result=plagiarismX.check_plagiarism(c1,code_file_path)
            else:
                result=plagiarismX.check_plagiarism(c1)

            res=plagiarismX.format_results(result)
            context = {'results':res}
            return render(request, 'plagiarism.html', context)
        except:
            return render(request,'plagiarism.html')

    return render(request,'plagiarism.html')


@login_required()
def analysis_view(request):
    if request.method == 'POST':
        code = request.POST.get('code', None)
        code_file = request.FILES.get('codeFile', None)
        if code_file:
            analysisX.save_uploaded_file(code_file)
        else:
            if code:
                analysisX.save_string_as_py_file(code)
            else:
                analysisX.save_string_as_py_file("None")
        code_content=analysisX.read_file()
        result=analysisX.analyze_code(code_content)
        formated_res=analysisX.format_analysis_result(result)
        print(formated_res)
        context={'result':formated_res}
        return render(request,'analysis.html',context)
    return render(request,'analysis.html')


def editor_view(request):
    filelist=EditorX.get_all_file_names()
    context={'codelist':filelist}
    item_name = request.GET.get('item_name', None)
    action = request.GET.get('action')
    if item_name is not None:
        code=EditorX.getcode(item_name)
        context ={ 'codelist':filelist,'code': code}
        return render(request, 'Editor.html',context)

    if (action == 'run'):
        codes=EditorX.get_all_file_paths()
        if(EditorX.check_eval()):
            pass
        else:
            cases, inp, out = EditorX.read_test_cases()
            result = []
            cases, inp, out = EditorX.read_test_cases()
            for code in codes:
                res = manualevalX.run_python_code(filename=codes[1],input_text=inp[0], expected_output=out[0])
                result.append(res)
            context['info']=result
            return render(request, 'Editor.html',context)
        if(EditorX.check_plagpath()):
            pass
        else:
            pass


    return render(request, 'Editor.html',context)

def file_view(request):
    if request.method == 'POST':
        uploaded_file = request.FILES.get('selectedFile')
        if uploaded_file:
            fileX.unzip_uploaded_zip(uploaded_file)
            context={'filename':  f'{uploaded_file.name} is Uploaded Successfully.'}
            return render(request, 'file.html',context)
    return render(request, 'file.html')

def exe_view(request):
    if request.method == 'POST':
        evaluation_function = request.POST.get('evaluationFunction',None)
        test_cases_file = request.FILES.get('testCasesFile',None)
        if evaluation_function:
            exeX.save_string_as_py_file(evaluation_function)
            return render(request, 'exe.html', {'context': 'Evaluation Code is Uploaded Successfully'})
        if test_cases_file:
            exeX.delete_file()
            exeX.save_uploaded_file(test_cases_file, 'TestCase.txt')
            return render(request,'exe.html',{'context' : 'Test Case is Uploaded Successfully' })
    return render(request, 'exe.html')

def format_view(request):
    # np = ast.literal_eval(nf['cnf'])
    if request.method == 'POST':
        code_name_format = request.POST.get('cnf')
        if code_name_format:
            formatX.save_string_to_txt_file(code_name_format)
            return render(request, 'exe.html', {'context': f'{code_name_format} RegX set Successfully'})
    return render(request, 'format.html')

def plagfile_view(request):
    if request.method == 'POST':
        zip_file = request.FILES.get('zipFileInput')
        directory_path = request.POST.get('directoryPathInput',None)
        if zip_file:
            plagfileX.unzip_uploaded_zip(zip_file)
            render(request, 'plagfile.html', {'context': f" {zip_file.name} is set for additional Plagiarism Check."})
        if directory_path:
            plagfileX.delete_directory()
            plagfileX.save_string_to_txt_file(directory_path)
            return render(request, 'plagfile.html',{'context': f" {directory_path} is set for additional Plagiarism Check."})

    return render(request, 'plagfile.html')

def dashboard_view(request):
    try:
        fp=load_dict_from_json('filepath.json')
        nf=load_dict_from_json('name_format.json')
        exe=load_dict_from_json('execution.json')
        action = request.GET.get('action')
        extrac_loc = zipextract.extract_archive_file(fp['filename'])
        code_list = file.get_filenames_in_directory(extrac_loc)
        filename = os.path.basename(fp['filename'])
        if(action=='run'):
            files_loc = os.path.splitext(fp['filename'])[0]
            auto_eval=automatic_eval.run_file_list(files_loc,'py',exe['exp_input'],exe['exp_output'])
            auto_eval_res=automatic_eval.format_output_to_string(auto_eval)
            print(auto_eval_res)
            print(files_loc)
            pl=plagiarism.check_plagiarism_all(files_loc)
            all_plag=plagiarism.format_results(pl)
            np = ast.literal_eval(nf['cnf'])
            print(np)
            worng=check.check_filenames_in_directory(files_loc,name_pattern=np,valid_extension='py')
            worng=str(worng)+ ' Files with wrong Submission Format'
            an=analysis.analyze_files_in_directory(files_loc)
            anal=str(analysis.format_results(an))
            print(anal)
        if (nf['file_type'] == 'code'):
            extrac_loc=zipextract.extract_archive_file(fp['filename'])
            code_list=file.get_filenames_in_directory(extrac_loc)
            item_name = request.GET.get('item_name', None)
            if(item_name is not None):
                code_path=extrac_loc+'/'+item_name
                code = manual_check.mannual_eval(code_path)
                annna=analysisX.analyze_code(code)
                aaaa=analysisX.format_analysis_result(annna)
                result=execute.run_python_code(code_path,exe['exp_input'],exe['exp_output'])
                res=f"Output: {result['output']}\nRuntime: {result['runtime']}\nResult: {result['error']}"
                plagiar=plagiarism.check_man_plagiarism(code_path)
                plag=plagiarism.convert_to_line_separated(plagiar)
                print(plag)
                an_sing=str(analysis.analyze_single_file(code_path))
                an_sing=aaaa
                return render(request,'Dashboard.html',{'items': code_list,'code':code,'item_name':item_name,'output':res,'plag':plag,'zipname':filename,'des':an_sing})
            return render(request, 'Dashboard.html', {'items': code_list,'code':auto_eval_res,'zipname':filename,'plag':all_plag,'output':worng,'des':anal})
        else:
            pass
    except:
        pass
    return render(request,'Dashboard.html',{'items': code_list,'zipname':filename})
    #return HttpResponse('<h1>This is index page</h1>')

# def file_path_view(request):
#     return render(request, 'file_path.html')


def file_path_view(request):
    if request.method == 'POST':
        selected_file = request.FILES.get('selectedFile')
        if selected_file:
            print(selected_file.name)
            # return HttpResponse(f'<h1>{selected_file.name}</h1>')
            save_path = 'G:/Autoeval/sadlab/mainapp/Zips/' + selected_file.name
            with open(save_path, 'wb') as destination:
                for chunk in selected_file.chunks():
                    destination.write(chunk)
            save_dict_to_json({'filename':f'G:/Autoeval/sadlab/mainapp/Zips/{selected_file.name}'},'filepath.json')
            return render(request, 'file_path.html', {'filename': selected_file.name + " is Uploaded."})

    return render(request, 'file_path.html')


def execution_view(request):
    if request.method == 'POST':
        exp_input = request.POST.get('input_data', '')
        exp_output = request.POST.get('output_data', '')
        parallel_check = request.POST.get('parallel_check', False)
        code_to_check = request.POST.get('code_to_check', '')
        data_dict = {
            'exp_input': exp_input,
            'exp_output': exp_output,
            'parallel_check': parallel_check,
            'code_to_check': code_to_check,
        }
        save_dict_to_json(data_dict, 'execution.json')
        context = {
            'exp_input': " Expected Input: "+exp_input,
            'exp_output': " Expected Output: "+ exp_output,
            'parallel_check': " Parallel Check : "+ str(parallel_check),
            'code_to_check': " Parallel Check Function: "+code_to_check,
        }
        return render(request, 'execution.html',{'exe':context,'status':'Saved'})
    else:
        return render(request, 'execution.html')

def name_format_view(request):
    if request.method == 'POST':
        file_type = request.POST.get('fileType')
        language = request.POST.get('language')
        znf = request.POST.get('znf')
        cnf = request.POST.get('cnf')
        data_dict = {
            'file_type': file_type,
            'language': language,
            'znf': znf,
            'cnf': cnf,
        }
        save_dict_to_json(data_dict,'name_format.json')
        return render(request, 'name_format.html',{'file_type':f'File Type : {file_type}','language':f'Language : {language}','znf':f' Zip File format : {znf}','cnf':f'Code file Format : {cnf}','isSelected': 'Selected'})
    return render(request,'name_format.html')

# def dashboard(request):
#     return render(request,'Dashboard.html')
#
# def execute_function(request):
#     text_to_display = "Hello, this text is displayed by the execute_function!"
#     return render(request, 'home.html', {'t': text_to_display})
#
# def fileup(request):
#     filelist=get_item_paths_in_directory('C:/')
#     return render(request,'Dashboard.html',{'filepath':'text'})