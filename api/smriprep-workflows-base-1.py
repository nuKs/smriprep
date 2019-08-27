import os
from collections import OrderedDict
from pybids import BIDSLayout
os.environ['FREESURFER_HOME'] = os.getcwd()
from smriprep.workflows.base import init_smriprep_wf
wf = init_smriprep_wf(
    debug=False,
    freesurfer=True,
    hires=True,
    layout=BIDSLayout('.', validate=False),
    longitudinal=False,
    low_mem=False,
    omp_nthreads=1,
    output_dir='.',
    output_spaces=OrderedDict([('MNI152NLin2009cAsym', {}),
                               ('fsaverage5', {})]),
    run_uuid='testrun',
    skull_strip_fixed_seed=False,
    skull_strip_template=('OASIS30ANTs', {}),
    subject_list=['smripreptest'],
    work_dir='.',
)