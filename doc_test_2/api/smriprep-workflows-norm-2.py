from smriprep.workflows.norm import init_anat_norm_wf
wf = init_anat_norm_wf(
    debug=False,
    omp_nthreads=1,
    reportlets_dir='.',
    template_list=['MNI152NLin2009cAsym', 'MNI152NLin6Asym'],
)