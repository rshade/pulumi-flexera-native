# coding=utf-8
# *** WARNING: this file was generated by pulumi. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

from . import _utilities
import typing
# Export this package's modules as members:
from .provider import *
from .random import *
_utilities.register(
    resource_modules="""
[
 {
  "pkg": "flexera-native",
  "mod": "index",
  "fqn": "pulumi_flexera_native",
  "classes": {
   "flexera-native:index:Random": "Random"
  }
 }
]
""",
    resource_packages="""
[
 {
  "pkg": "flexera-native",
  "token": "pulumi:providers:flexera-native",
  "fqn": "pulumi_flexera_native",
  "class": "Provider"
 }
]
"""
)