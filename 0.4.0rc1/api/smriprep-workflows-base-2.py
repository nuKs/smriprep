import os
from collections import namedtuple
BIDSLayout = namedtuple('BIDSLayout', ['root'])
os.environ['FREESURFER_HOME'] = os.getcwd()
from smriprep.workflows.base import init_smriprep_wf
from niworkflows.utils.spaces import SpatialReferences, Space
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
    run_uuid='testrun',
    skull_strip_fixed_seed=False,
    skull_strip_template=Space.from_string('OASIS30ANTs')[0],
    spaces=SpatialReferences(['MNI152NLin2009cAsym', 'fsaverage5']),
    subject_list=['smripreptest'],
    work_dir='.',
)