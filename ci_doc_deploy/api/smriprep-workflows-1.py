from collections import OrderedDict
from smriprep.workflows.anatomical import init_anat_preproc_wf
wf = init_anat_preproc_wf(
    bids_root='.',
    freesurfer=True,
    hires=True,
    longitudinal=False,
    num_t1w=1,
    omp_nthreads=1,
    output_dir='.',
    output_spaces=OrderedDict([
        ('MNI152NLin2009cAsym', {}), ('fsaverage5', {})]),
    reportlets_dir='.',
    skull_strip_template=('MNI152NLin2009cAsym', {}),
)