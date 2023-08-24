import ast
import numbers
from django.shortcuts import render
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

def index(request):
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
                result=execute.run_python_code(code_path,exe['exp_input'],exe['exp_output'])
                res=f"Output: {result['output']}\nRuntime: {result['runtime']}\nResult: {result['error']}"
                plagiar=plagiarism.check_man_plagiarism(code_path)
                plag=plagiarism.convert_to_line_separated(plagiar)
                print(plag)
                an_sing=str(analysis.analyze_single_file(code_path))
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