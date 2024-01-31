#!/usr/bin/env bash
set -xe

datamodel-codegen \
  --input="$*" \
  --input-file-type=openapi \
  --output=_gen.py \
  --output-model-type=pydantic_v2.BaseModel \
  --use-annotated \
  --use-subclass-enum \
  --use-unique-items-as-set \
  --capitalize-enum-members \
  --enable-version-header \
  --use-double-quotes \
  --target-python-version=3.8 \
  --use-field-description \
  --field-constraints \
  --use-generic-container-types \
  --use-standard-collections \
  --use-non-positive-negative-number-constrained-types \
  --use-unique-items-as-set \
  --collapse-root-models \
  --openapi-scopes=schemas \
  --use-operation-id-as-name
