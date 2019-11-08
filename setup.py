from setuptools import setup, find_packages

setup(name='lime',
      version='0.1.1.36',
      description='Local Interpretable Model-Agnostic Explanations for machine learning classifiers',
      url='http://github.com/marcotcr/lime',
      author='Marco Tulio Ribeiro',
      author_email='marcotcr@gmail.com',
      license='BSD',
      packages= find_packages(exclude=['js', 'node_modules', 'tests']),
      install_requires=[
          'matplotlib',
          'matplotlib',
          'numpy',
          'scipy',
          'progressbar',
          'scikit-learn>=0.18'
      ],
      include_package_data=True,
      zip_safe=False)
