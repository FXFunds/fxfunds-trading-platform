from setuptools import setup

with open("README.md", encoding="utf-8") as f:
    long_description = f.read()

setup(
    name="fxfunds-trading-platform",
    version="1.0.0",
    description="FXFunds Trading Platform reference data — company-reported profile, market categories, payment status and verify-before-trading checklist.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    author="FXFunds",
    url="https://github.com/fxfunds/fxfunds-trading-platform",
    project_urls={
        "Homepage": "https://fxfunds.com/",
        "Documentation": "https://fxfunds-trading-platform.readthedocs.io",
    },
    license="MIT",
    py_modules=["fxfunds_platform"],
    python_requires=">=3.8",
    entry_points={"console_scripts": ["fxfunds-info=fxfunds_platform:main"]},
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
)
