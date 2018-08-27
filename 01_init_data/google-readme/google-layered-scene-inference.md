
# Layer-structured 3D Scene Inference via View Synthesis

This code accompanies the paper 

Layer-structured 3D Scene Inference via View Synthesis\
Shubham Tulsiani, Richard Tucker, Noah Snavely\
In ECCV, 2018.

*Please note that this is not an officially supported Google product.*

[Project Page](https://shubhtuls.github.io/lsi/)

This is the initial release of the Layered Scene Inference TensorFlow code for learning to infer layered depth images (LDIs) from single input views via multi-view supervision.

<img src="https://shubhtuls.github.io/lsi/resources/images/teaser.png" width="60%">

## Training and Evaluating
You'll first need to follow the [installation instructions](docs/installation.md). To subsequently train and evaluate the LDI prediction models, see the documentation for running experiments using the [Synthetic](docs/synth.md) or [KITTI](docs/kitti.md) datasets.

### Citation
If you use this code for your research, please consider citing:
```
@inProceedings{lsiTulsiani18,
  title={Layer-structured 3D Scene Inference via View Synthesis},
  author = {Shubham Tulsiani
  and Richard Tucker
  and Noah Snavely},
  booktitle={ECCV},
  year={2018}
}
```
