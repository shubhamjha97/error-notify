from setuptools import setup, find_packages

setup(name='error-notify',
      version='0.1',
      description='A simple tool to notify you about errors via system notifications and Telegram.',
      url='https://github.com/shubhamjha97/error-notify',
      author='Shubham Jha, Mayank Kushal',
      author_email='jha1shubham@gmail.com, mayankkushal26@gmail.com',
      license='MIT',
      long_description=open('README.md').read(),
      long_description_content_type="text/markdown",
      install_requires=[
        'telegram-send==0.20'
    	],
      packages=find_packages(),
      classifiers = ('Intended Audience :: Developers', 'Natural Language :: English', 'Programming Language :: Python :: 3.6'),
      zip_safe=False)