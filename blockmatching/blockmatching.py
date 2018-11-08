from nipype.interfaces.base import (
    TraitedSpec,
    CommandLineInputSpec,
    CommandLine,
    File,
    traits,
)


class BlockmatchingInputSpec(CommandLineInputSpec):

    reference = File(
        exists=True,
        desc='Reference image',
        argstr='-reference %s',
        mandatory=True,
    )

    floating = File(
        exists=True,
        desc='Floating image',
        argstr='-floating %s',
        mandatory=True,
    )

    result = File(
        exists=False,
        desc='Resampled image',
        argstr='-result %s',
        mandatory=False,
    )

    result_trsf = File(
        exists=False,
        desc='Result transform',
        argstr='-result-transformation %s',
        mandatory=False,
    )

    initial_trsf = File(
        exists=False,
        desc='Initial transform',
        argstr='-initial-transformation %s',
        mandatory=False,
    )

    trsf_type = traits.Enum(
        'translation2D',
        'translation3D',
        'translation-scaling2D',
        'translation-scaling3D',
        'rigid2D',
        'rigid3D',
        'rigid',
        'similitude2D',
        'similitude3D',
        'similitude',
        'affine2D',
        'affine3D',
        'affine',
        'vectorfield2D',
        'vectorfield3D',
        'vectorfield',
        'vector',
        desc='Transformation type',
        argstr='-transformation-type %s',
    )

    pyramid_lowest = traits.Int(
        0,  # original dimension
        desc="Pyramid lowest level",
        argstr='-pyramid-lowest-level %d',
    )

    pyramid_highest = traits.Int(
        3,
        desc="Pyramid highest level",
        argstr='-pyramid-highest-level %d',
    )

    pyramid_gaussian_filtering = traits.Bool(
        desc='Gaussian smoothing before subsampling',
        argstr='-pyramid-gaussian-filtering',
        usedefault=True,
    )



class BlockmatchingOutputSpec(TraitedSpec):
    out_file = File(desc='Output image')



class Blockmatching(CommandLine):
    input_spec = BlockmatchingInputSpec
    output_spec = BlockmatchingOutputSpec
    _cmd = 'blockmatching'

    def _list_outputs(self):
        outputs = self.output_spec().get()
        return outputs
