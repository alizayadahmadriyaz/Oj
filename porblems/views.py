from django.shortcuts import render
from porblems.models import problemm,Test_Case
from django.shortcuts import render,redirect
from django.contrib.auth.decorators import login_required
from real_compiler.formm import CodeSubmissionForm
from real_compiler.views import run_code
from real_compiler.models import CodeSubmission
# Create your views here.
@ login_required
def all_problems(request):
    all_problemm=problemm.objects.all()
    context={
        "all_problemm":all_problemm,
    }

    return render(request, 'problemm.html', context)

# @login_required
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from real_compiler.formm import CodeSubmissionForm
from porblems.models import problemm, Test_Case, solution
import subprocess
import uuid
from pathlib import Path
from django.conf import settings

@login_required
def problems_description(request, id):
    problem = problemm.objects.get(id=id)
    form = CodeSubmissionForm()

    if request.method == 'POST':
        form = CodeSubmissionForm(request.POST)
        if form.is_valid():
            submission = form.save(commit=False)
            submission.problem = problem  # Associate the submission with the problem
            submission.save()
            
            # Run code against all test cases
            test_cases = Test_Case.objects.filter(problem=problem)
            results = []
            for test_case in test_cases:
                output = run_code(submission.language, test_case.Input, submission.code)
                verdict = "Accepted" if output == test_case.Output else "Wrong Answer"
                results.append({
                    'input': test_case.Input,
                    'expected_output': test_case.Output,
                    'actual_output': output,
                    'verdict': verdict
                })

            # Save results or handle them as needed
            submission.output_data = results  # Save results for rendering or further processing
            submission.save()

            context = {
                "problem": problem,
                "form": form,
                "submission": submission,
                "results": results
            }
            return render(request, 'problem.html', context)

    # GET request
    context = {
        "problem": problem,
        "form": form,
    }
    return render(request, 'problem.html', context)







