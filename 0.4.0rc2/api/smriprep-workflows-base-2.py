import os
from collections import OrderedDict, namedtuple
BIDSLayout = namedtuple('BIDSLayout', ['root'])
os.environ['FREESURFER_HOME'] = os.getcwd()
from smriprep.workflows.base import init_smriprep_wf
wf = init_smriprep_wf(
    debug=False,
    freesurfer=True,
    fs_subjects_dir=None,
    hires=True,
    layout=BIDSLayout('.'),
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