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

## Choosing the "Best" Available Model

Do not interpret "best" as a permanent model name. Before each notebook, compare current official weight metadata and select against the competition objective:

- For an accuracy-first baseline, prefer the strongest official validation metric for the matching task and dataset family.
- Also record parameter count, checkpoint size, FLOPs/latency, memory, input resolution, license, and whether the competition permits the pretraining data.
- If latency, model size, or deployment is part of the score, a lower-mAP architecture can be the better competition model.
- State the selection criterion in the notebook. Do not call a model universally best based on one benchmark.

For the current Torchvision catalog, `fasterrcnn_resnet50_fpn_v2` is the accuracy-first general object-detection baseline used by these notebooks because its official COCO weights report 46.7 box mAP. Re-check the installed catalog and official metadata for future environments.

When a checkpoint is optional, expose that choice explicitly (for example, `use_pretrained=False`) and explain that `weights=...DEFAULT` can download files. For an offline competition, pre-cache or attach the permitted checkpoint rather than downloading during notebook execution.

## Substitution Rules

- Never present a related architecture as the exact requested model. State both the unavailable model and the chosen substitute.
- Choose substitutes by task and modeling behavior, not name similarity.
- Preserve the requested model's conceptual material even when executable practice uses a substitute.
- Explain any important semantic difference affecting data targets, loss, post-processing, or evaluation.

Current CV examples under the allowlist:

| Requested topic | Exact allowed implementation | Useful allowed alternatives |
|---|---|---|
| YOLO detection | None in the current allowlist | Accuracy-first: Faster R-CNN ResNet50-FPN V2. Conceptually closer one-stage alternatives: FCOS, RetinaNet, SSD/SSDLite |
| SSD | `torchvision.models.detection.ssd300_vgg16` and SSDLite builders | FCOS or RetinaNet for other one-stage baselines |
| DETR | Hugging Face `transformers` DETR models/checkpoints | Torchvision detectors when Transformer checkpoints are unavailable |
| U-Net | None in Torchvision | Teach U-Net manually when architecture is the objective; for competition baselines also consider pretrained Torchvision DeepLabV3, FCN, or LRASPP |

Official references:

- Torchvision FCOS: https://docs.pytorch.org/vision/stable/models/fcos.html
- Torchvision SSD: https://docs.pytorch.org/vision/stable/models/ssd.html
- Torchvision DeepLabV3: https://docs.pytorch.org/vision/stable/models/deeplabv3.html
- Transformers DETR: https://huggingface.co/docs/transformers/model_doc/detr
- Torchvision Faster R-CNN ResNet50-FPN V2: https://docs.pytorch.org/vision/stable/models/generated/torchvision.models.detection.fasterrcnn_resnet50_fpn_v2.html

Re-check these catalogs when generating future notebooks because library APIs and available weights change over time.

## Competition Validation and Ensembling Default

For competition-oriented training notebooks, a single `train_test_split` is a teaching shortcut, not the default final workflow.

1. Build a custom file-backed `Dataset` that owns path loading, target parsing, transforms, and validation. Avoid making `TensorDataset` or raw `Subset` the main competition data boundary.
2. Create deterministic out-of-fold splits and store fold membership by stable sample ID.
3. Use `StratifiedKFold` for ordinary single-label independent samples.
4. If samples share patients, videos, products, scenes, or other leakage groups, use a group-aware splitter. For multilabel detection or segmentation, define and document a suitable stratification proxy or iterative multilabel method; plain single-label stratification is not automatically valid.
5. Train one model per fold, save fold-specific checkpoints, and generate OOF predictions only from the fold that did not train on each sample.
6. Verify every training observation appears in exactly one validation fold and no leakage group crosses train/validation.
7. Calculate the main metric from the complete OOF table. Use the fold distribution to understand stability.
8. Ensemble fold models on test data using a task-appropriate rule: average probabilities/logits for classification, average masks/probabilities for segmentation, and use class-aware box fusion or NMS/weighted box fusion logic for detection.

A simple holdout remains appropriate when split mechanics are the lesson, runtime is intentionally constrained, temporal validation is required, or the competition defines a fixed validation set. State that reason explicitly.
