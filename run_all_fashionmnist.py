import subprocess

alg_choices = ['stocBiO', 'VRBO', 'MRBO', 'STABLE', 'TTSA', 'BSA', 'reverse', 'AID-CG', 'AID-FP', 'MSTSA']

for alg in alg_choices:
    command = f"python fashionmnist_exp.py --alg {alg}"
    subprocess.run(command, shell=True)