from setuptools import setup

setup(name='weight-augmentations',
      version='0.0.1',
      packages=["weight_augmentations"]
      install_requires=[
          "jax",
          "chex",
          "numpy",
          ],
      )
