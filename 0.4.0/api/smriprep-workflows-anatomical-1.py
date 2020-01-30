from niworkflows.utils.spaces import SpatialReferences, Space
from smriprep.workflows.anatomical import init_anat_preproc_wf
wf = init_anat_preproc_wf(
    bids_root='.',
    freesurfer=True,
    hires=True,
    longitudinal=False,
    num_t1w=1,
    omp_nthreads=1,
    output_dir='.',
    reportlets_dir='.',
    skull_strip_template=Space.from_string('OASIS30ANTs')[0],
    spaces=SpatialReferences(['MNI152NLin2009cAsym', 'fsaverage5']),
)