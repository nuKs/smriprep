from collections import OrderedDict
from smriprep.workflows.base import init_single_subject_wf
BIDSLayout = namedtuple('BIDSLayout', ['root'])
wf = init_single_subject_wf(
    debug=False,
    freesurfer=True,
    hires=True,
    layout=BIDSLayout('.', validate=False),
    longitudinal=False,
    low_mem=False,
    name='single_subject_wf',
    omp_nthreads=1,
    output_dir='.',
    output_spaces=OrderedDict([('MNI152NLin2009cAsym', {}),
                               ('fsaverage5', {})]),
    reportlets_dir='.',
    skull_strip_fixed_seed=False,
    skull_strip_template=('OASIS30ANTs', {}),
    subject_id='test',
)