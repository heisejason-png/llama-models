# Copyright (c) Meta Platforms, Inc. and affiliates.
# All rights reserved.
#
# This source code is licensed under the terms described in the LICENSE file in
# top-level folder for each specific model found within the models/ directory at
# the top-level of this source tree.

from dataclasses import dataclass
from typing import Any, Dict, List

from jinja2 import Template


@dataclass
class PromptTemplate:
    template: str
    data: Dict[str, Any]

    def render(self):
        template = Template(self.template)
        return template.render(self.data)


class PromptTemplateGeneratorBase:
    """
    Base class for prompt template generators.
    """

    def gen(self, *args, **kwargs) -> PromptTemplate:
        raise NotImplementedError()

    def data_examples(self) -> List[Any]:
        raise NotImplementedError()