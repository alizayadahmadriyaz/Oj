from django.shortcuts import render
from real_compiler.formm import CodeSubmissionForm
import os,uuid
import subprocess
from pathlib import Path
from django.conf import settings
from django.http import HttpResponse

# Create your views here.
def submit(request):
    if request.method=='POST':
        form = CodeSubmissionForm(request.POST)
        if form.is_valid():
            submission=form.save()
            print(submission.language)
            print(submission.code)
            output=run_code(submission.language,submission.input_data,submission.code)
            print("output->      ", output)
            submission.output_data=output
            submission.save()
            context={"submission":submission}
            return render(request,'result.html',context)
    else:
        form = CodeSubmissionForm()
        return render(request,'ind.html',{"form":form})
    

def run_code(language,input_data,code):
    proj_path=Path(settings.BASE_DIR)
    directories=['input','output','code']

    for direc in directories:

        dir_path=proj_path/f"{direc}"
        if not dir_path.exists():
            
            dir_path.mkdir(parents=True, exist_ok=True)

    code_dir=proj_path/"code"
    input_dir=proj_path/"input"
    output_dir=proj_path/"output"
    unique=uuid.uuid4()
    input_file=input_dir/(str(unique)+".txt")
    output_file=output_dir/(str(unique)+".txt")
    code_file=code_dir/(str(unique)+f".{language}")
    
    with open(code_file,'w') as f:
        f.write(code)
    
    with open(input_file,'w') as f:
        f.write(input_data)
    
    if language=="cpp":
        executable_path=code_dir/str(unique)
        
        # compile_res=['clang++',str(code_file_path)]

        res=subprocess.run(["g++",str(code_file),"-o",str(executable_path)])
        if res.returncode==0:
            with open(input_file,'r') as f1:
              with open(output_file,'w') as f2:  
                    subprocess.run(
                      [str(executable_path)],
                      stdin=f1,
                      stdout=f2
                    )

    elif language=="py":
         with open(input_file,'r') as f1:
              with open(output_file,'w') as f2:  
                    subprocess.run(
                      ["python3",str(code_file)],
                      stdin=f1,
                      stdout=f2
                    )
    
    with open(output_file,'r') as f2:  
        output_data=f2.read()
    
    return output_data

