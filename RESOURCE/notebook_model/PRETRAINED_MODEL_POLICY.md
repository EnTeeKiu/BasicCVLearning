# Pretrained Model and Architecture Policy

The learner is preparing for competitions whose imports are restricted by `RESOURCE/library.png`. Notebook design must therefore distinguish three separate questions:

1. **Library availability:** Is the package that defines the model allowed by `library.png`?
2. **Checkpoint availability:** Is a compatible pretrained checkpoint already cached, attached as competition data, or legally downloadable before the run?
3. **Competition legality:** Do the specific competition rules permit external/pretrained weights and the checkpoint's training data?

A model is usable only when all applicable answers are yes. An allowlisted Python package does not automatically make a remotely hosted checkpoint available or competition-legal.

## Required Selection Order

Before asking the learner to write a neural-network architecture from scratch:

1. Inspect the current official model catalogs of the allowlisted libraries and the locally installed versions.
2. Prefer an exact task/model implementation from an allowed library.
3. Prefer its official pretrained weights when the checkpoint is permitted and available locally. Do not make a notebook silently depend on a network download.
4. If weights are unavailable, use the official library architecture with `weights=None` (and disable pretrained backbone weights as needed) so the API and model boundary remain competition-relevant.
5. Implement an architecture manually only when its internals are the explicit lesson objective (for example, U-Net architecture), or when no allowed library provides a suitable implementation.

When a checkpoint is optional, expose that choice explicitly (for example, `use_pretrained=False`) and explain that `weights=...DEFAULT` can download files. For an offline competition, pre-cache or attach the permitted checkpoint rather than downloading during notebook execution.

## Substitution Rules

- Never present a related architecture as the exact requested model. State both the unavailable model and the chosen substitute.
- Choose substitutes by task and modeling behavior, not name similarity.
- Preserve the requested model's conceptual material even when executable practice uses a substitute.
- Explain any important semantic difference affecting data targets, loss, post-processing, or evaluation.

Current CV examples under the allowlist:

| Requested topic | Exact allowed implementation | Useful allowed alternatives |
|---|---|---|
| YOLO detection | None in the current allowlist | Torchvision FCOS (one-stage, anchor-free), RetinaNet, SSD/SSDLite, or Faster R-CNN |
| SSD | `torchvision.models.detection.ssd300_vgg16` and SSDLite builders | FCOS or RetinaNet for other one-stage baselines |
| DETR | Hugging Face `transformers` DETR models/checkpoints | Torchvision detectors when Transformer checkpoints are unavailable |
| U-Net | None in Torchvision | Teach U-Net manually when architecture is the objective; for competition baselines also consider pretrained Torchvision DeepLabV3, FCN, or LRASPP |

Official references:

- Torchvision FCOS: https://docs.pytorch.org/vision/stable/models/fcos.html
- Torchvision SSD: https://docs.pytorch.org/vision/stable/models/ssd.html
- Torchvision DeepLabV3: https://docs.pytorch.org/vision/stable/models/deeplabv3.html
- Transformers DETR: https://huggingface.co/docs/transformers/model_doc/detr

Re-check these catalogs when generating future notebooks because library APIs and available weights change over time.
